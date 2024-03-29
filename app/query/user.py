from sqlalchemy.orm import Session
from app.schemas import User as UserSchema
from app.models import User
from app.registry import create,get_with_conditions
from app.exceptions import NotFoundError

class UserService():
    _db:Session

    def __init__(self,db:Session) -> None:
        self._db=db

    def create_user(self,user:UserSchema):
        return create(User,self._db,user)

    def get_user(self,user:UserSchema):
        user=get_with_conditions(User,self._db,user.model_dump())
        if user is None:
            raise NotFoundError
        return user