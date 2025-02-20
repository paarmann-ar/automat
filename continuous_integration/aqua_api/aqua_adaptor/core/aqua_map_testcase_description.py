from continuous_integration.aqua_api.aqua_adaptor.core.base_aqua_adapter import (
    BaseAquaAdapter,
)
from continuous_integration.aqua_api.aqua_adaptor.config.aqua_adapter_config import (
    AquaAdapterConfig,
)
import os
from toolboxs.decorators import singleton
from continuous_integration.aqua_api.aqua_adaptor.core.get_all_class_in_test_application import (
    GetAllClassInTestApplication,
)

# --
# ...
# --


@singleton
class AquaMapTestcaseDescription(BaseAquaAdapter):
    def __init__(self, get_all_class_in_test_application) -> None:
        self.default_testcase_description = self.instance.config_dictionary.get(
            "default_testcase_description"
        )

        self.get_all_class_in_test_application = get_all_class_in_test_application

        self.no_go_method = [
            "log",
            "info",
            "error",
            "stack",
            "wait_for_element_until_invisibile",
            "attributes_excel_file_address",
            "is_use_excel_attributs",
            "mail",
            "config_dictionary",
            "elements",
            "components",
            "action_simulator",
            "back",
            "chain",
            "checkbox",
            "clear",
            "click",
            "click_button",
            "combobox",
            "context_click",
            "conver_result_type",
            "current_element",
            "current_element_dir",
            "current_frame",
            "delay",
            "delete_all_cookies",
            "double_click",
            "driver",
            "wait_for_element_to_be_clickable",
            "forward",
            "get",
            "get_alle_cookies",
            "get_attribute_value",
            "get_config_dictionary",
            "get_property",
            "get_random",
            "instance",
            "instance_args",
            "is_class_wait_for_validation_failed",
            "is_displayed",
            "is_element_there",
            "is_enabled",
            "is_selected",
            "keys",
            "move_click",
            "quit",
            "restore_current_Frame",
            "save_current_Frame",
            "search_text_on_current_page_text",
            "send_keys",
            "text",
            "textbox",
            "wait_for_alert",
            "wait_for_element_visibility_by_text",
            "wait_for_visibility",
            "wait_for_not_uniqe_element_visibility",
            "__abstractmethods__",
            "__call__",
            "__class__",
            "__delattr__",
            "__dict__",
            "__dir__",
            "__doc__",
            "__eq__",
            "__format__",
            "__ge__",
            "__getattribute__",
            "__getstate__",
            "__gt__",
            "__hash__",
            "__init__",
            "__init_subclass__",
            "__le__",
            "__lt__",
            "__module__",
            "__ne__",
            "__new__",
            "__reduce__",
            "__reduce_ex__",
            "__repr__",
            "__setattr__",
            "__sizeof__",
            "__slots__",
            "__str__",
            "__subclasshook__",
            "__weakref__",
            "_abc_impl",
            "get_components",
            "get_elements",
            "setup",
            "teardown",
            "prepare",
            "tab_administration",
            "wait_for",
            "wait_for_element_until_visibile",
            "alert",
            "context_menu",
            "light_box",
            "aqua",
            "state",
        ]
        self.__setup()

        print(__class__.__name__, id(__class__))

    # --
    # ...
    # --

    def __setup(self): ...

    # --
    # ...
    # --

    @classmethod
    def get_config_dictionary(cls):
        return AquaAdapterConfig().instance.dictionary

    # --
    # ... methods
    # --

    def get_description_for_class(self, item):

        try:

            for class_ in self.get_all_class_in_test_application.classes:
                if class_.__module__ != item:
                    continue

                description = self.default_testcase_description

                for method in dir(class_):
                    if method.count("__") > 0 or method in self.no_go_method:
                        continue

                    description = f"{description} <p>{method}</p>\n\n"

                self.aqua_api.testcase_api.description = f"{description}<p>&nbsp;</p>\n"
                break

        except Exception as exp:
            print(f"map_tastcase_from_framework_to_aqua: {exp}")
