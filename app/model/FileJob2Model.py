# app/model/FileJobModel.py
from app.model.Model2 import Model2
from databases import Database

class FileJob2Model(Model2):
    def __init__(self, database: Database):
        self.connection = database

    def get_connection(self):
        return self.connection

    def table(self):
        return self.connection
