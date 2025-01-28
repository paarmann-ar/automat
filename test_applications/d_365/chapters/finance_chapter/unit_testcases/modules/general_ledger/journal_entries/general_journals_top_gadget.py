from typing import Any
from test_applications.d_365.core.object_provider import ObjectProvider
from test_applications.d_365.chapters.core.base_chapter import BaseChapter
from test_applications.d_365.abstrct_classes.page.page import Page


# --
# ...
# --


class GeneralJournalsTopGadget(BaseChapter, Page):
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

    @BaseChapter.wait_for(
        element_for_waiting_until_visible="frm_general_journals",
        type_of_element="text_to_search",
    )
    @BaseChapter.log
    def back(self) -> bool:

        try:

            self.click_button(self.elements.btn_back)

            self.delay(220)

            return True

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
    def save(self) -> bool:

        try:

            self.click_button(self.elements.btn_save)

            self.delay(220)

            return True

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
    def new(self) -> bool:

        try:

            self.click_button(self.elements.btn_new)

            self.delay(220)

            return True

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
    def import_journal(self) -> bool:

        try:

            self.click_button(self.elements.btn_import_journal)

            self.delay(220)

            return True

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
    def delete(self) -> bool:

        try:

            self.click_button(self.elements.btn_delete)

            self.delay(220)

            self.lightbox(action="Yes")
            self.delay(1000)

            self.lightbox(action="Yes")
            self.blocking_message()

            return True

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
    def import_excel(self) -> bool:

        try:

            self.click_button(self.elements.btn_import_excel)

            self.delay(220)

            return True

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
    def validate(self) -> bool:

        try:

            self.click_button(self.elements.btn_validate)
            self.delay(220)

            self.wait_for_visibility(self.elements.ctm_validation)
            self.delay(220)

            return True

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
    def validate_validate(self) -> bool:

        try:

            self.click_button(self.elements.btn_validate_validate)

            self.delay(220)

            if self.lightbox(action=""):
                self.lightbox(lightbox="wait_until_lightbox_disapear")
                
            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False
