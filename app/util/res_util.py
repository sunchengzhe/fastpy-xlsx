# app/util/res_util.py

class ResUtil:
    @staticmethod
    def success(data=None):
        return {
            "code": 2000,
            "success": True,
            "data": data,
        }

    @staticmethod
    def fail(message="未知失败", code=9999):
        return {
            "code": code,
            "success": False,
            "message": message
        }
