from typing import Any
from abc import ABC, abstractmethod
from test_applications.d_365.core.base import Base

# --
# ...
# --


class BaseUserStory(Base):
    def __new__(cls, **kwargs: Any):

        if hasattr(cls, "instance_args"):
            if cls.instance_args != kwargs:
                cls.instance = None

        if not hasattr(cls, "instance") or not cls.instance:
            cls.instance = super().__new__(cls)
            cls.instance_args = kwargs

        print(__class__.__name__, id(__class__))
        return cls.instance

    def __init__(self, *args, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
