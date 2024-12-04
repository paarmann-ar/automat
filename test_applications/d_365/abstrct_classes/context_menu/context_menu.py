from typing import Any
from test_applications.d_365.core.object_provider import ObjectProvider
from test_applications.d_365.core.base import Base


# --
# ...
# --


class ContextMenu(Base):
    def __init__(self,*args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        
        self.elements = self.get_elements()
        print(__class__.__name__, id(__class__))

    # --
    # ...
    # --

    def get_elements(self) -> str:
        return ObjectProvider()(__file__.replace(".py", ".json ", -1).replace("\\", "/").replace(" c", ""))
    
    # --
    # ... setup, teardown and prepare
    # --

    def __setup(self, element) -> bool:

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

    def __call__(self, element) -> bool:

        try:

            self.wait_for_visibility(element)
            self.context_click(self.current_element)
            return self

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False

    # --
    # ...
    # --

    def click_context(self, context_menu="view_details", operation="click") -> bool:

        try:

            self.wait_for_visibility(self.elements.ctm_popup)

            match context_menu:
                case "view_details":
                    self.wait_for_visibility(self.elements.ctm_popup_view_details)
                    self.delay(220)

            if operation == "click":
                self.click(self.current_element)
                return True

            raise Exception("object not found or not clicked")

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False
