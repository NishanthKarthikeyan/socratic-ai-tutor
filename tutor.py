import sys
import google.generativeai as genai
import os
from dotenv import load_dotenv

# --- Initialization and Model Service ---

def initialize_model():
    """
    Configures the API key and returns the Gemini model.
    """
    load_dotenv()
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError(
            "GOOGLE_API_KEY environment variable not set. "
            "Please create a .env file and add your key."
        )

    genai.configure(api_key=api_key)
    
    model = genai.GenerativeModel('models/gemini-1.5-flash-latest')
    return model

def get_socratic_response(user_input: str, model) -> str:
    """
    Sends the user's input to the LLM with a Socratic prompt.
    """
    socratic_prompt = (
        "You are an AI Socratic tutor. Your purpose is to help users learn by asking "
        "them questions, not by giving them direct answers. Your questions should "
        "be open-ended, thought-provoking, and designed to guide the user towards "
        "a deeper understanding of the topic. Do not provide definitions or facts "
        "unless a user explicitly asks for clarification. Instead, respond to the "
        "user's statement or question with a new question. Your tone should be "
        "conversational and encouraging."
    )

    full_prompt = f"{socratic_prompt}\n\nUser: {user_input}\nAI:"

    try:
        response = model.generate_content(full_prompt)
        return response.text
    except Exception as e:
        return f"An error occurred: {e}"

# --- Main Application Loop ---

def run_socratic_tutor():
    """
    Runs the main conversational loop for the Socratic Tutor.
    """
    try:
        model = initialize_model()
        print("Socratic Tutor: Hello! I'm here to help you think through a topic. What would you like to explore today?")
        print("Type 'exit' or 'quit' to end the conversation.")
        
        while True:
            user_input = input("\nUser: ")
            
            if user_input.lower() in ['exit', 'quit']:
                print("Socratic Tutor: It was a pleasure to learn with you. Goodbye!")
                break
            
            # --- START: CUSTOM UPDATE ---
            # Check for questions about the creator before calling the AI
            creator_keywords = ["who created you", "who made you", "your creator", "who founded you"]
            if any(keyword in user_input.lower() for keyword in creator_keywords):
                print("Socratic Tutor: I was created by Nishanth K, a third-year B.Tech student studying Artificial Intelligence and Data Science in Hosur.")
                continue # Skip the AI call and ask for the next input
            # --- END: CUSTOM UPDATE ---
            
            if not user_input.strip():
                print("Socratic Tutor: Please enter a question or a statement to begin.")
                continue

            ai_response = get_socratic_response(user_input, model)
            print("Socratic Tutor:", ai_response)

    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    run_socratic_tutor()