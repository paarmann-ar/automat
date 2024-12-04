from typing import Any
from continuous_integration.aqua_api.core.base import Base
from continuous_integration.aqua_api.aqua_api.aqua_api import AquaApi

# --
# ...
# --


class BaseAquaAdapter(Base):
    def __init__(self, **kwargs: Any) -> None:
        pass
    
# --
# ...
# --

    def __new__(cls, **kwargs: Any):
        
        if hasattr(cls, 'instance_args'):
            if cls.instance_args != kwargs:
                cls.instance = None
                
        if not hasattr(cls, 'instance') or not cls.instance:
            cls.instance = super().__new__(cls)
            
            cls.instance_args = kwargs

            cls.aqua_api = AquaApi()

        print(__class__.__name__, id(__class__))
        return cls.instance

    # --
    # ...
    # --

    @classmethod
    def get_config_dictionary(cls) -> str:
        return ""
