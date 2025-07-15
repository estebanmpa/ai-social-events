from src.services.google_search_service import GoogleSearchService

class GoogleSearchUseCase:
    def __init__(self, service: GoogleSearchService):
        self.service = service

    async def handle(self, query: str):
        return await self.service.search(query)
