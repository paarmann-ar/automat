from config_dictionary.base_dictionary import BaseDictionary
from services.disk.json.json_manager import JSONManager
import CONSTS

# --
# ...
# --

class TemplateConfig(BaseDictionary):
    @classmethod
    def get_dictionary(cls, *args) -> dict:
        json = JSONManager().instance
        config_json = json.operation(CONSTS.CONFIG_JSON)
        
        return config_json[__name__] if __name__ in config_json else {}