from drivers.web.selenium.core.base_selenium import BaseSelenium
from selenium.webdriver.common.action_chains import ActionChains

# --
# ...
# --


class Chains(BaseSelenium):
    def __init__(self) -> None:
        super().__init__()
        print(__class__.__name__, id(__class__))

    # --
    # ...
    # --

    def chain(self):

        try:
            
            print(f"success on: {__class__} => action_chains created")
            return ActionChains(self.driver)

        except Exception as exp:
            self.error(f"faild on: {__class__}.{repr(exp)}\n{__class__}.{str(exp)}\n{self.stack()}")
            return False
    # --
    # ...
    # --

    @BaseSelenium.log
    def double_click(self, element, is_click=True):

        try:

            if not is_click:
                return True

            action_chain = ActionChains(self.driver)

            self.wait_for_visibility(element)
            action_chain.move_to_element(self.current_element)
            action_chain.double_click(self.current_element).perform()

            return True

        except Exception as exp:
            self.error(f"faild on: {__class__}.{repr(exp)}\n{__class__}.{str(exp)}\n{self.stack()} => {element}")
            return False

    # --
    # ...
    # --

    @BaseSelenium.log
    def move_click(self, element, is_click=True):

        try:

            if not is_click:
                return True

            action_chain = ActionChains(self.driver)

            if self.wait_for_visibility(element):
                action_chain.move_to_element(self.current_element)
                action_chain.click(self.current_element).perform()

            return True

        except Exception as exp:
            self.error(f"faild on: {__class__}.{repr(exp)}\n{__class__}.{str(exp)}\n{self.stack()} => {element}")
            return False

    # --
    # ...
    # --

    @BaseSelenium.log
    def context_click(self, element, is_click=True, offset_x=5, offset_y=5):

        try:

            if not is_click:
                return True

            action_chain = ActionChains(self.driver)

            self.wait_for_visibility(element)
            action_chain.move_to_element(self.current_element)
            action_chain.context_click()
            action_chain.perform()
            return True

        except Exception as exp:
            self.error(f"faild on: {__class__}.{repr(exp)}\n{__class__}.{str(exp)}\n{self.stack()} => {element}")
            return False
