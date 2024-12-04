from continuous_integration.aqua_api.aqua_api.core.base_aqua_api import BaseAquaApi
from continuous_integration.aqua_api.aqua_api.config.aqua_api_config import (
    AquaApiConfig,
)

# --
# ...
# --


class AquaSubfolderApi(BaseAquaApi):
    def __init__(self, **kwargs) -> None:
        self.base_url = self.instance.config_dictionary.get("base_url")
        self.project_url = self.instance.config_dictionary.get("project_url")
        self.folder_url = self.instance.config_dictionary.get("folder_url")
        self.subfolder_path_url = self.instance.config_dictionary.get(
            "subfolder_path_url"
        )

        self.access_token = kwargs.get("access_token", None)
        self.current_project_id = kwargs.get("current_project_id", None)
        self.current_folder_id = kwargs.get("current_folder_id", None)

        self.subfolder_id = "?"
        self.current_subfolder = None
        self.subfolder_dictionary = {}

        self.parsed_subfolder = {}

        print(__class__.__name__, id(__class__))

    # --
    # ...
    # --

    @classmethod
    def get_config_dictionary(cls):
        return AquaApiConfig().instance.dictionary

    # --
    # ...
    # --

    def __call__(self, project_name=None, folder_name=None) -> str:
        self.update_subfolders()

    # --
    # ... subfolder
    # --

    def update_subfolders(self):

        try:

            response = self.request(
                method="get",
                url=f"{self.base_url}{self.project_url}/{self.current_project_id}{self.folder_url}/{self.current_folder_id}{self.subfolder_path_url}",
                headers={
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {self.access_token}",
                },
                json={
                    "projectId": self.current_project_id,
                    "folderId": 0,
                    # "recursive": True,
                },
                delay=0.1,
            )

            if not response:
                return

            for folder in response:
                id = folder.get("Id")
                name = folder.get("Name")
                parent_id = folder.get("ParentFolderId")

                self.subfolder_dictionary[id] = {
                    "name": name,
                    "parent_id": parent_id,
                }

            if len(response) > 0:
                for folder_id in self.subfolder_dictionary:
                    if folder_id not in self.parsed_subfolder:

                        print(
                            f"update folder dictionary {folder_id}: {self.subfolder_dictionary[folder_id]}"
                        )

                        self.current_folder_id = folder_id
                        self.parsed_subfolder[folder_id] = ""
                        self.update_subfolders()
            else:
                return

        except RuntimeError:
            pass
        except Exception as exp:
            print(f"update_subfolders: {exp}")
