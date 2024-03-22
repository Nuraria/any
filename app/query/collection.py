from sqlalchemy.orm import Session
from app.schemas import CollectionCreate,CollectionUpdate
from app.models import Collection
from app.registry import create,get_with_conditions,update,delete

class CollectionService():

    _db:Session

    def __init__(self,db:Session) -> None:
        self._db=db

    def create_collection(self,collection:CollectionCreate):
        return create(Collection,self._db,collection)

    def get_collections_by_category(self,category_id:int):
        return get_with_conditions(Collection,self._db,{"category_id":category_id})

    def update_collection(self,id:int,collection:CollectionUpdate):
        return update(Collection,self._db,id,collection.model_dump(exclude=None))

    def delete_collection(self,id:int):
        return delete(Collection,self._db,id)