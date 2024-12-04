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
        return ObjectProvider()(
            __file__.replace(".py", ".json ", -1).replace("\\", "/").replace(" c", "")
        )

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
        procurement_category=("1300000", True),
        deferred=("NO", True),
        quantity=("1", True),
        unit_price=("400", True),
        line_net_amount=("", True),
        cost_center=("131000", True),
        cost_group=("", True),
    ) -> bool:

        try:

            if super().prepare():
                return True

            self.procurement_category = procurement_category
            self.deferred = deferred
            self.quantity = quantity
            self.unit_price = unit_price
            self.line_net_amount = line_net_amount
            self.cost_center = cost_center
            self.cost_group = cost_group
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

            self.click_button(self.elements.btn_add_line)

            self.delay(220)

            self.textbox(
                self.elements.cmb_procurement_category,
                self.procurement_category,
                is_press_enter=True,
            )

            self.textbox(self.elements.txb_deferred, self.deferred, is_press_enter=True)
            self.textbox(
                self.elements.txb_quantity, self.quantity, is_double_click_befor=True
            )
            self.textbox(self.elements.cmb_unit_price, self.unit_price)
            self.textbox(
                self.elements.txb_line_net_amount,
                self.line_net_amount,
                is_clear=False,
            )
            self.textbox(
                self.elements.cmb_cost_center,
                self.cost_center,
                is_press_tab=True,
            )
            self.textbox(self.elements.cmb_cost_group, self.cost_group, is_clear=False)

            self.delay(220)

            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False
