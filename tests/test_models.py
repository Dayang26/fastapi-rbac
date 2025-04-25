import sys
from pathlib import Path

# 将项目根目录添加到Python路径
sys.path.append(str(Path(__file__).parent.parent))

from app.models.base import RBACBase
from sqlmodel import create_engine, inspect


engine = create_engine("mysql+pymysql://aaron:nos000000@localhost/dev_ai")


def test_table_structure():
    inspector = inspect(engine)

    # 验证五张表是否存在
    tables = inspector.get_table_names()
    assert "db_users" in tables
    assert "db_roles" in tables
    assert "db_permissions" in tables
    assert "db_user_roles" in tables
    assert "db_role_permissions" in tables

    # 验证用户表字段
    user_columns = [col["name"] for col in inspector.get_columns("db_users")]
    assert "email" in user_columns
    assert "hashed_password" in user_columns
    assert "is_active" in user_columns