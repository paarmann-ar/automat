from test_applications.d_365.core.object_provider import ObjectProvider
from test_applications.d_365.chapters.core.base_chapter import BaseChapter
from typing import Any
from test_applications.d_365.abstrct_classes.page.page import Page
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.accounts_payable.invoices.invoice_journal.invoice_journal_top_gadget import InvoiceJournalTopGadget
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.accounts_payable.invoices.invoice_journal.invoice_journal_standard_view import InvoiceJournalStandardView
from test_applications.d_365.chapters.finance_chapter.unit_testcases.toolbars.toolbars import Toolbars

# --
# ...
# --

class InvoiceJournalManager(BaseChapter, Page):
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
                    self.invoice_manager_rollback(**kwargs)

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

            self.invoice_journal_top_gadget = InvoiceJournalTopGadget()
            self.invoice_journal_standard_view = InvoiceJournalStandardView()
            self.toolbars = Toolbars()

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
    @BaseChapter.wait_for(
        element_for_waiting_until_visible="frm_invoice_journal",
        type_of_element="text_to_search",
    )
    @BaseChapter.log
    def goto_start_point(self) -> bool:

        try:

            self.toolbars.search_for_a_page_text = ("Invoice journal", True)
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
    def invoice_manager_rollback(self) -> bool:

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
        type_of_element="text_to_search",
    )
    @BaseChapter.log
    def invoice_journal_manager(self, **kwargs) -> bool:

        try:

            for _, tab in kwargs.items():
                match tab:
                    case "back":
                        self.invoice_journal_top_gadget.back()

                    case "save":
                        self.invoice_journal_top_gadget.save()

                    case _:
                        pass

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False
