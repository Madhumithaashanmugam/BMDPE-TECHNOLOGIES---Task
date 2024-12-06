from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class CreateProduct(BaseModel):
    name: str
    category: str
    quantity: Optional[int] = 0
    price: float

class UpdateProduct(BaseModel):
    name: Optional[str]
    category: Optional[str]
    quantity: Optional[int]
    price: Optional[float]

class ViewProduct(BaseModel):
    id: str
    name: str
    category: str
    quantity: int
    price: float
    low_stock: bool
    created_datetime: datetime
    updated_datetime: datetime

    class Config:
        orm_mode = True
