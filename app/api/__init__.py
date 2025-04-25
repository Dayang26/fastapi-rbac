from fastapi import APIRouter
from app.api.routes import role

api_router = APIRouter()
api_router.include_router(role.router, prefix="/api", tags=["Role"])
