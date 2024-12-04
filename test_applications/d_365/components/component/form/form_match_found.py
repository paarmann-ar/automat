from typing import Any
from test_applications.d_365.core.object_provider import ObjectProvider
from test_applications.d_365.core.base import Base
from selenium.webdriver.common.keys import Keys
from test_applications.d_365.components.component.basic_operations.combobox_dropdown import (
    ComboboxDropdown,
)
from test_applications.d_365.components.component.basic_operations.textbox_text import (
    TextboxText,
)

# --
# ...
# --


class FormMatchFound(Base):
    def __init__(self) -> None:
        self.elements = self.get_elements()

        print(__class__.__name__, id(__class__))

    # --
    # ...
    # --

    def get_elements(self) -> str:
        return ObjectProvider()(__file__.replace(".py", ".json ", -1).replace("\\", "/").replace(" c", ""))

    # --
    # ...
    # --

    def __call__(self) -> bool:

        try:

            self.delay(220)

            if not self.is_element_there(self.elements.frm_match_found):
                raise Exception("lightbox is not there")
    
            self.click_button(self.elements.btn_use_match)

            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False
