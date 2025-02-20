from dotenv import load_dotenv
import os

load_dotenv()

MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")
POSTGRES_URL = os.getenv("POSTGRES_URL")
REDIS_URL = os.getenv("REDIS_URL")

EMBEDDING_MODEL = "mistral-embed"
CHAT_MODEL = "mistral-medium"

DATABASE_URL = "postgresql://username:password@localhost:5432/personaflow"  # Update with your DB credentials
