import os
from mistralai import Mistral
import numpy as np
from config import MISTRAL_API_KEY, EMBEDDING_MODEL, CHAT_MODEL
MISTRAL_EMBEDDING_URL = "https://api.mistral.ai/v1/embeddings"
MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")

def get_embedding(texts):
    """
    Calls Mistral API to generate embeddings.
    
    Args:
        texts (str or list of str): The text(s) to embed.

    Returns:
        List of embedding vectors.
    """
    if isinstance(texts, str):
        texts = [texts]  # Convert single text to list

    headers = {
        "Authorization": f"Bearer {MISTRAL_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "input": texts,
        "model": "mistral-embed",  # Use Mistral's embedding model
        "encoding_format": "float"
    }

    try:
        response = requests.post(MISTRAL_EMBEDDING_URL, json=payload, headers=headers)
        response.raise_for_status()  # Raise error if the request failed
        return response.json()["data"]  # Extract embeddings
    except requests.exceptions.RequestException as e:
        print(f"Error getting embedding: {e}")
        return None  # Handle failure gracefully
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