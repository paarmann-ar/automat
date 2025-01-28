from typing import Any
from abc import ABC, abstractmethod
from drivers.web.web_driver_provider import WebDriverProvider
from drivers.windows.pywin.win_driver_provider import WinDriverProvider
import CONSTS
from collections import namedtuple
from services.mail.email_provider import EMailProvider
from services.log_.log_provider import LogProvider
from drivers.ranorex.ranorex_driver_provider import RanorexDriverProvider

# --
# ...
# --


class Base(ABC):
    # hire must store staate zwichen module or test or arttribute. this dictionaray is shared data between test
    state = {}

    def __new__(cls, *args, **kwargs: Any):

        if hasattr(cls, "instance_args"):
            if cls.instance_args != kwargs:
                cls.instance = None

        if not hasattr(cls, "instance"):
            cls.instance = super().__new__(cls)
            cls.state['base_id'] = id(cls)
            cls.state['root_address'] = CONSTS.ROOT_DIR

            cls.instance_args = kwargs

            cls.instance.elements = cls.instance.get_elements()
            cls.instance.components = cls.instance.get_components()

            cls.instance.mail = EMailProvider().email

            cls.instance.info = LogProvider().info
            cls.instance.error = LogProvider().error
            cls.instance.stack = LogProvider().stack

            temp_selenium_driver = WebDriverProvider().selenium_driver

            for method in dir(temp_selenium_driver):
                if (method[0:1] != "_") and (method[0:2] != "__"):
                    setattr(
                        cls.instance, method, getattr(temp_selenium_driver, method)
                    )

            temp_pywin = WinDriverProvider().pywin_driver
            
            for method in dir(temp_pywin):
                if (method[0:1] != "_") and (method[0:2] != "__"):
                    setattr(
                        cls.instance, method, getattr(temp_pywin, method)
                    )

            cls.instance.ranorex_driver = RanorexDriverProvider().ranorex_driver

            cls.instance.config_dictionary = cls.get_config_dictionary()

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

    # --
    # ...
    # --

    @classmethod
    def get_components(cls) -> str:
        return None