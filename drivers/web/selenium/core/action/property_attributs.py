from drivers.web.selenium.core.base_selenium import BaseSelenium
from selenium.webdriver.common.keys import Keys

# --
# ...
# --


class PropertyAttributs(BaseSelenium):
    def __init__(self) -> None:
        super().__init__()

        print(__class__.__name__, id(__class__))

    # --
    # ... convert driver to object in self.elements
    # --

    @BaseSelenium.log
    def search_text_on_current_page_text(self, text_to_search: tuple) -> bool:

        try:

            _, text_to_search = text_to_search

            if isinstance(text_to_search, tuple):
                text_to_search, _ = text_to_search

            self.current_page_text = self.driver.page_source

            return text_to_search in self.current_page_text

        except Exception as exp:
            self.error(
                f"faild on: {__class__}.{repr(exp)}\n{self.stack()} => now I am waiting for preaparing text '{text_to_search}'."
            )

    # --
    # ... get_attribute_value
    # --

    @BaseSelenium.log
    def get_attribute_value(self, element, attribute_name, is_wait_for_visibility=True):

        try:

            if is_wait_for_visibility:
                self.wait_for_visibility(element)

            else :
                self.current_element = self.driver.find_element(*element)

            if self.current_element_dir(attribute_name):
                attribute_value = self.current_element.get_attribute(attribute_name)

            else:
                attribute_value = self.current_element.get_dom_attribute(
                    attribute_name
                )
                self.info(f"attribute {attribute_name} is on {element} is {attribute_value}")

            if attribute_value:
                return self.conver_result_type(attribute_value)

            raise Exception(
                f"attribute-{attribute_name} not found in {self.current_element.tag_name} element => role is:{self.current_element.aria_role} in {self.current_element.accessible_name}"
            )

        except Exception as exp:
            self.error(
                f"faild on: {__class__}.{repr(exp)}\n{self.stack()} => {element}"
            )
            return False

    def conver_result_type(self, result):
        if result in ["false", "true"]:
            return False if result == "false" else True

        else:
            return result

    # --
    # ...
    # --

    @BaseSelenium.log
    def is_class_wait_for_validation_failed(self, element):
        self.delay(3000)

        if self.get_attribute_value(element, "class").find("validationFailed"):
            print(f"Validation Failed for element {element}")
            self.delay(3000)

    # --
    # ... get_property
    # --

    @BaseSelenium.log
    def get_property(self, element, property_name="attributes"):

        try:

            self.wait_for_visibility(element)

            attribute_value = self.current_element.get_property(property_name)

            if attribute_value:
                return self.conver_result_type(attribute_value)

            raise Exception("frame_work core: property not found")

        except Exception as exp:
            self.error(
                f"faild on: {__class__}.{repr(exp)}\n{self.stack()} => {element}"
            )
            return False

    # --
    # ... get_attributes
    # --

    @BaseSelenium.log
    def get_attributes(self, element):

        try:

            self.wait_for_visibility(element)

            attribute_value = self.driver.execute_script('var items = {}; for (index = 0; index < arguments[0].attributes.length; ++index) { items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value }; return items;', self.current_element)

            if attribute_value:
                return attribute_value

            raise Exception("frame_work core: attribute_value is not valid")

        except Exception as exp:
            self.error(
                f"faild on: {__class__}.{repr(exp)}\n{self.stack()} => {element}"
            )
            return False

    # --
    # ... get_text
    # --

    @BaseSelenium.log
    def get_text(self, element):

        try:

            self.wait_for_visibility(element)

            text_value = self.current_element.text

            if text_value:
                return self.conver_result_type(text_value)

            raise Exception("frame_work core: property not found")

        except Exception as exp:
            self.error(
                f"faild on: {__class__}.{repr(exp)}\n{self.stack()} => {element}"
            )
            return False
        
    # --
    # ... is displayed, enabled, selected
    # --

    @BaseSelenium.log
    def is_displayed(self, element):

        try:

            self.wait_for_visibility(element)

            return self.current_element.is_displayed()

        except Exception as exp:
            self.error(
                f"faild on: {__class__}.{repr(exp)}\n{self.stack()} => {element}"
            )
            return False

    @BaseSelenium.log
    def is_enabled(self, element):

        try:

            self.wait_for_visibility(element)

            return self.current_element.is_enabled()

        except Exception as exp:
            self.error(
                f"faild on: {__class__}.{repr(exp)}\n{self.stack()} => {element}"
            )
            return False

    @BaseSelenium.log
    def is_selected(self, element):

        try:

            self.wait_for_visibility(element)

            return self.current_element.is_selected()

        except Exception as exp:
            self.error(
                f"faild on: {__class__}.{repr(exp)}\n{self.stack()} => {element}"
            )
            return False
