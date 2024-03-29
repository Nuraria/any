from sqlalchemy.orm import Session
from app.schemas import CollectionCreate,CollectionUpdate
from app.models import Collection
from app.registry import create,get_with_conditions,update,delete,get
from app.exceptions import NotFoundError
from app.query import CategoryService
from sqlalchemy.exc import IntegrityError

class CollectionService():

    _db:Session

    def __init__(self,db:Session,) -> None:
        self._db=db

    def get_all_collections(self):
        return get(Collection,self._db)
    
    def get_collection(self,id:int):
        collection = get_with_conditions(Collection,self._db,{"id":id})
        if collection is None:
            raise NotFoundError
        return collection

    def create_collection(self,collection:CollectionCreate):
        try:
            return create(Collection,self._db,collection)
        except IntegrityError:
            raise NotFoundError

    def get_collections_by_category(self,category_id:int):
        return get_with_conditions(Collection,self._db,{"category_id":category_id})

    def update_collection(self,id:int,collection:CollectionUpdate):
        update_count=update(Collection,self._db,id,collection.model_dump(exclude=None))
        if update_count<1:
            raise NotFoundError
        return None
    
    def delete_collection(self,id:int):
        delete_count=delete(Collection,self._db,id)
        if delete_count<1:
            raise NotFoundError
        return None