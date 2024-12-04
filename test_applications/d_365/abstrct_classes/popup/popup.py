from typing import Any
from test_applications.d_365.core.base import Base


class Popup(Base):
    def __init__(self) -> None:
        pass

    # --
    # ... prepare
    # --

    def prepare(self, popup_header_text) -> bool:

        try:

            while not self.search_text_on_current_page_text(popup_header_text):
                self.delay(220)

            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False
