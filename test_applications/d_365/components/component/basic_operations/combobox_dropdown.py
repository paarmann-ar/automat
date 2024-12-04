from typing import Any
from test_applications.d_365.core.object_provider import ObjectProvider
from test_applications.d_365.core.base import Base
from selenium.webdriver.common.keys import Keys

# --
# ...
# --


class ComboboxDropdown(Base):
    def __init__(self) -> None:
        print(__class__.__name__, id(__class__))

    # --
    # ...
    # --

    def __call__(
        self,
        element,
        is_click_befor=True,
    ):

        try:

            self.wait_for_visibility(element)

            while not self.get_attribute_value(self.current_element, "aria-expanded"):
                if is_click_befor:
                    if self.current_element_dir("click"):
                        self.double_click(self.current_element)

                if self.current_element_dir("send_keys"):
                    self.current_element.send_keys(Keys.ALT + Keys.ARROW_DOWN)
                    self.delay(150)

                    return True

                self.delay(220)

            raise Exception("method not allowd")

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False
