# app/auth/models/permission.py

from sqlalchemy import Column, String, Integer, Text
from sqlalchemy.orm import relationship
from app.db.base import Base
from app.db.mixins import TimestampMixin


class Permission(Base,TimestampMixin):
    __tablename__ = "db_permissions"

    id = Column(Integer, primary_key=True)
    code = Column(String(50), unique=True, comment="权限标识符")
    name = Column(String(100), comment="权限名称")
    description = Column(Text, comment="详细说明")

    # 逻辑关系（无物理外键）
    roles = relationship(
        "Role",
        secondary="db_role_permissions",
        back_populates="permissions",
        primaryjoin="Permission.id == foreign(RolePermission.permission_id)",  # 明确指定如何连接
        secondaryjoin="Role.id == foreign(RolePermission.role_id)",  # 明确指定如何连接
    )