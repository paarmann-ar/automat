from typing import Any
from test_applications.d_365.core.object_provider import ObjectProvider
from test_applications.d_365.chapters.core.base_chapter import BaseChapter
from test_applications.d_365.abstrct_classes.tab.tab import Tab

# --
# ...
# --


class TabVendorProfile(BaseChapter, Tab):
    def __init__(
        self,
        *args,
        **kwargs,
    ) -> None:
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
                    self.tab_vendor_profile()

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

    def __prepare(
        self,
        is_bid_only=(True, True),
        is_one_time_supplier=(True, True),
        is_locally_owned=(True, True),
        is_small_business=(True, True),
        is_owner_is_a_service_veteran=(True, True),
        is_owner_is_disabled=(True, True),
        is_original_vendor_in_reporting=(True, True),
        is_self_invoice_vendor=(True, True),
    ) -> bool:

        try:

            if super().prepare():
                return True

            self.chk_bid_only = is_bid_only
            self.chk_one_time_supplier = is_one_time_supplier
            self.chk_locally_owned = is_locally_owned
            self.chk_small_business = is_small_business
            self.chk_owner_is_a_service_veteran = is_owner_is_a_service_veteran
            self.chk_owner_is_disabled = is_owner_is_disabled
            self.chk_original_vendor_in_reporting = is_original_vendor_in_reporting
            self.self_invoice_vendor = is_self_invoice_vendor
            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False

    # --
    # ... methods
    # --
    
    @Tab.expand_tab
    @BaseChapter.wait_for(element_for_waiting_until_visible="btn_tab")
    @BaseChapter.log
    def tab_vendor_profile(self) -> bool:

        try:

            self.checkbox(self.elements.chk_bid_only, self.is_bid_only)
            self.checkbox(
                self.elements.chk_one_time_supplier, self.is_one_time_supplier
            )
            self.checkbox(self.elements.chk_locally_owned, self.is_locally_owned)
            self.checkbox(self.elements.chk_small_business, self.is_small_business)
            self.checkbox(
                self.elements.chk_owner_is_a_service_veteran,
                self.is_owner_is_a_service_veteran,
            )
            self.checkbox(
                self.elements.chk_owner_is_disabled, self.is_owner_is_disabled
            )
            self.checkbox(
                self.elements.chk_original_vendor_in_reporting,
                self.is_original_vendor_in_reporting,
            )
            self.checkbox(
                self.elements.self_invoice_vendor, self.is_self_invoice_vendor
            )

            self.delay(220)

            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False
