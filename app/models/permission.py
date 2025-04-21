# app/models/permission.py
from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.orm import relationship
from app.db.base import Base
from datetime import datetime, timezone


class Permission(Base):
    __tablename__ = "db_permissions"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(50), unique=True, nullable=False)  # 权限标识
    name = Column(String(100), nullable=False)  # 权限描述
    created_at = Column(TIMESTAMP, default=lambda: datetime.now(timezone.utc))
    updated_at = Column(TIMESTAMP, default=lambda: datetime.now(timezone.utc),
                        onupdate=lambda: datetime.now(timezone.utc))


roles = relationship("Role", secondary="db_role_permissions", back_populates="permissions")