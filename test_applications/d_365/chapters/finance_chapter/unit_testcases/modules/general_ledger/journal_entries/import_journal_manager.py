from test_applications.d_365.core.object_provider import ObjectProvider
from test_applications.d_365.chapters.core.base_chapter import BaseChapter
from typing import Any
from test_applications.d_365.abstrct_classes.form.form import Form
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.general_ledger.journal_entries.import_journal.import_journal_page_manager import ImportJournalPageManager
from test_applications.d_365.chapters.finance_chapter.unit_testcases.toolbars.toolbars import (
    Toolbars,
)
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.general_ledger.journal_entries.general_journals_page import (
    GeneralJournalsPage,
)
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.general_ledger.journal_entries.general_journals_top_gadget import (
    GeneralJournalsTopGadget,
)

# --
# ...
# --


class ImportJournalManager(BaseChapter, Form):
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
                    self.import_journal_manager()

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
            self.import_journal_page_manager = ImportJournalPageManager()
            self.general_journals_page = GeneralJournalsPage()
            self.general_journals_top_gadget = GeneralJournalsTopGadget()

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

            self.toolbars.search_for_a_page = ("General journals", True)
            self.toolbars.full_address = "General ledger > Journal entries"
            self.toolbars.set_full_address_in_search_for_a_page()

            self.tipbox()

            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False

    # --
    # ... rollback
    # --
    
    @BaseChapter.log
    def import_journal_rollback(self) -> bool:

        try:

            self.goto_start_point()
            self.general_journals_page.select_show()
            self.general_journals_page.select_show_user_created_only()

            self.elements.txb_GeneralJournalsPage_description = "xpath", f"//input[@title='{self.state['GeneralJournalsPage_description']}']"
           
            self.double_click(self.elements.txb_GeneralJournalsPage_description)

            self.general_journals_top_gadget.delete()
                
            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False
        
    # --
    # ... methods
    # --

    @BaseChapter.wait_for(
        element_for_waiting_until_visible="frm_import_journal",
        type_of_element="text_to_search",
    )
    @BaseChapter.log
    def import_journal_manager(self, **kwargs) -> bool:

        try:

            for _, tab in kwargs.items():
                match tab:

                    case "select_show":
                        self.general_journals_page.select_show()

                    case "new":
                        self.general_journals_top_gadget.new()

                    case "enter_name_description":
                        self.general_journals_page.enter_name_description()

                    case "import_journal":
                        self.general_journals_top_gadget.import_journal()

                    case "import_journal_page_manager":
                        self.import_journal_page_manager.import_journal_page_manager(
                            step_10 = "tab_parameters",
                            step_20 = "tab_run_in_the_background",
                            step_30 = "save",
                        )

                    case "validate":
                        self.general_journals_top_gadget.validate()
                        self.wait_for_visibility(self.elements.ctm_validation)

                        self.delay(500)

                    case "validate_validate":
                        self.general_journals_top_gadget.validate_validate()

                    case _:
                        pass
                
                self.delay(220)

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False
