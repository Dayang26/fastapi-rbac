from passlib.context import CryptContext
from app.schemas.user import PasswordStr

# 配置密码哈希上下文
pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto",
    bcrypt__rounds=12  # 适当增加计算强度
)

def get_password_hash(password: PasswordStr) -> str:
    """生成带盐值的密码哈希"""
    return pwd_context.hash(password)

def verify_password(plain_password: PasswordStr, hashed_password: str) -> bool:
    """验证密码与哈希是否匹配"""
    return pwd_context.verify(plain_password, hashed_password)