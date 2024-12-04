from typing import Any
from test_applications.d_365.core.base import Base


# --
# ...
# --

class Tab(Base):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    # --
    # ... expand tab
    # --

    def expand_tab(function) -> bool:

        try:

            def inner_function(*args, **kwargs):
                class_ = args[0]
                btn_tab = class_.elements.btn_tab

                if not class_.get_attribute_value(btn_tab, "aria-expanded"):
                    class_.move_click(btn_tab)
                    class_.delay(1000)

                return function(*args, **kwargs)

            return inner_function

        except Exception as exp:
            print(f"{repr(exp)}")
            return False
