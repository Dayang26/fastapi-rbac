#app/auth/models/role_permission.py

from sqlalchemy import Column, Integer

from app.db.base import Base
from app.db.mixins import TimestampMixin


class RolePermission(Base,TimestampMixin):
    __tablename__ = "db_role_permissions"

    # 只有普通字段
    role_id = Column(Integer, primary_key=True)  # 逻辑关联 roles.id
    permission_id = Column(Integer, primary_key=True)  # 逻辑关联 permissions.id

    __table_args__ = {
        "comment": "角色-权限逻辑关联表",
        "info": {"no_fk": True}  # 自定义标记
    }