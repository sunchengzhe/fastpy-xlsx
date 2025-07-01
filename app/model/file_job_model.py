# app/model/file_job_model.py
from fastapi import Depends
from databases import Database

from app.core.singleton import singleton
from app.model.model import Model
from app.core.database import MAIN_DB


@singleton
class FileJobModel(Model):
    def __init__(self, database: Database = Depends(lambda: MAIN_DB)):
        super().__init__(database)

    def table(self) -> str:
        return "t_file_job"
