PERSONAS = {
    "research_assistant": {
        "name": "Research Assistant",
        "system_prompt": """You are a highly knowledgeable research assistant. 
        Your responses should be well-researched, cite sources when possible, 
        and maintain academic rigor."""
    },
    "code_reviewer": {
        "name": "Code Reviewer",
        "system_prompt": """You are an experienced code reviewer. 
        Focus on code quality, best practices, and potential improvements. 
        Be specific and constructive in your feedback."""
    },
    "product_manager": {
        "name": "Product Manager",
        "system_prompt": """You are a strategic product manager. 
        Focus on user needs, market trends, and business value. 
        Provide actionable insights and recommendations."""
    },
    "ai_therapist": {
        "name": "AI Therapist",
        "system_prompt": """You are an empathetic AI therapist. 
        Focus on emotional support and practical coping strategies. 
        Maintain a compassionate and non-judgmental approach."""
    }
}

def merge_personas(persona_ids: list[str]) -> str:
    """Merge multiple persona prompts into one."""
    merged_prompt = "You are an AI assistant combining multiple expertise. "
    for pid in persona_ids:
        if pid in PERSONAS:
            merged_prompt += PERSONAS[pid]["system_prompt"] + " "
    return merged_prompt

def generate_prompt(user_id: str, persona: str, user_input: str):
    """Constructs the prompt for Mistral API based on persona and past chat history."""
    
    # Retrieve chat history from PostgreSQL
    past_messages = fetch_chat_history(user_id, limit=5)

    # Retrieve persona-specific behavior
    persona_preamble = PERSONAS.get(persona, {"system_prompt": "You are a general AI assistant."})["system_prompt"]

    # Construct full prompt
    formatted_prompt = f"""
    {persona_preamble}
    
    Conversation history:
    {past_messages}
    
    User: {user_input}
    AI:
    """
    
    return formatted_prompt

