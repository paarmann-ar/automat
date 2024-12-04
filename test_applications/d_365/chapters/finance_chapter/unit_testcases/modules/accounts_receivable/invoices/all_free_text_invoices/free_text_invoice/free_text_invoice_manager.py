from test_applications.d_365.core.object_provider import ObjectProvider
from test_applications.d_365.chapters.core.base_chapter import BaseChapter
from typing import Any
from test_applications.d_365.abstrct_classes.page.page import Page
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.accounts_receivable.invoices.all_free_text_invoices.free_text_invoice.tab_free_text_invoice_header import (
    TabFreeTextInvoiceHeader,
)
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.accounts_receivable.invoices.all_free_text_invoices.free_text_invoice.tab_detail_lines import (
    TabDetailLines,
)
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.accounts_receivable.invoices.all_free_text_invoices.free_text_invoice.tab_lines import (
    TabLines,
)
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.accounts_receivable.invoices.all_free_text_invoices.free_text_invoice.free_text_invoice_top_gadget import (
    FreeTextInvoiceTopGadget,
)

# --
# ...
# --


class FreeTextInvoiceManager(BaseChapter, Page):
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
                    self.add_new_free_text_invoice(**kwargs)

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
        return ObjectProvider()(
            __file__.replace(".py", ".json ", -1).replace("\\", "/").replace(" c", "")
        )

    # --
    # ... setup, teardown and prepare
    # --

    def __setup(self) -> bool:

        try:

            super().setup()

            self.tab_free_text_invoice_header = TabFreeTextInvoiceHeader()
            self.tab_lines = TabLines()
            self.tab_detail_lines = TabDetailLines()
            self.free_text_invoice_top_gadget = FreeTextInvoiceTopGadget()

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

    @BaseChapter.wait_for(
        element_for_waiting_until_visible="frm_free_text_invoice",
        type_of_element="text_to_search",
    )
    @BaseChapter.log
    def add_new_free_text_invoice(self, **kwargs) -> bool:

        try:

            for _, tab in kwargs.items():
                match tab:
                    case "tab_free_text_invoice_header":
                        self.tab_free_text_invoice_header()

                    case "tab_lines":
                        self.tab_lines()

                    case "tab_detail_lines":
                        self.tab_detail_lines()

                    case "post":
                        self.free_text_invoice_top_gadget.post()

                    case "save":
                        self.free_text_invoice_top_gadget.save()

                    case _:
                        pass

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False
