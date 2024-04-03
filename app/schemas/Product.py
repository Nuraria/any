from pydantic import BaseModel
from typing import Optional

class ProductCreate(BaseModel):
    parent_collection:int
    name:str
    description:str
    price:int
    positionx:float
    positiony:float
    img:str

class Product(ProductCreate):
    id:int

class ProductUpdate(BaseModel):
    name:Optional[str]=None
    description:Optional[str]=None
    price:Optional[str]=None
    cordinates:Optional[str]=None
    img:Optional[str]=None