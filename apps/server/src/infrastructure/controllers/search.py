from fastapi import APIRouter
from src.factories import make_google_search_use_case

router = APIRouter()

@router.get("/")
async def retrieve(q: str):
    use_case = make_google_search_use_case()
    results = await use_case.handle(q)
    return results