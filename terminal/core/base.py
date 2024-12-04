from typing import Any
from abc import ABC, abstractmethod
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
        
        if hasattr(cls, 'instance_args'):
            if cls.instance_args != kwargs:
                cls.instance = None
                
        if not hasattr(cls, 'instance') or not cls.instance:
            cls.instance = super().__new__(cls)
            cls.instance_args = kwargs

            cls.instance.config_dictionary = cls.get_config_dictionary()
            cls.instance.json = ServiceDiskProvider().json
            cls.instance.file = ServiceDiskProvider().file

                               
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
        return ''
        
