from typing import Any
from test_applications.d_365.core.object_provider import ObjectProvider
from test_applications.d_365.chapters.core.base_chapter import BaseChapter
from test_applications.d_365.abstrct_classes.page.page import Page

# --
# ...
# --


class GeneralJournalsPage(BaseChapter, Page):
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
        show=("All", True),
        show_user_created_only=(True, True),
        name=("139_J_GENE", True),
        description=("Test F24 VAT", True),
    ) -> bool:

        try:

            if super().prepare():
                return True

            self.show = show
            self.show_user_created_only = show_user_created_only
            self.name = name
            self.description = description

            self.state["GeneralJournalsPage_description"], _ = description

            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False

    # --
    # ... methods
    # --

    @BaseChapter.wait_for(
        element_for_waiting_until_visible="frm_general_journals",
        type_of_element="text_to_search",
    )
    @BaseChapter.log
    def select_show(self) -> bool:

        try:

            self.textbox(
                self.elements.cmb_show,
                self.show,
                is_press_enter=True,
            )

            self.delay(220)

            return False

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False

    # --
    # ...
    # --

    @BaseChapter.wait_for(
        element_for_waiting_until_visible="frm_general_journals",
        type_of_element="text_to_search",
    )
    @BaseChapter.log
    def select_show_user_created_only(self) -> bool:

        try:

            self.checkbox(
                self.elements.chk_show_user_created_only,
                self.show_user_created_only,
            )

            self.delay(220)

            return False

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False

    # --
    # ...
    # --

    @BaseChapter.wait_for(
        element_for_waiting_until_visible="frm_general_journals",
        type_of_element="text_to_search",
    )
    @BaseChapter.log
    def enter_name_description(self) -> bool:

        try:

            self.textbox(
                self.elements.txb_name,
                self.name,
                is_click_befor=False,
                is_double_click_befor=True,
                is_check_readonly=False,
                is_press_enter = True,
            )

            self.textbox(
                self.elements.txb_description,
                self.description,
                is_click_befor=False,
                is_double_click_befor=True,
                is_check_readonly=False,
            )

            self.delay(220)

            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False
