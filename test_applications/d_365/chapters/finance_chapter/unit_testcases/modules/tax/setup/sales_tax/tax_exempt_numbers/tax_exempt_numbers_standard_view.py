from typing import Any
from test_applications.d_365.core.object_provider import ObjectProvider
from test_applications.d_365.chapters.core.base_chapter import BaseChapter
from test_applications.d_365.abstrct_classes.standard_view.standard_view import StandardView

# --
# ...
# --


class TaxExemptNumbersStandardView(BaseChapter, StandardView):
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
    # ... setup and teardown and prepare
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
        country=("ITA", True),
        tax_exempt_number=("00272430635", True),
        company_name=("vendor test112", True),
    ) -> bool:

        try:

            if super().prepare():
                return True
            
            self.search_item_text = "Tax exempt number"
            self.search_item = tax_exempt_number

            self.country = country
            self.tax_exempt_number = tax_exempt_number
            self.company_name = company_name

            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False

    # --
    # ... methods
    # --

    @BaseChapter.wait_for(
        element_for_waiting_until_visible="frm_invoice_journal",
        type_of_element="text_to_search",
    )
    @BaseChapter.log
    def select_tax_exempt_number(self, **kwargs) -> bool:

        try:

            return self.select_item(**kwargs)

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False
        
    # --
    # ... methods ausnahme das function is da
    # --

    @BaseChapter.wait_for(
        element_for_waiting_until_visible="frm_tax_exempt_numbers",
        type_of_element="text_to_search",
    )
    @BaseChapter.log
    def add_new_tax_exempt_number(self) -> bool:

        try:

            self.textbox(self.elements.cmb_lv_country, self.country, is_press_tab=True)
            self.textbox(
                self.elements.txb_lv_tax_exempt_number,
                self.tax_exempt_number,
                is_press_tab=True,
            )
            self.textbox(
                self.elements.txb_lv_company_name, self.company_name, is_press_tab=True
            )

            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False