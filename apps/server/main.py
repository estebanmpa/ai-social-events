from fastapi import FastAPI
from src.infrastructure.controllers import accounts, events, posts, favourites

app = FastAPI()

app.include_router(accounts.router, prefix="/accounts")
app.include_router(events.router, prefix="/events")
app.include_router(posts.router, prefix="/posts")
app.include_router(favourites.router, prefix="/favourites")