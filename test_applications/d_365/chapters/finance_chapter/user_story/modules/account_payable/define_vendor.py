from typing import Any
from test_applications.d_365.core.object_provider import ObjectProvider
from test_applications.d_365.chapters.core.base_chapter import BaseChapter
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.accounts_payable.vendors.all_vendors.vendor_new_record.vendor_new_record_manager import (
    VendorNewRecordManager,
)
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.accounts_payable.vendors.all_vendors.vendor_bank_accounts.vendor_bank_accounts import (
    VendorBankAccounts,
)
from test_applications.d_365.chapters.core.base_user_story import BaseUserStory
from test_applications.d_365.chapters.finance_chapter.user_story.modules.tax.setup.sales_tax.tax_exempt_numbers.define_new_tax_exempt_number import (
    DefineNewTaxExemptNumber,
)
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.accounts_payable.vendors.all_vendors.vendor_bank_accounts.vendor_bank_accounts import (
    VendorBankAccounts,
)
from test_applications.d_365.chapters.finance_chapter.unit_testcases.toolbars.toolbars import (
    Toolbars,
)
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.accounts_payable.vendors.all_vendors.all_vendors_standard_view import (
    AllVendorsStandardView,
)
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.accounts_payable.vendors.all_vendors.all_vendors_top_gadget import (
    AllVendorsTopGadget,
)

# --
# ...
# --


class DefineVendor(BaseChapter, BaseUserStory):
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
            self.all_vendors_top_gadget = AllVendorsTopGadget()
            self.all_vendors_standard_view = AllVendorsStandardView()
            self.vendor_new_record_manager = VendorNewRecordManager()

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

            self.toolbars.search_for_a_page = ("all vendors", True)
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
    def define_new_vendor_rollback(self) -> bool:

        try:

            self.goto_start_point()

            self.all_vendors_standard_view.search_item_text= "Name"
            self.all_vendors_standard_view.search_item = self.state["vendor_name"]
            while self.all_vendors_standard_view.select_vendor():
                self.delay(500)

                self.all_vendors_top_gadget.delete_vendor()
                self.delay(220)

                self.delete_all_cookies()
                self.delay(200)

            self.delay(220)

            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False
        
    # --
    # ... methods
    # --

    @BaseChapter.log
    def define_new_vendor(self) -> bool:

        try:

            self.goto_start_point()

            self.vendor_new_record_manager.add_new_vendor(
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

            self.delay(220)

            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False
