# app/model/FileJobModel.py
from app.model.Model2 import Model2
from databases import Database

class FileJob2Model():
    def __init__(self):
        self.connection = 'database'

    def get_connection(self):
        return self.connection

    def table(self):
        return self.connection
