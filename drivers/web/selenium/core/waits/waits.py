from typing import Any
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from drivers.web.selenium.core.base_selenium import BaseSelenium
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException, ElementClickInterceptedException, ElementNotInteractableException
from selenium.common.exceptions import JavascriptException

# --
# ...
# --


class Waits(BaseSelenium):
    def __init__(self) -> None:
        super().__init__()

        print(__class__.__name__, id(__class__))

    # --
    # ... wait_for_not_uniqe_element_visibility
    # --

    @BaseSelenium.log
    def wait_for_not_uniqe_element_visibility(
        self, element, delay=None, wait_for_visibility_timeout=None
    ):

        try:

            if wait_for_visibility_timeout is None:
                wait_for_visibility_timeout = self.instance.config_dictionary[
                    "wait_for_visibility_timeout"
                ]

            delay = (
                self.instance.config_dictionary["wait_for_visibility_delay"]
                if not delay
                else delay
            )

            self.delay(delay)

            self.current_element = WebDriverWait(
                self.driver,
                wait_for_visibility_timeout,
                0.2,
                [StaleElementReferenceException, ElementClickInterceptedException, ElementNotInteractableException],
            ).until(lambda x: self.driver.find_elements(*element))

            self.delay(delay)

            return True

        except Exception as exp:
            self.error(
                f"Not found on: {__class__}.{repr(exp)}\n{self.stack()} => {element}"
            )
            return False

    # --
    # ... wait_for_visibility
    # --

    @BaseSelenium.log
    def wait_for_visibility(
        self, element, delay=None, wait_for_visibility_timeout=None
    ):

        try:

            if wait_for_visibility_timeout is None:
                wait_for_visibility_timeout = self.instance.config_dictionary[
                    "wait_for_visibility_timeout"
                ]

            delay = (
                self.instance.config_dictionary["wait_for_visibility_delay"]
                if not delay
                else delay
            )

            self.delay(delay)

            self.current_element = WebDriverWait(
                self.driver,
                wait_for_visibility_timeout,
                0.2,
                [StaleElementReferenceException, ElementClickInterceptedException, ElementNotInteractableException],
            ).until(lambda x: self.driver.find_element(*element))

            try:

                self.driver.execute_script(
                    "return arguments[0].scrollIntoView(true);", self.current_element
                )

            except JavascriptException as exp:
                self.info(
                    f"View port, There is no scroll there: {__class__}.{repr(exp)}\n{self.stack()} => {element}"
                )

            finally:

                self.current_element = WebDriverWait(
                    self.driver,
                    wait_for_visibility_timeout,
                ).until(EC.visibility_of_element_located(element))

                return True

        except Exception as exp:
            self.error(
                f"Not found on: {__class__}.{repr(exp)}\n{self.stack()} => {element}"
            )
            return False

    # --
    # ... wait_for_element_to_be_clickable
    # --

    @BaseSelenium.log
    def wait_for_element_to_be_clickable(self, element, delay=None):

        try:

            delay = (
                self.instance.config_dictionary["wait_for_visibility_delay"]
                if not delay
                else delay
            )

            self.delay(delay)

            self.current_element = WebDriverWait(
                self.driver,
                self.instance.config_dictionary["wait_for_visibility_timeout"],
                0.2,
                [StaleElementReferenceException, ElementClickInterceptedException, ElementNotInteractableException],
            ).until(EC.element_to_be_clickable(element))

            self.delay(delay)

            return True

        except Exception as exp:
            self.error(
                f"Not found on: {__class__}.{repr(exp)}\n{self.stack()} => {element}"
            )
            return False

    # --
    # ... wait_for_element_visibility_by_text
    # --

    @BaseSelenium.log
    def wait_for_element_visibility_by_text(self, element, delay=None, time_out=10):

        try:

            delay = (
                self.instance.config_dictionary["wait_for_visibility_delay"]
                if not delay
                else delay
            )

            self.delay(delay)

            _, text = element

            while self.driver.page_source.find(text) < 0:
                self.delay(delay)

                if time_out ==0:
                    break

                time_out -=1
                self.delay(1000)

            return True

        except Exception as exp:
            self.error(
                f"Not found on: {__class__}.{repr(exp)}\n{self.stack()} => {element}"
            )
            return False

    # --
    # ... wait_for_alert
    # --

    @BaseSelenium.log
    def wait_for_alert(self, delay=None):

        try:

            delay = (
                self.instance.config_dictionary["wait_for_alert_delay"]
                if not delay
                else delay
            )

            self.delay(delay)

            self.current_element = WebDriverWait(
                self.driver,
                self.instance.config_dictionary["wait_for_alert_timeout"],
                0.2,
                [StaleElementReferenceException, ElementClickInterceptedException, ElementNotInteractableException],
            ).until(EC.alert_is_present())

            self.delay(delay)

            return True

        except Exception as exp:
            self.error(f"Not found on: {__class__}.{repr(exp)}\n{self.stack()}")
            return False

    # --
    # ... is_element_there
    # --

    @BaseSelenium.log
    def is_element_there(self, element: tuple, delay=None):

        try:

            delay = (
                self.instance.config_dictionary["wait_for_visibility_delay"]
                if not delay
                else delay
            )

            self.delay(delay)

            element_type, text = element

            if element_type == "text_to_search":
                return True if self.driver.page_source.find(text) > 0 else False

            else:
                findet_element = self.driver.find_element(*element)
                element_style = self.get_attribute_value(element, "style")
                if isinstance(element_style, str):
                    if element_style.find("display: none") > 0:
                        element_style = False

                is_element_displayed = self.driver.find_element(*element).is_displayed()

                self.info(findet_element)
                self.info(element_style)
                self.info(is_element_displayed)

            return element_style or is_element_displayed

        except Exception as exp:
            self.error(
                f"Not found on: {__class__}.{repr(exp)}\n{self.stack()} => {element}"
            )
            return False

    # --
    # ... wait_for_element_until_visibile
    # --

    @BaseSelenium.log
    def wait_for_element_until_visibile(
        self, element, delay=None, type_of_element="xpath"
    ):

        try:

            delay = (
                self.instance.config_dictionary["wait_for_visibility_delay"]
                if not delay
                else delay
            )

            if type_of_element.lower() in [
                "id",
                "xpath",
                "link text",
                "partial link text",
                "name",
                "tag name",
                "class name",
                "css selector",
            ]:
                while not self.wait_for_visibility(element, delay=None):
                    self.delay(delay)

            elif type_of_element in ["text_to_search"]:
                while not self.wait_for_element_visibility_by_text(element, delay=None):
                    self.delay(delay)

            return True

        except Exception as exp:
            self.error(
                f"Not found on: {__class__}.{repr(exp)}\n{self.stack()} => {element}"
            )
            return False

    # --
    # ... wait_for_element_until_invisibile
    # --

    @BaseSelenium.log
    def wait_for_element_until_invisibile(
        self, element, delay=None, type_of_element="xpath"
    ):

        try:

            delay = (
                self.instance.config_dictionary["wait_for_visibility_delay"]
                if not delay
                else delay
            )

            if type_of_element.lower() in [
                "id",
                "xpath",
                "link text",
                "partial link text",
                "name",
                "tag name",
                "class name",
                "css selector",
            ]:
                while self.wait_for_visibility(
                    element, delay=None, wait_for_visibility_timeout=500
                ):
                    self.delay(delay)

            elif type_of_element in ["text_to_search"]:
                while self.wait_for_element_visibility_by_text(element, delay=None):
                    self.delay(delay)

            return True

        except Exception as exp:
            self.error(
                f"Not found on: {__class__}.{repr(exp)}\n{self.stack()} => {element}"
            )
            return False
