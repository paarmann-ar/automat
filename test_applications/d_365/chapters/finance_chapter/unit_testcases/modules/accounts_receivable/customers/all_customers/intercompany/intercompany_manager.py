from test_applications.d_365.core.object_provider import ObjectProvider
from test_applications.d_365.chapters.core.base_chapter import BaseChapter
from typing import Any
from test_applications.d_365.abstrct_classes.page.page import Page
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.accounts_receivable.customers.all_customers.intercompany.page_trading_relationship import PageTradingRelationship
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.accounts_receivable.customers.all_customers.intercompany.page_account_mapping import PageAccountMapping
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.accounts_receivable.customers.all_customers.intercompany.intercompany_top_gadget import IntercompanyTopGadget

# --
# ...
# --


class IntercompanyManager(BaseChapter, Page):
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
                case"":
                    self.setup_intercompany(**kwargs)
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

            self.page_trading_relationship = PageTradingRelationship()
            self.page_account_mapping = PageAccountMapping()
            self.intercompany_top_gadget = IntercompanyTopGadget()
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
    # ... methods
    # --

    @BaseChapter.wait_for(
        element_for_waiting_until_visible="frm_intercompany",
        type_of_element="text_to_search",
    )
    @BaseChapter.log
    def setup_intercompany(self, **kwargs) -> bool:

        try:

            for _, tab in kwargs.items():
                match tab:
                    case "setup_trading_relationship":
                        self.page_trading_relationship()

                    case "setup_account_mapping":
                        self.page_account_mapping()

                    case "save_intercompany":
                        self.intercompany_top_gadget.save()

                    case "back_intercompany":
                        self.intercompany_top_gadget.back()
                    case _:
                        pass

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False
