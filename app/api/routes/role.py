# app/api/routes/role.py

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_session
from app.auth.services.role_service import create_role
from app.schemas.auth.role import RoleRead, RoleCreate

router = APIRouter()


@router.post("/roles", response_model=RoleRead)
async def create_role_api(
    role_in: RoleCreate,
    db: AsyncSession = Depends(get_session),
):
    role = await create_role(role_in, db)
    return role
