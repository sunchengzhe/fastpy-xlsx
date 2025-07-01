# app/core/lifespan.py

from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.core.database import MAIN_DB, SLAVE_DB


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("🚀 正在连接数据库")
    await MAIN_DB.connect()
    await SLAVE_DB.connect()
    print("✅ 数据库连接成功")

    yield  # 应用运行中

    print("🧹 正在断开数据库连接")
    await MAIN_DB.disconnect()
    await SLAVE_DB.disconnect()
    print("✅ 数据库已断开")
