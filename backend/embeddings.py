import os
import requests
import numpy as np
from mistralai import Mistral
from config import MISTRAL_API_KEY, EMBEDDING_MODEL, CHAT_MODEL

MISTRAL_EMBEDDING_URL = "https://api.mistral.ai/v1/embeddings"

# Initialize Mistral client
client = Mistral(api_key=MISTRAL_API_KEY)

def get_embedding(text: str) -> np.ndarray:
    """Get embedding vector for text using Mistral API."""
    try:
        response = client.embeddings(
            model=EMBEDDING_MODEL,
            input=text
        )
        embedding = np.array(response.data[0].embedding)
        print(f"Generated embedding shape: {embedding.shape}")  # Debug log
        return embedding
    except Exception as e:
        print(f"Error getting embedding: {str(e)}")
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
        print(f"Error in get_chat_response: {str(e)}")
        raise Exception(f"Failed to get chat response: {str(e)}")