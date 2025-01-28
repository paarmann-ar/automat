from typing import Any
from test_applications.d_365.core.object_provider import ObjectProvider
from test_applications.d_365.chapters.core.base_chapter import BaseChapter
from test_applications.d_365.chapters.core.base_user_story import BaseUserStory
from test_applications.d_365.chapters.finance_chapter.unit_testcases.toolbars.toolbars import (
    Toolbars,
)
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.accounts_receivable.inquiries_and_reports.mq.customer_erp_to_d365.customer_erp_to_d365_standard_view import (
    CustomerErpToD365StandardView,
)
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.accounts_receivable.inquiries_and_reports.mq.customer_erp_to_d365.customer_erp_to_d365_top_gadget import (
    CustomerErpToD365TopGadget,
)
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.accounts_receivable.customers.all_customers.all_customers_standard_view import (
    AllCustomersStandardView,
)
from test_applications.d_365.chapters.finance_chapter.user_story.epics.customer_erp_to_d365.ax_2009_intergration import (
    Ax2009Intergration,
)


# --
# ...
# --


class CustomerErpToD365(BaseChapter, BaseUserStory):
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
        return ObjectProvider()(
            __file__.replace(".py", ".json ", -1).replace("\\", "/").replace(" c", "")
        )

    # --
    # ... setup, teardown and prepare
    # --

    def __setup(self) -> bool:

        try:

            super().setup()

            self.toolbars = Toolbars()
            self.customer_erp_to_d365_standard_view = CustomerErpToD365StandardView()
            self.customer_erp_to_d365_top_gadget = CustomerErpToD365TopGadget()
            self.ax2009_intergration = Ax2009Intergration()
            self.all_customers_standard_view = AllCustomersStandardView()

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

    @BaseChapter.log
    def customer_erp_to_d365(self) -> bool:

        try:

            self.state["expected_result"] = {
                "ax_d365_customer_id": {
                    "customer_id": "DIC11000",
                    "result": False,
                }
            }

            self.ax2009_intergration.ax_2009_intergration()

            self.state["ax_d365_customer_id"] = "DIC11000", True

            self.toolbars.change_mandant()

            self.toolbars.search_for_a_page = ("Customer ERP to D365", True)
            self.toolbars.set_text_in_search_for_a_page()

            self.delay(220)

            self.customer_erp_to_d365_standard_view.search_item = self.state[
                "ax_d365_customer_id"
            ]
            self.customer_erp_to_d365_standard_view.select_external_customer_account_id()

            self.toolbars.search_for_a_page = ("all customers", True)
            self.toolbars.set_text_in_search_for_a_page()

            self.all_customers_standard_view.search_item = self.state[
                "expected_result"
            ].get("ax_d365_customer_id")["customer_id"]

            self.state["expected_result"].get("ax_d365_customer_id")[
                "result"
            ] = self.all_customers_standard_view.select_customer_account_number()

            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False
