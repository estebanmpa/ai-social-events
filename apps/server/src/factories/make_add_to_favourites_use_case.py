from src.application.use_cases import AddToFavouritesUseCase


def make_add_to_favourites_use_case() -> AddToFavouritesUseCase:
    service: AddToFavouritesUseCase = AddToFavouritesUseCase()
    return AddToFavouritesUseCase(service)
