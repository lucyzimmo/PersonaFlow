import numpy as np
from embeddings import get_embedding
import faiss

memory_index = faiss.IndexFlatL2(768)

vector_dim = 768  # Embedding size from Mistral API

def store_memory(user_id, user_input, ai_response):
    """Converts chat history to vector embeddings and stores in FAISS."""
    embedding = get_embedding(f"{user_input} {ai_response}")
    memory_index.add(np.array([embedding]))

def retrieve_memory(user_input):
    """Finds the most relevant past conversation based on vector similarity."""
    query_embedding = get_embedding(user_input)
    D, I = memory_index.search(np.array([query_embedding]), k=3)
    return I  # Returns indices of most relevant past interactions

