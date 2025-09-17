<<<<<<< HEAD
# AI Socratic Tutor

A command-line AI tutor that uses Google's Gemini model to help users explore topics through the Socratic method of questioning. Instead of providing direct answers, the tutor asks guiding, open-ended questions to encourage deeper understanding and critical thinking.

This project is created by Nishanth K, a third-year B.Tech student in Artificial Intelligence and Data Science.

## Features

-   **Interactive Chat:** A simple and intuitive command-line interface.
-   **Socratic Method:** The AI is specifically prompted to act as a Socratic tutor, fostering a unique learning experience.
-   **Powered by Gemini:** Utilizes the powerful `gemini-1.5-flash` model from Google for intelligent and context-aware responses.
-   **Custom Identity:** Includes a hardcoded response to identify its creator when asked.
-   **Easy Setup:** Uses a `.env` file to securely manage your API key.

## Requirements

-   Python 3.7+
-   A Google AI API Key. You can get one from the [Google AI Studio](https://aistudio.google.com/app/apikey).

## Setup and Installation

Follow these steps to get the Socratic Tutor running on your local machine.

### 1. Clone the Repository (or Download the Files)
If this were a Git repository, you would clone it. For now, just make sure your files are in a dedicated project folder.
```bash
# Example:
mkdir socratic-tutor
cd socratic-tutor
```

### 2. Create a Virtual Environment
It's highly recommended to use a virtual environment to manage project dependencies.

```bash
# Create the virtual environment
python -m venv venv

# Activate it
# On Windows:
.\venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
Install the required Python libraries using the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

### 4. Create the Environment File
Create a file named `.env` in the root of your project directory. This file will store your API key securely.

```
GOOGLE_API_KEY="YOUR_API_KEY_HERE"
```
Replace `"YOUR_API_KEY_HERE"` with your actual Google AI API key.

## Usage

Once the setup is complete, run the application from your terminal:

```bash
python tutor.py
```

The tutor will greet you, and you can start the conversation. Type `exit` or `quit` to end the session.

## File Structure

The project directory should look like this:

```
socratic-tutor/
├── venv/
├── tutor.py
├── requirements.txt
├── .env
└── README.md
```

## Customization

The creator's identity is set directly in the `tutor.py` script within the `run_socratic_tutor` function. You can modify the `creator_keywords` list and the printed response to change this behavior.
=======
# socratic-ai-tutor
>>>>>>> 08b0f3b0841c9ef2f2822fb5a1f58d9f5fa1f4a1
