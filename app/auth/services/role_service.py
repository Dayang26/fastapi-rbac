from sqlalchemy.ext.asyncio import AsyncSession
from app.auth.models.role import Role
from app.schemas.auth.role import RoleCreate


async def create_role(role_in: RoleCreate, db: AsyncSession) -> Role:
    new_role = Role(**role_in.dict())
    db.add(new_role)
    await db.flush()  # 获取ID或其他更新字段
    return new_role
