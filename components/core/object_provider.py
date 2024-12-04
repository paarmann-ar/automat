from typing import Any
from test_applications.d_365.chapters.finance_chapter.core.md365_config import MD365Config
 
#--
#...
#-- 

class ObjectProvider:
    def __init__(self, *args: Any, **kwargs:Any) -> None:
        pass
    
#--
#...
#-- 

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        for key,value in MD365Config(*args, **kwargs, is_json_data_has_unexpected_char=True).instance.dictionary.items():
            setattr(self, key, *value.items())
        return self

