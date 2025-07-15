from src.application.use_cases.google_search_use_case import GoogleSearchUseCase
from src.services.google_search_service import GoogleSearchService

def make_google_search_use_case() -> GoogleSearchUseCase:
    print("make_google_search_use_case")
    service: GoogleSearchService = GoogleSearchService()
    return GoogleSearchUseCase(service)
