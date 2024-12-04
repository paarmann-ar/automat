from drivers.web.selenium.core.base_selenium import BaseSelenium
from selenium.webdriver.common.keys import Keys

# --
# ...
# --


class ComplexActions(BaseSelenium):
    def __init__(self) -> None:
        super().__init__()

        print(__class__.__name__, id(__class__))

    # --
    # ...
    # --

    @BaseSelenium.log
    def text(
        self,
        element,
        keys: tuple,
        is_press_enter=False,
        is_click_befor=True,
        is_clear=True,
        is_check_key_there=True,
        is_wait_for_validation_faild=False,
    ):

        try:

            keys, is_keys = keys

            if not is_keys:
                return True

            self.wait_for_visibility(element)

            if is_click_befor:
                if self.current_element_dir("click"):
                    self.current_element.click()

            if is_clear:
                if self.current_element_dir("clear"):
                    self.current_element.clear()
                    self.delay(150)

            if self.current_element_dir("send_keys"):
                self.current_element.send_keys(keys)
                self.delay(150)

                if is_check_key_there and self.current_element_dir("value"):
                    return (
                        True
                        if keys == self.current_element.getAttribute("value")
                        else False
                    )

                if is_press_enter:
                    self.current_element.click()
                    self.current_element.send_keys(Keys.ENTER)

                if is_wait_for_validation_faild:
                    self.is_class_wait_for_validation_failed(element)

                return True

            raise Exception("method not allowd")

        except Exception as exp:
            self.error(f"faild on: {__class__}.{repr(exp)}\n{__class__}.{str(exp)}\n{self.stack()} => {element}")
            return False
