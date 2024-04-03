from fastapi import APIRouter,Depends, HTTPException, status, UploadFile, Form
from fastapi.responses import FileResponse
from .dependencies import get_product_db
from app.schemas import Product,ProductCreate,ProductUpdate
from app.query import ProductService
from app.exceptions import NotFoundError
from os import path
from typing import Annotated
import re

router=APIRouter(prefix="/product",tags=["product"])

@router.post("/")
def create(file:UploadFile,parent_collection:Annotated[int,Form()],name:Annotated[str,Form()],description:Annotated[str,Form()],price:Annotated[int,Form()],positionX:Annotated[float,Form()],positionY:Annotated[float,Form()],product_service:ProductService=Depends(get_product_db)):
    pure_name=re.sub(".*/","",file.filename)
    try:
        basepath = path.dirname(__file__)
        file_location = path.abspath(path.join(basepath,"..","imges/imges_products", pure_name ))
        with open(file_location, "wb+") as file_object:
            file_object.write(file.file.read())
        product=ProductCreate(parent_collection=parent_collection,name=name,description=description,price=price,positionx=positionX,positiony=positionY,img=pure_name)    
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
    
@router.get("/img/{img}")
def get_image(img:str):
    basepath = path.dirname(__file__)
    file_location = path.abspath(path.join(basepath,"..","imges", img ))
    if(path.exists(file_location)):
        return FileResponse("app/imges/imges_products/"+img)
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="file does not exist")
    
    
@router.delete("/{id}")
def delete(id:int,product_service:ProductService=Depends(get_product_db)):
    try:
        return  product_service.delete_product(id)
    except NotFoundError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Collection not found")