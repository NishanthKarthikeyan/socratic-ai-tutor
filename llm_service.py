import google.generativeai as genai
import os
from dotenv import load_dotenv

def initialize_model():
    """
    Configures the API key and returns the Gemini Pro model.
    Raises a ValueError if the API key is not found.
    """
    load_dotenv()
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError(
            "GOOGLE_API_KEY environment variable not set. "
            "Please create a .env file and add your key."
        )

    genai.configure(api_key=api_key)
    
    # Use the corrected, widely compatible model name.
    model = genai.GenerativeModel('gemini-pro')
    return model

def get_socratic_response(user_input: str, model) -> str:
    """
    Sends the user's input to the LLM with a Socratic persona prompt
    and returns the AI's question as a response.
    """
    socratic_prompt = (
        "You are an AI Socratic tutor. Your purpose is to help users learn by asking "
        "them questions, not by giving them direct answers. Your questions should "
        "be open-ended, thought-provoking, and designed to guide the user towards "
        "a deeper understanding of the topic. "
        "Do not provide definitions or facts unless a user explicitly asks for clarification. "
        "Instead, respond to the user's statement or question with a new question. "
        "Your response should be in a conversational and encouraging tone."
    )

    full_prompt = f"{socratic_prompt}\n\nUser: {user_input}\nAI:"

    try:
        response = model.generate_content(full_prompt)
        return response.text
    except Exception as e:
        return f"An error occurred while communicating with the AI: {e}"