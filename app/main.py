from fastapi import FastAPI
from app.routers import category_router,collection_router,user_router,product_router
from app.models import Base
from app.database import engine
from fastapi.middleware.cors import CORSMiddleware
Base.metadata.create_all(bind=engine)


app=FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router=category_router)
app.include_router(router=collection_router)
app.include_router(router=user_router)
app.include_router(router=product_router)