# app/model/FileData2Model.py
from databases import Database

from app.model.Model2 import Model2
from app.util.DBBuilder import MAIN_DB

class FileData2Model(Model2):
    _instance = None

    def __init__(self, database: Database):
        super().__init__(database)

    @classmethod
    def get_instance(cls) -> "FileData2Model":
        if cls._instance is None:
            cls._instance = cls(MAIN_DB)
        return cls._instance

    def table(self) -> str:
        return "t_file_data"
