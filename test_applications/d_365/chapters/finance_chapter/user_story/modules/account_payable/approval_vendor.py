from typing import Any
from test_applications.d_365.core.object_provider import ObjectProvider
from test_applications.d_365.chapters.core.base_chapter import BaseChapter
from test_applications.d_365.chapters.finance_chapter.unit_testcases.login.login import Login
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.accounts_payable.vendors.all_vendors.all_vendors_top_gadget import (
    AllVendorsTopGadget,
)
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.accounts_payable.vendors.all_vendors.all_vendors_standard_view import (
    AllVendorsStandardView,
)
from test_applications.d_365.chapters.core.base_user_story import BaseUserStory
from test_applications.d_365.chapters.finance_chapter.unit_testcases.toolbars.toolbars import (
    Toolbars,
)
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.accounts_payable.inquiries_and_reports.vendor_approval_status.vendor_approval_status_standard_view import (
    VendorApprovalStatusStandardView,
)
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.accounts_payable.inquiries_and_reports.vendor_approval_status.vendor_approval_status_top_gadget import (
    VendorApprovalStatusTopGadget,
)

# --
# ...
# --


class ApprovalVendor(BaseChapter, BaseUserStory):
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
            self.login = Login()
            self.all_vendors_top_gadget = AllVendorsTopGadget()
            self.all_vendors_standard_view = AllVendorsStandardView()
            self.vendor_approval_status_top_gadget = VendorApprovalStatusTopGadget()
            self.vendor_approval_status_standard_view = (
                VendorApprovalStatusStandardView()
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

            self.toolbars.search_for_a_page = ("all vendors", True)
            self.toolbars.set_text_in_search_for_a_page()

            self.delay(220)

            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False

    # --
    # ... methods
    # --

    @BaseChapter.log
    def approval_vendor(self) -> bool:

        try:

            self.state["user_create_vendor"]=self.state["current_user"]
            self.goto_start_point()

            self.all_vendors_standard_view.search_item = (
                self.state["vendor_account"],
                True,
            )
            self.all_vendors_standard_view.search_item_text = "Vendor account"
            self.all_vendors_standard_view.select_vendor()

            self.delay(220)

            self.all_vendors_top_gadget.first_approval_vendor()

            self.toolbars.logout()
            self.login.username = 'Dummy365F2@redcare-pharmacy.com', True
            self.login.password = 'pVrg2q5z7mAx', True
            self.login.login(is_use_iifa=False, is_wait_for_stay_signed_in=False)

            self.toolbars.search_for_a_page = ("Vendor Approval Status", True)
            self.toolbars.set_text_in_search_for_a_page()

            self.delay(220)

            self.vendor_approval_status_standard_view.search_item = self.state["user_create_vendor"], True
            self.vendor_approval_status_standard_view.search_item_text = "Created from"
            self.vendor_approval_status_standard_view.select_vendor(is_click_on_selected=False)

            self.vendor_approval_status_top_gadget.second_approval_vendor()

            self.delay(1000)

            self.toolbars.logout()

            self.login.username = 'Dummy365F1@redcare-pharmacy.com', True
            self.login.password = 'TR5QWgRXqLOW', True
            self.login.login(is_use_iifa=False, is_wait_for_stay_signed_in=False)

            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False

    # --
    # ... rollback
    # --

    @BaseChapter.log
    def rollback_approval_vendor(self) -> bool:

        try:

            self.goto_start_point()

            self.delay(220)

            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False
