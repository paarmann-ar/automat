from typing import Any
from abc import ABC, abstractmethod
from drivers.web.web_driver_provider import WebDriverProvider
from collections import namedtuple

# --
# ...
# --

class BaseComponent(ABC):

    def __new__(cls, **kwargs: Any):

        if hasattr(cls, 'instance_args'):
            if cls.instance_args != kwargs:
                cls.instance = None

        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
            cls.instance_args = kwargs

            cls.instance.config_dictionary = cls.get_config_dictionary()
            cls.instance.elements = cls.instance.get_elements()

            temp_selenium_driver = WebDriverProvider().selenium_driver

            for method in dir(temp_selenium_driver):
                if (method[0:1] != '_') and (method[0:2] != '__'):
                    setattr(cls.instance, method, getattr(
                        temp_selenium_driver, method))

        print(__class__.__name__, id(__class__))
        return cls.instance

# --
# ...
# --

    def __init__(self, *args, **kwargs: Any) -> None:
        pass

# --
# ...
# --

    @classmethod
    def get_config_dictionary(cls) -> str:
        return None

# --
# ...
# --

    @classmethod
    def get_elements(cls) -> str:
        return None
