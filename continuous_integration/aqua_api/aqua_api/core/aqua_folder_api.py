from continuous_integration.aqua_api.aqua_api.core.base_aqua_api import BaseAquaApi
from continuous_integration.aqua_api.aqua_api.config.aqua_api_config import AquaApiConfig

# --
# ...
# --

class AquaFolderApi(BaseAquaApi):
    def __init__(self, **kwargs) -> None:
        self.base_url = self.instance.config_dictionary.get("base_url")
        self.project_url = self.instance.config_dictionary.get("project_url")
        self.folder_url = self.instance.config_dictionary.get("folder_url")

        self.aqua_token_api = kwargs.get('aqua_token_api', None)
        self.aqua_access_token = self.aqua_token_api.aqua_access_token

        self.current_project_id = kwargs.get("current_project_id", None)
        
        self.current_folder_id = "0"
        self.current_folder_name = None

        # self.folder = {"name": "name", "parent_id": None}
        self.folder = {}
        
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
        self.get_top_folder()

    # --
    # ... folder
    # --

    def get_top_folder(self):
            
        try:

            self.aqua_token_api()
            self.aqua_access_token = self.aqua_token_api.aqua_access_token

            response = self.request(
                method="get",
                url=f"{self.base_url}{self.project_url}/{self.current_project_id}{self.folder_url}",
                headers={
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {self.aqua_access_token}",
                },
            )

            if response :
                self.current_folder_id = response[0].get("Id")
                self.current_folder_name = response[0].get("Name")

            else:

                self.current_folder_id = 0
                self.current_folder_name = ""

            print(f"top folder {self.current_folder_id}: {self.current_folder_name}")
            
        except Exception as exp:
            print(f"get_top_folder: {exp}")

    # --
    # ...
    # --
    
    def create_folder(self):

        try:

            self.aqua_token_api()
            self.aqua_access_token = self.aqua_token_api.aqua_access_token

            response = self.request(
                method="post",
                url=f"{self.base_url}{self.project_url}/{self.current_project_id}{self.folder_url}/{self.folder.get("parent_id")}/Subfolder",
                headers={
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {self.aqua_access_token}",
                },
                json={
                    "projectId": self.current_project_id,
                    "folderId": self.folder.get("parent_id"),
                    "Name": self.folder.get("name"),
                },
            )

            return response.get("Result")

        except Exception as exp:
            print(f"create_folder: {exp}")

    # --
    # ...
    # --
    
    def delete_folder(self):

        try:

            self.aqua_token_api()
            self.aqua_access_token = self.aqua_token_api.aqua_access_token

            response = self.request(
                method="delete",
                url=f"{self.base_url}{self.project_url}/{self.current_project_id}{self.folder_url}/{self.current_folder_id}",
                headers={
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {self.aqua_access_token}",
                },
                json={
                    "projectId": self.current_project_id,
                    "folderId": self.current_folder_id,
                    "deleteContent":True
                },
            )

            return response

        except Exception as exp:
            print(f"delete_folder: {exp}")
