from fastapi import APIRouter,Depends
from .dependencies import get_category_db
from app.schemas import Category,CategoryCreate,CategoryUpdate
from app.query import CategoryService

router=APIRouter(prefix="/category")

@router.post("/create/")
def create(category:CategoryCreate,category_service:CategoryService=Depends(get_category_db)):
    return category_service.create_category(category)

@router.patch("/update/{id}")
def update(category:CategoryUpdate,id:int,category_service:CategoryService=Depends(get_category_db)):
    return category_service.update_category(id,category)

@router.get("/get/",response_model=list[Category])
def get(category_service:CategoryService=Depends(get_category_db)):
    return category_service.get_category()

@router.delete("/delete/")
def delete(id:int,category_service:CategoryService=Depends(get_category_db)):
    return category_service.delete_category(id)