# app/main.py
from fastapi import FastAPI
from fastapi import Depends
from fastapi import Request
from fastapi.responses import JSONResponse
from contextlib import asynccontextmanager

from app.service.FileJob2Service import FileJob2Service, get_file_job2_service_singleton
from app.util.SystemException import SystemException
from app.util.Res import Res
from app.util.DBBuilder import MAIN_DB
from app.util.DBBuilder import SLAVE_DB


# 定义 lifespan 生命周期上下文
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("🚀 正在连接数据库")
    await MAIN_DB.connect()
    await SLAVE_DB.connect()
    print("✅ 数据库连接成功")

    yield  # 等待 app 运行

    print("🧹 正在断开数据库连接")
    await MAIN_DB.disconnect()
    await SLAVE_DB.disconnect()
    print("✅ 数据库已断开")


# 创建 FastAPI 应用，传入 lifespan 生命周期
app = FastAPI(lifespan=lifespan)


# 全局异常处理器
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exception: Exception):
    # 如果是我们自定义的业务异常
    if isinstance(exception, SystemException):
        return JSONResponse(
            status_code=200,
            content=Res.fail(message=exception.message, code=exception.code)
        )

    # 系统错误（兜底）
    return JSONResponse(
        status_code=500,
        content=Res.fail(message=str(exception), code=9999)
    )


@app.get("/")
async def root():
    return {"message": "Hello, FastAPI!"}

# @app.get("/testSetData")
# async def test_set_data(file_job_service: FileJobService = Depends(lambda: container.file_job_service())):
#     result = await file_job_service.test_set_data()
#
#     return Res.success(result)
#
#
# @app.get("/testGetData")
# async def test_get_data(file_job_service: FileJobService = Depends(lambda: container.file_job_service())):
#     result = await file_job_service.test_get_data()
#
#     return Res.success(result)



@app.get("/testSetData2")
async def test_set_data(file_job2_service: FileJob2Service = Depends(get_file_job2_service_singleton)):
    result = await file_job2_service.test_set_data()

    return Res.success(result)
