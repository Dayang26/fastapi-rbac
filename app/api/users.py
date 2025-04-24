from fastapi import APIRouter, Depends, status
from sqlmodel import Session

from app.db.session import get_session
from app.schemas.user import UserCreateRequest, UserResponse
from app.services.user_service import UserService

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={
        status.HTTP_400_BAD_REQUEST: {"description": "无效输入"},
        status.HTTP_409_CONFLICT: {"description": "资源冲突"}
    }
)

@router.post(
    "/",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
    responses={
        status.HTTP_201_CREATED: {
            "description": "用户创建成功",
            "content": {
                "application/json": {
                    "example": {
                        "id": 1,
                        "email": "user@example.com",
                        "is_active": True,
                        "created_at": "2023-01-01T00:00:00Z"
                    }
                }
            }
        }
    }
)
async def create_user(
    user_data: UserCreateRequest,
    db: Session = Depends(get_session())
):
    """创建新用户"""
    service = UserService(db)
    return await service.create_user(user_data)