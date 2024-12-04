from typing import Any
from test_applications.d_365.core.base import Base
from selenium.webdriver.common.keys import Keys


class StandardView(Base):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.filter_row_text = None
        self.filter_header_text=None
        self.filter_row_search_item = None
        self.search_item_text = None
        self.search_item = None

    # --
    # ... select_item
    # --

    def select_item(self, **kwargs) -> bool:

        try:

            is_select_search_field = kwargs.get("is_select_search_field", True)
            is_click_on_selected = kwargs.get("is_click_on_selected", True)
            is_filter_row = kwargs.get("is_filter_row", False)

            self.blocking_message()

            self.textbox(
                self.elements.txb_search, self.search_item, is_check_readonly=False
            )

            self.click(self.elements.txb_search)

            type_, value_ = self.elements.itm
            search_item, _ = self.search_item

            if is_select_search_field:
                self.select_search_field(search_item)

            if is_filter_row:
                self.filter_row()

            self.elements.item = (type_, value_.replace("?", search_item))

            self.delay(1000)

            if is_click_on_selected:
                item_to_search = (_, f'title="{search_item}')
                if self.search_text_on_current_page_text(item_to_search):
                    self.click(self.elements.item)                   
                    return True

                item_to_search = (_, f'value="{search_item}"')
                if self.search_text_on_current_page_text(item_to_search):
                    self.click(self.elements.item)
                    return True
            else:
                return True

            return False

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False

    # --
    # ... select_search_field
    # --

    def select_search_field(self, search_item_value) -> bool:

        try:

            self.delay(750)

            elements_in_search_listbox_F = (
                "xpath",
                """//li[contains(@id,"QuickFilter") and contains(@id,"listbox_item")]/span[1]""",
            )

            elements_in_search_listbox_f = (
                "xpath",
                """//li[contains(@id,"Quickfilter") and contains(@id,"listbox_item")]/span[1]""",
            )
            
            if self.wait_for_not_uniqe_element_visibility(elements_in_search_listbox_F):
                elements_in_search_listbox = self.driver.find_elements(
                    *elements_in_search_listbox_F
                )

            else:
                self.wait_for_not_uniqe_element_visibility(elements_in_search_listbox_f)

                elements_in_search_listbox = self.driver.find_elements(
                    *elements_in_search_listbox_f
                )

            self.delay(150)

            for element_in_search_listbox in elements_in_search_listbox:
                element_in_search_listbox_text = element_in_search_listbox.text
                if element_in_search_listbox_text == self.search_item_text:
                    print(
                        f"\n\n************\nclick on filter -> {element_in_search_listbox_text} : {search_item_value}\n************\n\n"
                    )
                    element_in_search_listbox.click()
                    break

                self.delay(150)

            self.keys(
                self.elements.txb_search,
                keys=(Keys.ENTER, True),
                is_check_key_there=False,
            )

            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False

    # --
    # ... filter
    # --

    def filter_row(self) -> bool:

        try:

            btn_header_item = ("xpath", """//div[contains(@id,"_header") and contains(@id,"?")]""".replace("?", self.filter_header_text))
            txb_filter_row = ("xpath", """//input[contains(@id,"__FilterField_") and contains(@id,"?")]""".replace("?", self.filter_row_text))
            btn_filter_row_apply =  ("xpath", """//button[contains(@id,"ApplyFilters")and contains(@id,"?")]""".replace("?", self.filter_header_text))
            btn_filter_row_clear =  ("xpath", """//button[contains(@id,"ResetFilters")and contains(@id,"?")]""".replace("?", self.filter_header_text))


            self.double_click(btn_header_item)
            self.delay(150)

            while not self.is_element_there(btn_filter_row_clear):
                self.double_click(btn_header_item)
                self.delay(150)

            self.click_button(btn_filter_row_clear)
            self.delay(150)

            self.double_click(btn_header_item)
            self.delay(150)

            self.textbox(txb_filter_row, (self.filter_row_search_item, True))
            self.delay(150)

            self.click_button(btn_filter_row_apply)

            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False
