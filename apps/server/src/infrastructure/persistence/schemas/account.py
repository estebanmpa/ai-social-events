import uuid
from typing import List, Optional
from sqlmodel import SQLModel, Field, Relationship, UniqueConstraint


class AccountDB(SQLModel, table=True):
    __tablename__ = "accounts"

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    name: str = Field(unique=True, index=True)
    title: str
    link: str
    snippet: str
    image: Optional[str] = None

    favourites: List["Favourite"] = Relationship(back_populates="account")
