from typing import Any
from drivers.core.base_driver import BaseDriver
import pywinauto
from pywinauto.application import Application
from pywinauto.keyboard import send_keys
from typing import Any
import CONSTS

"""

    * **class_name**     Elements with this window class
    * **class_name_re**  Elements whose class matches this regular expression
    * **parent**         Elements that are children of this
    * **process**        Elements running in this process
    * **title**          Elements with this text
    * **title_re**       Elements whose text matches this regular expression
    * **top_level_only** Top level elements only (default=**True**)
    * **visible_only**   Visible elements only (default=**True**)
    * **enabled_only**   Enabled elements only (default=False)
    * **best_match**     Elements with a title similar to this
    * **handle**         The handle of the element to return
    * **ctrl_index**     The index of the child element to return
    * **found_index**    The index of the filtered out child element to return
    * **predicate_func** A user provided hook for a custom element validation
    * **active_only**    Active elements only (default=False)
    * **control_id**     Elements with this control id
    * **control_type**   Elements with this control type (string; for UIAutomation elements)
    * **auto_id**        Elements with this automation id (for UIAutomation elements)
    * **framework_id**   Elements with this framework id (for UIAutomation elements)
    * **backend**        Back-end name to use while searching (default=None means current active backend)

"""

# --
# ...
# --


class Pywin(BaseDriver):
    def __init__(self) -> None:
        super().__init__()

        print(__class__.__name__, id(__class__))

    # --
    # ...
    # --

    def tuple_element_to_dictionary_element(self, element) -> dict:
        # element = dict((property_, value_) for property_, value_ in (element,))
        property_, value_ = element
        return {property_: value_}

    # --
    # ...
    # --

    def windriver_connect(self, element) -> bool:

        try:

            element = self.tuple_element_to_dictionary_element(element)

            while len(pywinauto.findwindows.find_elements(**element)) == 0:
                self.delay(220)

            application_window = pywinauto.findwindows.find_elements(**element)[0]
            application_window_handle = application_window.handle

            self.application = Application(allow_magic_lookup=False).connect(
                handle=application_window_handle, timeout=30000
            )
            self.delay(220)

            self.windriver_wait_for()

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False

    # --
    # ...
    # --

    def windriver_wait_for(self) -> bool:

        try:

            self.delay(220)

            self.application_dialog = self.application.top_window()

            self.application_dialog.wait("ready", timeout=30000)

            self.application_dialog.print_control_identifiers( filename=f"{CONSTS.ROOT_DIR}/temp_print_control_identifiers.txt")

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False

    # --
    # ...
    # --

    def windriver_sendkeys(self, element, keys) -> bool:

        try:

            _, element = element
            self.delay(220)

            self.application_dialog[element].click()
            self.delay(220)

            self.application_dialog[element].type_keys(keys, with_spaces=True)

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False

    # --
    # ...
    # --

    def windriver_click(self, element) -> bool:

        try:

            _, element = element
            self.delay(220)

            self.application_dialog[element].click()

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False

    # --
    # ...
    # --

    def windriver_click_button(self, element) -> bool:

        try:

            _, element = element
            self.application_dialog[element].click()

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False

    # --
    # ...
    # --

    def windriver_textbox(
        self, element, text, is_press_enter=False, is_back_space=False, is_set_focus=True
    ) -> bool:

        try:

            _, element = element
            # element = self.tuple_element_to_dictionary_element(element)

            self.delay(220)

            textbox = self.application_dialog[element]

            self.delay(220)

            if is_set_focus: 
                textbox.set_focus()

            if is_back_space:
                for i in range(len(textbox.texts()[0])):
                    # send_keys("{BACKSPACE 2}")
                    self.delay(100)
                    send_keys("{BACKSPACE}")

            self.delay(220)

            textbox.type_keys(text, with_spaces=True)

            if is_press_enter:
                send_keys("{ENTER}")

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False
