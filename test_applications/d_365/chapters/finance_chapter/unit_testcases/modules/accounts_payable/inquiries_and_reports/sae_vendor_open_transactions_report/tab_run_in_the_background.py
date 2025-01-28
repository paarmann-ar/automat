from typing import Any
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.system_administration.periodic_tasks.email_processing.email_distributor_batch.tab_run_in_the_background import (
    TabRunInTheBackground as Tab_Run_In_The_Background
)

# --
# ...
# --


class TabRunInTheBackground(Tab_Run_In_The_Background):
    def __init__(
        self,
        *args,
        **kwargs,
    ) -> None:
        super().__init__(*args, **kwargs)

        self.task_description=("Sae Vendor open transactions report", True)