# app/models/role.py
from datetime import datetime, timezone
from typing import Optional, List

from sqlmodel import SQLModel, Field, Relationship
from app.models.user_roles import UserRoleLink  # 引入关联表
from app.models.role_permissions import RolePermissionLink  # 引入关联表



class Role(SQLModel, table=True):
    __tablename__ = "db_roles"

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True, nullable=False, max_length=50)
    description: Optional[str] = Field(default=None, max_length=200)

    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )

    updated_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        sa_column_kwargs={"onupdate": lambda: datetime.now(timezone.utc)}
    )

    users: List["User"] = Relationship(
        back_populates="roles",
        link_model=UserRoleLink
    )

    permissions: List["Permission"] = Relationship(
        back_populates="roles",
        link_model=RolePermissionLink
    )


