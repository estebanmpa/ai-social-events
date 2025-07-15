from fastapi import FastAPI
from src.infrastructure.controllers import accounts, events, posts, favourites, search
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "*",
]

app = FastAPI()

app.include_router(search.router, prefix="/api/search")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
