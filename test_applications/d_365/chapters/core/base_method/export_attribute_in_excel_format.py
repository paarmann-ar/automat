from services.disk.service_disk_provider import ServiceDiskProvider
from test_applications.d_365.chapters.core.base_method.base_method import BaseMethod
import inspect

# --
# ...
# --


class ExportAttributeInExcelFormat(BaseMethod):
    def __init__(self, **kwargs) -> None:
        self.class_ = kwargs.get("class_", None)
        self.is_create_excel_file = kwargs.get("is_create_excel_file", True)

        self.workbook = self.instance.workbook
        self.no_go_attributs = [
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
        ]

    # --
    # ...
    # --

    def start(self):

        self.excel = ServiceDiskProvider().excel

        class_dict = {method: "-" for method in dir(self.class_) if method[0:1] != "_"}
        class_vars = vars(self.class_.instance)
        class_dict.update(class_vars)

        from test_applications.d_365.chapters.core.base_chapter import BaseChapter

        class_dict = {
            k: v
            for k, v in class_dict.items()
            if k not in self.no_go_attributs and not isinstance(v, BaseChapter)
        }

        attributs = []
        attribut = []
        i = 1
        j = 0

        for key, value in class_dict.items():

            value_ = list(value)[0] if type(value) is tuple else value
            value__ = list(value)[1] if type(value) is tuple else value
            if not isinstance(value__, bool):
                value__ = ""

            attribut.append({(i, j): key})
            attribut.append({(i, j + 1): value_})
            attribut.append({(i, j + 2): value__})
            attributs.append(attribut)
            attribut = []
            i += 1

        # set header
        attributs.insert(0, [{(0, 0): "Set name"}, {(0, 1): self.class_.__name__}, {(0, 2): "is_active"}])
        self.workbook.append({f"{self.class_.__qualname__}"[:30]: attributs})

        # add more sheet to workbook
        if self.is_create_excel_file:
            self.excel.workbook = self.workbook
            self.excel.operation(file_name=f"/{self.class_.__name__}.xlsx")

        print(self.class_.__name__)
        return self.workbook
