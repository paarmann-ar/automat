from config_dictionary.base_dictionary import BaseDictionary
from services.disk.json.json_manager import JSONManager

# --
# ...
# --

class MD365Config(BaseDictionary):
    @classmethod
    def get_dictionary(cls, *args, **kwargs) -> dict:
        json = JSONManager().instance
        return json.operation(*args, **kwargs)