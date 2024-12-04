from typing import Any
from test_applications.d_365.core.object_provider import ObjectProvider
from test_applications.d_365.chapters.core.base_chapter import BaseChapter
from test_applications.d_365.abstrct_classes.tab.tab import Tab
from test_applications.d_365.components.component.form.form_vendor_name import (
    FormVendorName,
)

# --
# ...
# --


class TabVendorGeneral(BaseChapter, Tab):
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
                    self.tab_general()

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
            
            self.form_vendor_name = FormVendorName()
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
        vendor_account=("", False),
        external_vendor=("", False),
        workday_account_number=("", False),
        type=("Organization", True),
        vendor_invoice_type=("None", False),
        vendor_type=("Standard", True),
        payment_priority=("", False),
        name=("vendor test112", True),
        search_name=("vendor test112", True),
        group=("GOODS-IT", True),
        DUNS_number=("", False),
        address_books=("", True),
        phonetic_name=("phonetic_name", False),
        languges=("it", True),
        collaboration_activation=("Active (PO is auto-confirmed)", True),
    ) -> bool:

        try:

            if super().prepare():
                return True

            self.vendor_account = vendor_account
            self.external_vendor = external_vendor
            self.workday_account_number = workday_account_number
            self.type = type
            self.vendor_invoice_type = vendor_invoice_type
            self.vendor_type = vendor_type
            self.payment_priority = payment_priority
            self.name = name
            self.search_name = search_name
            self.group = group
            self.DUNS_number = DUNS_number
            self.address_books = address_books
            self.phonetic_name = phonetic_name
            self.languges = languges
            self.collaboration_activation = collaboration_activation
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
    def tab_general(self) -> bool:

        try:

            self.textbox(self.elements.txb_vendor_account, self.vendor_account)
            self.textbox(self.elements.txb_external_vendor, self.external_vendor)

            self.textbox(
                self.elements.txb_workday_account_number, self.workday_account_number
            )

            self.textbox(self.elements.cmb_type, self.type, is_press_enter=True)

            self.textbox(
                self.elements.txb_vendor_invoice_type, self.vendor_invoice_type
            )

            self.textbox(
                self.elements.cmb_vendor_type,
                self.vendor_type,
                is_press_enter=True,
            )

            self.textbox(
                self.elements.txb_payment_priority,
                self.payment_priority,
            )

            # self.textbox(
            #     self.elements.cmb_name,
            #     self.name,
            # )

            # self.keys(self.elements.cmb_name, "\ue007")

            self.form_vendor_name(
                self.elements.cmb_name,
                self.name,
            )

            self.click(self.elements.txb_search_name)

            # self.textbox(
            #     self.elements.txb_search_name, self.search_name, is_press_enter=True
            # )

            self.add_object_to_possible_appeared_objects_stack(
                {
                    "form_match_found": (
                        {"text_to_search": "Match found"},
                        self.components.form_match_found(),
                    )
                },
            )
            self.is_object_in_possible_appeared_objects_appeared()

            self.delete_object_to_possible_appeared_objects_stack( "form_match_found")

            self.textbox(self.elements.txb_groupe, self.group, is_press_enter=True)

            self.textbox(
                self.elements.txb_DUNS_number,
                self.DUNS_number,
            )

            self.is_class_wait_for_validation_failed(self.elements.txb_DUNS_number)

            self.components.form_select_and_sort_item(
                self.elements.cmb_address_books, self.address_books
            )

            self.textbox(self.elements.txb_phonetic_name, self.phonetic_name)
            self.textbox(
                self.elements.cmb_languges,
                self.languges,
                is_press_tab=True,
                is_clear=True,
            )

            self.textbox(
                self.elements.cmb_collaboration_activation,
                self.collaboration_activation,
                is_press_enter=True,
                is_clear=True,
            )

            self.lightbox(action="Yes")

            self.delay(220)

            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False

    # --
    # ...
    # --

    @Tab.expand_tab
    @BaseChapter.wait_for(element_for_waiting_until_visible="btn_tab")
    @BaseChapter.log
    def get_vendor_account(self) -> bool:

        try:

            self.state["vendor_account"] = self.read_textbox(
                self.elements.txb_vendor_account
            )          

            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False
