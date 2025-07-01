# app/main.py
from fastapi import FastAPI
from fastapi import Depends

from app.core.lifespan import lifespan
from app.core.exception import global_exception

from app.util.res_util import ResUtil
from app.service.file_job_service import FileJobService

# 创建 FastAPI 应用，传入 lifespan 生命周期
app = FastAPI(lifespan=lifespan)

# 注册全局异常处理器
app.add_exception_handler(Exception, global_exception)


@app.get("/")
async def root():
    return {"message": "Hello, FastAPI!"}


@app.get("/testSetData")
async def test_set_data(file_job_service: FileJobService = Depends(FileJobService.instance)):
    result = await file_job_service.test_set_data()

    return ResUtil.success(result)
