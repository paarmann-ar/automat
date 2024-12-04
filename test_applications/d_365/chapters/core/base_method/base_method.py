from typing import Any
from abc import ABC, abstractmethod

# --
# ...
# --


class BaseMethod(ABC):
    def __new__(cls, *args, **kwargs: Any):

        if hasattr(cls, "instance_args"):
            if cls.instance_args != kwargs:
                cls.instance = None

        if not hasattr(cls, "instance") or not cls.instance:
            cls.instance = super().__new__(cls)
            cls.instance_args = kwargs

            cls.instance.workbook=[]

        print(__class__.__name__, id(__class__))
        return cls.instance
