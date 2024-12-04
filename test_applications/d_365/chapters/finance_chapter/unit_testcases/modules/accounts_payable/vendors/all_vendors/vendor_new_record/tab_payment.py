from typing import Any
from test_applications.d_365.core.object_provider import ObjectProvider
from test_applications.d_365.chapters.core.base_chapter import BaseChapter
from test_applications.d_365.abstrct_classes.tab.tab import Tab

# --
# ...
# --


class TabPayment(BaseChapter, Tab):
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
                    self.tab_payment()

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
        term_of_payment=("N0", True),
        method_of_payment=("MP05_WireT", True),
        payment_type=("Electronic payment", False),
        payment_specification=("", False),
        payment_schedule=("", False),
        cash_discount=("IT0D_0%", True),
        bank_account=("01", False),
        payment_id=("", False),
        payment_day=("", False),
        bank_account_number=("", False),
        use_cash_discount=("Never", False),
        central_bank_purpose_code=("", False),
        purpose_text=("purpose_text", False),
        secondars_languge=("ko", False),
        min_num_of_invoices_covering_letter=("", False),
    ) -> bool:

        try:

            if super().prepare():
                return True

            self.term_of_payment = term_of_payment
            self.method_of_payment = method_of_payment
            self.payment_type = payment_type
            self.payment_specification = payment_specification
            self.payment_schedule = payment_schedule
            self.cash_discount = cash_discount
            self.bank_account = bank_account
            self.payment_id = (
                self.get_random(type="int"),
                payment_id[1] if payment_id[0] == "" else payment_id[1],
            )
            self.payment_day = payment_day
            self.bank_account_number = bank_account_number
            self.use_cash_discount = use_cash_discount
            self.central_bank_purpose_code = central_bank_purpose_code
            self.purpose_text = purpose_text
            self.secondars_languge = secondars_languge
            self.min_num_of_invoices_covering_letter = (
                self.get_random(type="int"),
                (
                    min_num_of_invoices_covering_letter[1]
                    if min_num_of_invoices_covering_letter[0] == ""
                    else min_num_of_invoices_covering_letter[1]
                ),
            )
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
    def tab_payment(self) -> bool:

        try:

            self.textbox(
                self.elements.cmb_term_of_payment,
                self.term_of_payment,
                is_press_enter=True,
            )
            self.textbox(self.elements.cmb_method_of_payment, self.method_of_payment, is_press_enter=True,)
            self.textbox(self.elements.txb_payment_type, self.payment_type, is_press_enter=True,)
            self.components.combobox_type_2(
                self.elements.cmb_payment_specification, self.payment_specification
            )
            self.components.combobox_type_2(
                self.elements.cmb_payment_schedule, self.payment_schedule
            )
            self.textbox(
                self.elements.cmb_cash_discount, self.cash_discount, is_press_enter=True
            )
            self.components.combobox_type_2(
                self.elements.cmb_bank_account, self.bank_account
            )
            self.textbox(self.elements.txb_payment_id, self.payment_id)

            self.components.combobox_type_2(
                self.elements.cmb_payment_day, self.payment_day
            )
            self.textbox(
                self.elements.txb_bank_account_number, self.bank_account_number
            )
            self.textbox(self.elements.cmb_use_cash_discount, self.use_cash_discount)
            self.components.combobox_type_2(
                self.elements.cmb_central_bank_purpose_code,
                self.central_bank_purpose_code,
            )
            self.textbox(self.elements.txb_purpose_text, self.purpose_text)
            self.textbox(
                self.elements.cmb_secondars_languge,
                self.secondars_languge,
                is_press_enter=True,
            )
            self.textbox(
                self.elements.txb_min_num_of_invoices_covering_letter,
                self.min_num_of_invoices_covering_letter,
            )

            self.delay(220)

            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False
