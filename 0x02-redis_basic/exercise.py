#!/usr/bin/env python3
""" THis script shall write into redis cache """
from typing import Union, Optional, Callable, Any
import redis
import uuid
from functools import wraps


class Cache:
    """This shall represent the Cache class """
    def __init__(self):
        """" THis instance shall store a Redis client as private variable"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ This shall store the data in redis cache """
        cle = str(uuid.uuid4())
        self._redis.set(cle, data)
        return cle
