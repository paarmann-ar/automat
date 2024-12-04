from typing import Any
from test_applications.d_365.core.object_provider import ObjectProvider
from test_applications.d_365.chapters.core.base_chapter import BaseChapter
from test_applications.d_365.abstrct_classes.tab.tab import Tab

# --
# ...
# --


class TabAdministration(BaseChapter, Tab):
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
                    self.tab_administration(),

                case _:
                    raise Exception(
                        f"class {__class__.__name__} have no method {action}."
                    )

            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False

    # --
    # ... get_elements
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
        vendor_hold=("Invoice", True),
        reason_code=("ChargeB", True),
        vendor_hold_realeas_date=("4/9/2024 12:00 AM", True),
        is_deactivated=(True, True),
        buyer_group=("", True),
        status=("None", True),
        vendor_interface_group=("DeActVend", True),
    ) -> bool:

        try:

            if super().prepare():
                return True

            self.vendor_hold = vendor_hold
            self.reason_code = reason_code
            self.vendor_hold_realeas_date = vendor_hold_realeas_date
            self.is_deactivated = is_deactivated
            self.buyer_group = buyer_group
            self.status = status
            self.vendor_interface_group = vendor_interface_group
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
    def tab_administration(self) -> bool:

        try:

            self.textbox(self.elements.cmb_vendor_hold, self.vendor_hold)
            self.textbox(
                self.elements.cmb_reason_code, self.reason_code, is_press_enter=True
            )
            self.textbox(
                self.elements.dt_vendor_hold_realeas_date, self.vendor_hold_realeas_date
            )

            self.checkbox(
                self.elements.chk_deactivated,
                self.is_deactivated,
            )
            self.components.combobox_type_2(
                self.elements.cmb_buyer_group, self.buyer_group
            )
            self.textbox(self.elements.txb_status, self.status)
            self.textbox(
                self.elements.cmb_vendor_interface_group,
                self.vendor_interface_group,
                is_press_enter=True,
            )

            self.delay(220)

            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False
