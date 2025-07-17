from src.application.use_cases import GoogleSearchUseCase
from src.infrastructure.external.google_search import GoogleSearchService, map_google_response_to_accounts


def make_google_search_use_case() -> GoogleSearchUseCase:
    service: GoogleSearchService = GoogleSearchService()
    mapper = map_google_response_to_accounts
    return GoogleSearchUseCase(service, mapper)
