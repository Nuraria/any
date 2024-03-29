from pydantic import BaseModel
from pydantic_extra_types.color import Color
from typing import Optional

class CategoryCreate(BaseModel):
    category_name:str
    color:Color

class Category(CategoryCreate):
    id:int

class CategoryUpdate(BaseModel):
    category_name:Optional[str]=None
    color:Optional[Color]=None