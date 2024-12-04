from typing import Any
from test_applications.d_365.core.object_provider import ObjectProvider
from test_applications.d_365.chapters.core.base_chapter import BaseChapter
from test_applications.d_365.abstrct_classes.tab.tab import Tab
from datetime import date

# --
# ...
# --


class TabRunInTheBackground(BaseChapter, Tab):
    def __init__(
        self,
        *args,
        **kwargs,
    ) -> None:
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
                    self.tab_run_in_the_background()
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

    def __prepare(
        self,
        is_batch_processing=(True, False),
        task_description=("Email distributor batch", False),
        batch_group=("", False),
        is_private=(True, False),
        is_critical_job=(True, False),
        monitoring_category=("Undefined", False),
    ) -> bool:

        try:

            if super().prepare():
                return True

            self.is_batch_processing = is_batch_processing
            self.task_description = task_description
            self.batch_group = batch_group
            self.is_private = is_private
            self.is_critical_job = is_critical_job
            self.monitoring_category = monitoring_category

            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False

    # --
    # ... methods
    # --
    @Tab.expand_tab
    @BaseChapter.wait_for(element_for_waiting_until_visible="btn_tab")
    @BaseChapter.log
    def tab_run_in_the_background(self) -> bool:

        try:

            self.checkbox(self.elements.chk_batch_processing, self.is_batch_processing)
            self.textbox(self.elements.txb_task_description, self.task_description)
            self.textbox(self.elements.cmb_batch_group, self.batch_group)
            self.checkbox(self.elements.chk_private, self.is_private)
            self.checkbox(self.elements.chk_critical_job, self.is_critical_job)
            self.textbox(self.elements.cmb_monitoring_category, self.monitoring_category)

            self.delay(220)

            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False
