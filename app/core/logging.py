# app/core/logging.py
import json
import sys
from pathlib import Path
from loguru import logger

from app.core.config import settings

LOG_DIR = Path("logs")
LOG_DIR.mkdir(parents=True, exist_ok=True)

# 移除默认配置
logger.remove()

# 增强版日志格式
ENHANCED_FORMAT = (
    "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | "
    "<level>{level: <8}</level> | "
    "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> | "
    "<magenta>trace_id={extra[trace_id]}</magenta> | "
    "<yellow>ip={extra[client_ip]}</yellow> | "
    "<blue>ua={extra[user_agent]}</blue> | "
    "<cyan>path={extra[path]}</cyan> | "
    "<magenta>method={extra[method]}</magenta> | "
    "<yellow>params={extra[query_params]}</yellow> | "
    "<level>{message}</level>"
)

# 开发环境控制台输出
if settings.DEBUG:
    logger.add(
        sys.stderr,
        format=ENHANCED_FORMAT,
        level=settings.LOG_LEVEL,
        colorize=True,
        backtrace=True,
        diagnose=True
    )

# 文件日志配置（结构化JSON格式）
logger.add(
    LOG_DIR / "rbac_{time:YYYY-MM-DD}.log",
    rotation="100 MB",
    retention="30 days",
    format="{message}",
    serialize=True,  # 自动转为JSON
    level="INFO",
    enqueue=True
)

# 初始化默认上下文
logger.configure(extra={
    "trace_id": "SYSTEM",
    "client_ip": "",
    "user_agent": "",
    "path": "",
    "method": "",
    "query_params": ""
})