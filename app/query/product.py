from sqlalchemy.orm import Session
from app.schemas import ProductCreate,ProductUpdate
from app.models import Product
from app.registry import create,get_with_conditions,update,delete
from app.exceptions import NotFoundError
from app.query import CollectionService
from sqlalchemy.exc import IntegrityError
class ProductService:

    _db:Session
    _collection:CollectionService

    def __init__(self,db:Session,collection:CollectionService) -> None:
        self._db=db
        self._collection=collection

    def create_product(self,product:ProductCreate):
        try:
            return create(Product,self._db,product)
        except IntegrityError:
            raise NotFoundError
        

    def get_product_by_collection_id(self,parent_collection:int):
        self._collection.get_collection(parent_collection)
        return get_with_conditions(Product,self._db,{"parent_collection":parent_collection})

    def delete_product(self,id:int):
        delete_count=delete(Product,self._db,id)
        if delete_count<1:
            raise NotFoundError
        return None

    def update_product(self,id:int,product:ProductUpdate):
        update_count=update(Product,self._db,id,product.model_dump(exclude=None))
        if update_count<1 :
            raise NotFoundError
        return None 