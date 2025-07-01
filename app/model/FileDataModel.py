# app/model/FileDataModel.py
from fastapi import Depends
from databases import Database

from app.util.singleton import singleton
from app.model.Model import Model
from app.util.DBBuilder import MAIN_DB

@singleton
class FileDataModel(Model):
    def __init__(self, database: Database = Depends(lambda: MAIN_DB)):
        super().__init__(database)

    def table(self) -> str:
        return "t_file_data"
