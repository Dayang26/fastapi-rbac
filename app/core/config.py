# app/core/config.py

from pydantic import SecretStr
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: SecretStr
    SECRET_KEY: SecretStr
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    DEBUG: bool = False
    LOG_LEVEL: str = "INFO"  # 可选项：TRACE/DEBUG/INFO/WARNING/ERROR/CRITICAL

    # API_PREFIX: str

    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'  # 重要：处理中文环境


settings = Settings()
