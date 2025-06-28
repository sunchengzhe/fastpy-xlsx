# app/model/Model.py
from abc import ABC, abstractmethod
from databases import Database

class Model(ABC):
    def __init__(self, database: Database):
        self.database = database

    @abstractmethod
    def table(self) -> str:
        pass

    async def find(self, id: int) -> dict:
        sql = f"SELECT * FROM {self.table()} WHERE id = :id"
        return await self.database.fetch_one(query=sql, values={"id": id})

    async def find_all(self, order_by: str = None) -> list:
        sql = f"SELECT * FROM {self.table()}"
        if order_by:
            sql += f" ORDER BY {order_by}"
        return await self.database.fetch_all(sql)

    async def insert(self, data: dict) -> int:
        keys = ", ".join(data.keys())
        placeholders = ", ".join([f":{k}" for k in data.keys()])
        sql = f"INSERT INTO {self.table()} ({keys}) VALUES ({placeholders})"
        await self.database.execute(query=sql, values=data)
        return await self._last_insert_id()

    async def update(self, data: dict, where: dict) -> int:
        set_clause = ", ".join([f"{k} = :set_{k}" for k in data.keys()])
        where_clause = " AND ".join([f"{k} = :where_{k}" for k in where.keys()])
        values = {f"set_{k}": v for k, v in data.items()}
        values.update({f"where_{k}": v for k, v in where.items()})
        sql = f"UPDATE {self.table()} SET {set_clause} WHERE {where_clause}"
        return await self.database.execute(query=sql, values=values)

    async def delete(self, where: dict) -> int:
        where_clause = " AND ".join([f"{k} = :{k}" for k in where.keys()])
        sql = f"DELETE FROM {self.table()} WHERE {where_clause}"
        return await self.database.execute(query=sql, values=where)

    async def _last_insert_id(self) -> int:
        result = await self.database.fetch_one("SELECT LAST_INSERT_ID() AS id")
        return result["id"] if result else 0
