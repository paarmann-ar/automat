from typing import Any
from test_applications.d_365.core.object_provider import ObjectProvider
from test_applications.d_365.chapters.core.base_chapter import BaseChapter
from test_applications.d_365.abstrct_classes.page.page import Page
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.accounts_receivable.customers.all_customers.all_customers_top_gadget import AllCustomersTopGadget


# --
# ...
# --


class AllCustomersTopGadget(AllCustomersTopGadget):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        print(__class__.__name__, id(__class__))