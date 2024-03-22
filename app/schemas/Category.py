from pydantic import BaseModel
from typing import Optional

class CategoryCreate(BaseModel):
    category_name:str
    color:str

class Category(CategoryCreate):
    id:int

class CategoryUpdate(BaseModel):
    category_name:Optional[str]=None
    color:Optional[str]=None