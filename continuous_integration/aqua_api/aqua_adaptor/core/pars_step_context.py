class ParsStepContext:
    def __init__(self) -> None:
        return

    # --
    # ...
    # --

    def pars_step_context(self, module_source, method):

        try:

            list_methodes_in_module = module_source.split("def ")

            prepare_method = list(
                filter(lambda x: x[0:9] == "__prepare", list_methodes_in_module)
            )

            if len(prepare_method) > 0:
                attribute_dict = {}
                prepare_method_source_enumerate = list(
                    enumerate(
                        list(
                            filter(
                                lambda x: x != "",
                                [l.strip() for l in prepare_method[0].split("\n")],
                            )
                        )
                    )
                )

                for _, line in prepare_method_source_enumerate:
                    if line.find(", True)") > 0 or line.find(", False)") > 0:
                        attribute_line = line.split("=")
                        attribute_value = attribute_line[1].replace(", True)", "")
                        attribute_value = attribute_value.replace(", False)", "")
                        attribute_value = attribute_value.replace("(", "")
                        attribute_value = attribute_value.replace(",", "")
                        attribute_value = attribute_value.replace('"', "")
                        attribute_value = attribute_value.replace("'", "")
                        attribute_dict.update(
                            {
                                attribute_line[0]: attribute_value,
                            }
                        )

            list_methodes_in_module = list(
                filter(lambda x: x[1:2] != "_", list_methodes_in_module)
            )

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

            action_string = self.pars_on_actions_on_element_list(
                method_source_enumerate
            )
            action_string.extend(
                self.pars_on_external_common_methods_list(method_source_enumerate)
            )
            action_string.extend(
                self.pars_on_external_methods_list(method_source_enumerate)
            )

            action_string_ = []
            for line_number, contain in action_string:
                splitet_contain = contain.split(",")
                act_on_element = splitet_contain[0]

                set_on_element = None
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
                act_on_element = act_on_element.replace(
                    "self.select_item(**kwargs)", "select item on listview "
                )

                act_on_element = act_on_element.replace(
                    "self.toolbars.change_mandant()", "change mandant <Company>"
                )
                act_on_element = act_on_element.replace(
                    "self.toolbars.set_text_in_search_for_a_page()",
                    "Write text on search for a page ",
                )

                act_on_element = act_on_element.replace("self.elements.", "")
                act_on_element = act_on_element.replace(")", "")

                element_type_array = [
                    "btn_",
                    "txb_",
                    "cmb_",
                    "chk_",
                ]

                for element_type in element_type_array:
                    act_on_element = act_on_element.replace(element_type, " ")

                act_on_element = act_on_element.replace("lbl_", "lable ")
                act_on_element = act_on_element.replace("_", " ")

                if set_on_element:
                    set_on_element = set_on_element.replace("self.", "")
                    set_on_element = set_on_element.replace("(", "")
                    set_on_element = set_on_element.replace(")", "")
                    set_on_element = set_on_element.replace(" ", "")
                    set_on_element = attribute_dict.get(set_on_element, "n/a")

                else:
                    set_on_element = "True"

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

    # --
    # ...
    # --

    def pars_on_actions_on_element_list(self, method_source_enumerate):

        try:

            action_string = []

            actions_on_element_list = [
                "click",
                "click_button",
                "textbox",
                "combobox",
                "checkbox",
                "select_item",
            ]

            for action in actions_on_element_list:
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

            return action_string

        except StopIteration as exp:
            print(f"{repr(exp)},{str(exp)}")

    # --
    # ...
    # --

    def pars_on_external_common_methods_list(self, method_source_enumerate):

        try:

            action_string = []

            external_common_methods_list = [
                "toolbars.change_mandant",
                "toolbars.set_text_in_search_for_a_page",
            ]

            for action in external_common_methods_list:
                line = iter(method_source_enumerate)
                index = 1
                while len(method_source_enumerate) >= index:
                    _, context = next(line)

                    if context.find(f"self.{action}()") >= 0:
                        action_string.append((_, context))

                    index += 1

            return action_string

        except StopIteration as exp:
            print(f"{repr(exp)},{str(exp)}")

    # --
    # ...
    # --

    def pars_on_external_methods_list(self, method_source_enumerate):

        try:

            action_string = []

            external_common_methods_list = [
                "toolbars.mandant",
                "toolbars.search_for_a_page",
                "step",
            ]

            for action in external_common_methods_list:
                line = iter(method_source_enumerate)
                index = 1
                while len(method_source_enumerate) >= index:
                    _, context = next(line)

                    if context.find(f"{action}") >= 0:
                        context = context.split("=")
                        context = context[1].replace("\"", "")
                        context = "run testcase " + context
                        action_string.append((_, context))

                    index += 1

            return action_string

        except StopIteration as exp:
            print(f"{repr(exp)},{str(exp)}")
