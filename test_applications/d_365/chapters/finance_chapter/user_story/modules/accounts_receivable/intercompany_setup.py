from typing import Any
from test_applications.d_365.core.object_provider import ObjectProvider
from test_applications.d_365.chapters.core.base_chapter import BaseChapter
from test_applications.d_365.chapters.core.base_user_story import BaseUserStory
from test_applications.d_365.chapters.finance_chapter.unit_testcases.toolbars.toolbars import (
    Toolbars,
)
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.accounts_receivable.customers.all_customers.all_customers_standard_view import (
    AllCustomersStandardView,
)
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.accounts_receivable.customers.all_customers.all_customers_top_gadget import (
    AllCustomersTopGadget,
)
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.accounts_receivable.customers.all_customers.intercompany.intercompany_manager import (
    IntercompanyManager,
)

# --
# ...
# --


class IntercompanySetup(BaseChapter, BaseUserStory):
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
            self.all_customers_top_gadget = AllCustomersTopGadget()
            self.all_customers_standard_view = AllCustomersStandardView()
            self.intercompany_manager = IntercompanyManager()

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

            self.toolbars.search_for_a_page = ("all customers", True)
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
    def setup_intercompany_rollback(self) -> bool:

        try:

            self.goto_start_point()
            
            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False
        
    # --
    # ... methods
    # --

    @BaseChapter.log
    def setup_intercompany(self) -> bool:

        try:

            self.goto_start_point()

            self.all_customers_standard_view.select_customer_account_number()
            self.delay(220)
            
            self.all_customers_top_gadget.all_customers_general_intercompany()

            self.intercompany_manager(
                step_10="setup_trading_relationship",
                # step_20="setup_account_mapping",
                # step_30="save_intercompany",
                step_40="back_intercompany",
            )

            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False
