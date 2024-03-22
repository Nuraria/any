from pydantic import BaseModel
from typing import Optional

class ProductCreate(BaseModel):
    name:str
    description:str
    price:str
    cordinates:str

class Product(ProductCreate):
    id:int

class ProductUpdate(BaseModel):
    name:Optional[str]=None
    description:Optional[str]=None
    price:Optional[str]=None
    cordinates:Optional[str]=None