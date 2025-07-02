# app/main.py

from fastapi import FastAPI

from app.core.lifespan import lifespan
from app.core.global_exception import global_exception
from app.core.router_loader import router_loader

# 创建 FastAPI 应用，传入 lifespan 生命周期
app = FastAPI(lifespan=lifespan)

# 注册全局异常处理器
app.add_exception_handler(Exception, global_exception)

# 自动注册所有 controller 里的 router
router_loader(app)
