import uuid
from typing import List, Optional
from sqlmodel import SQLModel, Field, Relationship, UniqueConstraint

class Favourite(SQLModel, table=True):
    __tablename__ = "favourites"
    __table_args__ = (UniqueConstraint("user_id", "account_id"),)

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    user_id: uuid.UUID = Field(index=True)
    account_id: uuid.UUID = Field(foreign_key="accounts.id")

    account: Optional["Account"] = Relationship(back_populates="favourites")
