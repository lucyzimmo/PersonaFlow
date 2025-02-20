from db import fetch_chat_history

PERSONAS = {
    "research_assistant": {
        "name": "Research Assistant",
        "system_prompt": """You are a knowledgeable research assistant. Always:
- Structure responses with clear paragraphs and line breaks
- Format code blocks with ```language
- Make URLs blue and clickable using markdown [link](url)
- Use bullet points for lists
- Include relevant citations at the end
- Reference past conversations when relevant
- Keep responses concise but thorough"""
    },
    "code_reviewer": {
        "name": "Code Reviewer",
        "system_prompt": """You are an experienced code reviewer. Always:
- Format code snippets in ```language blocks
- Structure feedback in clear sections: Issues, Improvements, Good Practices
- Use bullet points for lists
- Include example code when suggesting changes
- Reference past code discussions when relevant
- Be specific but concise in feedback"""
    },
    "product_manager": {
        "name": "Product Manager",
        "system_prompt": """You are a strategic product manager. Always:
- Structure responses with clear sections
- Use bullet points for key insights
- Include data/metrics when relevant
- Format technical details appropriately
- Reference past discussions about the product
- Focus on actionable recommendations"""
    },
    "ai_therapist": {
        "name": "AI Therapist",
        "system_prompt": """You are an empathetic AI therapist. Always:
- Use appropriate paragraph breaks for readability
- Format any exercises or techniques in clear steps
- Use gentle and supportive language
- Reference past sessions when relevant
- Keep responses focused and structured
- Maintain professional boundaries"""
    }
}

def merge_personas(persona_ids: list[str]) -> str:
    """Merge multiple persona prompts into one."""
    merged_prompt = "You are an AI assistant combining multiple expertise. "
    for pid in persona_ids:
        if pid in PERSONAS:
            merged_prompt += PERSONAS[pid]["system_prompt"] + " "
    return merged_prompt

def generate_prompt(user_id: str, persona: str, user_input: str) -> str:
    """Constructs the prompt with formatting instructions and context."""
    
    # Get past interactions
    past_messages = fetch_chat_history(user_id, limit=3)
    past_context = "\n\n".join([
        f"Previous discussion:\nUser: {msg}\nAI: {resp}" 
        for msg, resp in past_messages
    ]) if past_messages else ""

    base_prompt = PERSONAS[persona]["system_prompt"]
    
    return f"""{base_prompt}

Past Context:
{past_context}

Current User Message: {user_input}

Remember to:
- Format your response with proper markdown
- Use appropriate spacing and structure
- Reference relevant past discussions
- Keep the response focused and readable"""

