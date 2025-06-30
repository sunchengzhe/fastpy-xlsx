# app/util/DBBuilder.py
from databases import Database

# 数据库连接配置
DATABASE_URL = "mysql+aiomysql://root:123456@192.168.51.104:3307/pythonXlsx?pool_recycle=600"

# 创建数据库连接实例（会被 FastAPI 启动时 connect）
database = Database(DATABASE_URL)