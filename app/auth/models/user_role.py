# app/auth/models/user_role.py
from sqlalchemy import Column, Integer

from app.db.base import Base
from app.db.mixins import TimestampMixin


class UserRole(Base, TimestampMixin):
    __tablename__ = "db_user_roles"

    # 只有普通字段，无ForeignKey约束
    user_id = Column(Integer, primary_key=True)  # 逻辑关联users.id
    role_id = Column(Integer, primary_key=True)  # 逻辑关联roles.id

    __table_args__ = {
        "comment": "用户-角色逻辑关联表",
        "info": {"no_fk": True}  # 自定义标记
    }
