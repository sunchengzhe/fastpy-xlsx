# app/service/FileJobService.py

from app.model.FileJob2Model import FileJob2Model
from app.service.FileData2Service import FileData2Service

class FileJob2Service:
    _instance = None

    def __init__(self, file_job2_model: FileJob2Model, file_data2_service: FileData2Service):
        self.file_job2_model = file_job2_model
        self.file_data2_service = file_data2_service

    @classmethod
    def get_instance(cls) -> "FileJob2Service":
        if cls._instance is None:
            model = FileJob2Model.get_instance()
            service = FileData2Service.get_instance()
            cls._instance = cls(model, service)
        return cls._instance

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
