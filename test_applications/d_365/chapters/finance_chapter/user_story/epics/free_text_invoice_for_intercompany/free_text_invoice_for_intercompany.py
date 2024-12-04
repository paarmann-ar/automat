from typing import Any
from test_applications.d_365.core.object_provider import ObjectProvider
from test_applications.d_365.chapters.core.base_chapter import BaseChapter
from test_applications.d_365.chapters.core.base_user_story import BaseUserStory
from test_applications.d_365.chapters.finance_chapter.unit_testcases.toolbars.toolbars import (
    Toolbars,
)
from test_applications.d_365.chapters.finance_chapter.user_story.modules.accounts_receivable.intercompany_setup import (
    IntercompanySetup,
)
from test_applications.d_365.chapters.finance_chapter.user_story.modules.accounts_receivable.create_free_text_invoice import (
    CreateFreeTextInvoice,
)
from test_applications.d_365.chapters.finance_chapter.user_story.epics.free_text_invoice_for_intercompany.free_text_invoice_for_intercompany_rollback import (
    FreeTextInvoiceForIntercompanyRollback,
)
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.accounts_receivable.invoices.batch_invoicing.free_text_invoice import (
    PostFreeTextInvoice,
)
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.accounts_payable.invoices.invoice_journal.invoice_journal_manager import (
    InvoiceJournalManager,
)
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.general_ledger.ledger_setup.ledger_calendars.ledger_calendars_manager import (
    LedgerCalendarsManager,
)

# --
# ...
# --


class FreeTextInvoiceForIntercompany(BaseChapter, BaseUserStory):
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
            self.intercompany_setup = IntercompanySetup()
            self.create_free_text_invoice = CreateFreeTextInvoice()
            self.free_text_invoice_for_intercompany_rollback = (
                FreeTextInvoiceForIntercompanyRollback()
            )
            self.post_free_text_invoice = PostFreeTextInvoice()
            self.invoice_journal_manager = InvoiceJournalManager()
            self.ledger_calendars_manager = LedgerCalendarsManager()

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
    def free_text_invoice_for_intercompany(self) -> bool:

        try:

            self.toolbars.mandant = ("100", True)
            self.toolbars.change_mandant()

            self.free_text_invoice_for_intercompany_rollback()

            self.ledger_calendars_manager(
                step_10="edit",
                step_20="select_period",
                step_30="change_entity",
                step_50="save",
                step_60="back",
            )

            self.intercompany_setup.setup_intercompany()

            self.delay(220)

            self.create_free_text_invoice.new_free_text_invoices()

            self.toolbars.mandant = ("110", True)
            self.toolbars.change_mandant()
            
            self.invoice_journal_manager(
                step_10="back",
            )

            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False
