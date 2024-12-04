from typing import Any
from test_applications.d_365.core.object_provider import ObjectProvider
from test_applications.d_365.chapters.core.base_chapter import BaseChapter
from test_applications.d_365.abstrct_classes.tab.tab import Tab
from datetime import date
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.system_administration.periodic_tasks.email_processing.email_distributor_batch.tab_run_in_the_background import TabRunInTheBackground

# --
# ...
# --


class TabRunInTheBackground(TabRunInTheBackground):
    def __init__(
        self,
        *args,
        **kwargs,
    ) -> None:
        super().__init__(*args, **kwargs)

        self.task_description=("Sae Vendor open transactions report", True)