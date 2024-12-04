from typing import Any
from abc import ABC, abstractmethod

# --
# ...
# --

class BaseDisk(ABC):
    
    def __new__(cls, **kwargs: Any):

        if hasattr(cls, "instance_args"):
            if cls.instance_args != kwargs:
                cls.instance = None

        if not hasattr(cls, "instance") or not cls.instance:
            cls.instance = super().__new__(cls)

            cls.instance_args = kwargs

            # create instance for loging
            cls.info = kwargs.get("log_info_class")
            cls.error = kwargs.get("log_error_class")

            cls.instance.config_dictionary = cls.get_config_dictionary()

        return cls.instance

    def __init__(self) -> None:
        pass

    # --
    # ...
    # --

    def __call__(self) -> str:
        return self.instance

    # --
    # ...
    # --

    @classmethod
    def get_config_dictionary(cls) -> str:
        return ""
