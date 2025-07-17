from pydantic import HttpUrl
import uuid
from typing import List, Optional
from sqlmodel import SQLModel, Field, Relationship, UniqueConstraint


class AccountDB(SQLModel, table=True):
    __tablename__ = "accounts"

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    name: str = Field(unique=True, index=True)
    title: str
    link: HttpUrl
    snippet: str
    image: Optional[HttpUrl] = None

    favourites: List["Favourite"] = Relationship(back_populates="account")
