from fastapi import APIRouter
from src.factories import make_add_to_favourites_use_case, make_remove_from_favourites_use_case

router = APIRouter()

@router.post("/")
async def add():
    use_case = make_add_to_favourites_use_case()
    await use_case.handle()
    return []

@router.delete("/")
async def remove():
    use_case = make_remove_from_favourites_use_case()
    await use_case.handle()
    return None