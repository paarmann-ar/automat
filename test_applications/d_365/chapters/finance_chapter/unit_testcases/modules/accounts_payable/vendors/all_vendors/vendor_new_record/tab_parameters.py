from typing import Any
from test_applications.d_365.core.object_provider import ObjectProvider
from test_applications.d_365.chapters.core.base_chapter import BaseChapter
from test_applications.d_365.abstrct_classes.tab.tab import Tab

# --
# ...
# --


class TabParameters(BaseChapter, Tab):
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
                    self.tab_parameters()

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
        vendor_interface_group=("DeActVend", True),
        secondary_language=("de-DE", True),
        min_num_of_invoice_covering_letter=("", True),
        datev_vendor_number=("", True),
        tax_authority_interface_id=("", True),
        is_deactivated=(True, True),
        lead_time=("", True),
        delivery_time_external=("", True),
        external_processing_time=("", True),
        transit_time=("", True),
        processing_time_internal=("", True),
        is_senden_an_rechnungskonto=(True, True),
        is_bestellpositionen_ubertragen=(True, True),
        note=("note", True),
        vendor_type=("Hospital", True),
        invoice_type=("", True),
        external_vendor=("external_vendor", True),
        customer_account=("customer_account", True),
    ) -> bool:

        try:

            if super().prepare():
                return True

            self.vendor_interface_group = vendor_interface_group
            self.secondary_language = secondary_language
            self.min_num_of_invoice_covering_letter = (
                self.get_random(type="int"),
                (
                    min_num_of_invoice_covering_letter[1]
                    if min_num_of_invoice_covering_letter[0] == ""
                    else min_num_of_invoice_covering_letter[1]
                ),
            )
            self.datev_vendor_number = (
                self.get_random(type="int"),
                (
                    datev_vendor_number[1]
                    if datev_vendor_number[0] == ""
                    else datev_vendor_number[1]
                ),
            )
            self.tax_authority_interface_id = (
                self.get_random(type="int"),
                (
                    tax_authority_interface_id[1]
                    if tax_authority_interface_id[0] == ""
                    else tax_authority_interface_id[1]
                ),
            )
            self.is_deactivated = is_deactivated, lead_time[1]
            self.lead_time = (
                self.get_random(type="int") if lead_time[0] == "" else lead_time[1]
            )
            self.delivery_time_external = (
                self.get_random(type="int"),
                (
                    delivery_time_external[1]
                    if delivery_time_external[0] == ""
                    else delivery_time_external[1]
                ),
            )
            self.external_processing_time = (
                self.get_random(type="int"),
                (
                    external_processing_time[1]
                    if external_processing_time[0] == ""
                    else external_processing_time[1]
                ),
            )
            self.transit_time = (
                self.get_random(type="int"),
                transit_time[1] if transit_time[0] == "" else transit_time[1],
            )
            self.processing_time_internal = (
                self.get_random(type="int"),
                (
                    processing_time_internal[1]
                    if processing_time_internal[0] == ""
                    else processing_time_internal[1]
                ),
            )
            self.is_senden_an_rechnungskonto = is_senden_an_rechnungskonto
            self.is_bestellpositionen_ubertragen = is_bestellpositionen_ubertragen
            self.note = note
            self.vendor_type = vendor_type
            self.invoice_type = invoice_type
            self.external_vendor = external_vendor
            self.customer_account = customer_account
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
    def tab_parameters(self) -> bool:

        try:

            self.textbox(
                self.elements.cmb_vendor_interface_group,
                self.vendor_interface_group,
                is_press_enter=True,
            )
            self.textbox(
                self.elements.cmb_secondary_language,
                self.secondary_language,
                is_press_enter=True,
            )

            self.textbox(
                self.elements.txb_min_num_of_invoice_covering_letter,
                self.min_num_of_invoice_covering_letter,
                is_press_enter=True,
            )

            self.textbox(
                self.elements.txb_datev_vendor_number, self.datev_vendor_number
            )

            self.textbox(
                self.elements.txb_tax_authority_interface_id,
                self.tax_authority_interface_id,
            )

            self.checkbox(self.elements.chk_deactivated, self.is_deactivated)
            self.textbox(self.elements.txb_lead_time, self.lead_time)
            self.textbox(
                self.elements.txb_delivery_time_external, self.delivery_time_external
            )

            self.textbox(
                self.elements.txb_external_processing_time,
                self.external_processing_time,
            )

            self.textbox(self.elements.txb_transit_time, self.transit_time)
            self.textbox(
                self.elements.txb_processing_time_internal,
                self.processing_time_internal,
            )

            self.checkbox(
                self.elements.chk_senden_an_rechnungskonto,
                self.is_senden_an_rechnungskonto,
            )

            self.checkbox(
                self.elements.chk_bestellpositionen_ubertragen,
                self.is_bestellpositionen_ubertragen,
            )

            self.textbox(self.elements.txb_note, self.note)
            self.textbox(self.elements.cmb_vendor_type, self.vendor_type)
            self.textbox(self.elements.txb_invoice_type, self.invoice_type)
            self.textbox(self.elements.txb_external_vendor, self.external_vendor)
            self.textbox(self.elements.txb_customer_account, self.customer_account)

            self.delay(220)

            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False
