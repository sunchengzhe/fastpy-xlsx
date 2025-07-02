# app/controller/main_controller.py

from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def root():
    return {"message": "Hello, FastAPI!"}
