from app.database import Base
from sqlalchemy import Column,Integer,String,ForeignKey,Float, Text
class User(Base):
    __tablename__="user"
    id = Column(Integer,primary_key=True)
    login = Column(String(25))
    password = Column(String(70))

class Collection(Base):
    __tablename__="collection"
    id=Column(Integer,primary_key=True)
    img=Column(String(255))
    category_id=Column(Integer, ForeignKey("category.id"))

class Category(Base):
    __tablename__="category"
    id = Column(Integer,primary_key=True)
    category_name=Column(String(50))
    color= Column(String(15))

class Product(Base):
    __tablename__="products"
    id = Column(Integer,primary_key=True)
    parent_collection=Column(Integer,ForeignKey("collection.id"))
    price = Column(Integer)
    description = Column(Text)
    positionx=Column(Float)
    positiony=Column(Float)
    name = Column(String(70)) 