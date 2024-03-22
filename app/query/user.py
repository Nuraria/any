from sqlalchemy.orm import Session
from app.schemas import User as UserSchema
from app.models import User
from app.registry import create,get_with_conditions

class UserService():
    _db:Session

    def __init__(self,db:Session) -> None:
        self._db=db

    def create_user(self,user:UserSchema):
        return create(User,self._db,user)

    def get_user(self,user:UserSchema):
        return get_with_conditions(User,self._db,user.model_dump())