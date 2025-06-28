# app/util/Container.py

from dependency_injector import containers, providers
from databases import Database
from app.model.FileDataModel import FileDataModel
from app.model.FileJobModel import FileJobModel
from app.service.FileDataService import FileDataService
from app.service.FileJobService import FileJobService


class Container(containers.DeclarativeContainer):
    # 0. 自动装配容器
    wiring_config = containers.WiringConfiguration(modules=["app.main"])

    # 1. 注册 数据库
    database = providers.Singleton(Database,"mysql+aiomysql://root:123456@192.168.51.104:3307/pythonXlsx?pool_recycle=600")

    # 2. 注册 Model
    file_job_model = providers.Singleton(FileJobModel, database=database)
    file_data_model = providers.Singleton(FileDataModel, database=database)

    # 3. 注册 Service
    file_data_service = providers.Singleton(
        FileDataService,
        file_data_model=file_data_model
    )
    file_job_service = providers.Singleton(
        FileJobService,
        file_job_model=file_job_model,
        file_data_service=file_data_service,
    )
