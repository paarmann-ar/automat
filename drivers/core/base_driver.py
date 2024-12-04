from typing import Any
from abc import ABC, abstractmethod
import time
from drivers.windows.action_simulator.action_simulator import ActionSimulator
from toolboxs.toolbox import Toolbox
from services.log_.log_provider import LogProvider

# --
# ...
# --

class BaseDriver(ABC):
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

            cls.instance.config_dictionary = cls.get_config_dictionary()
            cls.instance.delay = cls.delay
            cls.instance.get_random = cls.get_random

            cls.instance.error = LogProvider().error
            cls.instance.info = LogProvider().info
            cls.instance.stack = LogProvider().stack

            cls.instance.action_simulator = ActionSimulator()

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
    def get_config_dictionary(cls):
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

    # --
    # ...
    # --

    @classmethod
    def get_random(cls, start_string="RND ", type="string", limit=10000) -> str:
        return Toolbox.get_random(start_string=start_string, type=type, limit=limit)

    # --
    # ... decorator
    # --

    def log(function) -> object:

        try:

            def inner_function(*args, **kwargs):
                element = kwargs.get("element", None)

                if not element and len(args)>1:
                    element=""
                    for item in args[1:]:
                        element =f"{element} >>> {item}"

                args[0].info(f"{function.__module__}.{function.__name__}, {element}")
                return function(*args, **kwargs)

            return inner_function

        except Exception as exp:
            print(f"{repr(exp)}")
            return False
