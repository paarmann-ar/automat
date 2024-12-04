from typing import Any
from continuous_integration.aqua_api.core.base import Base
from services.connection.connection_provider import ConnectionProvider

# --
# ...
# --

class BaseAquaApi(Base):
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

            cls.request = ConnectionProvider().request

            cls.instance.config_dictionary = cls.get_config_dictionary()

        print(__class__.__name__, id(__class__))
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