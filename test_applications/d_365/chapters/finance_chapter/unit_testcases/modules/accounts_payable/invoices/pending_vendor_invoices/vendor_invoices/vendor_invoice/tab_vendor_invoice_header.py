from typing import Any
from test_applications.d_365.core.object_provider import ObjectProvider
from test_applications.d_365.chapters.core.base_chapter import BaseChapter
from test_applications.d_365.abstrct_classes.tab.tab import Tab
from selenium.webdriver.common.keys import Keys

# --
# ...
# --


class TabVendorInvoiceHeader(BaseChapter, Tab):
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
                    self.tab_vendor_invoice_header()
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
        company=("139", True),
        invoice_account=("V139100004", True),
        purches_number=("LEGNAZZI & PARTNERS STPRL", True),
        number=("", True),
        invoice_description=("Text1", True),
        purchase_order=("", False),
        purchase_receipt=("", False),
        purchase_agreement=("", False),
        invoice_received_date=("04.07.2024", True),
        invoice_date=("", False),
        date_of_vendor_VAT_register=("", False),
        posting_date=("04.07.2024", True),
        due_date=("04.07.2024", True),
        is_on_hold=(False, False),
        is_credit_correction=(False, False),
        is_recharge=(False, False),
        archiva_protokol=("45698745", True),
        is_confidential=(False, False),
        header_budget_check_results=("Budget check not performed", True),
        plafond_date=("", False),
        is_imported=(False, False),
        imported_gross_amount=("", False),
        imported_net_amount=("", False),
        imported_tax_amount=("", False),
        invoice_amount=(Keys.HOME+"40", True),
        rest=("", False),
    ) -> bool:

        try:

            if super().prepare():
                return True

            self.company = company
            self.invoice_account = invoice_account
            self.purches_number = purches_number
            self.number = number

            self.number = (
                self.get_random(type="int"),
                (number[1] if number[0] == "" else number[1]),
            )

            self.invoice_description = invoice_description
            self.purchase_order = purchase_order
            self.purchase_receipt = purchase_receipt
            self.purchase_agreement = purchase_agreement
            self.invoice_received_date = invoice_received_date
            self.invoice_date = invoice_date
            self.date_of_vendor_VAT_register = date_of_vendor_VAT_register
            self.posting_date = posting_date
            self.due_date = due_date
            self.is_on_hold = is_on_hold
            self.is_credit_correction = is_credit_correction
            self.is_recharge = is_recharge
            self.archiva_protokol = archiva_protokol
            self.is_confidential = is_confidential
            self.header_budget_check_results = header_budget_check_results
            self.plafond_date = plafond_date
            self.is_imported = is_imported
            self.imported_gross_amount = imported_gross_amount
            self.imported_net_amount = imported_net_amount
            self.imported_tax_amount = imported_tax_amount
            self.invoice_amount = invoice_amount
            self.rest = rest

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
    def tab_vendor_invoice_header(self) -> bool:

        try:

            self.textbox(self.elements.cmb_company, self.company)
            self.textbox(
                self.elements.cmb_invoice_account,
                self.invoice_account,
                is_press_enter=True,
            )

            self.delay(220)

            self.textbox(self.elements.txb_purchese_number, self.purches_number)
            self.textbox(self.elements.txb_number, self.number)
            self.textbox(
                self.elements.txb_invoice_description, self.invoice_description
            )
            self.textbox(self.elements.txb_purchase_order, self.purchase_order)
            self.textbox(self.elements.txb_purchase_receipt, self.purchase_receipt)
            self.textbox(self.elements.cmb_purchase_agreement, self.purchase_agreement)
            self.textbox(
                self.elements.txb_invoice_received_date, self.invoice_received_date
            )
            self.textbox(self.elements.txb_invoice_date, self.invoice_date)
            self.textbox(
                self.elements.txb_date_of_vendor_VAT_register,
                self.date_of_vendor_VAT_register,
            )
            self.textbox(self.elements.txb_posting_date, self.posting_date)
            self.textbox(self.elements.txb_due_date, self.due_date)
            self.checkbox(self.elements.chk_on_hold, self.is_on_hold)
            self.checkbox(
                self.elements.chk_credit_correction, self.is_credit_correction
            )
            self.checkbox(self.elements.chk_recharge, self.is_recharge)
            self.textbox(self.elements.txb_archiva_protokol, self.archiva_protokol)
            self.checkbox(self.elements.chk_confidential, self.is_confidential)
            self.textbox(
                self.elements.txb_header_budget_check_results,
                self.header_budget_check_results,
            )
            self.textbox(self.elements.txb_plafond_date, self.plafond_date)
            self.checkbox(self.elements.chk_imported, self.is_imported)
            self.textbox(
                self.elements.txb_imported_gross_amount, self.imported_gross_amount
            )
            self.textbox(
                self.elements.txb_imported_net_amount, self.imported_net_amount
            )
            self.textbox(
                self.elements.txb_imported_tax_amount, self.imported_tax_amount
            )

            self.keys(self.elements.txb_invoice_amount, self.invoice_amount)
            self.textbox(self.elements.txb_rest, self.rest)

            self.state["vendor_invoice_nummer"] = self.read_textbox(self.elements.txb_number)

            self.delay(220)

            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False
