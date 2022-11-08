from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class Product(BaseModel):
    id: int
    text: str
    quantity: int
    created_date: datetime
    completed: bool


class ProductCreate(BaseModel):
    text: str
    quantity: Optional[int] = Field(None, gt=0)
    completed: Optional[bool]


class ProductUpdate(BaseModel):
    text: Optional[str]
    quantity: Optional[int] = Field(None, gt=0)
    completed: Optional[bool]
