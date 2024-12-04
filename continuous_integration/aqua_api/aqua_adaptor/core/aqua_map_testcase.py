from continuous_integration.aqua_api.aqua_adaptor.core.base_aqua_adapter import (
    BaseAquaAdapter,
)
from continuous_integration.aqua_api.aqua_adaptor.config.aqua_adapter_config import (
    AquaAdapterConfig,
)
import os
import inspect
from toolboxs.decorators import singleton
from test_applications.d_365_dev.get_all_class_in_test_application import (
    GetAllClassInTestApplication,
)
from continuous_integration.aqua_api.aqua_adaptor.core.aqua_map_testcase_description import (
    AquaMapTestcaseDescription,
)

# --
# ...
# --


@singleton
class AquaMapTestcase(BaseAquaAdapter):
    def __init__(self) -> None:
        self.test_application_address = self.instance.config_dictionary.get(
            "test_application_address"
        )

        self.intersect_framework_aqua_folder_file_tree = {}
        self.test_application_folder_file_tree = {
            # "id": {
            #     "name": None,
            #     "adress": None,
            #     "files": None,
            #     "parent_id": None,
            # },
        }
        self.no_go_folder_name = [
            "__pycache__",
            "core",
            "base",
            "base_method",
            "base_methods",
            "config",
        ]

        self.__setup()

        print(__class__.__name__, id(__class__))

    # --
    # ...
    # --

    def __setup(self):
        self.get_all_class_in_test_application = GetAllClassInTestApplication()
        self.aqua_map_testcase_description = AquaMapTestcaseDescription(
            get_all_class_in_test_application=self.get_all_class_in_test_application
        )

        self.get_all_class_in_test_application.no_go_module = [
            "base_chapter",
            "base_user_story",
            "md365_config",
            "__init__",
            "base_method",
            "base_chapter_config",
            "import_attribute_in_excel_format",
            "export_attribute_in_excel_format",
            "base_method",
        ]

        self.current_folder_id = self.aqua_api.folder_api.current_folder_id

    # --
    # ...
    # --

    @classmethod
    def get_config_dictionary(cls):
        return AquaAdapterConfig().instance.dictionary

    # --
    # ... methods
    # --

    def get_test_application_file_tree(self):

        try:

            test_application_folder_id = {}

            is_root = True
            folder_index = 1

            for folder_adress, sub_folders, files in os.walk(
                self.test_application_address
            ):

                folder_adress = folder_adress.replace("\\", "/")

                folder_name = folder_adress.split("/")[-1]
                folder_id = folder_adress.replace("/", ">")
                folder_parent = ">".join(folder_id.split(">")[0:-1])

                if is_root:
                    is_root = False
                    test_application_folder_id[folder_parent] = 0

                test_application_folder_id[folder_id] = test_application_folder_id.get(
                    folder_id, folder_index
                )
                test_application_folder_id[folder_parent] = (
                    test_application_folder_id.get(folder_parent, None)
                )

                folder_index += 1

                if folder_name in self.no_go_folder_name:
                    continue

                self.test_application_folder_file_tree[
                    test_application_folder_id[folder_id]
                ] = {
                    "name": folder_name,
                    "adress": folder_adress,
                    "files": list(
                        map(
                            lambda x: x[:-3],
                            list(filter(lambda x: x[-3:] == ".py", files)),
                        )
                    ),
                    "parent_id": test_application_folder_id[folder_parent],
                }

        except Exception as exp:
            print(f"get_test_application_file_tree: {exp}")

    # --
    # ...
    # --

    def update_intersect_framework_aqua_folder_file_tree(self):

        try:

            framwork = self.test_application_folder_file_tree
            aqua = self.aqua_api.subfolder_api.subfolder_dictionary

            for k_0, v_0 in aqua.items():
                index = len(framwork)
                while 1:
                    for k_1, v_1 in framwork.items():
                        if (
                            v_0["parent_id"] == v_1["parent_id"]
                            and v_0["name"] == v_1["name"]
                        ):

                            for k_2, v_2 in framwork.items():
                                if v_2["parent_id"] == k_1:
                                    framwork[k_2]["parent_id"] = k_0

                            framwork[k_0] = (
                                self.intersect_framework_aqua_folder_file_tree[k_0]
                            ) = {
                                "name": v_0["name"],
                                "adress": v_1["adress"],
                                "files": v_1["files"],
                                "parent_id": v_0["parent_id"],
                            }

                            if k_0 != k_1:
                                del framwork[k_1]

                        index -= 1
                        if index == 0:
                            break
                    break

        except Exception as exp:
            print(f"update_intersect_framework_aqua_folder_file_tree: {exp}")

    # --
    # ...
    # --

    def delete_all_testcase_in_aqua(self):

        try:

            for id, data in self.aqua_api.testcase_api.testcases_dictionary.items():
                self.aqua_api.testcase_api.testcase_id = id
                self.aqua_api.testcase_api.delete_testcase()
                print(f"delete {id}, {data}")

        except Exception as exp:
            print(f"delete_all_testcase_in_aqua: {exp}")

    # --
    # ...
    # --

    def map_tastcase_from_framework_to_aqua(self):

        try:

            self.get_all_class_in_test_application.get_list_of_all_classes_in_unit_testcases()

            for (
                folder_id,
                folder_data,
            ) in self.intersect_framework_aqua_folder_file_tree.items():

                self.aqua_api.testcase_api.current_project_id = (
                    self.aqua_api.project_api.current_project_id
                )
                self.aqua_api.testcase_api.access_token = self.aqua_api.access_token_api
                self.aqua_api.testcase_api.folder_id = folder_id

                for item in folder_data["files"]:
                    self.aqua_api.testcase_api.testcase_name["Value"] = item

                    self.aqua_map_testcase_description.get_description_for_class(item)

                    self.aqua_map_teststep(item)

                    self.aqua_api.testcase_api.create_testcase_object()
                    self.aqua_api.testcase_api.create_testcases()

        except Exception as exp:
            print(f"map_tastcase_from_framework_to_aqua: {exp}")

    # --
    # ...
    # --

    def aqua_map_teststep(self, item):

        try:

            for class_ in self.get_all_class_in_test_application.classes:
                if class_.__module__ != item:
                    continue

                no_go_methode = [
                    "aqua",
                    "get_components",
                    "get_config_dictionary",
                    "get_elements",
                    "log",
                    "prepare",
                    "setup",
                    "state",
                    "teardown",
                    "wait_for",
                ]
                class_dir_filtered__ = list(
                    filter(lambda x: x[:2] != "__", dir(class_))
                )
                class_dir_filtered_ = list(
                    filter(lambda x: x[:1] != "_", class_dir_filtered__)
                )

                aqua_candidate_methode = list(
                    filter(lambda x: x not in no_go_methode, class_dir_filtered_)
                )






                setattr(class_, "is_aqua", True)
                instance = class_()

                for methode in aqua_candidate_methode:
                    
                    getattr(instance, methode)()

                    for test_step in instance.aqua_source:
                        self.aqua_api.testcase_api.test_step_name = test_step

                class_.is_aqua = False

                self.aqua_api.testcase_api.create_test_steps_object()

                break

        except Exception as exp:
            print(f"aqua_map_teststep: {exp}")