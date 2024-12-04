from typing import Any
from test_applications.d_365.core.object_provider import ObjectProvider
from test_applications.d_365.chapters.core.base_chapter import BaseChapter
from test_applications.d_365.chapters.core.base_user_story import BaseUserStory
from test_applications.d_365.chapters.finance_chapter.unit_testcases.toolbars.toolbars import (
    Toolbars,
)
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.accounts_payable.invoices.pending_vendor_invoices.pending_vendor_invoices_standard_view import (
    PendingVendorInvoicesStandardView,
)
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.accounts_payable.invoices.pending_vendor_invoices.pending_vendor_invoices_top_gadget import (
    PendingVendorInvoicesTopGadget,
)
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.accounts_payable.invoices.pending_vendor_invoices.pending_vendor_invoices_top_gadget import (
    PendingVendorInvoicesTopGadget,
)
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.accounts_payable.invoices.pending_vendor_invoices.vendor_invoices.vendor_invoice.vendor_invoice_manager import (
    VendorInvoiceManager,
)
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.accounts_payable.invoices.pending_vendor_invoices.vendor_invoices.vendor_invoice.vendor_invoice_top_gadget import (
    VendorInvoiceTopGadget,
)

from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.accounts_payable.invoices.pending_vendor_invoices.vendor_invoices.attachments_for_vendor_invoices.attachments_for_vendor_invoice_manager import (
    AttachmentsForVendorInvoiceManager,
)
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.accounts_payable.invoices.pending_vendor_invoices.vendor_invoices.attachments_for_vendor_invoices.attachments_for_vendor_invoice_top_gadget import (
    AttachmentsForVendorInvoiceTopGadget,
)
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.accounts_payable.invoices.pending_vendor_invoices.vendor_invoices.workflow_for_vendor_invoces.workflow_for_vendor_invoice import (
    WorkflowForVendorInvoice,
)

from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.vendor_invoice_recognition.vendor_invoice_lines.vendor_invoice_lines_top_gadget import (
    VendorInvoiceLinesTopGadget,
)
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.vendor_invoice_recognition.vendor_invoice_lines.vendor_invoice_lines_standard_view import (
    VendorInvoiceLinesStandardView,
)
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.vendor_invoice_recognition.invoice_overview_for_approvers.invoice_overview_for_approvers_standard_view import (
    InvoiceOverviewForApproversStandardView,
)
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.vendor_invoice_recognition.invoice_overview_for_approvers.invoice_overview_for_approvers_top_gadget import (
    InvoiceOverviewForApproversTopGadget,
)
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.accounts_payable.inquiries_and_reports.invoice.invoice_journal.invoice_journal_standard_view import (
    InvoiceJournalStandardView,
)
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.accounts_payable.inquiries_and_reports.invoice.invoice_journal.invoice_journal_top_gadget import (
    InvoiceJournalTopGadget,
)

# --
# ...
# --


