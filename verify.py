import os

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    print("API key not set or invalid.")