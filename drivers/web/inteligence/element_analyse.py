from drivers.web.selenium.core.base_selenium import BaseSelenium
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup
from requests_html import HTML
import execjs

# --
# ...
# --


class ElementAnalyse():
    def __init__(self) -> None:
        super().__init__()
        self.current_page_addresss = (
            "https://sae-weu-uat-std.sandbox.operations.eu.dynamics.com"
        )
        self.current_page_text = ""
        self.analysed_elements = []

        print(__class__.__name__, id(__class__))

    # --
    # ... convert driver to object in self.elements
    # --

    def search_text_on_current_page_text(self, text_to_search: tuple) -> bool:

        try:

            _, text_to_search = text_to_search

            self.current_page_text = self.driver.page_source

            return bool(self.current_page_text.index(text_to_search))

        except Exception as exp:
            print(str(exp) + " now I am waiting for preaparing page!" )

    # --
    # ... return driver of find element, for use must change or add to self.elements
    # --

    def get_all_elements_of_tag(self, tag="input", sugesstion_key_value={}, C=True):

        try:

            self.delay(220)
            
            self.analysed_elements = []
            tag = "//" + tag

            match tag:
                case "//input":
                    self.__loop_for_tag(tag)

                case "//button":
                    self.__loop_for_tag(tag)
                case _:
                    raise Exception("Tag is unkown")

            if sugesstion_key_value:
                sugesstion_key, sugesstion_value = sugesstion_key_value

                # if element contains full key-value
                for element in self.analysed_elements:
                    if element[sugesstion_key] == sugesstion_value:
                        return self.__convert_drivere_to_elements_object(element)

                # if element contain halbe key-value
                for element in self.analysed_elements:

                    try:

                        if element[sugesstion_key].index(sugesstion_value) >= 0:
                            return self.__convert_drivere_to_elements_object(element)

                    except Exception:
                        pass

            return self.analysed_elements

        except Exception as exp:
            self.error(f"faild on: {__class__}.{repr(exp)}\n{__class__}.{str(exp)}\n{self.stack()} => {element}")

    # --
    # ... loops
    # --

    def __loop_for_tag(self, tag):

        try:

            analysed_element = {}

            for element in self.driver.find_elements(By.XPATH, tag):

                if "tag_name" in dir(element):
                    if element.tag_name != "":
                        analysed_element["tag_name"] = element.tag_name

                if "text" in dir(element):
                    if element.text != "":
                        analysed_element["text"] = element.text

                if "accessible_name" in dir(element):
                    if element.accessible_name != "":
                        analysed_element["accessible_name"] = element.accessible_name

                if "element" in dir(element):
                    analysed_element["element"] = element.element

                if "aria_role" in dir(element):
                    if element.aria_role != "":
                        analysed_element["aria_role"] = element.aria_role

                if "id" in dir(element):
                    if element.id != "":
                        analysed_element["id"] = element.id

                self.analysed_elements.append(analysed_element)

        except Exception as exp:
            self.error(f"faild on: {__class__}.{repr(exp)}\n{__class__}.{str(exp)}\n{self.stack()} => {element}")

    # --
    # ... convert driver to object in self.elements
    # --

    def __convert_drivere_to_elements_object(self, driver_object):

        try:

            element_id = driver_object["element"].get_attribute("id")

            if element_id != "":
                return ["xpath", '//*[@id="' + element_id + '"]']

            raise Exception("I can not create a object like objects in self.elements")

        except Exception as exp:
            self.error(f"faild on: {__class__}.{repr(exp)}\n{__class__}.{str(exp)}\n{self.stack()} => {element}")
