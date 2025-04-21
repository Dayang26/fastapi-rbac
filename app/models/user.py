from sqlalchemy import Column, Integer, ForeignKey
from fastapi_users.db import SQLAlchemyBaseUserTable
from app.db.session import Base


class User(SQLAlchemyBaseUserTable[int],Base):
    __tablename__ = "db_users"  # 对应已有表名
    role_id = Column(Integer, ForeignKey("roles.id"))  # 复用现有字段