import os
from mistralai import Mistral
import numpy as np
from config import MISTRAL_API_KEY, EMBEDDING_MODEL, CHAT_MODEL

# Initialize Mistral client
client = Mistral(api_key=MISTRAL_API_KEY)

def get_embedding(text: str) -> np.ndarray:
    """Get embedding vector for text using Mistral API."""
    try:
        response = client.embeddings(
            model=EMBEDDING_MODEL,
            input=text
        )
        return np.array(response.data[0].embedding)
    except Exception as e:
        print(f"Error getting embedding: {e}")
        raise

def get_chat_response(messages: list) -> str:
    """Get chat completion from Mistral API."""
    try:
        chat_response = client.chat.complete(
            model=CHAT_MODEL,
            messages=messages
        )
        return chat_response.choices[0].message.content
    except Exception as e:
        print(f"Error in get_chat_response: {str(e)}")  # Debug log
        raise Exception(f"Failed to get chat response: {str(e)}")