# app/service/file_job_service.py

from fastapi import Depends

from app.core.singleton import singleton
from app.model.file_job_model import FileJobModel
from app.service.file_data_service import FileDataService


@singleton
class FileJobService:
    def __init__(self, file_job_model: FileJobModel = Depends(FileJobModel.instance),
                 file_data_service: FileDataService = Depends(FileDataService.instance)):
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
