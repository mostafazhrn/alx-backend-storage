#!/usr/bin/env python3
""" THis script shall write into redis cache """
from typing import Union, Optional, Callable, Any
import redis
import uuid
from functools import wraps


def call_history(method: Callable) -> Callable:
    """ This shall store the history of calls of a method """
    cle = method.__qualname__
    ios = cle + ":inputs"
    outs = cle + ":outputs"

    @wraps(method)
    def wrapper(self, *args, **kwargs) -> Any:
        """ This shall wrap the method """
        self._redis.rpush(ios, str(args))
        donne = method(self, *args, **kwargs)
        self._redis.rpush(outs, str(donne))
        return donne
    return wrapper


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

    @call_history
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


def replay(method: Callable):
    """ This shall replay the history of calls of a method """
    cle = method.__qualname__
    ios = cle + ":inputs"
    outs = cle + ":outputs"
    redis = method.__self__._redis
    compte = redis.get(cle).decode('utf-8')
    print("{} was called {} times:".format(cle, compte))
    ios_lst = redis.lrange(ios, 0, -1)
    outs_lst = redis.lrange(outs, 0, -1)
    redis_zip = list(zip(ios_lst, outs_lst))
    for x, y in redis_zip:
        attribute, donne = x.decode('utf-8'), y.decode('utf-8')
        print("{}(*{}) -> {}".format(cle, attribute, donne))
