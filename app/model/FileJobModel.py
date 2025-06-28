# app/model/FileJobModel.py
from app.model.Model import Model
from databases import Database

class FileJobModel(Model):
    def __init__(self, database: Database):
        super().__init__(database)

    def table(self) -> str:
        return "t_file_job"
