from typing import Any
from test_applications.d_365.core.object_provider import ObjectProvider
from test_applications.d_365.chapters.core.base_chapter import BaseChapter
from test_applications.d_365.abstrct_classes.tab.tab import Tab

# --
# ...
# --


class TabBankGeneral(BaseChapter, Tab):
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
                    self.tab_general()

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
        bank_groups=("", False),
        vendor_account=("V139000270", True),
        routing_number_type=("None", True),
        DUNS=("", False),
        DUNS_segment=("", False),
        routing_number=("", False),
        bank_account_number=("0532013000", False),
        CIN=("", False),
        SWIFT_code=("", False),
        IBAN=("DE89370400440532013000", True),
        Active_date=("", False),
        expiration_date=("", False),
        status=("Active", True),
    ) -> bool:

        try:

            if super().prepare():
                return True

            self.bank_groups = bank_groups
            self.vendor_account = vendor_account
            self.routing_number_type = routing_number_type
            self.DUNS = DUNS
            self.DUNS_segment = DUNS_segment
            self.routing_number = routing_number
            self.bank_account_number = bank_account_number
            self.CIN = CIN
            self.SWIFT_code = SWIFT_code
            self.IBAN = IBAN
            self.Active_date = Active_date
            self.expiration_date = expiration_date
            self.status = status
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
    def tab_general(self) -> bool:

        try:

            self.textbox(self.elements.cmb_bank_groups, self.bank_groups)
            self.textbox(self.elements.txb_vendor_account, self.vendor_account)
            self.textbox(
                self.elements.cmb_routing_number_type, self.routing_number_type
            )
            self.textbox(self.elements.cmb_DUNS, self.DUNS)
            self.textbox(self.elements.txb_DUNS_segment, self.DUNS_segment)
            self.textbox(self.elements.txb_routing_number, self.routing_number)
            self.textbox(
                self.elements.txb_bank_account_number, self.bank_account_number
            )
            self.textbox(self.elements.txb_CIN, self.CIN)
            self.textbox(self.elements.txb_SWIFT_code, self.SWIFT_code)
            self.textbox(self.elements.txb_IBAN, self.IBAN)
            self.textbox(self.elements.txb_Active_date, self.Active_date)
            self.textbox(self.elements.txb_expiration_date, self.expiration_date)
            self.textbox(self.elements.txb_status, self.status)

            self.delay(220)

            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False
