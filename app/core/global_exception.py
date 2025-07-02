# app/util/global_exception.py

from fastapi import Request
from fastapi.responses import JSONResponse

from app.util.res_util import ResUtil


# 自定义业务异常类定义区
class SystemException(Exception):
    def __init__(self, message="业务异常", code=4000):
        self.message = message
        self.code = code


# FastAPI 全局异常处理器
async def global_exception(request: Request, exception: Exception):
    # 自定义业务异常
    if isinstance(exception, SystemException):
        return JSONResponse(
            status_code=200,
            content=ResUtil.fail(exception.message, exception.code)
        )

    # 系统错误（兜底）
    return JSONResponse(
        status_code=500,
        content=ResUtil.fail(str(exception))
    )
