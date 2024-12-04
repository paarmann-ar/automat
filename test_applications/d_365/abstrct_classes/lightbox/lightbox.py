from typing import Any
from test_applications.d_365.core.object_provider import ObjectProvider
from test_applications.d_365.core.base import Base


# --
# ...
# --


class Lightbox(Base):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.elements = self.get_elements()
        print(__class__.__name__, id(__class__))

    # --
    # ...
    # --

    def get_elements(self) -> str:
        return ObjectProvider()(
            __file__.replace(".py", ".json ", -1).replace("\\", "/").replace(" c", "")
        )

    # --
    # ... setup, teardown and prepare
    # --

    def __setup(self) -> bool:

        try:

            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False

    def __teardown(self) -> bool:

        try:

            super().teardown()

            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False

    def __prepare(self) -> bool:

        try:

            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False

    # --
    # ...
    # --

    def __call__(
        self,
        lightbox="is_visible",
        action="Close",
    ) -> bool:

        try:

            self.delay(1000)
            
            if not self.is_element_there(self.elements.lightbox_):
                raise Exception("lightbox is not there")
                    
            self.instance.info(
                f"\n\n\n******************************************\n\n{self.get_text(self.elements.lbl_message)}\n\n******************************************\n\n\n"
            )

            match lightbox:
                case "wait_until_lightbox_disapear":
                    while self.is_element_there(self.elements.lightbox_):
                        self.delay(1000)

                case _:
                    pass

            match action:
                case "Close":
                    self.click_button(self.elements.btn_close)
                    self.confirm_action_has_been_donn(action)
                    return True

                case "Yes":
                    self.click_button(self.elements.btn_yes)
                    self.confirm_action_has_been_donn(action)
                    return True

                case "No":
                    self.click_button(self.elements.btn_no)
                    self.confirm_action_has_been_donn(action)
                    return True

                case "Cancel":
                    self.click_button(self.elements.btn_cancel)
                    self.confirm_action_has_been_donn(action)
                    return True
                
                case "Ok":
                    self.click_button(self.elements.btn_ok)
                    self.confirm_action_has_been_donn(action)
                    return True

                case _:
                    return True

            raise Exception("lightbox notfound or have no this method")

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False

    # --
    # ...
    # --

    def confirm_action_has_been_donn(self, action="Close") -> bool:

        try:
            
            self.delay(1000)

    #         while self.is_element_there(self.elements.lightbox_):
    #             match action:
    #                 case "Close":
    #                     self.click_button(self.elements.btn_close)

    #                 case "Yes":
    #                     self.click_button(self.elements.btn_yes)

    #                 case "No":
    #                     self.click_button(self.elements.btn_no)

    #                 case "Cancel":
    #                     self.click_button(self.elements.btn_cancel)

    #     except Exception as exp:
    #         self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
    #         return False

    # def is_button_there(self, button_name="Close") -> bool:

    #     try:

    #         match button_name:
    #             case "Close":
    #                 btn = self.driver.find_element(*self.elements.btn_close)
    #                 if btn.get_attribute("style").find("display: none") == -1:
    #                     return True

    #             case "Yes":
    #                 btn = self.driver.find_element(*self.elements.btn_yes)
    #                 if btn.get_attribute("style").find("display: none") == -1:
    #                     return True

    #             case "No":
    #                 btn = self.driver.find_element(*self.elements.btn_no)
    #                 if btn.get_attribute("style").find("display: none") == -1:
    #                     return True
                    
    #             case "Cancel":
    #                 btn = self.driver.find_element(*self.elements.btn_cancel)
    #                 if btn.get_attribute("style").find("display: none") == -1:
    #                     return True
                    
    #             case "Yes_To_All":
    #                 btn = self.driver.find_element(*self.elements.btn_yes_to_all)
    #                 if btn.get_attribute("style").find("display: none") == -1:
    #                     return True
                    
    #             case "No_To_All":
    #                 btn = self.driver.find_element(*self.elements.btn_no_to_all)
    #                 if btn.get_attribute("style").find("display: none") == -1:
    #                     return True
                    
    #             case "Ok":
    #                 btn = self.driver.find_element(*self.elements.btn_ok)
    #                 if btn.get_attribute("style").find("display: none") == -1:
    #                     return True
                    
        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False
