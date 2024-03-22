from sqlalchemy.orm import Session
from app.schemas import CategoryCreate,CategoryUpdate
from app.models import Category
from app.registry import create,update,delete,get

class CategoryService():

    _db:Session

    def __init__(self,db:Session) -> None:
        self._db=db

    def create_category(self,category:CategoryCreate):
        return create(Category,self._db,category)
    
    def get_category(self):
        return get(Category,self._db)

    def update_category(self,id:int,category:CategoryUpdate):
        return update(Category,self._db,id,category.model_dump(exclude=None))

    def delete_category(self,id:int):
        return delete(Category,self._db,id)