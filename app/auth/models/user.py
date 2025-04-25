# app/auth/models/user_db.py
from sqlalchemy import Column, String, Boolean, Integer
from sqlalchemy.orm import relationship

from app.db.base import Base
from app.db.mixins import TimestampMixin


class User(Base, TimestampMixin):
    __tablename__ = "db_users"

    id = Column(Integer, primary_key=True)
    email = Column(String(255), unique=True, index=True)
    hashed_password = Column(String(255))
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)
    is_verified = Column(Boolean, default=False)

    # 逻辑关系：指定逻辑外键
    roles = relationship(
        "Role",
        secondary="db_user_roles",  # 中间表
        back_populates="users",
        # foreign_keys="[UserRole.user_id]",  # 指定逻辑外键
        primaryjoin="User.id == foreign(UserRole.user_id)",  # 明确指定如何连接
        secondaryjoin="Role.id == foreign(UserRole.role_id)",  # 明确指定如何连接
    )
