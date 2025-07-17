from pydantic import BaseModel, HttpUrl
from typing import Optional

class Account(BaseModel):
    name: str
    title: str
    link: HttpUrl
    snippet: str
    image: Optional[HttpUrl] = None
    like: bool