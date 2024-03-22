from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

connection_string="mysql+pymysql://root@localhost:3306/mydb"

engine=create_engine(connection_string,echo=True)

LocalSession=sessionmaker(bind=engine,autoflush=False)

Base=declarative_base()
