from pydantic import BaseModel
from typing import Optional


class Book(BaseModel):
    id: int
    author: str
    description: str
    year: int
    status: Optional[str] = None
