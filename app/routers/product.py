from fastapi import APIRouter,Depends, HTTPException, status
from .dependencies import get_product_db
from app.schemas import Product,ProductCreate,ProductUpdate
from app.query import ProductService
from app.exceptions import NotFoundError

router=APIRouter(prefix="/product")

@router.post("/")
def create(product:ProductCreate,product_service:ProductService=Depends(get_product_db)):
    try:
        return product_service.create_product(product)
    except NotFoundError:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Collection not found")

@router.patch("/{id}")
def update(product:ProductUpdate,id:int,product_service:ProductService=Depends(get_product_db)):
    try:
        product_service.update_product(id,product)
    except NotFoundError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Product not found")

@router.get("/{collection_id}", response_model=list[Product])
def get(collection_id:int,product_service:ProductService=Depends(get_product_db)):
    try:
        return  product_service.get_product_by_collection_id(collection_id)
    except NotFoundError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Collection not found")
    
    
@router.delete("/{id}")
def delete(id:int,product_service:ProductService=Depends(get_product_db)):
    try:
        return  product_service.delete_product(id)
    except NotFoundError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Collection not found")