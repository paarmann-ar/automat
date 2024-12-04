from typing import Any
from test_applications.d_365.core.object_provider import ObjectProvider
from test_applications.d_365.core.base import Base
from selenium.webdriver.common.keys import Keys
from test_applications.d_365.components.component.basic_operations.combobox_dropdown import ComboboxDropdown
from test_applications.d_365.components.component.basic_operations.textbox_text import TextboxText

# --
# ...
# --


class FormSelectAndSortItem(Base):
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

    def __call__(self, combobox, select_item="") -> bool:

        try:

            ComboboxDropdown()(combobox)

            self.current_element.send_keys(select_item)

            self.double_click(self.elements.btn_select)

            self.delay(220)

            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False