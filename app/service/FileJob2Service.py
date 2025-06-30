# app/service/FileJobService.py
from fastapi import Depends
from app.model.FileJob2Model import FileJob2Model


class FileJob2Service:
    def __init__(self, file_job2_model: FileJob2Model = Depends()):
        self.file_job2_model = file_job2_model

    async def test_set_data(self):
        return {'id': self.file_job2_model.connection}

    async def get_connection(self):
        return self.file_job2_model.connection
