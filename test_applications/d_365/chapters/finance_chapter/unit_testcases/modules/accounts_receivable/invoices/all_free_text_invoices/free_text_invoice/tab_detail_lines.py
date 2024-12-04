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
        invoice_text=("invoice_text", False),
        fixed_asset_number=("", True),
        book=("", True),
        customer_reference=("", True),

        intercompany_main_account=("0144101", True),
        intercompany_sales_tax_group=("NL-V-IC", True),
        intercompany_item_sales_tax_group=("S-High", True),
        intercompany_invoice_text=("vendor invoice text", True),
    ) -> bool:

        try:

            if super().prepare():
                return True

            self.invoice_text = invoice_text
            self.fixed_asset_number = fixed_asset_number
            self.book = book
            self.customer_reference = customer_reference

            self.intercompany_main_account = intercompany_main_account
            self.intercompany_sales_tax_group = intercompany_sales_tax_group
            self.intercompany_item_sales_tax_group = intercompany_item_sales_tax_group
            self.intercompany_invoice_text = intercompany_invoice_text

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

            self.click_button(self.elements.btn_intercompany)
            self.delay(220)

            self.textbox(
                self.elements.cmb_intercompany_main_account,
                self.intercompany_main_account,
                is_press_enter=True,
            )
            self.textbox(
                self.elements.cmb_intercompany_sales_tax_group,
                self.intercompany_sales_tax_group,
                is_press_enter=True,
            )
            self.textbox(
                self.elements.cmb_intercompany_item_sales_tax_group,
                self.intercompany_item_sales_tax_group,
                is_press_enter=True,
            )
            self.textbox(
                self.elements.txb_intercompany_invoice_text,
                self.intercompany_invoice_text,
                is_press_enter=True,
            )

            self.click_button(self.elements.btn_general)
            self.delay(220)

            self.textbox(
                self.elements.txb_invoice_text, self.invoice_text, is_press_enter=True
            )
            self.textbox(
                self.elements.txb_fixed_asset_number,
                self.fixed_asset_number,
                is_press_enter=True,
            )
            self.textbox(self.elements.cmb_book, self.book, is_press_enter=True)
            self.textbox(
                self.elements.txb_customer_reference,
                self.customer_reference,
                is_press_enter=True,
            )

            self.delay(220)

            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False
