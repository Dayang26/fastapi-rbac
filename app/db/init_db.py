# app/db/init_db.py

from session import engine


async def init_db():
    from base import Base
    from sqlmodel import SQLModel

    async with engine.begin() as conn:
        # 同时创建两类表
        await conn.run_sync(Base.metadata.create_all)
        await conn.run_sync(SQLModel.metadata.create_all)
