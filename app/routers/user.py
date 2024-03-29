from fastapi import APIRouter,Depends,HTTPException,status
from .dependencies import get_user_db
from app.schemas import User
from app.query import UserService
from app.exceptions import NotFoundError



router=APIRouter(prefix="/user",tags=["user"])

@router.post("/")
def create(user:User,user_service:UserService=Depends(get_user_db)):
    return user_service.create_user(user)

@router.post("/validate/")
def validate(user:User,user_service:UserService=Depends(get_user_db)):
    try:
        return user_service.get_user(user)
    except NotFoundError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User not found")