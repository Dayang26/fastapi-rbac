# app/db/session.py

from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlmodel.ext.asyncio.session import AsyncSession as SQLModelAsyncSession

from app.core.config import settings

# 确保使用正确的连接字符串格式
DATABASE_URL = settings.DATABASE_URL.get_secret_value().replace(
    "mysql+pymysql", "mysql+aiomysql"
)



# 2. 创建共享引擎（关键修改）
engine = create_async_engine(
    DATABASE_URL,
    echo=True,
    pool_pre_ping=True,
    pool_size=20,
    max_overflow=10,
    connect_args={
        "connect_timeout": 30,
    },
)

# 3. 创建统一会话工厂（核心修改）
SessionLocal = async_sessionmaker(
    bind=engine,
    class_=SQLModelAsyncSession,  # 优先使用SQLModel的AsyncSession
    expire_on_commit=False,
    autoflush=False,  # 必须添加
    future=True  # 确保使用2.0风格API
)

# 4. 获取会话的依赖项（优化版）
async def get_session() -> AsyncGenerator[SQLModelAsyncSession, None]:
    async with SessionLocal() as session:
        try:
            yield session
            await session.commit()  # 自动提交
        except Exception:
            await session.rollback()  # 自动回滚
            raise
        finally:
            await session.close()  # 确保关闭