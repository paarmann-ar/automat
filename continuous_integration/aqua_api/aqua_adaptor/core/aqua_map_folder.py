from continuous_integration.aqua_api.aqua_adaptor.core.base_aqua_adapter import (
    BaseAquaAdapter,
)
from continuous_integration.aqua_api.aqua_adaptor.config.aqua_adapter_config import (
    AquaAdapterConfig,
)
import os
from toolboxs.decorators import singleton

# --
# ...
# --


@singleton
class AquaMapFolder(BaseAquaAdapter):
    def __init__(self) -> None:
        self.test_application_address = self.instance.config_dictionary.get(
            "test_application_address"
        )

        self.test_application_folder_tree = {
            # "id": {
            #     "name": "None",
            #     "adress": "None",
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
        self.aqua_parent_folder_id = self.aqua_api.folder_api.current_folder_id

    # --
    # ...
    # --

    @classmethod
    def get_config_dictionary(cls):
        return AquaAdapterConfig().instance.dictionary

    # --
    # ... methods
    # --

    def get_test_application_folder_tree(self):

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

                self.test_application_folder_tree[
                    test_application_folder_id[folder_id]
                ] = {
                    "name": folder_name,
                    "adress": folder_adress,
                    "parent_id": test_application_folder_id[folder_parent],
                    "contains_files": files,
                    "contains_sub_folders": sub_folders,
                }

        except Exception as exp:
            print(f"get_test_application_folder_tree: {exp}")

    # --
    # ...
    # --

    def delete_all_folders_in_aqua(self):

        try:

            for id, name in self.aqua_api.subfolder_api.subfolder_dictionary.items():
                self.aqua_api.folder_api.current_folder_id = id
                self.aqua_api.folder_api.delete_folder()

                print(f"delete {id}, {name}")

            self.aqua_parent_folder_id = 0

        except Exception as exp:
            print(f"delete_all_folders_in_aqua: {exp}")

    # --
    # ...
    # --

    def map_folder_from_framework_to_aqua(self):

        try:

            created_folder = {}
            folder_index = 1

            while 1:

                id = folder_index

                if folder_index not in self.test_application_folder_tree:
                    folder_index += 1
                    continue

                folder = self.test_application_folder_tree[folder_index]

                if folder["parent_id"] == 0:
                    folder["parent_id"] = self.aqua_parent_folder_id

                aqua_folder_object = {
                    "name": folder["name"],
                    "parent_id": folder["parent_id"],
                }

                self.aqua_api.folder_api.folder["name"] = folder["name"]
                self.aqua_api.folder_api.folder["adress_in_framework"] = folder["adress"]
                self.aqua_api.folder_api.folder["parent_id"] = folder["parent_id"]

                if id in created_folder:
                    break

                new_folder_id = self.aqua_api.folder_api.create_folder()

                if new_folder_id is None:
                    break

                print(f"create {new_folder_id}: {aqua_folder_object}")

                self.update_testcase_elements_repository_json(folder, new_folder_id)

                created_folder[new_folder_id] = aqua_folder_object

                for id_, folder_data_ in self.test_application_folder_tree.items():
                    if folder_data_["parent_id"] == id:
                        self.test_application_folder_tree[id_] = {
                            "name": folder_data_["name"],
                            "parent_id": new_folder_id,
                            "adress": folder_data_["adress"],
                            "contains_files": folder_data_["contains_files"],
                            "contains_sub_folders": folder_data_[
                                "contains_sub_folders"
                            ],
                        }

                self.test_application_folder_tree[new_folder_id] = (
                    self.test_application_folder_tree[id]
                )
                del self.test_application_folder_tree[id]

                folder_index += 1

        except Exception as exp:
            print(f"map_folder_from_framework_to_aqua: {exp}")

    # --
    # ...
    # --

    def map_reset_folder_from_framework_to_aqua(self):

        try:

            self.get_test_application_folder_tree()
            self.delete_all_folders_in_aqua()
            self.map_folder_from_framework_to_aqua()

        except Exception as exp:
            print(f"map_reset_folder_from_framework_to_aqua: {exp}")

        # --
        # ...
        # --

    def update_testcase_elements_repository_json(
        self, test_application_folder_object, aqua_folder_id
    ):

        try:

            aqua_json_files = []

            for file in test_application_folder_object["contains_files"]:

                if file[-5:] == ".json":

                    if file[-10:] == "_aqua.json":
                        aqua_repository = file

                    else:
                        aqua_repository = f"{file[:-5]}_aqua.json"

                    if aqua_repository in aqua_json_files:
                        continue

                    self.json.operation(
                        address=f"{test_application_folder_object["adress"]}/{aqua_repository}",
                        context=f"""{{"aqua_folder": {{"id": {aqua_folder_id}}}}}""",
                        mode="append_or_replace",
                    )

                    aqua_json_files.append(aqua_repository)
                    continue

                elif file[-3:] == ".py":

                    if file[-10:] == "_aqua.json":
                        aqua_repository = file

                    else:
                        aqua_repository = f"{file[:-3]}_aqua.json"

                    if aqua_repository in aqua_json_files:
                        continue

                    self.json.operation(
                        address=f"{test_application_folder_object["adress"]}/{aqua_repository}",
                        context=f"""{{"aqua_folder": {{"id": {aqua_folder_id}}}}}""",
                        mode="append_or_replace",
                    )

                    aqua_json_files.append(aqua_repository)









            return True

        except Exception as exp:
            print(f"map_reset_folder_from_framework_to_aqua: {exp}")
            return False
