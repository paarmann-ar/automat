from typing import Any
from test_applications.d_365.core.object_provider import ObjectProvider
from test_applications.d_365.chapters.core.base_chapter import BaseChapter
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.accounts_payable.vendors.all_vendors.vendor_new_record.tab_contact_information_popup_edit_contact_information import (
    TabContactInformationPopupEditContactInformation,
)
from test_applications.d_365.abstrct_classes.tab.tab import Tab

# --
# ...
# --


class TabContactInformation(BaseChapter, Tab):
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
    # ... get_elements
    # --

    def get_elements(self) -> str:
        return ObjectProvider()(__file__.replace(".py", ".json ", -1).replace("\\", "/").replace(" c", ""))

    # --
    # ... setup, teardown and prepare
    # --

    def __setup(self) -> bool:

        try:

            super().setup()

            self.tab_contact_information_popup_edit_contact_information = (
                TabContactInformationPopupEditContactInformation()
            )

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
        description=("description", True),
        type=("Phone", True),
        contact_number=("", True),
        extention=("extention", True),
    ) -> bool:

        try:

            if super().prepare():
                return True

            self.description = description
            self.type = type
            self.contact_number = (
                self.get_random(),
                contact_number[1] if contact_number[0] == "" else contact_number[1],
            )
            self.extention = extention
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
    def add_contact_information(self) -> bool:

        try:

            self.click_button(self.elements.btn_add)
            self.delay(1000)

            if self.lightbox():
                return True

            self.textbox(
                self.elements.lv_add_contact_info_description, self.description
            )
            self.textbox(
                self.elements.lv_add_contact_info_type,
                self.type,
                is_press_tab=True,
                is_clear=True,
            )
            self.textbox(
                self.elements.lv_add_contact_info_contact_number,
                self.contact_number,
                is_press_tab=True,
            )
            self.textbox(
                self.elements.lv_add_contact_info_extention,
                self.extention,
                is_press_tab=True,
            )

            self.delay(220)

            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False

    @BaseChapter.wait_for(element_for_waiting_until_visible="btn_tab")
    @BaseChapter.log
    def edit_contact_information(self) -> bool:

        try:

            self.click_button(self.elements.btn_edit)

            self.tab_contact_information_popup_edit_contact_information()

            self.delay(220)

            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False

    @BaseChapter.wait_for(element_for_waiting_until_visible="btn_tab")
    @BaseChapter.log
    def remove_contact_information(self) -> bool:

        try:

            self.click_button(self.elements.btn_remove)
            self.delay(220)

            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False
