from typing import Any
from test_applications.d_365.core.base import Base

class Sidebar(Base):
    def __init__(self) -> None:
        pass

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