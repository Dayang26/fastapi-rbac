# app/models/role_permissions.py
from sqlalchemy import Column, Integer, TIMESTAMP
from app.db.base import Base
from datetime import datetime, timezone


class RolePermission(Base):
    __tablename__ = "db_role_permissions"

    role_id = Column(Integer, primary_key=True)
    permission_id = Column(Integer, primary_key=True)
    created_at = Column(TIMESTAMP, default=lambda: datetime.now(timezone.utc))
    updated_at = Column(TIMESTAMP, default=lambda: datetime.now(timezone.utc),
                        onupdate=lambda: datetime.now(timezone.utc))