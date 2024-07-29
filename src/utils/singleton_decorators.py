from functools import wraps
import logging
from typing import Any, Callable, Tuple

from polars import DataFrame

def singleton(orig_cls):
    orig_new = orig_cls.__new__
    instance = None

    @wraps(orig_cls.__new__)
    def __new__(cls, *args, **kwargs):
        nonlocal instance
        if instance is None:
            instance = orig_new(cls, *args, **kwargs)
        return instance
    orig_cls.__new__ = __new__
    return orig_cls

def pre_log(msg : str):
    def decorator(func: Callable[...,Any]) -> Callable[...,Any]:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            logging.info(msg)
            value = func(*args, **kwargs)
            return value
        return wrapper
    return decorator

def post_log(msg : str):
    def decorator(func: Callable[...,Any]) -> Callable[...,Any]:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            value = func(*args, **kwargs)
            logger.info(msg)
            return value
        return wrapper
    return decorator

