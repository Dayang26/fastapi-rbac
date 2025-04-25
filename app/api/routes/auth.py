# app/api/routes/auth.py


from fastapi import APIRouter
from app.auth.dependencies.user_db import fastapi_users

router = APIRouter()

# 注册用户路由
router.include_router(
    fastapi_users.get_register_router(),  # 自动提供的注册路由
    prefix="/auth",
    tags=["auth"],
)