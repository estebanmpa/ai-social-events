from src.application.use_cases import RemoveFromFavouritesUseCase


def make_remove_from_favourites_use_case() -> RemoveFromFavouritesUseCase:
    service: RemoveFromFavouritesUseCase = RemoveFromFavouritesUseCase()
    return RemoveFromFavouritesUseCase(service)
