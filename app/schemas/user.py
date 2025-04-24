# app/schemas/user.py


from datetime import datetime
from pydantic import BaseModel, EmailStr, Field, field_validator, model_validator
from typing import Optional, Annotated
from pydantic.functional_validators import AfterValidator

# 密码复杂度验证器
def validate_password_complexity(v: str) -> str:
    if len(v) < 8:
        raise ValueError("密码至少需要8个字符")
    if not any(c.isupper() for c in v):
        raise ValueError("密码需要包含大写字母")
    if not any(c.isdigit() for c in v):
        raise ValueError("密码需要包含数字")
    return v

# 使用类型注解应用验证器
PasswordStr = Annotated[str, Field(min_length=8), AfterValidator(validate_password_complexity)]

class UserCreateRequest(BaseModel):
    email: EmailStr = Field(..., example="user@example.com")
    password: PasswordStr = Field(..., example="SecurePass123")
    password_confirm: str = Field(..., example="SecurePass123")

    @model_validator(mode="after")
    def check_passwords_match(self) -> "UserCreateRequest":
        if self.password != self.password_confirm:
            raise ValueError("两次输入的密码不一致")
        return self

    class Config:
        json_schema_extra = {
            "example": {
                "email": "user@example.com",
                "password": "SecurePass123",
                "password_confirm": "SecurePass123"
            }
        }


class UserResponse(BaseModel):
    id: int = Field(..., example=1)
    email: EmailStr = Field(..., example="user@example.com")
    is_active: bool = Field(default=True, example=True)
    created_at: datetime = Field(..., example="2023-01-01T00:00:00Z")

    @field_validator("email")
    @classmethod
    def email_must_contain_at(cls, v: str) -> str:
        if "@" not in v:
            raise ValueError("邮箱格式不正确")
        return v.lower()