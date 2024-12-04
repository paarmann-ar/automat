from typing import Any
from test_applications.d_365.core.object_provider import ObjectProvider
from test_applications.d_365.chapters.core.base_chapter import BaseChapter
from test_applications.d_365.abstrct_classes.popup.popup import Popup

# --
# ...
# --


class TabAddressesPopupNewAddress(BaseChapter, Popup):
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
        location_id=("", False),
        name_or_description=("vendor test112", True),
        purpose=("Business", True),
        country=("ITA", True),
        zip=("12345", True),
        street=("Milano str. 5", True),
        city=("Rome", True),
        district=("", False),
        address_addition=("", False),
        is_primary=(True, True),
        is_private=(False, False),
        is_primary_for_country=(True, True),
    ) -> bool:

        try:

            if super().prepare():
                return True

            self.location_id = location_id
            self.name_or_description = (
                self.get_random(),
                (
                    name_or_description[1]
                    if name_or_description[0] == ""
                    else name_or_description[1]
                ),
            )
            self.purpose = purpose
            self.country = country
            self.zip = self.get_random(type="int"), zip[1] if zip[0] == "" else zip[1]
            self.street = self.get_random(), street[1] if street[0] == "" else street[1]
            self.city = city
            self.district = self.get_random(), (
                district[1] if district[0] == "" else district[1]
            )
            self.address_addition = (
                self.get_random(),
                address_addition[1] if address_addition[0] == "" else address_addition[1],
            )
            self.is_primary = is_primary
            self.is_private = is_private
            self.is_primary_for_country = is_primary_for_country
            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False

    # --
    # ... methods
    # --

    @BaseChapter.wait_for(
        element_for_waiting_until_visible="frm_popup_new_address",
        type_of_element="text_to_search",
    )
    @BaseChapter.log
    def new_address(self) -> bool:

        try:

            self.textbox(self.elements.txb_location_id, self.location_id)
            self.textbox(
                self.elements.txb_name_or_description, self.name_or_description
            )
            self.components.form_radio_button_and_select(
                self.elements.cmb_purpose, self.purpose
            )

            self.textbox(self.elements.cmb_country, self.country, is_press_tab=True)

            self.textbox(self.elements.cmb_zip, self.zip, is_press_tab=True)

            self.textbox(self.elements.txb_street, self.street)
            self.textbox(self.elements.cmb_city, self.city, is_press_tab=True)
            self.textbox(self.elements.txb_district, self.district)
            self.textbox(self.elements.txb_address_addition, self.address_addition)

            self.checkbox(
                self.elements.chk_primary,
                self.is_primary,
            )

            self.checkbox(
                self.elements.chk_private,
                self.is_private,
            )

            self.checkbox(
                self.elements.chk_primary_for_country,
                self.is_primary_for_country,
            )

            self.click_button(self.elements.btn_ok)

            self.delay(220)
            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False
