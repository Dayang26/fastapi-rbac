# app/auth/dependencies/user_db.py

from typing import AsyncGenerator

from fastapi import Depends
from fastapi_users.db import SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth.managers.user import UserManager
from app.auth.models.user import User
from app.db.session import get_session


async def get_user_db(session: AsyncSession = Depends(get_session)) -> AsyncGenerator:
    yield SQLAlchemyUserDatabase(session, User)


async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)


