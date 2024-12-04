from typing import Any
from test_applications.d_365.core.object_provider import ObjectProvider
from test_applications.d_365.core .base import Base
from selenium.webdriver.common.keys import Keys

# --
# ...
# --


class TextboxText(Base):
    def __init__(self) -> None:
        print(__class__.__name__, id(__class__))

    # --
    # ...
    # --

    def __call__(self, element, text_to_search: tuple = ("", True), is_click_befor=True, is_clear=True):

        try:


            text_to_search, is_text_to_search = text_to_search

            if not is_text_to_search:
                return True
            
            self.wait_for_visibility(element)

            if is_click_befor:
                if self.current_element_dir("click"):
                    self.instance.current_element.click()

            if is_clear:
                if self.current_element_dir("clear"):
                    self.instance.current_element.clear()
                    self.delay(150)

            if self.current_element_dir("send_keys"):
                self.instance.current_element.send_keys(text_to_search)
                self.delay(150)

                return True

            raise Exception("method not allowd")

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False
