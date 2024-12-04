from typing import Any
from test_applications.d_365.core.object_provider import ObjectProvider
from test_applications.d_365.chapters.core.base_chapter import BaseChapter
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.tax.setup.sales_tax.tax_exempt_numbers.tax_exempt_numbers_standard_view import (
    TaxExemptNumbersStandardView,
)
from test_applications.d_365.abstrct_classes.tab.tab import Tab

# --
# ...
# --


class TabInvoiceAndDelivery(BaseChapter, Tab):
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
                    self.tab_invoice_and_delivery()

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
            self.tax_exempt_numbers_standard_view = TaxExemptNumbersStandardView()
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
        invoice_account=("", False),
        Number_sequence_group=("", False),
        vendor_price_tolerance_group=("", False),
        vendor_exception_group=("", False),
        offset_account_account_type=("", False),
        offset_account=("", False),
        UPS_zone=("", False),
        delivery_terms=("", False),
        mode_of_delivery=("", False),
        destination_code=("", False),
        sales_tax_group=("IT-V-DOM", True),
        is_prices_include_sales_tax=(True, False),
        tax_exempt_number=("00272430635", True),
        fiscal_code=("", False),
        is_calculate_withholding_tax=(True, False),
        withholding_tax_group=("", False),
        evenue_typology=("", False),
        is_e_invoice=(True, False),
    ) -> bool:

        try:

            if super().prepare():
                return True

            self.invoice_account = invoice_account
            self.Number_sequence_group = Number_sequence_group
            self.vendor_price_tolerance_group = vendor_price_tolerance_group
            self.vendor_exception_group = vendor_exception_group
            self.offset_account_account_type = offset_account_account_type
            self.offset_account = offset_account
            self.UPS_zone = self.get_random(type="int"), (
                UPS_zone[1] if UPS_zone[0] == "" else UPS_zone[1]
            )
            self.delivery_terms = delivery_terms
            self.mode_of_delivery = mode_of_delivery
            self.destination_code = destination_code
            self.sales_tax_group = sales_tax_group
            self.is_prices_include_sales_tax = is_prices_include_sales_tax
            self.tax_exempt_number = tax_exempt_number
            self.fiscal_code = (
                self.get_random(type="int"),
                fiscal_code[1] if fiscal_code[0] == "" else fiscal_code[1],
            )
            self.is_calculate_withholding_tax = is_calculate_withholding_tax
            self.withholding_tax_group = withholding_tax_group
            self.evenue_typology = evenue_typology
            self.is_e_invoice = is_e_invoice
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
    def tab_invoice_and_delivery(self) -> bool:

        try:

            self.textbox(self.elements.cmb_invoice_account, self.invoice_account)
            self.textbox(
                self.elements.cmb_Number_sequence_group, self.Number_sequence_group
            )
            self.textbox(
                self.elements.txb_vendor_price_tolerance_group,
                self.vendor_price_tolerance_group,
            )
            self.components.combobox_type_2(
                self.elements.cmb_vendor_exception_group, self.vendor_exception_group
            )
            self.textbox(
                self.elements.txb_offset_account_account_type,
                self.offset_account_account_type,
            )
            self.textbox(self.elements.txb_offset_account, self.offset_account)
            self.textbox(self.elements.txb_UPS_zone, self.UPS_zone)
            self.components.combobox_type_2(
                self.elements.cmb_delivery_terms, self.delivery_terms
            )
            self.components.combobox_type_2(
                self.elements.cmb_mode_of_delivery, self.mode_of_delivery
            )
            self.components.combobox_type_2(
                self.elements.cmb_destination_code, self.destination_code
            )
            self.textbox(
                self.elements.cmb_sales_tax_group,
                self.sales_tax_group,
                is_press_enter=True,
            )
            self.checkbox(
                self.elements.chk_prices_include_sales_tax,
                self.is_prices_include_sales_tax,
            )
            self.textbox(
                self.elements.cmb_tax_exempt_number,
                self.tax_exempt_number,
                is_press_enter=True,
            )

            # self.context_menu(self.elements.lbl_tax_exempt_number).click_context()
            # self.tax_exempt_numbers_standard_view.add_new_tax_exempt_number()

            self.textbox(self.elements.txb_fiscal_code, self.fiscal_code)
            self.checkbox(
                self.elements.chk_calculate_withholding_tax,
                self.is_calculate_withholding_tax,
            )
            self.components.combobox_type_2(
                self.elements.cmb_withholding_tax_group, self.withholding_tax_group
            )
            self.components.combobox_type_2(
                self.elements.cmb_evenue_typology, self.evenue_typology
            )
            self.checkbox(self.elements.chk_e_invoice, self.is_e_invoice)

            self.delay(220)

            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False
