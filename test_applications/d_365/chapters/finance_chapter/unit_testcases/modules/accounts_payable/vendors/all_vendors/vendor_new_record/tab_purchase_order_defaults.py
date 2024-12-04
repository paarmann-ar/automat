from typing import Any
from test_applications.d_365.core.object_provider import ObjectProvider
from test_applications.d_365.chapters.core.base_chapter import BaseChapter
from test_applications.d_365.abstrct_classes.tab.tab import Tab

# --
# ...
# --


class TabPurchaseOrderDefaults(BaseChapter, Tab):
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
                    self.tab_purchase_order_defaults()

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
        charges_group=("", True),
        site=("", True),
        warehause=("", True),
        default_inventory_status_ID=("", True),
        item_vendor_group=("", True),
        purchasing_pool=("", True),
        our_account_number=("", True),
        amount_in_transaction_currency=("", True),
        is_purchase_order_prices_amount=(True, True),
        purchase_calendar=("WFC", True),
        is_send_purchase_order_via_cXML=(True, True),
        multiline_discount=("", True),
        total_discount_group=("", True),
        price_group=("", True),
        line_discount_group=("", True),
        supplementary_item_group=("", True),
        is_override_settings=(True, True),
        is_activate_change_management=(True, True),
        is_allow_override_of_settings_per_purchase=(True, True),
        advanced_notes_group=("", True),
    ) -> bool:

        try:

            if super().prepare():
                return True

            self.charges_group = charges_group
            self.site = site
            self.warehause = warehause
            self.default_inventory_status_ID = default_inventory_status_ID
            self.item_vendor_group = item_vendor_group
            self.purchasing_pool = purchasing_pool
            self.our_account_number = (
                self.get_tandom(type="int")
                if our_account_number == ""
                else our_account_number
            )
            self.amount_in_transaction_currency = (
                self.get_tandom(type="int")
                if amount_in_transaction_currency == ""
                else amount_in_transaction_currency
            )
            self.is_purchase_order_prices_amount = is_purchase_order_prices_amount
            self.purchase_calendar = purchase_calendar
            self.is_send_purchase_order_via_cXML = is_send_purchase_order_via_cXML
            self.multiline_discount = multiline_discount
            self.total_discount_group = total_discount_group
            self.price_group = price_group
            self.line_discount_group = line_discount_group
            self.supplementary_item_group = supplementary_item_group
            self.is_override_settings = is_override_settings
            self.is_activate_change_management = is_activate_change_management
            self.is_allow_override_of_settings_per_purchase = (
                is_allow_override_of_settings_per_purchase
            )
            self.advanced_notes_group = advanced_notes_group
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
    def tab_purchase_order_defaults(self) -> bool:

        try:

            self.components.combobox_type_2(
                self.elements.cmb_charges_group, self.charges_group
            )
            self.components.combobox_type_2(self.elements.cmb_site, self.site)
            self.components.combobox_type_2(self.elements.cmb_warehause, self.warehause)
            self.components.combobox_type_2(
                self.elements.cmb_default_inventory_status_ID,
                self.default_inventory_status_ID,
            )
            self.components.combobox_type_2(
                self.elements.cmb_item_vendor_group, self.item_vendor_group
            )
            self.components.combobox_type_2(
                self.elements.cmb_purchasing_pool, self.purchasing_pool
            )
            self.textbox(self.elements.txb_our_account_number, self.our_account_number)
            self.textbox(
                self.elements.txb_amount_in_transaction_currency,
                self.amount_in_transaction_currency,
            )
            self.checkbox(
                self.elements.chk_purchase_order_prices_amount,
                self.is_purchase_order_prices_amount,
            )
            self.textbox(
                self.elements.cmb_purchase_calendar,
                self.purchase_calendar,
                is_press_enter=True,
            )
            self.checkbox(
                self.elements.chk_send_purchase_order_via_cXML,
                self.is_send_purchase_order_via_cXML,
            )
            self.components.combobox_type_2(
                self.elements.cmb_multiline_discount, self.multiline_discount
            )
            self.components.combobox_type_2(
                self.elements.cmb_total_discount_group, self.total_discount_group
            )
            self.components.combobox_type_2(
                self.elements.cmb_price_group, self.price_group
            )
            self.components.combobox_type_2(
                self.elements.cmb_line_discount_group, self.line_discount_group
            )
            self.components.combobox_type_2(
                self.elements.cmb_supplementary_item_group,
                self.supplementary_item_group,
            )
            self.checkbox(
                self.elements.chk_override_settings, self.is_override_settings
            )
            self.checkbox(
                self.elements.chk_activate_change_management,
                self.is_activate_change_management,
            )
            self.checkbox(
                self.elements.chk_allow_override_of_settings_per_purchase,
                self.is_allow_override_of_settings_per_purchase,
            )
            self.components.combobox_type_2(
                self.elements.cmb_advanced_notes_group, self.advanced_notes_group
            )

            self.delay(220)

            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False
