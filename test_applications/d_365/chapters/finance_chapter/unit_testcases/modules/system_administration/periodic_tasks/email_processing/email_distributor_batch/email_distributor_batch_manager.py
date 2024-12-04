from test_applications.d_365.core.object_provider import ObjectProvider
from test_applications.d_365.chapters.core.base_chapter import BaseChapter
from typing import Any
from test_applications.d_365.abstrct_classes.form.form import Form
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.system_administration.periodic_tasks.email_processing.email_distributor_batch.tab_run_in_the_background import TabRunInTheBackground
from test_applications.d_365.chapters.finance_chapter.unit_testcases.toolbars.toolbars import Toolbars

# --
# ...
# --

class EmailDistributorBatchManager(BaseChapter, Form):
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
                    self.email_distributor_batch_manager(**kwargs)

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
            self.tab_run_in_the_background = TabRunInTheBackground()
            
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
        self
    ) -> bool:

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

            self.toolbars.search_for_a_page = ("Email distributor batch", True)
            self.toolbars.full_address = "System administration > Periodic tasks > Email processing"
            self.toolbars.set_full_address_in_search_for_a_page()
            
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
    def ledger_calendars_rollback(self) -> bool:

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
        element_for_waiting_until_visible="frm_email_distributor_batch",
        type_of_element="text_to_search",
    )
    @BaseChapter.log
    def email_distributor_batch_manager(self, **kwargs) -> bool:

        try:

            for _, tab in kwargs.items():
                match tab:
                      
                    case "tab_run_in_the_background":
                        self.tab_run_in_the_background()

                    case "save":
                        self.click_button(self.elements.btn_ok)

                    case _:
                        pass

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False