# app/models/User.py

from datetime import datetime, timezone
from typing import Optional, List

from sqlmodel import SQLModel, Field, Relationship

from app.models.user_roles import UserRoleLink  # 引入关联表


class User(SQLModel, table=True):
    __tablename__ = "db_user"

    # 主键 ID
    id: Optional[int] = Field(default=None, primary_key=True, index=True)

    # 用户邮箱（唯一）
    email: str = Field(index=True, nullable=False, max_length=255)

    # 加密后的密码
    hashed_password: str = Field(nullable=False, max_length=255)

    # 是否激活
    is_active: bool = Field(default=True)

    # 创建和更新时间（UTC）
    created_at: Optional[datetime] = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        sa_column_kwargs={"onupdate": lambda: datetime.now(timezone.utc)}
    )
    # 与角色的多对多关系（中间表无外键）
    roles: List["Role"] = Relationship(
        back_populates="users",
        link_model=UserRoleLink
    )