from typing import Any
from test_applications.d_365.core.object_provider import ObjectProvider
from test_applications.d_365.chapters.core.base_chapter import BaseChapter
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.accounts_payable.vendors.all_vendors.vendor_new_record.vendor_new_record_manager import (
    VendorNewRecordManager,
)
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.accounts_payable.vendors.all_vendors.vendor_bank_accounts.vendor_bank_accounts import (
    VendorBankAccounts,
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
from test_applications.d_365.chapters.finance_chapter.user_story.modules.account_payable.vendor_bank_account import VendorBankAccount
from test_applications.d_365.chapters.finance_chapter.user_story.modules.account_payable.create_vendor_invoice import CreateVendorInvoice

# --
# ...
# --


class InvoiceWorkflowRollback(BaseChapter, BaseUserStory):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.elements = self.get_elements()
        self.__prepare(**kwargs)
        self.__setup()

        print(__class__.__name__, id(__class__))

    # --
    # ... call
    # --

    def __call__(self, action="rollback", **kwargs) -> Any:

        try:

            if super_result := super().__call__(action, **kwargs):
                return super_result

            match action:
                case "rollback":
                    self.invoice_workflow_rollback()

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
            self.define_new_tax_exempt_numbers = DefineNewTaxExemptNumber()
            self.all_vendors_top_gadget = AllVendorsTopGadget()
            self.define_vendor = DefineVendor()
            self.vendor_bank_account = VendorBankAccount()
            self.create_vendor_invoice = CreateVendorInvoice()
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
    def invoice_workflow_rollback(self) -> bool:

        try:

            self.create_vendor_invoice.rollback_new_vendor_invoice()

            self.define_vendor.define_new_vendor_rollback()

            self.define_new_tax_exempt_numbers.define_new_tax_exempt_number_rollback()

            self.vendor_bank_account.vendor_bank_accounts_rollback()
            
            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False
