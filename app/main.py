from contextlib import asynccontextmanager

from fastapi import FastAPI,Request

from app.api import users
from app.core.config import settings
from app.core.logging import logger
from app.core.middleware import LoggingMiddleware


@asynccontextmanager
async def lifespan(application: FastAPI):
    safe_config = settings.model_dump()
    safe_config.update({
        'DATABASE_URL': '***',
        'SECRET_KEY': '***'
    })
    if settings.DEBUG:
        logger.debug("Full config loaded (DEBUG ONLY): {}", settings.model_dump())
    else:
        logger.info("Starting with config: {}", safe_config)

    yield
    logger.warning("Shutting down")


app = FastAPI(lifespan=lifespan)

# 注册中间件（推荐使用add_middleware方式）
app.add_middleware(LoggingMiddleware)


# 注册路由
app.include_router(
    users.router,
    # prefix=settings.API_PREFIX  # 例如: /api/v1
)

@app.get("/")
async def root(request: Request):
    # 从请求中获取trace_id保持一致性
    logger.bind(trace_id=request.state.trace_id).info("Root endpoint accessed")
    return {
        "status": "ok",
        "trace_id": request.state.trace_id
    }