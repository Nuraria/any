from sqlalchemy.orm import Session
from pydantic import BaseModel

def get(table,db:Session):
    return db.query(table).all()

def get_with_conditions(table,db:Session,condition:dict):
    return db.query(table).filter_by(**condition).all()

def create(table,db:Session,data:BaseModel):
    new_row=table(**data.model_dump())
    db.add(new_row)
    db.commit()
    db.refresh(new_row)
    return new_row

def update(table,db:Session,id:int,set:dict):
    return db.query(table).filter_by(id=id).update(set)

def delete(table,db:Session,id:int):
    return db.query(table).filter_by(id=id).delete()