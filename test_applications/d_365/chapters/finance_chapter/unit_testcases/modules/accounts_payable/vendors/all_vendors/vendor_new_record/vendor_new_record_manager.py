from test_applications.d_365.core.object_provider import ObjectProvider
from test_applications.d_365.chapters.core.base_chapter import BaseChapter
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.accounts_payable.vendors.all_vendors.vendor_new_record.tab_vendor_general import (
    TabVendorGeneral,
)
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.accounts_payable.vendors.all_vendors.vendor_new_record.tab_parameters import (
    TabParameters,
)
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.accounts_payable.vendors.all_vendors.vendor_new_record.tab_administration import (
    TabAdministration,
)
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.accounts_payable.vendors.all_vendors.vendor_new_record.tab_note import (
    TabNote,
)
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.accounts_payable.vendors.all_vendors.vendor_new_record.tab_others import (
    TabOthers,
)
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.accounts_payable.vendors.all_vendors.vendor_new_record.tab_addresses import (
    TabAddresses,
)
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.accounts_payable.vendors.all_vendors.vendor_new_record.tab_contact_information import (
    TabContactInformation,
)
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.accounts_payable.vendors.all_vendors.vendor_new_record.tab_miscellaneous_detail import (
    TabMiscellaneousDetail,
)
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.accounts_payable.vendors.all_vendors.vendor_new_record.tab_vendor_profile import (
    TabVendorProfile,
)
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.accounts_payable.vendors.all_vendors.vendor_new_record.tab_purchasing_demographics import (
    TabPurchasingDemographics,
)
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.accounts_payable.vendors.all_vendors.vendor_new_record.tab_invoice_and_delivery import (
    TabInvoiceAndDelivery,
)
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.accounts_payable.vendors.all_vendors.vendor_new_record.tab_purchase_order_defaults import (
    TabPurchaseOrderDefaults,
)
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.accounts_payable.vendors.all_vendors.vendor_new_record.tab_payment import (
    TabPayment,
)
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.accounts_payable.vendors.all_vendors.vendor_new_record.tab_retail import (
    TabRetail,
)
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.accounts_payable.vendors.all_vendors.vendor_new_record.tab_financial_dimensions import (
    TabFinancialDimensions,
)

from typing import Any
from test_applications.d_365.abstrct_classes.page.page import Page
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.accounts_payable.vendors.all_vendors.all_vendors_top_gadget import AllVendorsTopGadget
from test_applications.d_365.chapters.finance_chapter.unit_testcases.toolbars.toolbars import (
    Toolbars,
)
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.accounts_payable.vendors.all_vendors.all_vendors_standard_view import (
    AllVendorsStandardView,
)

# --
# ...
# --


class VendorNewRecordManager(BaseChapter, Page):
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
                    self.add_new_vendor_manager(**kwargs)

                case _:
                    raise Exception(
                        f"class {__class__.__name__} have no method {action}."
                    )

            return self

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
            self.tab_vendor_general = TabVendorGeneral()
            self.tab_parameters = TabParameters()
            self.tab_administration = TabAdministration()
            self.tab_note = TabNote()
            self.tab_others = TabOthers()
            self.tab_addresses = TabAddresses()
            self.tab_contact_information = TabContactInformation()
            self.tab_miscellaneous_detail = TabMiscellaneousDetail()
            self.tab_vendor_profile = TabVendorProfile()
            self.tab_purchasing_demographics = TabPurchasingDemographics()
            self.tab_invoice_and_delivery = TabInvoiceAndDelivery()
            self.tab_purchase_order_defaults = TabPurchaseOrderDefaults()
            self.tab_payment = TabPayment()
            self.tab_retail = TabRetail()
            self.tab_financial_dimensions = TabFinancialDimensions()
            self.all_vendors_standard_view = AllVendorsStandardView()

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

            self.tipbox()

            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False

    # --
    # ... rollback
    # --
    
    @BaseChapter.log
    def new_vendor_rollback(self) -> bool:

        try:

            self.goto_start_point()

            self.all_vendors_standard_view.search_item = self.state["vendor_name"]
            while self.all_vendors_standard_view.select_vendor():
                self.delay(1000)

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
    def add_new_vendor_manager(self, **kwargs) -> bool:

        try:

            for _, tab in kwargs.items():
                print(tab)

                match tab:
                    case "get_vendor_account":
                        self.tab_vendor_general.get_vendor_account()
                                              
                    case "new_vendor":
                        self.all_vendors_top_gadget.new_vendor()

                    case "edit_vendor":
                        self.all_vendors_top_gadget.edit_vendor()

                    case "save_vendor":
                         self.all_vendors_top_gadget.save_vendor()
                        
                    case "back_vendor":
                        self.all_vendors_top_gadget.back_vendor()

                    case "tab_vendor_general":
                        self.tab_vendor_general()

                    case "tab_parameters":
                        self.tab_parameters()

                    case "tab_administration":
                        self.tab_administration()

                    case "tab_note":
                        self.tab_note()

                    case "tab_others":
                        self.tab_others()

                    case "tab_addresses":
                        self.tab_addresses.add_new_address()

                    case "tab_contact_information":
                        self.tab_contact_information.add_contact_information()

                    case "tab_miscellaneous_detail":
                        self.tab_miscellaneous_detail()

                    case "tab_vendor_profile":
                        self.tab_vendor_profile()

                    case "tab_purchasing_demographics":
                        self.tab_purchasing_demographics()

                    case "tab_invoice_and_delivery":
                        self.tab_invoice_and_delivery()

                    case "tab_purchase_order_defaults":
                        self.tab_purchase_order_defaults()

                    case "tab_payment":
                        self.tab_payment()

                    case "tab_retail":
                        self.tab_retail()

                    case "tab_financial_dimensions":
                        self.tab_financial_dimensions()

                    case _:
                        pass

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False