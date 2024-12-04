from typing import Any
from test_applications.d_365.core.object_provider import ObjectProvider
from test_applications.d_365.chapters.core.base_chapter import BaseChapter
from test_applications.d_365.chapters.core.base_user_story import BaseUserStory
from test_applications.d_365.chapters.finance_chapter.unit_testcases.toolbars.toolbars import (
    Toolbars,
)
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.general_ledger.journal_entries.general_journals_standard_view import (
    GeneralJournalsStandardView,
)
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.general_ledger.journal_entries.general_journals_top_gadget import (
    GeneralJournalsTopGadget,
)
from test_applications.d_365.chapters.finance_chapter.user_story.modules.general_ledger.journal_entries.import_journal import (
    ImportJournal,
)

# --
# ...
# --

class ImportLedgerJournalAndValidation(BaseChapter, BaseUserStory):
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
            self.general_journals_standard_view = GeneralJournalsStandardView()
            self.general_journals_top_gadget = GeneralJournalsTopGadget()
            self.import_journal = ImportJournal()

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
    def import_journal_and_validate(self) -> bool:

        try:

            self.toolbars.change_mandant(mandant=("139", True))

            self.toolbars.search_for_a_page = ("General journals", True)
            self.toolbars.set_text_in_search_for_a_page()

            self.delay(220)

            self.import_journal.import_journal()

            self.general_journals_top_gadget.validate()
            self.general_journals_top_gadget.validate_validate()

            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False
