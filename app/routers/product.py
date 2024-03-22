from fastapi import APIRouter,Depends
from .dependencies import get_product_db
from app.schemas import Product,ProductCreate,ProductUpdate
from app.query import ProductService

router=APIRouter(prefix="/product")

@router.post("/create/")
def create(product:ProductCreate,product_service:ProductService=Depends(get_product_db)):
    return product_service.create_product(product)

@router.patch("/update/{id}")
def update(product:ProductUpdate,id:int,product_service:ProductService=Depends(get_product_db)):
    return product_service.update_product(id,product)

@router.post("/get/")
def get(collection_id:int,product_service:ProductService=Depends(get_product_db)):
    return product_service.get_product_by_collection_id(collection_id)

@router.delete("/delete/")
def delete(id:int,product_service:ProductService=Depends(get_product_db)):
    return product_service.delete_product(id)