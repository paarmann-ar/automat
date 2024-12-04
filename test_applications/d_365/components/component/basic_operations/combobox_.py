from typing import Any
from test_applications.d_365.core.object_provider import ObjectProvider
from test_applications.d_365.core.base import Base
from selenium.webdriver.common.keys import Keys

# --
# ...
# --


class Combobox_(Base):
    def __init__(self) -> None:
        print(__class__.__name__, id(__class__))

    # --
    # ...
    # --

    def __call__(self, element, text_to_search):

        try:

            element = self.driver.find_element(*element)
            text_to_search, _ = text_to_search
            element.send_keys(text_to_search)

            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False
