import sys
from llm_service import initialize_model, get_socratic_response

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