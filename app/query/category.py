from sqlalchemy.orm import Session
from app.schemas import CategoryCreate,CategoryUpdate
from app.models import Category
from app.registry import create,update,delete,get,get_with_conditions
from app.exceptions import NotFoundError

class CategoryService():

    _db:Session

    def __init__(self,db:Session) -> None:
        self._db=db

    def create_category(self,category:CategoryCreate):
        return create(Category,self._db,category)
    
    def get_all_categories(self):
        return get(Category,self._db)
    
    def get_category(self,id:int):
        category=get_with_conditions(Category,self._db,{"id":id})
        if category is None:
            raise NotFoundError
        return category
    
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