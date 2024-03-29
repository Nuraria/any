from sqlalchemy.orm import Session
from app.schemas import CategoryCreate,CategoryUpdate
from app.models import Category
from app.registry import create,update,delete,get
from app.exceptions import NotFoundError

class CategoryService():

    _db:Session

    def __init__(self,db:Session) -> None:
        self._db=db

    def create_category(self,category:CategoryCreate):
        return create(Category,self._db,category)
    
    def get_category(self):
        return get(Category,self._db)

    def update_category(self,id:int,category:CategoryUpdate):
        update_count=update(Category,self._db,id,category.model_dump(exclude=None))
        if update_count<1:
            raise NotFoundError
        return None

    def delete_category(self,id:int):
        delete_count=delete(Category,self._db,id)
        if delete_count<1:
            raise NotFoundError
        return None