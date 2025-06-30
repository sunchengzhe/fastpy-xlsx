# app/util/Res.py
class Res:
    @staticmethod
    def success(data=None):
        return {
            "code": 200,
            "data": data,
        }

    @staticmethod
    def fail(message="失败", code=9999):
        return {
            "code": code,
            "message": message
        }
