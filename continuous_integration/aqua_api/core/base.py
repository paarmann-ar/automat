from typing import Any
from abc import ABC, abstractmethod
import time
from services.disk.service_disk_provider import ServiceDiskProvider

# --
# ...
# --


class Base(ABC):
    def __init__(self, **kwargs: Any) -> None:
        pass

    # --
    # ...
    # --

    def __new__(cls, **kwargs: Any):

        if hasattr(cls, "instance_args"):
            if cls.instance_args != kwargs:
                cls.instance = None

        if not hasattr(cls, "instance") or not cls.instance:
            cls.instance = super().__new__(cls)

            cls.instance_args = kwargs

            # create instance for loging
            cls.info = kwargs.get("log_info_class", "log_info_class")
            cls.error = kwargs.get("log_error_class", "log_error_class")
            cls.instance.config_dictionary = cls.get_config_dictionary()
            cls.instance.delay = cls.delay

            # working with file
            cls.json = ServiceDiskProvider().json

        return cls.instance

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

    # --
    # ...
    # --

    @classmethod
    def delay(cls, delay=1000, message="") -> str:
        if message == "":
            print(f"wait for {delay} ms")
        else:
            print(message)

        delay /= 1000
        time.sleep(delay)
