from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
from mistralai import Mistral
from typing import List, Optional
from redis import Redis
import json
from datetime import datetime

from personas import PERSONAS, merge_personas
from memory import store_memory, retrieve_memory
from embeddings import get_chat_response
from config import REDIS_URL, MISTRAL_API_KEY

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins in development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize Redis client
try:
    redis_client = Redis.from_url(REDIS_URL)
except Exception as e:
    print(f"Warning: Redis connection failed: {e}")
    redis_client = None

# Initialize Mistral client
mistral_client = Mistral(api_key=MISTRAL_API_KEY)

print(f"MISTRAL_API_KEY: {MISTRAL_API_KEY}")  # Debug log

class ChatRequest(BaseModel):
    user_id: str
    persona: str
    message: str
    merge_with: Optional[List[str]] = None

@app.get("/")
async def root():
    return {"message": "PersonaFlow API is running"}

@app.get("/personas")
async def get_personas():
    return PERSONAS

@app.post("/chat")
async def chat(request: ChatRequest):
    try:
        # Get system prompt based on persona
        system_prompt = PERSONAS.get(request.persona, {}).get("system_prompt", "")
        if not system_prompt:
            raise HTTPException(status_code=400, detail="Invalid persona selected")

        # Retrieve relevant memories
        past_memories = retrieve_memory(request.user_id, request.message)
        memories_str = "\n\n".join(past_memories) if past_memories else ""

        # Construct messages with memory context
        messages = [
            {"role": "system", "content": f"{system_prompt}\n\nRelevant past interactions:\n{memories_str}"},
            {"role": "user", "content": request.message}
        ]

        # Get response from Mistral
        response = get_chat_response(messages)
        
        # Store the new interaction in memory
        store_memory(request.user_id, request.message, response)

        return {"response": response}
    except Exception as e:
        print(f"Error in chat endpoint: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
