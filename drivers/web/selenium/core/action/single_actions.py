from drivers.web.selenium.core.base_selenium import BaseSelenium
from selenium.webdriver.common.keys import Keys

# --
# ...
# --


class SingleActions(BaseSelenium):
    def __init__(self) -> None:
        super().__init__()

        print(__class__.__name__, id(__class__))

    # --
    # ...
    # --

    @BaseSelenium.log
    def click(self, element, is_click=True):

        try:

            if not is_click:
                return True

            self.wait_for_visibility(element)
            self.move_to_element()

            if self.current_element_dir("click"):
                self.current_element.click()

                return True

            raise Exception("method not allowd")

        except Exception as exp:
            self.error(f"faild on: {__class__}.{repr(exp)}\n{__class__}.{str(exp)}\n{self.stack()} => {element}")
            return False
        
    # --
    # ...
    # --

    @BaseSelenium.log
    def clear(self, element, is_clear=True):

        try:

            if not is_clear:
                return True

            self.wait_for_visibility(element)
            self.move_to_element()

            if self.current_element_dir("clear"):
                self.current_element.clear()
                return True

            raise Exception("method not allowd")

        except Exception as exp:
            self.error(f"faild on: {__class__}.{repr(exp)}\n{__class__}.{str(exp)}\n{self.stack()} => {element}")
            return False

    # --
    # ...
    # --

    @BaseSelenium.log
    def keys(self, element, keys: tuple, is_check_key_there=True):

        try:

            keys, is_keys = keys

            if not is_keys:
                return True

            self.wait_for_visibility(element)
            self.move_to_element()

            if self.current_element_dir("send_keys"):
                self.current_element.send_keys(keys)

                if is_check_key_there and self.current_element_dir("value"):
                    return (
                        True
                        if keys == self.current_element.getAttribute("value")
                        else False
                    )

                return True

            raise Exception("method not allowd")

        except Exception as exp:
            self.error(f"faild on: {__class__}.{repr(exp)}\n{__class__}.{str(exp)}\n{self.stack()} => {element}")
            return False

    # --
    # ...
    # --

    @BaseSelenium.log
    def send_keys(self, element, keys: tuple, is_check_key_there=True):

        try:

            keys, is_keys = keys

            if not is_keys:
                return True

            self.wait_for_visibility(element)
            self.move_to_element()

            if self.current_element_dir("send_keys"):
                self.current_element.send_keys(keys)

                if is_check_key_there and self.current_element_dir("value"):
                    return (
                        True
                        if keys == self.current_element.getAttribute("value")
                        else False
                    )

                return True

            raise Exception("method not allowd")

        except Exception as exp:
            self.error(f"faild on: {__class__}.{repr(exp)}\n{__class__}.{str(exp)}\n{self.stack()} => {element}")
            return False
        
    # --
    # ...
    # --

    @BaseSelenium.log
    def read_textbox(self, element, attribute_to_read="value"):

        try:

            self.wait_for_visibility(element)
            self.move_to_element()

            match attribute_to_read:
                case "value":
                    read_value = self.current_element.get_attribute("value")

                case "title":
                    read_value = self.current_element.get_attribute("title")

                case "text":
                    read_value = self.current_element.text

            print(f"success on: {__class__} => value on textbox => {read_value}")

            return read_value
            
        except Exception as exp:
            self.error(f"faild on: {__class__}.{repr(exp)}\n{__class__}.{str(exp)}\n{self.stack()} => {element}")
            return False
        
    # --
    # ...
    # --

    def move_to_element(self):

        try:

            self.chain().move_to_element(self.current_element).perform()

            print(f"success on: {__class__} => move to element")

            return
            
        except Exception as exp:
            self.error(f"faild on: {__class__}.{repr(exp)}\n{__class__}.{str(exp)}\n{self.stack()} => {self.current_element}")
            return False