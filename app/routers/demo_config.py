from fastapi import APIRouter
from app.config import settings

router = APIRouter()

@router.get("/")
async def get_config():
    return {'test': settings.some_random_string}