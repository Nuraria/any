from fastapi import APIRouter,Depends
from .dependencies import get_user_db
from app.schemas import User
from app.query import UserService



router=APIRouter(prefix="/user")

@router.post("/create/")
def create(user:User,user_service:UserService=Depends(get_user_db)):
    return user_service.create_user(user)

@router.post("/validate/")
def validate(user:User,user_service:UserService=Depends(get_user_db)):
    return user_service.get_user(user)