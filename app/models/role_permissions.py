# app/models/role_permissions.py

from sqlmodel import SQLModel, Field
from datetime import datetime, timezone
from typing import Optional


class RolePermissionLink(SQLModel, table=True):
    __tablename__ = "db_role_permissions"

    # 角色 ID（作为联合主键）
    role_id: int = Field(default=None, primary_key=True)

    # 权限 ID（作为联合主键）
    permission_id: int = Field(default=None, primary_key=True)

    # 创建时间 & 更新时间（UTC）
    created_at: Optional[datetime] = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        sa_column_kwargs={"onupdate": lambda: datetime.now(timezone.utc)}
    )
