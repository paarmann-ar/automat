from typing import Any
from test_applications.d_365.core.object_provider import ObjectProvider
from test_applications.d_365.chapters.core.base_chapter import BaseChapter
from test_applications.d_365.abstrct_classes.tab.tab import Tab

# --
# ...
# --


class TabSetup(BaseChapter, Tab):
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
                    self.tab_setup()

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
        text_code=("", True),
        message_to_bank=("", True),
        exchange_reference=("", True),
        cross_rate=("", True),
        payment_specification_parameter=("", True),
        currency=("", True),
    ) -> bool:

        try:

            if super().prepare():
                return True

            self.text_code = text_code
            self.message_to_bank = message_to_bank
            self.exchange_reference = exchange_reference
            self.cross_rate = cross_rate
            self.payment_specification_parameter = payment_specification_parameter
            self.currency = currency
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
    def tab_setup(self) -> bool:

        try:

            self.textbox(self.elements.txb_text_code, self.text_code)
            self.textbox(self.elements.txb_message_to_bank, self.message_to_bank)
            self.textbox(self.elements.txb_exchange_reference, self.exchange_reference)
            self.textbox(self.elements.txb_cross_rate, self.cross_rate)
            self.textbox(
                self.elements.txb_payment_specification_parameter,
                self.payment_specification_parameter,
            )
            self.textbox(self.elements.cmd_currency, self.currency)

            self.delay(220)

            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False
