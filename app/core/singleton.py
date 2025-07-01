# app/util/singleton.py
from functools import lru_cache
from typing import Type, TypeVar, cast, Protocol

T = TypeVar("T", bound="SingletonCompatible")


class SingletonCompatible(Protocol):
    @staticmethod
    def instance() -> "SingletonCompatible":
        ...


def singleton(cls: Type[T]) -> Type[T]:
    # 使用 lru_cache 封装构造函数
    _cached = lru_cache()(cls)
    # 动态挂载 instance 方法
    setattr(cls, "instance", _cached)
    # 使用 cast 告诉类型系统：cls 符合 SingletonCompatible 协议
    return cast(Type[T], cls)
