# app/util/res_util.py
class ResUtil:
    @staticmethod
    def success(data=None):
        return {
            "code": 2000,
            "message": 'success',
            "data": data,
        }

    @staticmethod
    def fail(details="未知失败", code=9999):
        return {
            "code": code,
            "message": 'fail',
            "details": details
        }
