from sqlalchemy.orm import Session
from app.schemas import ProductCreate,ProductUpdate
from app.models import Product
from app.registry import create,get_with_conditions,update,delete

class ProductService:

    _db:Session

    def __init__(self,db:Session) -> None:
        self._db=db

    def create_product(self,product:ProductCreate):
        return create(Product,self._db,product)

    def get_product_by_collection_id(self,parent_collection:int):
        return get_with_conditions(Product,self._db,{"parent_collection":parent_collection})

    def delete_product(self,id:int):
        return delete(Product,self._db,id)

    def update_product(self,id:int,product:ProductUpdate):
        return update(Product,self._db,id,product.model_dump(exclude=None))