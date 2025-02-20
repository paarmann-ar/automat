import importlib.util
import glob
import importlib
import inspect
import CONSTS
from continuous_integration.aqua_api.aqua_adaptor.core.pars_step_context import ParsStepContext
# --
# ...
# --


class GetAllClassInTestApplication:
    def __init__(self) -> None:
        self.classes = {}
        self.no_go_module = ["Base"]
        self.no_go_method = [
            "aqua",
            "get_components",
            "get_config_dictionary",
            "get_elements",
            "handel_tipbox",
            "log",
            "prepare",
            "setup",
            "state",
            "teardown",
            "wait_for",
            "select_search_field",
            "select_item",
            "expand_tab",
            "filter_row",
            "select",
        ]

    # --
    # ...
    # --

    def get_list_of_all_classes_in_unit_testcases(self):

        try:

            i = 0

            for file in glob.glob(
                f"{CONSTS.ROOT_DIR}/test_applications/d_365/chapters/finance_chapter//**/*.py",
                recursive=True,
            ):
                class_json_adress = f"{file[:-3]}_aqua.json".replace("\\", "/")
                name = file.split("\\")[-1][:-3]

                if name in self.no_go_module:
                    continue

                spec = importlib.util.spec_from_file_location(name, file)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)

                class_name = "".join([word.capitalize() for word in name.split("_")])

                class_attribute = getattr(module, class_name)

                action_string_list = []

                for method in dir(class_attribute):
                    if (
                        method[:2] == "__"
                        or method[:1] == "_"
                        or method in self.no_go_method
                    ):
                        continue

                    module_source = inspect.getsource(module)
                    if class_name == "FreeTextInvoiceForIntercompany":
                        pass
                    # parse module source for get setps
                    # inja 2 bar dare ejra mikoneh
                    pars_step_action_string_list = ParsStepContext().pars_step_context(module_source, method)

                    if len(pars_step_action_string_list) > 0:
                        action_string_list.append(
                            {
                                "method_name": method,
                                "method_steps": pars_step_action_string_list,
                            }
                        )

                self.classes[i] = {
                    "class_name": class_name,
                    "class_attribute": class_attribute,
                    "class_member": action_string_list,
                    "class_member_step": action_string_list,
                    "class_source": module_source,
                    "class_json_adress": class_json_adress,
                }

                i += 1

            return True

        except Exception as exp:
            print(f"{repr(exp)},{str(exp)}")
            return False