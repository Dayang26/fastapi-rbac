# app/models/permission.py

from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime, timezone
from typing import Optional, List

from app.models.role_permissions import RolePermissionLink  # 引入关联表


class Permission(SQLModel, table=True):
    __tablename__ = "db_permissions"

    # 权限 ID（主键）
    id: Optional[int] = Field(default=None, primary_key=True, index=True)

    # 权限唯一标识
    code: str = Field(nullable=False, unique=True, max_length=50)

    # 权限描述
    name: str = Field(nullable=False, max_length=100)

    # 时间戳（UTC）
    created_at: Optional[datetime] = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        sa_column_kwargs={"onupdate": lambda: datetime.now(timezone.utc)}
    )
    # 与角色的多对多关系（通过无外键的中间表）
    roles: List["Role"] = Relationship(
        back_populates="permissions",
        link_model=RolePermissionLink
    )
