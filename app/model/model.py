# app/model/model.py

from fastapi import Depends
from abc import ABC, abstractmethod
from databases import Database

from app.core.database import MAIN_DB


class Model(ABC):
    def __init__(self, database: Database = Depends(lambda: MAIN_DB)):
        self.database = database

    @abstractmethod
    def table(self) -> str:
        raise NotImplementedError()

    async def find(self, id: int) -> dict:
        sql = f"SELECT * FROM {self.table()} WHERE id = :id"
        return await self.database.fetch_one(query=sql, values={"id": id})

    async def insert(self, data: dict) -> int:
        keys = ", ".join(data.keys())
        placeholders = ", ".join([f":{k}" for k in data.keys()])
        sql = f"INSERT INTO {self.table()} ({keys}) VALUES ({placeholders})"
        await self.database.execute(query=sql, values=data)
        return await self._last_insert_id()

    async def _last_insert_id(self) -> int:
        result = await self.database.fetch_one("SELECT LAST_INSERT_ID() AS id")
        return result["id"] if result else 0
