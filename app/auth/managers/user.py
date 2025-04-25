# app/auth/managers/user_db.py

from fastapi_users.manager import BaseUserManager

from app.auth.models.user import User
from app.core.config import settings

UserDB = User  # 你用自己的 User 模型就行


class UserManager(BaseUserManager[UserDB, int]):  # 你用的是 int 主键
    reset_password_token_secret = settings.SECRET_KEY
    verification_token_secret = settings.SECRET_KEY

    async def on_after_register(self, user: UserDB, request=None):
        print(f"User {user.email} has registered.")

    async def on_after_forgot_password(self, user: UserDB, token: str, request=None):
        print(f"User {user.email} forgot their password. Reset token: {token}")

    async def on_after_request_verify(self, user: UserDB, token: str, request=None):
        print(f"Verification requested for user {user.email}. Token: {token}")
