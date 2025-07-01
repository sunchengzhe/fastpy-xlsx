# app/model/FileData2Model.py
from functools import lru_cache

from databases import Database

from app.model.Model2 import Model2
from app.util.DBBuilder import MAIN_DB

@lru_cache()
def get_file_data2_model_singleton() -> "FileData2Model":
    return FileData2Model(MAIN_DB)

class FileData2Model(Model2):
    def __init__(self, database: Database):
        super().__init__(database)

    def table(self) -> str:
        return "t_file_data"
