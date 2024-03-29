from fastapi import APIRouter,Depends
from .dependencies import get_collection_db
from app.schemas import Collection,CollectionCreate,CollectionUpdate
from app.query import CollectionService

router=APIRouter(prefix="/collection")

@router.get("/")
def get_all(collection_service:CollectionService=Depends(get_collection_db)):
    return collection_service.get_all_collections()

@router.post("/")
def create(collection:CollectionCreate,collection_service:CollectionService=Depends(get_collection_db)):
    return collection_service.create_collection(collection)

@router.patch("/{id}")
def update(collection:CollectionUpdate,id:int,collection_service:CollectionService=Depends(get_collection_db)):
    return collection_service.update_collection(id,collection)

@router.get("/{id}",response_model=list[Collection])
def get(id_id:int,collection_service:CollectionService=Depends(get_collection_db)):
    return collection_service.get_collections_by_category(id_id)

@router.delete("/{id}")
def delete(id:int,collection_service:CollectionService=Depends(get_collection_db)):
    return collection_service.delete_collection(id)