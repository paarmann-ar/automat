from typing import Any
from test_applications.d_365.core.object_provider import ObjectProvider
from test_applications.d_365.chapters.core.base_chapter import BaseChapter
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.tax.setup.sales_tax.tax_exempt_numbers.tax_exempt_numbers_standard_view import (
    TaxExemptNumbersStandardView,
)
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.tax.setup.sales_tax.tax_exempt_numbers.tax_exempt_numbers_top_gadget import (
    TaxExemptNumbersTopGadget,
)
from test_applications.d_365.chapters.finance_chapter.unit_testcases.toolbars.toolbars import (
    Toolbars,
)

# --
# ...
# --


class TaxExemptNumberManager(BaseChapter):
    def __init__(self, *args, **kwargs) -> None:
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
                    self.goto_start_point()
                    self.tax_exempt_number_manager(**kwargs)

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

            self.toolbars = Toolbars()
            self.tax_exempt_numbers_top_gadget = TaxExemptNumbersTopGadget()
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

    def __prepare(self) -> bool:

        try:

            if super().prepare():
                return True

            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False

    # --
    # ... go to start point
    # --

    @BaseChapter.log
    def goto_start_point(self) -> bool:

        try:

            self.toolbars.search_for_a_page = ("Tax exempt numbers", True)
            self.toolbars.set_text_in_search_for_a_page()

            self.delay(220)

            self.tipbox()

            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False

    # --
    # ... rollback
    # --
    
    @BaseChapter.log
    def tax_exempt_number_rollback(self) -> bool:

        try:

            self.goto_start_point()
            
            self.tax_exempt_numbers_standard_view()

            self.tax_exempt_numbers_top_gadget.delete()

            self.delay(220)

            self.tax_exempt_numbers_top_gadget.back()

            self.delay(220)

            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False
        
    # --
    # ... methode
    # --

    @BaseChapter.handel_tipbox
    @BaseChapter.wait_for(
        element_for_waiting_until_visible="frm_tax_exempt_numbers",
        type_of_element="text_to_search",
    )
    @BaseChapter.log
    def tax_exempt_number_manager(self, **kwargs) -> bool:

        try:

            self.goto_start_point()

            for _, tab in kwargs.items():
                match tab:
                    case "new":
                        self.tax_exempt_numbers_top_gadget.new()

                    case "add_new_tax_exempt_number":
                        self.tax_exempt_numbers_standard_view.company_name = self.state["vendor_name"]
                        self.tax_exempt_numbers_standard_view.add_new_tax_exempt_number()

                    case "save":
                        self.tax_exempt_numbers_top_gadget.save()
                
                    case "back":
                        self.tax_exempt_numbers_top_gadget.back()

            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False