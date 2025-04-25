# app/db/mixins.py（按需创建）
from sqlalchemy import Column, DateTime
from sqlalchemy.sql import func


class TimestampMixin:
    created_at = Column(DateTime, default=func.now(), nullable=False)
    updated_at = Column(
        DateTime, default=func.now(), onupdate=func.now(), nullable=False
    )

    # 禁用延迟加载
    __mapper_args__ = {
        'eager_defaults': True
    }