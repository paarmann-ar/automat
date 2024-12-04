from typing import Any
from test_applications.d_365.core.object_provider import ObjectProvider
from test_applications.d_365.chapters.core.base_chapter import BaseChapter
from test_applications.d_365.abstrct_classes.popup.popup import Popup

# --
# ...
# --


class TabContactInformationPopupEditContactInformation(BaseChapter, Popup):
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
                    self.edit_contact_information()

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
        type=("Phone", False),
        international_calling_code=("", True),
        phone=("", False),
        extention=("", True),
        purpose=("Business", True),
        purpose_type=("Private", True),
        reachabilirty=("reachabilirty", True),
        is_valid=(True, True),
        is_mobile=(True, True),
        is_primary=(True, True),
        is_private=(True, True),
        is_marketing_opt_in=(True, True),
    ) -> bool:

        try:

            if super().prepare():
                return True

            self.description = description
            self.type = type
            self.international_calling_code = international_calling_code
            self.phone = self.get_random(), phone[1] if phone[0] == "" else phone[1]
            self.extention = self.get_random(), (
                extention[1] if extention[0] == "" else extention[1]
            )
            self.purpose = purpose
            self.purpose_type = purpose_type
            self.reachabilirty = reachabilirty
            self.is_valid = is_valid
            self.is_mobile = is_mobile
            self.is_primary = is_primary
            self.is_private = is_private
            self.is_marketing_opt_in = is_marketing_opt_in
            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False

    # --
    # ... methods
    # --
    
    @BaseChapter.wait_for(
        element_for_waiting_until_visible="frm_popup_edit_contact_information",
        type_of_element="text_to_search",
    )
    @BaseChapter.log
    def edit_contact_information(self) -> bool:

        try:

            self.textbox(self.elements.txb_description, self.description)
            self.textbox(self.elements.txb_type, self.type)
            self.textbox(
                self.elements.txb_international_calling_code,
                self.international_calling_code,
            )
            self.textbox(self.elements.txb_phone, self.phone)
            self.textbox(self.elements.txb_extention, self.extention)
            self.components.form_radio_button_and_select(
                self.elements.cmb_purpose, self.purpose
            )
            self.textbox(self.elements.cmb_purpose_type, self.purpose_type)
            self.textbox(self.elements.txb_reachabilirty, self.reachabilirty)
            self.checkbox(self.elements.chk_valid, self.is_valid)
            self.checkbox(self.elements.chk_mobile, self.is_mobile)
            self.checkbox(self.elements.chk_primary, self.is_primary)
            self.checkbox(self.elements.chk_private, self.is_private)
            self.checkbox(self.elements.chk_marketing_opt_in, self.is_marketing_opt_in)

            self.click_button(self.elements.btn_ok)

            self.delay(220)

            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False
