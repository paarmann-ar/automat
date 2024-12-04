from typing import Any
from test_applications.d_365.core.object_provider import ObjectProvider
from test_applications.d_365.chapters.core.base_chapter import BaseChapter
from test_applications.d_365.abstrct_classes.tab.tab import Tab

# --
# ...
# --


class TabDetailLines(BaseChapter, Tab):
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
                    self.tab_detail_lines()
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
        item_number=("", False),
        item_name=("", False),
        procurement_category=("", False),
        text=("Desciption field is mandatory for Vendor Invoice Lines for Italy legal entities", True),
        quantity=("", False),
        unit=("", False),
        unit_price=("", False),
        adjusted_unit_price=("", False),
        price_unit=("", False),
        line_net_amount=("", False),
        purchase_order=("", False),
        is_close_for_receipt=(True, False),
        item_sales_tax_group=("exemptN4", True),
    ) -> bool:

        try:

            if super().prepare():
                return True

            self.item_number = item_number
            self.item_name = item_name
            self.procurement_category = procurement_category
            self.text = text
            self.quantity = quantity
            self.unit = unit
            self.unit_price = unit_price
            self.adjusted_unit_price = adjusted_unit_price
            self.price_unit = price_unit
            self.line_net_amount = line_net_amount
            self.purchase_order = purchase_order
            self.is_close_for_receipt = is_close_for_receipt

            self.item_sales_tax_group = item_sales_tax_group

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
    def tab_detail_lines(self) -> bool:

        try:

            self.textbox(self.elements.cmb_item_number, self.item_number)
            self.textbox(self.elements.txb_item_name, self.item_name)
            self.textbox(
                self.elements.cmb_procurement_category, self.procurement_category
            )
            self.textbox(self.elements.txb_text, self.text)
            self.textbox(self.elements.txb_quantity, self.quantity)
            self.textbox(self.elements.cmb_unit, self.unit)
            self.textbox(self.elements.txb_unit_price, self.unit_price)
            self.textbox(
                self.elements.txb_adjusted_unit_price, self.adjusted_unit_price
            )
            self.textbox(self.elements.txb_price_unit, self.price_unit)
            self.textbox(self.elements.txb_line_net_amount, self.line_net_amount)
            self.textbox(self.elements.cmb_purchase_order, self.purchase_order)
            self.checkbox(
                self.elements.chk_close_for_receipt, self.is_close_for_receipt
            )

            self.click_button(self.elements.btn_setup)

            self.delay(220)

            self.textbox(
                self.elements.cmb_item_sales_tax_group,
                self.item_sales_tax_group,
                is_press_enter=True,
            )

            self.delay(220)

            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False
