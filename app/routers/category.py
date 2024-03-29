from fastapi import APIRouter,Depends, HTTPException,status
from .dependencies import get_category_db
from app.schemas import Category,CategoryCreate,CategoryUpdate
from app.query import CategoryService
from app.exceptions import NotFoundError

router=APIRouter(prefix="/category")

@router.post("/")
def create(category:CategoryCreate,category_service:CategoryService=Depends(get_category_db)):   
    return category_service.create_category(category)

@router.patch("/{id}")
def update(category:CategoryUpdate,id:int,category_service:CategoryService=Depends(get_category_db)):
    try: 
        category_service.update_category(id,category)
    except NotFoundError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="category does not exist")

@router.get("/",response_model=list[Category])
def get(category_service:CategoryService=Depends(get_category_db)):
    return category_service.get_all_categories()

@router.delete("/")
def delete(id:int,category_service:CategoryService=Depends(get_category_db)):
    try:
        category_service.delete_category(id)
    except NotFoundError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="category does not exist")