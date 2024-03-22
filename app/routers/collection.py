from fastapi import APIRouter,Depends
from .dependencies import get_collection_db
from app.schemas import Collection,CollectionCreate,CollectionUpdate
from app.query import CollectionService

router=APIRouter(prefix="/collection")

@router.post("/create/")
def create(collection:CollectionCreate,collection_service:CollectionService=Depends(get_collection_db)):
    return collection_service.create_collection(collection)

@router.patch("/update/{id}")
def update(collection:CollectionUpdate,id:int,collection_service:CollectionService=Depends(get_collection_db)):
    return collection_service.update_collection(id,collection)

@router.post("/get/",response_model=list[Collection])
def get(collection_id:int,collection_service:CollectionService=Depends(get_collection_db)):
    return collection_service.get_collections_by_category(collection_id)

@router.delete("/delete/")
def delete(id:int,collection_service:CollectionService=Depends(get_collection_db)):
    return collection_service.delete_collection(id)