import psycopg2
from config import DATABASE_URL

def get_db_connection():
    return psycopg2.connect(DATABASE_URL)

def fetch_chat_history(user_id: str, limit: int = 5) -> list:
    """Fetch recent chat history for a user from PostgreSQL."""
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            """
            SELECT message, response 
            FROM chat_history 
            WHERE user_id = %s 
            ORDER BY timestamp DESC 
            LIMIT %s
            """,
            (user_id, limit)
        )
        history = cur.fetchall()
        cur.close()
        conn.close()
        return history
    except Exception as e:
        print(f"Error fetching chat history: {str(e)}")
        return [] 