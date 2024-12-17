from test_applications.d_365.core.object_provider import ObjectProvider
from test_applications.d_365.chapters.core.base_chapter import BaseChapter
from typing import Any
from test_applications.d_365.abstrct_classes.form.form import Form
from test_applications.windows_components.open_file_dialog import OpenFileDialog
from test_applications.d_365.chapters.finance_chapter.unit_testcases.toolbars.toolbars import Toolbars


# --
# ...
# --


class CreateFreeTextInvoices(BaseChapter, Form):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.elements = self.get_elements()
        self.__prepare(**kwargs)
        self.__setup()

        print(__class__.__name__, id(__class__))

    # --
    # ... call
    # --

    def __call__(self, action="", **kwargs) -> Any:

        try:

            if super_result := super().__call__(action, **kwargs):
                return super_result

            match action:
                case "":
                    self.create_free_text_invoices()

                case _:
                    raise Exception(
                        f"class {__class__.__name__} have no method {action}."
                    )

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False

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

            super().setup()

            self.toolbars = Toolbars()

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

    def __prepare(
        self,
        is_post_free_text_invoices=(True, True),
        is_send_email=(True, True),
    ) -> bool:

        try:

            if super().prepare():
                return True

            self.is_post_free_text_invoices = is_post_free_text_invoices
            self.is_send_email = is_send_email

            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False

    # --
    # ... methods
    # --

    @BaseChapter.wait_for(
        element_for_waiting_until_visible="frm_create_free_text_invoices",
        type_of_element="text_to_search",
    )
    @BaseChapter.log
    def create_free_text_invoices(self, **kwargs) -> bool:

        try:

            self.checkbox(self.elements.chk_post_free_text_invoices, self.is_post_free_text_invoices)
            self.checkbox(self.elements.chk_send_email, self.is_send_email)

            self.click_button(self.elements.btn_ok)

            self.blocking_message()
            self.delay(220)

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False