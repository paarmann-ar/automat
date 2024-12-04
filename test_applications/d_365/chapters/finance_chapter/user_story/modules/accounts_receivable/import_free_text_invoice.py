from typing import Any
from test_applications.d_365.core.object_provider import ObjectProvider
from test_applications.d_365.chapters.core.base_chapter import BaseChapter
from test_applications.d_365.chapters.core.base_user_story import BaseUserStory
from test_applications.d_365.chapters.finance_chapter.unit_testcases.toolbars.toolbars import (
    Toolbars,
)

from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.accounts_receivable.periodic_tasks.free_text_invoice.free_text_invoice_import.free_text_invoice_import_file_selection_manual import (
    FreeTextInvoiceImportFileSelectionManual,
)
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.accounts_receivable.periodic_tasks.free_text_invoice.free_text_invoice_import.free_text_invoice_import_standard_view import (
    FreeTextInvoiceImportStandardView,
)
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.accounts_receivable.periodic_tasks.free_text_invoice.free_text_invoice_import.free_text_invoice_import_top_gadget import (
    FreeTextInvoiceImportTopGadget,
)

# --
# ...
# --


class ImportFreeTextInvoice(BaseChapter, BaseUserStory):
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
                case _:
                    raise Exception(
                        f"class {__class__.__name__} have no method {action}."
                    )

            return True

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
            self.free_text_invoice_import_file_selection_manual = (
                FreeTextInvoiceImportFileSelectionManual()
            )
            self.free_text_invoice_import_standard_view = (
                FreeTextInvoiceImportStandardView()
            )
            self.free_text_invoice_import_top_gadget = FreeTextInvoiceImportTopGadget()

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

            if super().prepare():
                return True

            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False

    # --
    # ... methods
    # --

    @BaseChapter.log
    def import_free_text_invoice(self) -> bool:

        try:

            self.toolbars.change_mandant(mandant=("139", True))

            self.toolbars.search_for_a_page = ("Free text invoice import", True)
            self.toolbars.set_text_in_search_for_a_page()

            self.delay(220)

            self.free_text_invoice_import_top_gadget.import_invoice_free_text_invoice_import()
            self.delay(220)

            self.free_text_invoice_import_file_selection_manual.free_text_invoice_import_file_selection_manual()
            self.delay(220)

            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False
