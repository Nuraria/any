from app.database import LocalSession
from fastapi import Depends
from sqlalchemy.orm import Session
from app.query import UserService,CollectionService,CategoryService,ProductService

def get_db():
    db=LocalSession()
    try:
        yield db
    finally:
        db.close()

def get_user_db(db:Session=Depends(get_db)):
    yield UserService(db)

def get_category_db(db:Session=Depends(get_db)):
    yield CategoryService(db)

def get_product_db(db:Session=Depends(get_db)):
    yield ProductService(db,get_collection_db(db,get_category_db(db)))

def get_collection_db(db:Session=Depends(get_db)):
    yield CollectionService(db)



