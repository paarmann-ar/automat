from typing import Any
from test_applications.d_365.core.object_provider import ObjectProvider
from test_applications.d_365.chapters.core.base_chapter import BaseChapter
from test_applications.d_365.abstrct_classes.page.page import Page
from  test_applications.d_365.chapters.finance_chapter.unit_testcases.toolbars.toolbars import Toolbars
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.accounts_receivable.periodic_tasks.free_text_invoice.free_text_invoice_import.free_text_invoice_import_top_gadget import (
    FreeTextInvoiceImportTopGadget,
)
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.accounts_receivable.periodic_tasks.free_text_invoice.free_text_invoice_import.free_text_invoice_import_standard_view import FreeTextInvoiceImportStandardView
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.accounts_receivable.periodic_tasks.free_text_invoice.free_text_invoice_import.free_text_invoice_import_file_selection_manual import (
    FreeTextInvoiceImportFileSelectionManual,
)
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.accounts_receivable.periodic_tasks.free_text_invoice.free_text_invoice_import.create_free_text_invoices.create_free_text_invoices import (
    CreateFreeTextInvoices,
)
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.accounts_receivable.invoices.all_free_text_invoices.all_free_text_invoices_standard_view import (
    AllFreeTextInvoicesStandardView,
)

# --
# ...
# --


class FreeTextInvoiceImportManager(BaseChapter, Page):
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
                    self.goto_start_point()
                    self.free_text_invoice_import_manager(**kwargs)

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
            self.free_text_invoice_import_top_gadget = FreeTextInvoiceImportTopGadget()
            self.free_ext_invoice_import_standard_view = FreeTextInvoiceImportStandardView()
            self.free_text_invoice_import_file_selection_manual = (
                FreeTextInvoiceImportFileSelectionManual()
            )
            self.create_free_text_invoices = CreateFreeTextInvoices()
            self.all_free_text_invoices_standard_view = (
                AllFreeTextInvoicesStandardView()
            )

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
    # ... go to start point
    # --

    @BaseChapter.log
    def goto_start_point(self) -> bool:

        try:

            self.toolbars.search_for_a_page = ("Free text invoice import", True)
            self.toolbars.set_text_in_search_for_a_page()

            self.tipbox()

            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False

    # --
    # ... rollback
    # --
    
    @BaseChapter.log
    def import_journal_rollback(self) -> bool:

        try:

            self.goto_start_point()
                
            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False
        
    # --
    # ... methods
    # --

    @BaseChapter.wait_for(
        element_for_waiting_until_visible="frm_free_text_invoice_import",
        type_of_element="text_to_search",
    )
    @BaseChapter.log
    def free_text_invoice_import_manager(self, **kwargs) -> bool:

        try:

            for _, tab in kwargs.items():
                match tab:

                    case "import":
                        self.free_text_invoice_import_top_gadget.import_invoice_free_text_invoice_import()

                    case "free_text_invoice_import_file_selection_manual":
                        self.free_text_invoice_import_file_selection_manual()
                        self.free_ext_invoice_import_standard_view.set_import_id()
                        self.free_ext_invoice_import_standard_view.search_item = self.state["import_id"]
                        self.free_ext_invoice_import_standard_view.select_free_text_invoice()

                    case "post":
                        self.free_text_invoice_import_top_gadget.import_invoice_free_text_invoice_post()

                    case "create_free_text_invoices":
                        self.create_free_text_invoices.create_free_text_invoices()

                    case "is_invoice_there":
                        self.toolbars.search_for_a_page = ("all free text invoice", True)
                        self.toolbars.set_text_in_search_for_a_page()

                        self.all_free_text_invoices_standard_view.search_item = self.state[
                            "customer_account"
                        ]
                        self.all_free_text_invoices_standard_view.select()

                    case _:
                        pass

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False