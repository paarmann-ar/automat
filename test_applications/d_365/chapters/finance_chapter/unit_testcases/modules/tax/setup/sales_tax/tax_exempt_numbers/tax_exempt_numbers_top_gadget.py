from typing import Any
from test_applications.d_365.core.object_provider import ObjectProvider
from test_applications.d_365.chapters.core.base_chapter import BaseChapter
from test_applications.d_365.abstrct_classes.page.page import Page

# --
# ...
# --


class TaxExemptNumbersTopGadget(BaseChapter, Page):
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

            self.country = country
            self.tax_exempt_number = tax_exempt_number
            self.company_name = self.state["vendor_name"]
            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False

        
    # --
    # ... methods
    # --

    @BaseChapter.wait_for(
        element_for_waiting_until_visible="frm_tax_exempt_numbers",
        type_of_element="text_to_search",
    )
    @BaseChapter.log
    def back(self) -> bool:

        try:

            self.click_button(self.elements.btn_back)

            self.delay(220)

            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False
        
    # --
    # ...
    # --

    @BaseChapter.wait_for(
        element_for_waiting_until_visible="frm_tax_exempt_numbers",
        type_of_element="text_to_search",
    )
    @BaseChapter.log
    def save(self) -> bool:

        try:

            self.click_button(self.elements.btn_save)

            self.delay(220)

            if self.lightbox():
                self.delete()

            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False

    # --
    # ... 
    # --

    @BaseChapter.wait_for(
        element_for_waiting_until_visible="frm_tax_exempt_numbers",
        type_of_element="text_to_search",
    )
    @BaseChapter.log
    def new(self) -> bool:

        try:

            self.click_button(self.elements.btn_new)
            
            self.delay(220)

            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False

    # --
    # ...
    # --

    @BaseChapter.wait_for(
        element_for_waiting_until_visible="frm_tax_exempt_numbers",
        type_of_element="text_to_search",
    )
    @BaseChapter.log
    def delete(self) -> bool:

        try:

            self.click_button(self.elements.btn_delete)

            self.delay(220)

            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False
