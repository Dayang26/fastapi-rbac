# app/core/middleware.py
import time
from fastapi import HTTPException

from fastapi import Request

from starlette.middleware.base import BaseHTTPMiddleware
import uuid
from loguru import logger


class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # 生成或获取trace_id
        trace_id = request.headers.get('X-Request-ID') or str(uuid.uuid4())
        request.state.trace_id = trace_id
        start_time = time.time()

        # 结构化日志元数据（包含API路径）
        log_context = {
            "trace_id": trace_id,
            "client_ip": request.client.host if request.client else None,
            "user_agent": request.headers.get("user-agent"),
            "path": request.url.path,  # 已包含API路径
            "method": request.method,
            "query_params": dict(request.query_params)
        }

        logger.bind(**log_context).debug("Request started")

        try:
            response = await call_next(request)
            latency_ms = (time.time() - start_time) * 1000
            response_size = int(response.headers.get("content-length", 0))

            log_context.update({
                "status": response.status_code,
                "latency_ms": f"{latency_ms:.2f}",
                "response_size": response_size
            })

            # 统一日志消息格式
            log_message = (
                f"Status: {response.status_code} | "
                f"Latency: {latency_ms:.2f}ms | "
                f"Size: {response_size}B"
            )

            if response.status_code >= 500:
                logger.bind(**log_context).error(log_message)
            elif response.status_code >= 400:
                # 对于4xx错误，记录更多细节
                error_detail = getattr(response, "body", b"").decode() if hasattr(response, "body") else ""
                logger.bind(**log_context, error_detail=error_detail).warning(log_message)
            else:
                logger.bind(**log_context).info(log_message)

            response.headers["X-Trace-ID"] = trace_id
            return response

        except HTTPException as http_exc:
            # 处理FastAPI HTTP异常
            latency_ms = (time.time() - start_time) * 1000
            logger.bind(
                **log_context,
                status_code=http_exc.status_code,
                error_detail=http_exc.detail,
                latency_ms=f"{latency_ms:.2f}"
            ).error(
                f"Status: {http_exc.status_code} | "
                f"Detail: {http_exc.detail} | "
                f"Latency: {latency_ms:.2f}ms"
            )
            raise

        except Exception as e:
            # 处理未捕获异常
            latency_ms = (time.time() - start_time) * 1000
            logger.bind(
                **log_context,
                latency_ms=f"{latency_ms:.2f}"
            ).opt(exception=e).error(
                f"{request.method} {request.url.path} crashed - "
                f"Latency: {latency_ms:.2f}ms"
            )
            raise