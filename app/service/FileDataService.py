# app/service/FileDataService.py
from app.model.FileDataModel import FileDataModel
import json

class FileDataService:
    def __init__(self, file_data_model: FileDataModel):
        self.file_data_model = file_data_model

    async def test_set_data(self):
        # 插入一条数据
        new_id = await self.file_data_model.insert({
            "trace_id": "adsasdas1",
            "page": "1",
            "data": json.dumps({'a': '111', 'b': '222'}),  # ✅ 显式转为字符串
        })

        return {'id': new_id}