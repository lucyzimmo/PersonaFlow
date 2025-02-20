import numpy as np
from embeddings import get_embedding
import faiss
from datetime import datetime
import json

# Initialize FAISS index
VECTOR_DIM = 768  # Embedding size from Mistral API
memory_index = faiss.IndexFlatL2(VECTOR_DIM)
memory_data = []  # Store metadata alongside vectors

def store_memory(user_id: str, user_input: str, ai_response: str) -> bool:
    """Converts chat history to vector embeddings and stores in FAISS."""
    try:
        # Create combined text for embedding
        combined_text = f"User: {user_input}\nAI: {ai_response}"
        
        # Get embedding
        embedding = get_embedding(combined_text)
        
        # Store in FAISS
        memory_index.add(np.array([embedding]))
        
        # Store metadata
        memory_data.append({
            'user_id': user_id,
            'user_input': user_input,
            'ai_response': ai_response,
            'timestamp': datetime.now().isoformat(),
            'index': len(memory_data)
        })
        
        print(f"Stored memory for user {user_id}. Total memories: {len(memory_data)}")
        return True
    except Exception as e:
        print(f"Error storing memory: {str(e)}")
        return False

def retrieve_memory(user_id: str, current_input: str, k: int = 3) -> list:
    """Finds the most relevant past conversations based on vector similarity."""
    try:
        # Get embedding for current input
        query_embedding = get_embedding(current_input)
        
        # Search in FAISS
        D, I = memory_index.search(np.array([query_embedding]), k)
        
        # Get relevant memories
        relevant_memories = []
        for idx in I[0]:  # I[0] because we only search for one query
            if idx < len(memory_data):
                memory = memory_data[idx]
                if memory['user_id'] == user_id:  # Only include memories from same user
                    relevant_memories.append(
                        f"User: {memory['user_input']}\nAI: {memory['ai_response']}"
                    )
        
        print(f"Retrieved {len(relevant_memories)} memories for user {user_id}")
        return relevant_memories
    except Exception as e:
        print(f"Error retrieving memory: {str(e)}")
        return []

