# app/service/FileJobService.py
from functools import lru_cache

from fastapi import Depends

from app.model.FileJob2Model import FileJob2Model, get_file_job2_model_singleton
from app.service.FileData2Service import FileData2Service, get_file_data2_service_singleton

@lru_cache()
def get_file_job2_service_singleton() -> "FileJob2Service":
    return FileJob2Service(
        file_job2_model=get_file_job2_model_singleton(),
        file_data2_service=get_file_data2_service_singleton()
   )

class FileJob2Service:
    def __init__(
        self,
        file_job2_model: FileJob2Model = Depends(get_file_job2_model_singleton),
        file_data2_service: FileData2Service = Depends(get_file_data2_service_singleton)
    ):
        self.file_job2_model = file_job2_model
        self.file_data2_service = file_data2_service

    async def test_set_data(self):
        result = await self.file_data2_service.test_set_data()
        print(result)

        # 插入一条数据
        new_id = await self.file_job2_model.insert({
            "username": "eadmin1",
            "trace_id": "adsasdas1",
            "status": "ready",
        })

        return {'id': new_id}
