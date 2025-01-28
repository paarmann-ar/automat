import importlib.util
import glob
import importlib
import inspect
import CONSTS
import re

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
                f"{CONSTS.ROOT_DIR}/test_applications/d_365/chapters/finance_chapter/unit_testcases//**/*.py",
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

                class_member = []
                action_string_list = []

                for method in dir(class_attribute):
                    if (
                        method[:2] == "__"
                        or method[:1] == "_"
                        or method in self.no_go_method
                    ):
                        continue

                    class_member.append(method)
                    module_source = inspect.getsource(module)

                    # parse module source for get setps
                    # inja 2 bar dare ejra mikoneh
                    action_string_list.append(
                        self.pars_step_context(module_source, method)
                    )
                    
                self.classes[i] = {
                    "class_name": class_name,
                    "class_attribute": class_attribute,
                    "class_member": class_member,
                    "class_member_step": action_string_list,
                    "class_source": module_source,
                    "class_json_adress": class_json_adress,
                }

                i += 1

            return True

        except Exception as exp:
            print(f"{repr(exp)},{str(exp)}")
            return False

    # --
    # ...
    # --

    def pars_step_context(self, module_source, method):

        try:

            list_methodes_in_module = module_source.split("def ")
            list_methodes_in_module = list(filter(lambda x: x[1:2] != "_", list_methodes_in_module))

            for method_source_text in list_methodes_in_module:
                if f"def {method_source_text}".find(f"def {method}") == 0:
                    break

            method_source_enumerate = list(
                enumerate(
                    list(
                        filter(
                            lambda x: x != "",
                            [l.strip() for l in method_source_text.split("\n")],
                        )
                    )
                )
            )

            actions_array = [
                "click",
                "click_button",
                "textbox",
                "combobox",
                "checkbox",
            ]

            action_string = []

            try:

                for action in actions_array:
                    line = iter(method_source_enumerate)

                    index = 1
                    while len(method_source_enumerate) >= index:
                        _, context = next(line)

                        if context.find(f"self.{action}(") >= 0:
                            action_string.append((_, context))
                            action_string_ = [(_, context)]

                            if context[-2:] == "):":
                                index += 1
                                continue

                            if context[-1:] != ")":
                                _ = next(iter(line))
                                index += 1

                                while _[1] != ")":
                                    action_string_.append(_)
                                    _ = next(iter(line))
                                    index += 1

                                action_string_.append(_)
                                line_number = action_string_[0][0]
                                action_string_ = [y for x, y in action_string_]
                                action_string_ = line_number, "".join(action_string_)

                                action_string.pop()
                                action_string.append(action_string_)
                        index += 1

            except StopIteration as exp:
                print(f"{repr(exp)},{str(exp)}")

            finally:
                ...

            action_string_ = []
            for line_number, contain in action_string:
                splitet_contain = contain.split(",")
                act_on_element = splitet_contain[0]

                set_on_element = "n/a"
                if len(splitet_contain) > 1:
                    set_on_element = contain.split(",")[1]

                act_on_element = act_on_element.replace("self.click(", "click on ")
                act_on_element = act_on_element.replace(
                    "self.click_button(", "click on button "
                )
                act_on_element = act_on_element.replace(
                    "self.textbox(", "write text on field "
                )
                act_on_element = act_on_element.replace(
                    "self.checkbox(", "tick checkbox "
                )
                act_on_element = act_on_element.replace("self.elements.", "")
                act_on_element = act_on_element.replace(")", "")

                set_on_element = set_on_element.replace("self.", "")
                set_on_element = set_on_element.replace("(", "")
                set_on_element = set_on_element.replace(")", "")

                action_string_.append((line_number, act_on_element, set_on_element))

            action_string_.sort(key=lambda x: x[0])
            action_string = action_string_

            # add step number
            action_string = list(enumerate([(y, z) for x, y, z in action_string]))

            action_string_list = [
                {
                    "name": f"step {x}",
                    "description": f"{y[0]}",
                    "expected_result": f"{y[1]}",
                }
                for x, y in action_string
            ]

            return action_string_list

        except Exception as exp:
            print(f"{repr(exp)},{str(exp)}")
            return False
