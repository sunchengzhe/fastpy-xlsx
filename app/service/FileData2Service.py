# app/service/FileData2Service.py
from functools import lru_cache
import json

from fastapi import Depends

from app.model.FileData2Model import FileData2Model, get_file_data2_model_singleton

@lru_cache()
def get_file_data2_service_singleton() -> "FileData2Service":
    return FileData2Service(get_file_data2_model_singleton())

class FileData2Service:
    def __init__(self, file_data2_model: FileData2Model = Depends(get_file_data2_model_singleton)):
        self.file_data2_model = file_data2_model

    async def test_set_data(self):
        # 插入一条数据
        new_id = await self.file_data2_model.insert({
            "trace_id": "adsasdas1",
            "page": "1",
            "data": json.dumps({'a': '111', 'b': '222'}),  # ✅ 显式转为字符串
        })

        return {'id': new_id}