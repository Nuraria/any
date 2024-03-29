from fastapi import APIRouter,Depends,HTTPException, status
from .dependencies import get_collection_db
from app.schemas import Collection,CollectionCreate,CollectionUpdate
from app.query import CollectionService
from app.exceptions import NotFoundError

router=APIRouter(prefix="/collection")

@router.get("/")
def get_all(collection_service:CollectionService=Depends(get_collection_db)):
    return collection_service.get_all_collections()

@router.post("/")
def create(collection:CollectionCreate,collection_service:CollectionService=Depends(get_collection_db)):
    try:
        return collection_service.create_collection(collection)
    except NotFoundError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Category does not exist")

@router.patch("/{id}")
def update(collection:CollectionUpdate,id:int,collection_service:CollectionService=Depends(get_collection_db)):
    try:
        collection_service.update_collection(id,collection)
    except NotFoundError:
        raise HTTPException(status_code=status)

@router.get("/{id}",response_model=list[Collection])
def get(id:int,collection_service:CollectionService=Depends(get_collection_db)):
    return collection_service.get_collections_by_category(id)

@router.delete("/{id}")
def delete(id:int,collection_service:CollectionService=Depends(get_collection_db)):
    try:
        collection_service.delete_collection(id)
    except NotFoundError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Collection not found")