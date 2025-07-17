from apps.server.src.infrastructure.external.google_search.google_search_service import GoogleSearchService
from src.domain.models.account import Account
from typing import List

class GoogleSearchUseCase:
    def __init__(self, service: GoogleSearchService, mapper):
        self.service = service
        self.mapper = mapper

    async def handle(self, query: str) -> List[Account]:
        searchResults = await self.service.search(query)
        return self.mapper(searchResults, [])
