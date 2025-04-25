# app/db/base.py


from sqlalchemy.ext.declarative import declarative_base
from sqlmodel import SQLModel

# 声明两个独立的Base类
SqlAlchemyBase = declarative_base()  # 用于纯SQLAlchemy模型
SqlModelBase = SQLModel              # 用于SQLModel模型

# RBAC模型必须全部使用SqlAlchemyBase
Base = SqlAlchemyBase  # 主Base指向SQLAlchemy的Base
