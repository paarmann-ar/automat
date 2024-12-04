from test_applications.d_365.core.object_provider import ObjectProvider
from test_applications.d_365.chapters.core.base_chapter import BaseChapter
from typing import Any

# --
# ...
# --


class Toolbars(BaseChapter):
    def __init__(self, *args, **kwargs) -> None:
        self.elements = self.get_elements()
        self.__prepare(**kwargs)
        self.__setup()

        print(__class__.__name__, id(__class__))

    # --
    # ... call
    # --

    def __call__(self, action, **kwargs) -> Any:

        try:

            if super().__call__(action, **kwargs):
                return True

            if super_result := super().__call__(action, **kwargs):
                return super_result

            match action:

                case _:
                    raise Exception(
                        f"rdc_automat: class {__class__.__name__} have no method {action}."
                    )

            return True

        except Exception as exp:
            print(repr(exp))
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

    # --
    # ...
    # --

    def __teardown(self) -> bool:

        try:

            super().teardown()

            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False

    # --
    # ...
    # --

    def __prepare(
        self,
        mandant=("139", True),
        search_for_a_page=("all vendors", True),
        full_address="Accounts payable > Inquiries and reports > Invoice",
    ) -> bool:

        try:

            if super().prepare():
                return True
            
            self.search_for_a_page_text = ""

            self.mandant = mandant
            self.search_for_a_page = search_for_a_page
            self.full_address = full_address

            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False

    # --
    # ...
    # --

    @BaseChapter.wait_for(element_for_waiting_until_visible="frm_toolbars")
    def change_mandant(self) -> bool:

        try:

            self.click(self.elements.btn_company_mandant)
            self.textbox(
                self.elements.cmb_mandant_change, self.mandant, is_press_enter=True
            )
            self.delay(1000)

            self.wait_for_visibility(self.elements.lbl_company_name)

            self.click_button(self.elements.btn_home)
            
            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False

    # --
    # ...
    # --

    # @BaseChapter.wait_for(element_for_waiting_until_visible="frm_toolbars")
    def set_text_in_search_for_a_page(self) -> bool:

        try:

            self.click(self.elements.txb_search_for_a_page)
            self.delay(500)
            self.click(self.elements.txb_search_for_a_page)
            self.delay(500)

            self.textbox(
                self.elements.txb_search_for_a_page,
                self.search_for_a_page,
                is_check_readonly=False,
            )

            self.click(self.elements.txb_search_for_a_page)

            while not self.alert(
                alert="is_please_wait_processing_your_request", is_log_exception=False
            ):
                self.confirm_search_txt_entered()

                if self.search_for_a_page_text == "":
                    self.search_for_a_page_text, _ = self.search_for_a_page

                if self.search_text_on_current_page_text(
                    ("text_to_search", self.search_for_a_page_text)
                ):
                    break

            self.blocking_message()
            self.search_for_a_page_text = ""

            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False

    # --
    # ...
    # --

    def confirm_search_txt_entered(self) -> bool:

        try:

            while (
                self.driver.find_element(*self.elements.lbx_search_for_a_page)
                .get_attribute("data-dyn-lastvisible")
                .find("true")
                != 0
            ):
                self.click(self.elements.txb_search_for_a_page)
                self.delay(250)

                self.textbox(
                    self.elements.txb_search_for_a_page,
                    self.search_for_a_page,
                    is_check_readonly=False,
                )

                self.delay(250)

            self.click(self.elements.txb_search_for_a_page)

            self.textbox(
                self.elements.txb_search_for_a_page,
                ("", True),
                is_clear=False,
                is_check_key_there=False,
                is_press_enter=True,
                is_check_readonly=False,
            )

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False

    # --
    # ...
    # --

    def set_full_address_in_search_for_a_page(self) -> bool:

        try:

            self.click(self.elements.txb_search_for_a_page)
            self.delay(500)
            self.click(self.elements.txb_search_for_a_page)
            self.delay(500)

            self.textbox(
                self.elements.txb_search_for_a_page,
                self.search_for_a_page,
                is_check_readonly=False,
            )

            self.click(self.elements.txb_search_for_a_page)

            while not self.alert(
                alert="is_please_wait_processing_your_request", is_log_exception=False
            ):
                self.confirm_full_address()

                if self.search_for_a_page_text == "":
                    self.search_for_a_page_text, _ = self.search_for_a_page

                if self.search_text_on_current_page_text(
                    ("text_to_search", self.search_for_a_page_text)
                ):
                    break

            self.blocking_message()
            self.search_for_a_page_text = ""
            
            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False

    # --
    # ...
    # --

    def confirm_full_address(self) -> bool:

        try:

            type_, value_ = self.elements.itm
            search_item = self.full_address

            self.elements.item = (type_, value_.replace("?", search_item))

            while (
                self.driver.find_element(*self.elements.lbx_search_for_a_page)
                .get_attribute("data-dyn-lastvisible")
                .find("true")
                != 0
            ):
                self.click(self.elements.txb_search_for_a_page)
                self.delay(250)

                self.textbox(
                    self.elements.txb_search_for_a_page,
                    self.search_for_a_page,
                    is_check_readonly=False,
                )

                self.delay(250)

            self.click(self.elements.txb_search_for_a_page)

            self.click(self.elements.item)

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False
