import os
from dotenv import load_dotenv

load_dotenv()

class InstagramService:
    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.api_url = "https://api.openai.com/v1/chat/completions"