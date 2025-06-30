# app/service/FileJobService.py
from fastapi import Depends
from app.model.FileJob2Model import FileJob2Model


class FileJob2Service:
    def __init__(self, file_job2_model: FileJob2Model = Depends()):
        self.file_job2_model = file_job2_model

    async def test_set_data(self):

        # 插入一条数据
        new_id = await self.file_job2_model.insert({
            "username": "eadmin1",
            "trace_id": "adsasdas1",
            "status": "ready",
        })

        return {'id': new_id}

    async def get_connection(self):
        return self.file_job2_model.connection
