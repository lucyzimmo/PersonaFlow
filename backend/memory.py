import numpy as np
from embeddings import get_embedding
import faiss
from datetime import datetime
import json

# Initialize FAISS index
VECTOR_DIM = 1024  # Embedding size from Mistral API
memory_index = faiss.IndexFlatL2(VECTOR_DIM)
memory_data = []  # Store metadata alongside vectors

def store_memory(user_id: str, user_input: str, ai_response: str) -> bool:
    """Converts chat history to vector embeddings and stores in FAISS."""
    try:
        combined_text = f"User: {user_input}\nAI: {ai_response}"
        
        embedding = get_embedding(combined_text)  # ✅ Generate embedding
        
        if embedding.shape[0] != VECTOR_DIM:
            raise ValueError(f"❌ Embedding size mismatch: Expected {VECTOR_DIM}, got {embedding.shape[0]}")

        # ✅ Ensure embedding is the correct dtype and format
        embedding = np.array([embedding], dtype=np.float32)  # FAISS requires float32
        
        memory_index.add(embedding)  # ✅ Store in FAISS

        memory_data.append({
            'user_id': user_id,
            'user_input': user_input,
            'ai_response': ai_response,
            'timestamp': datetime.now().isoformat(),
            'index': len(memory_data)
        })
        
        print(f"✅ Stored memory for user {user_id}. Total memories: {len(memory_data)}")
        return True
    except Exception as e:
        print(f"❌ Error storing memory: {str(e)}")
        return False


def retrieve_memory(user_id: str, current_input: str, k: int = 3) -> list:
    """Finds the most relevant past conversations based on vector similarity."""
    try:
        # Check if we have any memories stored
        if len(memory_data) == 0:
            print("ℹ️ No memories stored yet")
            return []

        query_embedding = get_embedding(current_input)
        
        # Ensure k doesn't exceed the number of stored memories
        k = min(k, len(memory_data))
        
        D, I = memory_index.search(np.array([query_embedding], dtype=np.float32), k)
        
        relevant_memories = []
        for idx in I[0]:
            if idx >= 0 and idx < len(memory_data):  # Check for valid index
                memory = memory_data[idx]
                if memory['user_id'] == user_id:
                    relevant_memories.append(f"User: {memory['user_input']}\nAI: {memory['ai_response']}")
        
        print(f"🔍 Retrieved {len(relevant_memories)} memories for user {user_id}")
        return relevant_memories
    except Exception as e:
        print(f"❌ Error retrieving memory: {str(e)}")
        return []
