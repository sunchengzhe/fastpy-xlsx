# app/service/FileJobService.py
from app.model.FileJobModel import FileJobModel
from app.service.FileDataService import FileDataService


class FileJobService:
    def __init__(self, file_job_model: FileJobModel, file_data_service: FileDataService):
        self.file_job_model = file_job_model
        self.file_data_service = file_data_service

    async def test_set_data(self):
        result = await self.file_data_service.test_set_data()
        print(result)

        # 插入一条数据
        new_id = await self.file_job_model.insert({
            "username": "eadmin1",
            "trace_id": "adsasdas1",
            "status": "ready",
        })

        return {'id': new_id}

    async def test_get_data(self):
        # 模拟业务逻辑
        return {"value": "Here is your data"}
