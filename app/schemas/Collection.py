from pydantic import BaseModel
from typing import Optional

class CollectionCreate(BaseModel):
    img:str
    category_id: int

class Collection(CollectionCreate):
    id:int

class CollectionUpdate(BaseModel):
    img:Optional[str]=None
    category_id:Optional[int]=None