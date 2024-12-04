from typing import Any
from test_applications.d_365.core.object_provider import ObjectProvider
from test_applications.d_365.chapters.core.base_chapter import BaseChapter
from test_applications.d_365.abstrct_classes.tab.tab import Tab

# --
# ...
# --


class TabPurchasingDemographics(BaseChapter, Tab):
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
                    self.tab_purchasing_demographics()

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
        currency=("EUR", True),
        primary_contact=("", True),
        line_of_business=("", True),
        birth_place=("Berlin", True),
        residence_foreign_country=("Germany", True),
        birth_county=("Berlin", True),
        is_heir=(True, True),
        employee_responsible=("", True),
        segment=("", True),
        subsegment=("", True),
        chain=("", True),
        notes=("Notes", True),
    ) -> bool:

        try:

            if super().prepare():
                return True

            self.currency = currency
            self.primary_contact = primary_contact
            self.line_of_business = line_of_business
            self.birth_place = birth_place
            self.residence_foreign_country = residence_foreign_country
            self.birth_county = birth_county
            self.is_heir = is_heir
            self.employee_responsible = employee_responsible
            self.segment = segment
            self.subsegment = subsegment
            self.chain = chain
            self.notes = notes
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
    def tab_purchasing_demographics(self) -> bool:

        try:

            self.textbox(self.elements.cmb_currency, self.currency, is_press_enter=True)
            self.components.combobox_type_2(
                self.elements.cmb_primary_contact, self.primary_contact
            )
            self.components.combobox_type_2(
                self.elements.cmb_line_of_business, self.line_of_business
            )
            self.textbox(self.elements.txb_birth_place, self.birth_place)
            self.textbox(
                self.elements.cmb_residence_foreign_country,
                self.residence_foreign_country,
            )
            self.textbox(self.elements.cmb_birth_county, self.birth_county)
            self.textbox(self.elements.chk_heir, self.is_heir)
            self.components.combobox_type_2(
                self.elements.cmb_employee_responsible, self.employee_responsible
            )
            self.components.combobox_type_2(self.elements.cmb_segment, self.segment)
            self.components.combobox_type_2(
                self.elements.cmb_subsegment, self.subsegment
            )
            self.components.combobox_type_2(self.elements.cmb_chain, self.chain)
            self.textbox(self.elements.txb_notes, self.notes)

            self.delay(220)

            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False
