from test_applications.d_365.core.object_provider import ObjectProvider
from test_applications.d_365.chapters.core.base_chapter import BaseChapter
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.accounts_payable.invoices.pending_vendor_invoices.vendor_invoices.vendor_invoice.tab_vendor_invoice_header import (
    TabVendorInvoiceHeader,
)

from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.accounts_payable.invoices.pending_vendor_invoices.vendor_invoices.vendor_invoice.tab_lines import (
    TabLines,
)
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.accounts_payable.invoices.pending_vendor_invoices.vendor_invoices.vendor_invoice.tab_detail_lines import (
    TabDetailLines,
)
from typing import Any
from test_applications.d_365.abstrct_classes.page.page import Page

# --
# ...
# --


class VendorInvoiceManager(BaseChapter, Page):
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

            self.tab_vendor_invoice_header = TabVendorInvoiceHeader()
            self.tab_lines = TabLines()
            self.tab_detail_lines = TabDetailLines()

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
        element_for_waiting_until_visible="frm_vendor_invoice",
        type_of_element="text_to_search",
    )
    @BaseChapter.log
    def add_new_vendor_invoice(self, **kwargs) -> bool:

        try:

            for _, tab in kwargs.items():
                match tab:
                    case "tab_header":
                        self.tab_vendor_invoice_header()

                    case "tab_lines":
                        self.tab_lines()

                    case "tab_detail_lines":
                        self.tab_detail_lines()

                    case _:
                        pass

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False
