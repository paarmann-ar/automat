from test_applications.d_365.core.object_provider import ObjectProvider
from test_applications.d_365.chapters.core.base_chapter import BaseChapter
from typing import Any
from test_applications.d_365.abstrct_classes.form.form import Form
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.general_ledger.ledger_setup.ledger_calendars.ledger_calendars_top_gadget import LedgerCalendarsTopGadget
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.general_ledger.ledger_setup.ledger_calendars.ledger_calendars_standard_view import LedgerCalendarsStandardView
from test_applications.d_365.chapters.finance_chapter.unit_testcases.toolbars.toolbars import Toolbars

# --
# ...
# --


class LedgerCalendarsManager(BaseChapter, Form):
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
                    self.ledger_calendars_manager(**kwargs)

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

            self.toolbars = Toolbars()
            self.ledger_calendars_standard_view = LedgerCalendarsStandardView()
            self.ledger_calendars_top_gadget = LedgerCalendarsTopGadget()
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

            self.toolbars.search_for_a_page = ("Ledger calendars", True)
            self.toolbars.full_address = "General ledger > Calendars"
            self.toolbars.set_full_address_in_search_for_a_page()
            
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
    def ledger_calendars_rollback(self) -> bool:

        try:

            self.goto_start_point()
            
            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False
        
    # --
    # ... methods
    # --

    @BaseChapter.wait_for(
        element_for_waiting_until_visible="frm_ledger_calendars",
        type_of_element="text_to_search",
    )
    @BaseChapter.log
    def ledger_calendars_manager(self, **kwargs) -> bool:

        try:
            
            for _, tab in kwargs.items():
                match tab:
                    case "select_period":
                        self.ledger_calendars_standard_view.select_period()

                    case "change_entity":
                        self.ledger_calendars_standard_view.change_entity()

                    case "change_secound_entity":
                        self.ledger_calendars_standard_view.change_secound_entity()
                
                    case "edit":
                        self.ledger_calendars_top_gadget.edit()

                    case "save":
                        self.ledger_calendars_top_gadget.save()

                    case "back":
                        self.ledger_calendars_top_gadget.back()

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False
