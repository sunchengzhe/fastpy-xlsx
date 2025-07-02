# app/util/database.py

from databases import Database

# 数据库连接配置
MAIN_URL = "mysql+aiomysql://root:123456@192.168.51.104:3307/fastpy-main?pool_recycle=600"
SLAVE_URL = "mysql+aiomysql://root:123456@192.168.51.104:3307/fastpy-slave?pool_recycle=600"

# 创建数据库连接实例（会被 FastAPI 启动时 connect）
MAIN_DB = Database(MAIN_URL)
SLAVE_DB = Database(SLAVE_URL)
