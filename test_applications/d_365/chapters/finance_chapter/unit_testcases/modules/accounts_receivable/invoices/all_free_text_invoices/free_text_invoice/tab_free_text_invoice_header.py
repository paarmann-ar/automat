from typing import Any
from test_applications.d_365.core.object_provider import ObjectProvider
from test_applications.d_365.chapters.core.base_chapter import BaseChapter
from test_applications.d_365.abstrct_classes.tab.tab import Tab

# --
# ...
# --


class TabFreeTextInvoiceHeader(BaseChapter, Tab):
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
                    self.tab_free_text_invoice_header()
                    return True

                case _:
                    raise Exception(
                        f"class {__class__.__name__} have no method {action}."
                    )

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
        customer_account=("DIC11000", True),
        name=("110 SA Europe B.V.", True),
        invoice_account=("", True),
        is_one_time_customer=(True, False),
        address=("Erik de rodeweg 11-13 5975WD Sevenum Nederland", True),
        invoice_date=("1/20/2024", True),
        invoice_Due=("1/20/2024", True),
        currency=("EUR", True),
        terms_of_payment=("", False),
        method_of_payment=("", False),
        payment_specification=("", False),
        bank_account=("", False),
        payment_schedule=("", False),
        cash_discount=("", False),
    ) -> bool:

        try:

            if super().prepare():
                return True

            self.customer_account = customer_account
            self.name = name
            self.invoice_account = invoice_account
            self.is_one_time_customer = is_one_time_customer
            self.address = address
            self.invoice_date = invoice_date
            self.invoice_Due = invoice_Due
            self.currency = currency
            self.terms_of_payment = terms_of_payment
            self.method_of_payment = method_of_payment
            self.payment_specification = payment_specification
            self.bank_account = bank_account
            self.payment_schedule = payment_schedule
            self.cash_discount = cash_discount

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
    def tab_free_text_invoice_header(self) -> bool:

        try:

            self.textbox(self.elements.cmb_customer_account, self.customer_account)
            self.textbox(self.elements.txb_name, self.name)
            self.textbox(self.elements.cmb_invoice_account, self.invoice_account)
            self.checkbox(
                self.elements.chk_one_time_customer, self.is_one_time_customer
            )
            self.textbox(self.elements.txb_address, self.address)
            self.textbox(self.elements.txb_invoice_date, self.invoice_date)
            self.textbox(self.elements.txb_invoice_Due, self.invoice_Due)
            self.textbox(self.elements.cmb_currency, self.currency)
            self.textbox(self.elements.cmb_terms_of_payment, self.terms_of_payment)
            self.textbox(self.elements.cmb_method_of_payment, self.method_of_payment)
            self.textbox(
                self.elements.cmb_payment_specification, self.payment_specification
            )
            self.textbox(self.elements.cmb_bank_account, self.bank_account)
            self.textbox(self.elements.cmb_payment_schedule, self.payment_schedule)
            self.textbox(self.elements.cmb_cash_discount, self.cash_discount)

            self.delay(220)

            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False
