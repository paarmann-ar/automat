from drivers.web.selenium.core.base_selenium import BaseSelenium

# --
# ...
# --


class BrowserActions(BaseSelenium):
    def __init__(self) -> None:
        super().__init__()

        print(__class__.__name__, id(__class__))

    # --
    # ...
    # --

    @BaseSelenium.log
    def get(self, web_address):

        try:

            self.driver.get(web_address)
            return True
        
        except Exception as exp:
            self.error(f"faild on: {__class__}.{repr(exp)}\n{self.stack()} => {web_address}\n{str(exp)}")
            return False

    # --
    # ...
    # --

    @BaseSelenium.log
    def quit(self):

        try:
        
            self.driver.quit()
            return True
        
        except Exception as exp:
            self.error(f"faild on: {__class__}.{repr(exp)}\n{self.stack()}")
            return False

    # --
    # ...
    # --

    @BaseSelenium.log
    def forward(self):

        try:
        
            self.driver.forward()
            return True
        
        except Exception as exp:
            self.error(f"faild on: {__class__}.{repr(exp)}\n{self.stack()}")
            return False

    # --
    # ...
    # --

    @BaseSelenium.log
    def back_browser(self):

        try:
        
            self.driver.back()
            return True
        
        except Exception as exp:
            self.error(f"faild on: {__class__}.{repr(exp)}\n{self.stack()}")
            return False

    # --
    # ...
    # --

    @BaseSelenium.log
    def delete_all_cookies(self):

        try:

            self.driver.delete_all_cookies()
            self.delay(220)

            self.driver.refresh()
            return True
        
        except Exception as exp:
            self.error(f"faild on: {__class__}.{repr(exp)}\n{self.stack()}")
            return False

    # --
    # ...
    # --

    @BaseSelenium.log
    def get_alle_cookies(self):

        try:
        
            self.driver.get_cookies()
            return True
        
        except Exception as exp:
            self.error(f"faild on: {__class__}.{repr(exp)}\n{self.stack()}")
            return False
