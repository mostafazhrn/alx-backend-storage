#!/usr/bin/env python3
""" THis script shall write into redis cache """
from typing import Union, Optional, Callable, Any
import redis
import uuid
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """ This shall count the number of calls of a method """
    cle = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs) -> Any:
        """ This shall wrap the method """
        self._redis.incr(cle)
        return method(self, *args, **kwargs)
    return wrapper


class Cache:
    """This shall represent the Cache class """
    def __init__(self):
        """" THis instance shall store a Redis client as private variable"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ This shall store the data in redis cache """
        cle = str(uuid.uuid4())
        self._redis.set(cle, data)
        return cle

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """ This shall convert redis data to wanted format """
        donne = self._redis.get(key)
        if fn:
            return fn(donne)
        return donne

    def get_str(self, cle: str) -> str:
        """ This shall convert redis data to string """
        donne = self._redis.get(cle)
        return donne.decode('utf-8')

    def get_int(self, cle: str) -> int:
        """ This shall convert redis data to int """
        donne = self._redis.get(cle)
        try:
            donne = int(value.decode('utf-8'))
        except Exception:
            donne = 0
        return donne
