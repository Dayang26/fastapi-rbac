# app/models/role.py
from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.orm import relationship
from app.db.base import Base
from datetime import datetime, timezone


class Role(Base):
    __tablename__ = "db_roles"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True, nullable=False)
    description = Column(String(200))
    created_at = Column(TIMESTAMP, default=lambda: datetime.now(timezone.utc))
    updated_at = Column(TIMESTAMP, default=lambda: datetime.now(timezone.utc),
                        onupdate=lambda: datetime.now(timezone.utc))

    permissions = relationship("Permission", secondary="db_role_permissions", back_populates="roles")
    users = relationship("User", secondary="db_user_roles", back_populates="roles")

