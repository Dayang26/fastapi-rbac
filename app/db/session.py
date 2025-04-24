# app/db/session.py
from sqlmodel import create_engine, Session

from app.core.config import settings

# 创建数据库引擎

# SQLModel风格的引擎配置
engine = create_engine(
    settings.DATABASE_URL.get_secret_value(),
    echo=True,  # 显示SQL语句(开发环境)
    pool_pre_ping=True,  # 连接前检查
    pool_size=20,  # 连接池大小
    max_overflow=10  # 最大溢出连接数
)

# 创建数据库会话
# 获取会话的依赖项
def get_session():
    with Session(engine) as session:
        yield session