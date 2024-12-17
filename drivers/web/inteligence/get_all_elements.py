from selenium.webdriver.common.by import By
from typing import Any
from selenium import webdriver
from typing import Any
from selenium.webdriver.chrome.service import Service
from typing import Any
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import CONSTS

# --
# ...
# --


class GetAllElements:
    def __init__(
        self,
        current_page_addresss="https://sae-weu-uat-std.sandbox.operations.eu.dynamics.com",
    ) -> None:

        self.driver = webdriver.Chrome(
            service=Service(
                f"{CONSTS.ROOT_DIR}/.external_files/web_drivers/chorom/123.0.6312.122/chromedriver.exe"
            )
        )
        self.driver.get(current_page_addresss)

        time.sleep(5)

        print(__class__.__name__, id(__class__))

    # --
    # ... convert driver to object in self.elements
    # --

    def get_all_element_attribute(self, tag_name: str) -> bool:

        try:

            xpath_string = f"""//{tag_name}[@id!=""]"""

            tags = self.driver.find_elements(By.XPATH, xpath_string)
            for tag in tags:
                for attribute in tag.get_property('value'):
                    for k,v in attribute.items():
                        print(k, v)



                tag_list = {
                    "attribute": tag.get_attribute('aria-hidden'),
                    "property": tag.get_property('attributes')
                }

                print(tag_list)

            return True

        except Exception as exp:
            self.error(f"faild on: {__class__}.{repr(exp)}\n{self.stack()} => {tag_name}")
