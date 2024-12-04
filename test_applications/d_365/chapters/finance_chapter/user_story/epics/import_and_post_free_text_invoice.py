from typing import Any
from test_applications.d_365.core.object_provider import ObjectProvider
from test_applications.d_365.chapters.core.base_chapter import BaseChapter
from test_applications.d_365.chapters.core.base_user_story import BaseUserStory
from test_applications.d_365.chapters.finance_chapter.unit_testcases.toolbars.toolbars import (
    Toolbars,
)
from test_applications.d_365.chapters.finance_chapter.user_story.modules.accounts_receivable.import_free_text_invoice import (
    ImportFreeTextInvoice,
)
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.accounts_receivable.periodic_tasks.free_text_invoice.free_text_invoice_import.free_text_invoice_import_top_gadget import (
    FreeTextInvoiceImportTopGadget,
)
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.accounts_receivable.invoices.all_free_text_invoices.all_free_text_invoices_top_gadget import (
    AllFreeTextInvoicesTopGadget,
)
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.accounts_receivable.invoices.all_free_text_invoices.all_free_text_invoices_standard_view import (
    AllFreeTextInvoicesStandardView,
)
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.accounts_receivable.periodic_tasks.free_text_invoice.free_text_invoice_import.create_free_text_invoices.create_free_text_invoices import (
    CreateFreeTextInvoices,
)
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.accounts_receivable.customers.all_customers.all_customers_standard_view import (
    AllCustomersStandardView,
)
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.accounts_receivable.customers.all_customers.all_customers_top_gadget import (
    AllCustomersTopGadget,
)
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.system_administration.setup.email.inquiries.email_history.email_history_top_gadget import (
    EmailHistoryTopGadget,
)
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.system_administration.setup.email.inquiries.email_history.email_history_standard_view import (
    EmailHistoryStandardView,
)
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.accounts_receivable.periodic_tasks.free_text_invoice.free_text_invoice_import.free_text_invoice_import_file_selection_manual import (
    FreeTextInvoiceImportFileSelectionManual,
)

# --
# ...
# --


class ImportAndPostFreeTextInvoice(BaseChapter, BaseUserStory):
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
            self.import_free_text_invoice = ImportFreeTextInvoice()
            self.free_text_invoice_import_top_gadget = FreeTextInvoiceImportTopGadget()
            self.create_free_text_invoices = CreateFreeTextInvoices()
            self.all_free_text_invoices_top_gadget = AllFreeTextInvoicesTopGadget()
            self.all_free_text_invoices_standard_view = (
                AllFreeTextInvoicesStandardView()
            )

            self.all_customers_top_gadget = AllCustomersTopGadget()
            self.all_Customers_standard_view = AllCustomersStandardView()

            self.email_history_top_gadget = EmailHistoryTopGadget()
            self.email_history_standard_view = EmailHistoryStandardView()
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
    def import_and_post_free_text_invoice(self) -> bool:

        try:

            self.toolbars.change_mandant(mandant=("139", True))

            self.toolbars.search_for_a_page = ("Free text invoice import", True)
            self.toolbars.set_text_in_search_for_a_page()

            self.delay(220)

            self.free_text_invoice_import_top_gadget.import_invoice_free_text_invoice_import()
            self.delay(220)

            self.free_text_invoice_import_file_selection_manual.debitor_nummer = (
                "D13900000049",
                True,
            )
            self.free_text_invoice_import_file_selection_manual.free_text_invoice_import_file_selection_manual()
            self.delay(220)

            self.toolbars.search_for_a_page = ("Free text invoice import", True)
            self.toolbars.set_text_in_search_for_a_page()

            self.free_text_invoice_import_top_gadget.import_invoice_free_text_invoice_post()
            self.delay(220)

            self.create_free_text_invoices.create_free_text_invoices()

            self.toolbars.search_for_a_page = ("all free text invoice", True)
            self.toolbars.search_for_a_page = ("Free text invoice", True)
            self.toolbars.set_text_in_search_for_a_page()

            self.all_free_text_invoices_standard_view.invoice_number = (
                "D13900000049",
                True,
            )
            self.all_free_text_invoices_standard_view.select()

            self.toolbars.search_for_a_page = ("all customers", True)
            self.toolbars.set_text_in_search_for_a_page()

            self.all_Customers_standard_view.account_number = ("D13900000049", True)
            self.all_Customers_standard_view.select_customer_account_number()
            self.all_customers_top_gadget.all_customers_customer_email_history()

            self.email_history_standard_view.reference_number = ("D13900000049", True)
            self.email_history_top_gadget.email_detail()

            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False
