# app/models/user_roles.py
from sqlalchemy import Column, Integer, TIMESTAMP
from app.db.base import Base
from datetime import datetime, timezone



class UserRole(Base):
    __tablename__ = "db_user_roles"

    user_id = Column(Integer, primary_key=True)
    role_id = Column(Integer, primary_key=True)
    created_at = Column(TIMESTAMP, default=lambda: datetime.now(timezone.utc))
    updated_at = Column(TIMESTAMP, default=lambda: datetime.now(timezone.utc),
                        onupdate=lambda: datetime.now(timezone.utc))