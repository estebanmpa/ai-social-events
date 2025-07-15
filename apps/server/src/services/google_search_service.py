import httpx
import os
from dotenv import load_dotenv

load_dotenv()

class GoogleSearchService:
    def __init__(self):
        self.api_key = os.getenv("GCP_SEARCH_API_KEY")
        self.search_id = os.getenv("GCP_SEARCH_ENGINE_ID")
        self.api_url = "https://www.googleapis.com/customsearch/v1"

    async def search(self, query: str):
        headers = {
            "Content-Type": "application/json"
        }

        query_params = {
            "key": self.api_key,
            "cx": self.search_id,
            "q": query
        }

        async with httpx.AsyncClient() as client:
            response = await client.get(self.api_url, headers=headers, params=query_params)
            response.raise_for_status()
            return response.json()