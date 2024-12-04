from components.core.object_provider import ObjectProvider
from components.core.base_component import BaseComponent
from selenium.webdriver.common.keys import Keys

# --
# ...
# --


class ComboboxComponents(BaseComponent):
    def __init__(self) -> None:
        self.elements = self.get_elements()

        print(__class__.__name__, id(__class__))

    # --
    # ...
    # --

    def get_elements(self) -> str:
        return ObjectProvider()(__file__.replace(".py", ".json ", -1).replace("\\", "/").replace(" c", ""))

    # --
    # ... combobox
    # --

    def combobox_dropdown(
        self,
        element,
        is_click_befor=True,
        is_clear=True,
    ):

        try:

            self.wait_for_visibility(element)

            while not self.get_attribute_value(self.elements, "aria-expanded"):
                if is_click_befor:
                    if self.instance.current_element_dir("click"):
                        self.double_click(self.instance.current_element)


                if is_clear:
                    if self.instance.current_element_dir("clear"):
                        self.instance.current_element.clear()
                        self.delay(150)

                if self.instance.current_element_dir("send_keys"):
                    self.instance.current_element.send_keys(Keys.ALT + Keys.ARROW_DOWN)
                    self.delay(150)

                    return True
                
                self.delay(220)

            raise Exception("method not allowd")

        except Exception as exp:
            print(repr(exp))
            return False

    def combobox_search_text(
        self, element, text_to_search="", is_click_befor=True, is_clear=True
    ):

        try:

            self.wait_for_visibility(element)

            if is_click_befor:
                if self.instance.current_element_dir("click"):
                    self.instance.current_element.click()

            if is_clear:
                if self.instance.current_element_dir("clear"):
                    self.instance.current_element.clear()
                    self.delay(150)

            if self.instance.current_element_dir("send_keys"):
                self.instance.current_element.send_keys(text_to_search)
                self.delay(150)

                return True

            raise Exception("method not allowd")

        except Exception as exp:
            print(repr(exp))
            return False

    # --
    # ...  cmb_type_1
    # --

    def cmb_type_1_select_and_search_item(self, cmb_type_1, search_text) -> bool:

        try:

            self.combobox_dropdown(cmb_type_1)
            self.combobox_search_text(
                self.elements.cmb_type_1_txb_search_text, search_text
            )
            self.double_click(self.elements.cmb_type_1_btn_select)

            self.delay(220)

            return True

        except Exception as exp:
            print(repr(exp))
            return False

    # --
    # ...  cmb_type_2
    # --

    def cmb_type_2_select_and_sort_item(self, cmb_type_2, select_item="") -> bool:

        try:

            self.combobox_dropdown(cmb_type_2,is_clear=False)

            self.instance.current_element.send_keys(select_item)

            self.double_click(self.elements.cmb_type_2_btn_select)

            self.delay(220)

            return True

        except Exception as exp:
            print(repr(exp))
            return False
        
    def cmb_type_2(self, cmb_type_2, select_item="") -> bool:

        try:

            self.combobox_dropdown(cmb_type_2)

            self.instance.current_element.send_keys(select_item)
            self.instance.current_element.send_keys(Keys.ENTER)

            self.delay(220)

            return True

        except Exception as exp:
            print(repr(exp))
            return False

    # --
    # ...  cmb_type_3
    # --

    def cmb_type_3_radio_button_and_select(self, cmb_type_3, radio_button_item="") -> bool:

        try:

            self.combobox_dropdown(cmb_type_3)

            self.delay(1500)

            radio_button_item = f"//input[@value='{radio_button_item}']"

            self.delay(220)
            self.double_click(('item',{'xpath': radio_button_item}))
            
            self.delay(1500)
            self.double_click(self.elements.cmb_type_3_btn_select)

            self.delay(220)

            return True

        except Exception as exp:
            print(repr(exp))
            return False