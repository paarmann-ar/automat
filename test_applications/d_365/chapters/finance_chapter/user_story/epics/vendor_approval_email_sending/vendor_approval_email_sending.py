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
from test_applications.d_365.chapters.finance_chapter.unit_testcases.toolbars.toolbars import (
    Toolbars,
)
from test_applications.d_365.chapters.finance_chapter.user_story.modules.account_payable.approval_vendor import (
    ApprovalVendor,
)
from test_applications.d_365.chapters.finance_chapter.user_story.epics.invoice_workflow.invoice_workflow_rollback import (
    InvoiceWorkflowRollback,
)
from test_applications.d_365.chapters.finance_chapter.user_story.modules.account_payable.vendor_bank_account import (
    VendorBankAccount,
)
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.tax.setup.sales_tax.tax_exempt_numbers.tax_exempt_number_manager import (
    TaxExemptNumberManager,
)
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.accounts_payable.inquiries_and_reports.vendor_approval_status.vendor_approval_status_top_gadget import (
    VendorApprovalStatusTopGadget,
)
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.accounts_payable.inquiries_and_reports.vendor_approval_status.create_alert_rule.create_alert_rule import CreateAlertRule
# --
# ...
# --


class VendorApprovalEmailSending(BaseChapter, BaseUserStory):
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
            self.tax_exempt_number_manager = TaxExemptNumberManager()
            self.vendor_bank_account = VendorBankAccount()
            self.vendor_new_record_manager = VendorNewRecordManager()
            self.approval_vendor = ApprovalVendor()
            self.invoice_workflow_rollback = InvoiceWorkflowRollback()
            self.vendor_approval_status_top_gadget = VendorApprovalStatusTopGadget()
            self.create_aler_rule = CreateAlertRule()

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
    def vendor_approval_email_sending(self) -> bool:

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

            self.toolbars.search_for_a_page = ("Vendor Approval Status", True)
            self.toolbars.set_text_in_search_for_a_page()

            self.vendor_approval_status_top_gadget.options()
            self.delay(1000)
            
            self.vendor_approval_status_top_gadget.create_a_custom_alert()
            self.delay(1000)

            self.create_aler_rule()

            self.delay(220)

            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False
