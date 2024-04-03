from fastapi import APIRouter,Depends,HTTPException, status, UploadFile, File, Form
from fastapi.responses import FileResponse
from .dependencies import get_collection_db
from app.schemas import Collection,CollectionCreate,CollectionUpdate
from app.query import CollectionService
from app.exceptions import NotFoundError
from typing import Annotated
from os import path
import re

router=APIRouter(prefix="/collection",tags=["collection"])

@router.get("/")
def get_all(collection_service:CollectionService=Depends(get_collection_db)):
    return collection_service.get_all_collections()

@router.post("/")
def create(file:UploadFile,category_id:Annotated[str,Form()],collection_service:CollectionService=Depends(get_collection_db)):
    pure_name=re.sub(".*/","",file.filename)
    try:
        collection = collection_service.create_collection(CollectionCreate(img=pure_name,category_id=category_id))
    except NotFoundError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Category does not exist")
    basepath = path.dirname(__file__)
    file_location = path.abspath(path.join(basepath,"..","imges", pure_name ))
    with open(file_location, "wb+") as file_object:
        file_object.write(file.file.read())
    return collection 

@router.patch("/{id}")
def update(collection:CollectionUpdate,id:int,collection_service:CollectionService=Depends(get_collection_db)):
    try:
        collection_service.update_collection(id,collection)
    except NotFoundError:
        raise HTTPException(status_code=status)

@router.get("/{id}",response_model=list[Collection])
def get(id:int,collection_service:CollectionService=Depends(get_collection_db)):
    return collection_service.get_collection(id)

@router.get("/category/{id}",response_model=list[Collection])
def get(id:int,collection_service:CollectionService=Depends(get_collection_db)):
    return collection_service.get_collections_by_category(id)

@router.get("/img/{img}")
def get_image(img:str):
    basepath = path.dirname(__file__)
    file_location = path.abspath(path.join(basepath,"..","imges", img ))
    if(path.exists(file_location)):
        return FileResponse("app/imges/"+img)
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="file does not exist")

@router.delete("/{id}")
def delete(id:int,collection_service:CollectionService=Depends(get_collection_db)):
    try:
        collection_service.delete_collection(id)
    except NotFoundError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Collection not found")