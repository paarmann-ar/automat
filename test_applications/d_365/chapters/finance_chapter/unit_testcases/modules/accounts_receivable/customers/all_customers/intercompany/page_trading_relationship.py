from typing import Any
from test_applications.d_365.core.object_provider import ObjectProvider
from test_applications.d_365.chapters.core.base_chapter import BaseChapter
from test_applications.d_365.abstrct_classes.page.page import Page


# --
# ...
# --


class PageTradingRelationship(BaseChapter, Page):
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
                    self.setup_trading_relationship()

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
        is_active=(True, False),
        my_company=("100", False),
        customer_account=("DIC11000", False),
        vendor_company=("110", False),
        my_account=("KIC10000", False),
    ) -> bool:

        try:

            if super().prepare():
                return True

            self.is_active = is_active
            self.my_company = my_company
            self.customer_account = customer_account
            self.vendor_company = vendor_company
            self.my_account = my_account

            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False

    # --
    # ... methods
    # --
    @Page.click_sidebar
    @BaseChapter.wait_for(
        element_for_waiting_until_visible="frm_setup_trading_relationship",
        type_of_element="text_to_search",
    )
    @BaseChapter.log
    def setup_trading_relationship(self) -> bool:

        try:

            self.checkbox(self.elements.chk_active, self.is_active)
            self.textbox(
                self.elements.txb_my_company, self.my_company, is_press_enter=True
            )
            self.textbox(
                self.elements.txb_customer_account,
                self.customer_account,
                is_press_enter=True,
            )
            self.textbox(
                self.elements.txb_vendor_company,
                self.vendor_company,
                is_press_enter=True,
            )
            self.textbox(
                self.elements.txb_my_account, self.my_account, is_press_enter=True
            )

            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False
