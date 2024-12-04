from typing import Any
from drivers.core.base_driver import BaseDriver
from selenium import webdriver
from typing import Any
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


# --
# ...
# --


class BaseSelenium(BaseDriver):

    def __init__(self) -> None:
        super().__init__()

        self.current_element = None
        self.current_frame = None
        driver_options = webdriver.ChromeOptions()

        driver_options.add_experimental_option("detach", True)
        driver_options.add_extension(
            self.instance.config_dictionary["terminal_client_extention_path"]
        )
        driver_options.add_argument("--start-maximized")
        driver_options.add_argument("-user-data-dir="+self.instance.config_dictionary["terminal_client_extention_path"])
        driver_options.add_argument("--disable-search-engine-choice-screen")

        self.driver = webdriver.Chrome(
            service=Service(
                self.instance.config_dictionary["selenium_chrome_webdriver_path"],
            ),
            options=driver_options
        )

        print(__class__.__name__, id(__class__))

    # --
    # ...
    # --

    def current_element_dir(self, method="", is_refresh=False):
        return True if method in dir(self.current_element) else False

    # --
    # ... Frame
    # --

    def restore_current_Frame(self):
        self.driver.switch_to.frame(self.current_frame)
        return True
        
    def save_current_Frame(self, element = None):
        self.current_frame = self.driver.find_element(*element)
        return True