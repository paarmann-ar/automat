from typing import Any
from test_applications.d_365.core.object_provider import ObjectProvider
from test_applications.d_365.chapters.core.base_chapter import BaseChapter
from test_applications.d_365.chapters.core.base_user_story import BaseUserStory
from test_applications.d_365.chapters.finance_chapter.unit_testcases.toolbars.toolbars import (
    Toolbars,
)
from test_applications.d_365.chapters.finance_chapter.user_story.epics.import_ledger_journal_and_validation.import_ledger_journal_and_validation_rollback import ImportLedgerJournalAndValidationRollback
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.general_ledger.journal_entries.import_journal_manager import (
    ImportJournalManager,
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
            self.import_journal_manager = ImportJournalManager()
            self.import_ledger_journal_and_validation_rollback = ImportLedgerJournalAndValidationRollback()

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

            self.toolbars.change_mandant()

            self.import_ledger_journal_and_validation_rollback.import_journal_and_validate_rollback()

            self.import_journal_manager.import_journal_manager(
                step_10="select_show",
                step_20="new",
                step_30="enter_name_description",
                step_40="import_journal",
                step_50="import_journal_page_manager",
                step_80="validate",
                step_90="validate_validate",
            )

            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False
