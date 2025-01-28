from drivers.web.selenium.core.base_selenium import BaseSelenium
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementNotInteractableException
from typing import Any
import inspect
from selenium.webdriver.common.keys import Keys

# --
# ...
# --


class DomElementAndAction(BaseSelenium):
    def __init__(self) -> None:
        super().__init__()

        print(__class__.__name__, id(__class__))

    # --
    # ... textbox
    # --

    @BaseSelenium.log
    def textbox(
        self,
        element,
        text: tuple,
        is_press_enter=False,
        is_click_befor=True,
        is_double_click_befor=False,
        is_clear=True,
        is_check_key_there=True,
        is_press_tab=False,
        is_char_by_char=False,
        is_press_esc=False,
        is_check_readonly=True,
    ):

        try:

            text, is_text = text

            if not is_text:
                print(
                    f"return (is_text={is_text}) on: {__class__}.{inspect.currentframe()} => {element}"
                )
                return True

            self.wait_for_visibility(element)

            if is_check_readonly:
                if self.get_attribute_value(element, "readonly"):
                    raise Exception(f"Textbox-> {element} is read only")

            self.chain().move_to_element(self.current_element).perform()
                    
            if is_double_click_befor:
                self.double_click(element)
                
            elif is_click_befor:
                if self.current_element_dir("click"):
                    self.current_element.click()

            self.delay(50)

            if is_clear:
                self.current_element.send_keys(Keys.CONTROL + "a")
                self.current_element.send_keys(Keys.DELETE)
                
                self.delay(150)
                
                for i in range(len(self.current_element.get_attribute("value"))):
                    self.current_element.send_keys(Keys.BACK_SPACE)

            if self.current_element_dir("send_keys"):
                self.current_element.send_keys(Keys.END)

                if is_char_by_char:
                    for chr in text:
                        self.delay(50)
                        self.current_element.send_keys(chr)
                else:
                    self.current_element.send_keys(text)
                    self.delay(50)

                if is_check_key_there and self.current_element_dir("value"):

                    print(
                        f"return (is_check_key_there={is_check_key_there}) on: {__class__}.{inspect.currentframe()} => {element}"
                    )
                    return (
                        True
                        if text == self.current_element.getAttribute("value")
                        else False
                    )

                if is_press_enter:
                    self.current_element.send_keys(Keys.ENTER)
                    self.delay(50)

                if is_press_esc:
                    self.current_element.send_keys(Keys.ESCAPE)
                    self.delay(50)

                if is_press_tab:
                    self.current_element.click()
                    self.delay(50)

                    self.current_element.send_keys(Keys.TAB)

                print(f"success on: {__class__}.{inspect.currentframe()} => {element}")
                return True

            raise Exception("method not allowd")

        except ElementNotInteractableException as exp:
            self.error(
                f"faild on: {__class__}->ElementNotInteractableException on {element}"
            )
            return False

        except Exception as exp:
            self.error(
                f"faild on: {__class__}.{repr(exp)}\n{__class__}.{str(exp)}\n{self.stack()} => {element}"
            )
            return False

    # --
    # ... combobox
    # --

    @BaseSelenium.log
    def combobox(
        self,
        element,
        item: tuple,
        is_press_enter=False,
        is_check_expand=False,
        is_press_tab=False,
    ):

        try:

            item, is_item = item

            if not is_item:
                print(
                    f"return (is_item={is_item}) on: {__class__}.{inspect.currentframe()} => {element}"
                )
                return True

            self.wait_for_visibility(element)
            self.chain().move_to_element(self.current_element).perform()

            if is_check_expand:
                while not self.get_attribute_value(
                    self.current_element, "aria-expanded"
                ):
                    self.current_element.click()
                    self.current_element.send_keys(Keys.ALT + Keys.ARROW_DOWN)
                    self.delay(220)
            else:
                self.current_element.click()

            ul_element = self.current_element.parent.find_element("xpath", "//ul")
            self.delay(1500)

            li_elements = ul_element.find_elements("xpath", f"//li[contains(.,{item})]")

            self.delay(220)

            li_text = [li.text for li in li_elements]

            if not item in li_text:
                raise Exception("item is not in combobox")

            for li in li_elements:
                self.delay(50)

                if li.text == item:
                    self.wait_for_element_to_be_clickable(li)
                    li.click()

                    self.delay(220)

                    if is_press_tab:
                        li.send_keys(Keys.TAB)

                    print(
                        f"success on: {__class__}.{inspect.currentframe()} => {element}"
                    )
                    return True

            raise Exception("method not allowd")

        except Exception as exp:
            self.error(
                f"faild on: {__class__}.{repr(exp)}\n{__class__}.{str(exp)}\n{self.stack()} => {element}"
            )
            return False

    # --
    # ... checkbox
    # --

    @BaseSelenium.log
    def checkbox(self, element, value: tuple = (True, True), versuchen_count=5):

        try:

            value, is_value = value

            if not is_value:
                print(
                    f"return (is_value={is_value}) on: {__class__}.{inspect.currentframe()} => {element}"
                )
                return True

            versuch_count = 0
            self.wait_for_visibility(element)
            self.chain().move_to_element(self.current_element).perform()

            # element_state = False if self.current_element.text.lower() == 'no' else True

            element_state = self.get_attribute_value(element, "aria-checked")

            if value and element_state:

                print(f"return on: {__class__}.{inspect.currentframe()} => {element}")
                return True

            if value or element_state:
                while element_state != value:
                    if self.current_element_dir("click"):
                        self.current_element.click()

                        print(
                            f"success on: {__class__}.{inspect.currentframe()} => {element}"
                        )
                        return True

                    self.delay(220)
                    versuch_count += versuch_count
                    if versuch_count > versuchen_count:
                        break

            raise Exception("method not allowd")

        except Exception as exp:
            self.error(
                f"faild on: {__class__}.{repr(exp)}\n{__class__}.{str(exp)}\n{self.stack()} => {element}"
            )
            return False

    # --
    # ... click_button
    # --

    @BaseSelenium.log
    def click_button(
        self, element, is_click=True, is_wait_for_not_uniqe_element_visibility=False
    ):

        try:

            if not is_click:
                print(
                    f"retun (is_click={is_click}) on: {__class__}.{inspect.currentframe()} => {element}"
                )
                return True

            if is_wait_for_not_uniqe_element_visibility:
                self.wait_for_not_uniqe_element_visibility(element)

                for element in self.current_element:

                    try:

                        element.click()

                        self.delay(220)

                    # I have change this exp to bestimmt exception
                    except Exception as exp:
                        self.error(
                            f"faild on: {__class__}.{repr(exp)}\n{__class__}.{str(exp)}\n{self.stack()} => {element}"
                        )

                return True

            else:

                if self.get_attribute_value(element, "disabled"):
                    raise Exception("element is disabled")

                self.current_element = self.driver.find_element(*element)
                # self.wait_for_visibility(element)
                # self.chain.move_to_element(self.current_element)

                if self.current_element_dir("click"):
                    self.current_element.click()

                print(f"success on: {__class__}.{inspect.currentframe()} => {element}")
                return True

        except Exception as exp:
            self.error(
                f"faild on: {__class__}.{repr(exp)}\n{__class__}.{str(exp)}\n{self.stack()} => {element}"
            )
            return False

    # --
    # ... view port
    # --

    @BaseSelenium.log
    def scroll_element(self, element):

        try:

            element = self.driver.find_element(*element)
            self.driver.execute_script(
                "return arguments[0].scrollIntoView(true);", element
            )

        except Exception as exp:
            self.error(
                f"faild on: {__class__}.{repr(exp)}\n{__class__}.{str(exp)}\n{self.stack()} => {element}"
            )
            return False