from fastapi import FastAPI
from app.routers import category_router,collection_router,user_router,product_router
from app.models import Base
from app.database import engine
Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

app=FastAPI()

app.include_router(router=category_router)
app.include_router(router=collection_router)
app.include_router(router=user_router)
app.include_router(router=product_router)