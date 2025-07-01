# app/service/FileData2Service.py
import json

from app.model.FileData2Model import FileData2Model

class FileData2Service:
    _instance = None

    def __init__(self, file_data2_model: FileData2Model):
        self.file_data2_model = file_data2_model

    @classmethod
    def get_instance(cls) -> "FileData2Service":
        if cls._instance is None:
            model = FileData2Model.get_instance()
            cls._instance = cls(model)
        return cls._instance

    async def test_set_data(self):
        # 插入一条数据
        new_id = await self.file_data2_model.insert({
            "trace_id": "adsasdas1",
            "page": "1",
            "data": json.dumps({'a': '111', 'b': '222'}),  # ✅ 显式转为字符串
        })

        return {'id': new_id}