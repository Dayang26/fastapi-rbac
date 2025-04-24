from sqlmodel import select, Session
from app.models.user import User
from app.schemas.user import UserCreateRequest, UserResponse
from app.core.security import get_password_hash
from fastapi import HTTPException, status


class UserService:
    def __init__(self, session: Session):
        self.session = session

    async def create_user(self, user_data: UserCreateRequest) -> User:
        # 检查邮箱唯一性
        existing_user = self.session.exec(
            select(User).where(User.email == user_data.email)
        ).first()

        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="该邮箱已被注册",
                headers={"WWW-Authenticate": "Bearer"}
            )

        # 创建用户记录
        db_user = User(
            email=user_data.email,
            hashed_password=get_password_hash(user_data.password),
            is_active=True
        )

        try:
            self.session.add(db_user)
            self.session.commit()
            self.session.refresh(db_user)
            return db_user
        except Exception as e:
            self.session.rollback()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="用户创建失败"
            ) from e