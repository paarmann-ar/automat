from typing import Any
from test_applications.d_365.core.object_provider import ObjectProvider
from test_applications.d_365.chapters.core.base_chapter import BaseChapter
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.accounts_payable.vendors.all_vendors.vendor_new_record.vendor_new_record_manager import (
    VendorNewRecordManager,
)

from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.accounts_payable.vendors.all_vendors.all_vendors_top_gadget import (
    AllVendorsTopGadget,
)
from test_applications.d_365.chapters.core.base_user_story import BaseUserStory
from test_applications.d_365.chapters.finance_chapter.user_story.modules.tax.setup.sales_tax.tax_exempt_numbers.define_new_tax_exempt_number import (
    DefineNewTaxExemptNumber,
)
from test_applications.d_365.chapters.finance_chapter.unit_testcases.toolbars.toolbars import (
    Toolbars,
)
from test_applications.d_365.chapters.finance_chapter.user_story.modules.account_payable.define_vendor import (
    DefineVendor,
)

from test_applications.d_365.chapters.finance_chapter.user_story.modules.account_payable.approval_vendor import (
    ApprovalVendor,
)
from test_applications.d_365.chapters.finance_chapter.user_story.modules.account_payable.create_vendor_invoice import (
    CreateVendorInvoice,
)
from test_applications.d_365.chapters.finance_chapter.user_story.epics.invoice_workflow.invoice_workflow_rollback import InvoiceWorkflowRollback
from test_applications.d_365.chapters.finance_chapter.user_story.modules.account_payable.vendor_bank_account import VendorBankAccount
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.tax.setup.sales_tax.tax_exempt_numbers.tax_exempt_number_manager import TaxExemptNumberManager


# --
# ...
# --


class InvoiceWorkflow(BaseChapter, BaseUserStory):
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
        return ObjectProvider()(__file__.replace(".py", ".json ", -1).replace("\\", "/").replace(" c", ""))

    # --
    # ... setup, teardown and prepare
    # --

    def __setup(self) -> bool:

        try:

            super().setup()

            self.toolbars = Toolbars()
            self.tax_exempt_number_manager = TaxExemptNumberManager()
            self.vendor_bank_account = VendorBankAccount()
            self.all_vendors_top_gadget = AllVendorsTopGadget()
            self.vendor_new_record_manager = VendorNewRecordManager()
            self.define_vendor = DefineVendor()
            self.approval_vendor = ApprovalVendor()
            self.create_vendor_invoice = CreateVendorInvoice()
            self.invoice_workflow_rollback = InvoiceWorkflowRollback()

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

            self.state["vendor_account"] = None
            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False

    # --
    # ... methods
    # --

    @BaseChapter.log
    def invoice_workflow(self) -> bool:

        try:

            self.state["vendor_name"] = "vendor test112", True

            self.toolbars.change_mandant()

            self.invoice_workflow_rollback()

            self.tax_exempt_number_manager(
                step_10="new",
                step_20="add_new_tax_exempt_number",
                step_30="save",
                step_40="back",
            )

            self.vendor_new_record_manager(
                step_1="new_vendor",
                step_2="tab_vendor_general",
                step_4="tab_addresses",
                step_45="get_vendor_account",
                step_5="tab_contact_information",
                step_6="tab_invoice_and_delivery",
                step_7="tab_payment",
                step_8="save_vendor",
                step_9="back_vendor",
            )

            self.vendor_bank_account()

            self.approval_vendor.approval_vendor()

            self.delay(220)

            self.create_vendor_invoice.create_new_vendor_invoice()

            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False
