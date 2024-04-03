from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import time

connection_string="mysql+pymysql://root@database:3306/mydb"
time.sleep(30)
engine=create_engine(connection_string,echo=True)

LocalSession=sessionmaker(bind=engine,autoflush=False)

Base=declarative_base()
