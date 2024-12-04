from typing import Any
from test_applications.d_365.core.object_provider import ObjectProvider
from test_applications.d_365.chapters.core.base_chapter import BaseChapter
from test_applications.d_365.abstrct_classes.tab.tab import Tab

# --
# ...
# --

class TabLines(BaseChapter, Tab):
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
                    self.tab_lines()
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
        description=("110 SA Europe B.V.", True),
        main_account=("0861010", True),
        sales_tax_group=("NL-C-IC", False),
        item_sales_tax_group=("S-High", True),
        deferred=("NO", True),
        quantity=("1", True),
        unit_price=("2000", True),
        amount=("", False),
    ) -> bool:

        try:

            if super().prepare():
                return True

            self.description = description
            self.main_account = main_account
            self.sales_tax_group = sales_tax_group
            self.item_sales_tax_group = item_sales_tax_group
            self.deferred = deferred
            self.quantity = quantity
            self.unit_price = unit_price
            self.amount = amount

            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False

    # --
    # ... methods
    # --

    @BaseChapter.log
    def tab_lines(self) -> bool:

        try:

            self.click(self.elements.btn_remove_line)
            self.blocking_message()
            
            self.click(self.elements.btn_add_line)
            self.blocking_message()

            self.delay(500)

            self.textbox(
                self.elements.txb_description,
                self.description,
                is_press_enter=False,
                is_clear=False,
                is_check_key_there=False,
                is_check_readonly=False,
            )
            self.textbox(
                self.elements.cmb_main_account, self.main_account, is_press_enter=True
            )
            self.textbox(
                self.elements.cmb_sales_tax_group,
                self.sales_tax_group,
                is_press_enter=True,
            )
            self.textbox(
                self.elements.cmb_item_sales_tax_group,
                self.item_sales_tax_group,
                is_press_enter=True,
            )
            self.textbox(self.elements.txb_deferred, self.deferred, is_press_enter=True)
            self.textbox(self.elements.txb_quantity, self.quantity, is_press_enter=True)
            self.textbox(
                self.elements.txb_unit_price, self.unit_price, is_press_enter=True
            )
            self.textbox(self.elements.txb_amount, self.amount, is_press_enter=True)

            self.delay(220)

            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False
