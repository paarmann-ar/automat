from typing import Any
from test_applications.d_365.core.object_provider import ObjectProvider
from test_applications.d_365.core.base import Base


# --
# ...
# --


class Tipbox(Base):
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

    def __call__(self, tipbox="is_visible", action="got_it") -> bool:

        try:

            match tipbox:
                case "is_visible":
                    if not self.is_element_there(self.elements.tipbox_):
                        raise Exception("tipbox is not there")

            match action:
                case "got_it":
                    self.click_button(self.elements.btn_got_it)
                    return True

            raise Exception("tipbox notfound or have no this method")

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False