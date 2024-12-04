from typing import Any
from test_applications.d_365.core.base import Base

# --
# ...
# --


class Page(Base):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    # --
    # ... prepare
    # --

    def prepare(self, page_text_element=None) -> bool:

        try:

            self.wait_for_visibility(page_text_element)

            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False

    # --
    # ... click_sidebar
    # --

    def click_sidebar(function) -> bool:

        try:

            def inner_function(*args, **kwargs):
                class_ = args[0]
                class_.move_click(class_.elements.btn_sidebar)

                return function(*args, **kwargs)

            return inner_function

        except Exception as exp:
            print(f"{repr(exp)}")
            return False