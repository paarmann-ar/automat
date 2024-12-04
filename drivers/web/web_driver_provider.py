from drivers.web.selenium.selenium_driver import SeleniumDriver
from toolboxs.decorators import singleton


#--
#...
#--
@singleton
class WebDriverProvider:
    def __init__(self) -> None:
        print(__class__.__name__, id(__class__))
        self.selenium_driver = SeleniumDriver().instance