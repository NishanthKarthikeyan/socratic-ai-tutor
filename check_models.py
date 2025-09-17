import google.generativeai as genai
import os
from dotenv import load_dotenv

def check_available_models():
    """
    Connects to the Google AI service and lists all models
    that support content generation.
    """
    try:
        load_dotenv()
        api_key = os.getenv("GOOGLE_API_KEY")

        if not api_key:
            raise ValueError(
                "GOOGLE_API_KEY environment variable not set. "
                "Please create a .env file and add your key."
            )

        genai.configure(api_key=api_key)

        print("Searching for available models...")
        print("-" * 25)
        
        model_found = False
        for m in genai.list_models():
            if 'generateContent' in m.supported_generation_methods:
                print(f"✅ {m.name}")
                model_found = True
        
        if not model_found:
            print("No models supporting 'generateContent' were found for your API key.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    check_available_models()