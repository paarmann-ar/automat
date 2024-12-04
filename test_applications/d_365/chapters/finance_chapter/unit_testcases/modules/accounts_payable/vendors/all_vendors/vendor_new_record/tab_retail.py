from typing import Any
from test_applications.d_365.core.object_provider import ObjectProvider
from test_applications.d_365.chapters.core.base_chapter import BaseChapter
from test_applications.d_365.abstrct_classes.tab.tab import Tab

# --
# ...
# --


class TabRetail(BaseChapter, Tab):
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
                    self.tab_retail()
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
        sales_price_rounding=("Rounding", True),
        is_Fixed_rate=(True, True),
        fixed_exchange_rate=("", True),
        vendor_type=("3rd party", True),
        hierarchy=("", True),
        is_create_bar_code_if_needed=(True, True),
        bar_code_number_sequence=("100_BANKAU", True),
        service_category=("", True),
        style_prefix=("", True),
        size_prefix=("", True),
        color_prefix=("", True),
    ) -> bool:

        try:

            if super().prepare():
                return True

            self.sales_price_rounding = sales_price_rounding
            self.is_Fixed_rate = is_Fixed_rate
            self.fixed_exchange_rate = (
                self.get_random(type="int"),
                (
                    fixed_exchange_rate[1]
                    if fixed_exchange_rate[0] == ""
                    else fixed_exchange_rate[1]
                ),
            )
            self.vendor_type = vendor_type
            self.hierarchy = hierarchy
            self.is_create_bar_code_if_needed = is_create_bar_code_if_needed
            self.bar_code_number_sequence = (
                self.get_random(type="int"),
                (
                    bar_code_number_sequence[1]
                    if bar_code_number_sequence[0] == ""
                    else bar_code_number_sequence[1]
                ),
            )
            self.service_category = service_category

            self.style_prefix = (
                self.get_random(type="int"),
                style_prefix[1] if style_prefix[0] == "" else style_prefix[1],
            )
            self.size_prefix = (
                self.get_random(type="int"),
                size_prefix[1] if size_prefix[0] == "" else size_prefix[1],
            )
            self.color_prefix = (
                self.get_random(type="int"),
                color_prefix[1] if color_prefix[0] == "" else color_prefix[1],
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
    def tab_retail(self) -> bool:

        try:

            self.textbox(
                self.elements.cmb_sales_price_rounding, self.sales_price_rounding
            )
            self.checkbox(self.elements.chk_Fixed_rate, self.is_Fixed_rate)
            self.textbox(
                self.elements.txb_fixed_exchange_rate, self.fixed_exchange_rate
            )
            self.textbox(self.elements.cmb_vendor_type, self.vendor_type)
            self.textbox(self.elements.cmb_hierarchy, self.hierarchy)
            self.checkbox(
                self.elements.chk_create_bar_code_if_needed,
                self.is_create_bar_code_if_needed,
            )
            # check
            self.textbox(
                self.elements.cmb_bar_code_number_sequence,
                self.bar_code_number_sequence,
            )
            self.textbox(self.elements.cmb_service_category, self.service_category)
            self.textbox(self.elements.txb_style_prefix, self.style_prefix)
            self.textbox(self.elements.txb_size_prefix, self.size_prefix)
            self.textbox(self.elements.txb_color_prefix, self.color_prefix)

            self.delay(220)

            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False
