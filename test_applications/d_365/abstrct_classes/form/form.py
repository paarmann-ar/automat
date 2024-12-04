from typing import Any
from test_applications.d_365.core.base import Base


class Form(Base):
    def __init__(self,*args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    # --
    # ... prepare
    # --

    def prepare(self, form_text_element=None) -> bool:

        try:

            self.wait_for_visibility(form_text_element)

            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False
