from typing import Any
from test_applications.d_365.core.object_provider import ObjectProvider
from test_applications.d_365.chapters.core.base_chapter import BaseChapter
from test_applications.d_365.chapters.core.base_user_story import BaseUserStory
from test_applications.d_365.chapters.finance_chapter.unit_testcases.toolbars.toolbars import (
    Toolbars,
)
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.accounts_receivable.invoices.all_free_text_invoices.all_free_text_invoices_top_gadget import AllFreeTextInvoicesTopGadget
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.accounts_receivable.invoices.all_free_text_invoices.free_text_invoice.free_text_invoice_manager import FreeTextInvoiceManager
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.accounts_receivable.invoices.batch_invoicing.free_text_invoice import FreeTextInvoice

# --
# ...
# --

class CreateFreeTextInvoice(BaseChapter, BaseUserStory):
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
            self.all_free_text_invoices_top_gadget = AllFreeTextInvoicesTopGadget()
            self.free_text_invoice_manager = FreeTextInvoiceManager()
            self.free_text_invoice = FreeTextInvoice()
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

            self.toolbars.search_for_a_page = ("all free text invoice", True)
            self.toolbars.search_for_a_page_text = ("Free text invoice", True)
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
    def create_free_text_invoice_rollback(self) -> bool:

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
    def new_free_text_invoices(self) -> bool:

        try:

            self.goto_start_point()

            self.all_free_text_invoices_top_gadget.new_free_text_invoice()

            self.free_text_invoice_manager(
                step_10="tab_free_text_invoice_header",
                step_20="tab_lines",
                step_30="tab_detail_lines",
                step_40="post",
            )

            self.free_text_invoice.post_free_text_invoice()

            self.free_text_invoice_manager(
                step_10="save",
            )

            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False
