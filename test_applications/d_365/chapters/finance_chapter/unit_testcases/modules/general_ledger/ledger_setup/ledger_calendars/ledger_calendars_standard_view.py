from test_applications.d_365.core.object_provider import ObjectProvider
from test_applications.d_365.chapters.core.base_chapter import BaseChapter
from typing import Any
from test_applications.d_365.abstrct_classes.form.form import Form
from test_applications.d_365.abstrct_classes.standard_view.standard_view import (
    StandardView,
)

# --
# ...
# --


class LedgerCalendarsStandardView(BaseChapter, StandardView):
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
        period=("Period 1", True),
        mandants=(["100", "110"], True),
        period_status=("Permanently closed", True),
    ) -> bool:

        try:

            if super().prepare():
                return True

            self.period = period
            self.mandants = mandants
            self.period_status = period_status

            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False

    # --
    # ... methods
    # --

    @BaseChapter.wait_for(
        element_for_waiting_until_visible="frm_ledger_calendars_standard_view",
        type_of_element="text_to_search",
    )
    @BaseChapter.log
    def select_period(self, **kwargs) -> bool:

        try:

            self.search_item_text = "Period name"
            self.search_item = self.period

            return self.select_item(**kwargs)

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False

    # --
    # ...
    # --

    @BaseChapter.wait_for(
        element_for_waiting_until_visible="frm_ledger_calendars_standard_view",
        type_of_element="text_to_search",
    )
    @BaseChapter.log
    def change_entity(self) -> bool:

        try:

            self.filter_row_text = "Ledger_Name"
            self.filter_header_text = "Period_Ledger"
            
            mandants, _ = self.mandants

            for mandant in mandants:
                self.filter_row_search_item = mandant

                self.filter_row()

                self.delay(1000)

                self.textbox(
                    self.elements.cmb_period_status,
                    ("Open", True),
                    is_double_click_befor=True,
                )

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False
