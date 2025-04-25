# app/auth/models/role.py
from sqlalchemy import Column, String, Text, Integer
from sqlalchemy.orm import relationship

from app.db.base import Base
from app.db.mixins import TimestampMixin


class Role(Base,TimestampMixin):
    __tablename__ = "db_roles"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, index=True)
    description = Column(Text)

    # 用户关系
    users = relationship(
        "User",
        secondary="db_user_roles",
        back_populates="roles",
        # foreign_keys="[UserRole.role_id]",
        primaryjoin="Role.id == foreign(UserRole.role_id)",  # 明确指定如何连接
        secondaryjoin="User.id == foreign(UserRole.user_id)",  # 明确指定如何连接
    )

    # 权限关系（更新版）
    permissions = relationship(
        "Permission",
        secondary="db_role_permissions",
        back_populates="roles",
        primaryjoin="Role.id == foreign(RolePermission.role_id)",  # 明确指定如何连接
        secondaryjoin="Permission.id == foreign(RolePermission.permission_id)",  # 明确指定如何连接
    )