class CreateVendorInvoice(BaseChapter, BaseUserStory):
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
                        f"rdc_automat: class {__class__.__name__} have no method {action}."
                    )

            return True

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

            self.toolbars = Toolbars()
            self.pending_vendor_invoices_top_gadget = PendingVendorInvoicesTopGadget()
            self.vendor_invoice_manager = VendorInvoiceManager()
            self.vendor_invoice_top_gadget = VendorInvoiceTopGadget()
            self.attachments_for_vendor_invoices_manager = (
                AttachmentsForVendorInvoiceManager()
            )

            self.Attachments_for_vendor_invoice_top_gadget = (
                AttachmentsForVendorInvoiceTopGadget()
            )

            self.workflow_for_vendor_invoice = WorkflowForVendorInvoice()
            self.vendor_invoice_lines_standard_view = VendorInvoiceLinesStandardView()
            self.vendor_invoice_lines_top_gadget = VendorInvoiceLinesTopGadget()
            self.invoice_overview_for_approvers_standard_view = (
                InvoiceOverviewForApproversStandardView()
            )
            self.invoice_overview_for_approvers_top_gadget = (
                InvoiceOverviewForApproversTopGadget()
            )
            self.invoice_journal_standard_view = InvoiceJournalStandardView()
            self.invoice_journal_top_gadget = InvoiceJournalTopGadget()

            self.pending_vendor_invoices_standard_view = (
                PendingVendorInvoicesStandardView()
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

            self.toolbars.search_for_a_page = ("pending vendor invoice", True)
            self.toolbars.set_text_in_search_for_a_page()

            self.delay(220)

            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False

    # --
    # ... rollback
    # --

    @BaseChapter.log
    def rollback_new_vendor_invoice(self) -> bool:

        try:

            self.goto_start_point()

            self.pending_vendor_invoices_standard_view.search_item_text = "Name"
            self.pending_vendor_invoices_standard_view.search_item = self.state["vendor_name"]
            self.pending_vendor_invoices_standard_view.select()

            self.pending_vendor_invoices_top_gadget.delete_pending_vendor_invoices()

            self.delay(220)

            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False
        
    # --
    # ... methods
    # --

    @BaseChapter.log
    def create_new_vendor_invoice(self) -> bool:

        try:

            self.goto_start_point()

            self.pending_vendor_invoices_top_gadget.new_pending_vendor_invoices()

            self.delay(220)

            self.vendor_invoice_manager.add_new_vendor_invoice(
                step_10="tab_header",
                step_20="tab_lines",
                step_30="tab_detail_lines",
            )

            self.vendor_invoice_top_gadget.attachments_vendor_invoice()
            self.Attachments_for_vendor_invoice_top_gadget.new_note_attachment()

            self.delay(220)

            self.attachments_for_vendor_invoices_manager.attachments_for_vendor_invoice(
                step_10="attachments_vendor_invoice",
                step_20="new_note_attachment",
                step_30="tab_attachment_for_vendor_invoices_general",
                step_40="tab_attachment",
                step_50="attachments_for_vendor_invoice_description",
            )

            self.Attachments_for_vendor_invoice_top_gadget.save()

            self.delay(220)

            self.Attachments_for_vendor_invoice_top_gadget.back()

            self.vendor_invoice_top_gadget.workflow_vendor_invoice()

            self.delay(220)

            self.workflow_for_vendor_invoice.workflow_for_vendor_invoice()

            self.delay(220)

            self.pending_vendor_invoices_top_gadget.save_pending_vendor_invoices()

            self.toolbars.search_for_a_page = ("Vendor Invoice Finance Overview", True)
            self.toolbars.set_text_in_search_for_a_page()

            self.delay(220)

            self.invoice_overview_for_approvers_standard_view.search_item = (
                self.state["vendor_invoice_nummer"],
                True,
            )
            self.invoice_overview_for_approvers_standard_view.search_item_text = (
                "Invoice"
            )
            self.invoice_overview_for_approvers_standard_view.select_number()

            self.invoice_overview_for_approvers_top_gadget.view_hide_attachment_invoice()

            self.delay(220)

            self.toolbars.search_for_a_page = ("Pending Invoice Lines", True)
            self.toolbars.set_text_in_search_for_a_page()

            self.delay(220)

            self.vendor_invoice_lines_standard_view.search_item = (
                self.state["vendor_invoice_nummer"],
                True,
            )
            self.vendor_invoice_lines_standard_view.search_item_text = "Invoice"

            self.vendor_invoice_lines_standard_view.select_pending_invoice_lines(
                is_select_search_field=False
            )
            self.vendor_invoice_lines_top_gadget.workflow_pending_invoice_lines()
            self.delay(220)

            self.workflow_for_vendor_invoice.approve_workflow_for_vendor_invoice()

            self.delay(220)

            self.toolbars.search_for_a_page = ("pending vendor invoice", True)
            self.toolbars.set_text_in_search_for_a_page()

            self.pending_vendor_invoices_standard_view.search_item = (
                self.state["vendor_invoice_nummer"],
                True,
            )
            self.pending_vendor_invoices_standard_view.search_item_text = "Invoice"
            self.pending_vendor_invoices_standard_view.select()

            self.delay(220)

            self.pending_vendor_invoices_top_gadget.post_pending_vendor_invoices()

            self.delay(220)

            self.toolbars.search_for_a_page = ("Invoice journal", True)
            self.toolbars.full_address = (
                "Accounts payable > Inquiries and reports > Invoice"
            )
            self.toolbars.set_full_address_in_search_for_a_page()

            self.delay(220)

            self.invoice_journal_standard_view.search_item = (
                self.state["vendor_invoice_nummer"],
                True,
            )
            self.invoice_journal_standard_view.search_item_text = "Invoice"
            self.invoice_journal_standard_view.select_invoice_journal_number(
                is_select_search_field=False
            )

            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False