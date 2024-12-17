from test_applications.d_365.core.object_provider import ObjectProvider
from test_applications.d_365.chapters.core.base_chapter import BaseChapter
from typing import Any
from test_applications.d_365.abstrct_classes.form.form import Form
from test_applications.windows_components.open_file_dialog import OpenFileDialog
import CONSTS

# --
# ...
# --


class FreeTextInvoiceImportFileSelectionManual(BaseChapter, Form):
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
                    self.free_text_invoice_import_file_selection_manual()

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

            self.open_file = OpenFileDialog()

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
        file_address=(
            f"{CONSTS.ROOT_DIR}/.external_files/sample_files/free_text_invoice_import_file.csv",
            True,
        ),
        debitor_nummer=("D13900000049", True),
    ) -> bool:

        try:

            if super().prepare():
                return True

            self.file_address = file_address
            self.debitor_nummer = debitor_nummer

            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False

    # --
    # ... methods
    # --

    @BaseChapter.wait_for(
        element_for_waiting_until_visible="frm_free_text_invoice_import_file_selection_manual",
        type_of_element="text_to_search",
    )
    @BaseChapter.log
    def free_text_invoice_import_file_selection_manual(self, **kwargs) -> bool:

        try:

            self.click_button(self.elements.btn_browse)

            self.open_file(file_address=self.file_address)

            self.delay(220)

            while self.is_element_there(self.elements.btn_ok):
                self.click_button(self.elements.btn_ok)
                self.delay(220)

            self.blocking_message()
            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False
