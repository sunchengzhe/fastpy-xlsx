# app/util/SystemException.py
class SystemException(Exception):
    def __init__(self, message="业务异常", code=4001):
        self.message = message
        self.code = code
