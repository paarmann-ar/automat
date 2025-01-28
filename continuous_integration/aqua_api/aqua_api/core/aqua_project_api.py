from continuous_integration.aqua_api.aqua_api.core.base_aqua_api import BaseAquaApi
from continuous_integration.aqua_api.aqua_api.config.aqua_api_config import AquaApiConfig
from continuous_integration.aqua_api.aqua_api.core.aqua_token_api import AquaTokenApi
# --
# ...
# --


class AquaProjectApi(BaseAquaApi):
    def __init__(self, **kwargs) -> None:
        self.base_url = self.instance.config_dictionary.get("base_url")
        self.project_url = self.instance.config_dictionary.get("project_url")
        self.default_project_name = self.instance.config_dictionary.get(
            "default_project_name"
        )

        self.aqua_token_api = kwargs.get('aqua_token_api', None)
        self.aqua_access_token = self.aqua_token_api.aqua_access_token

        self.current_project_id = "?"
        self.current_project_name = None
        
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

    def __call__(self, project_name=None) -> str:
        self.update_projects()

    # --
    # ...
    # --

    def update_projects(self):

        try:
            
            self.aqua_token_api()
            self.aqua_access_token = self.aqua_token_api.aqua_access_token
            
            response = self.request(
                method="get",
                url=f"{self.base_url}{self.project_url}",
                headers={
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {self.aqua_access_token}",
                },
            )

            self.current_project_id = response[0].get("Id")
            self.current_project_name = response[0].get("Name")

            print(f"project {self.current_project_id}: {self.current_project_name}")

        except Exception as exp:
            print(f"update_projects: {exp}")

    # --
    # ...
    # --

    def update_project_name(self, project_name=None):

        try:

            if not project_name:
                project_name = self.current_project_name

            self.aqua_token_api()
            self.aqua_access_token = self.aqua_token_api.aqua_access_token

            response = self.request(
                method="patch",
                url=f"{self.base_url}{self.project_url}/{self.current_project_id}",
                headers={
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {self.aqua_access_token}",
                },
                json={
                    "PatchOperation": "Rename",
                    "NewName": project_name,
                },
            )

            print(response)

        except Exception as exp:
            print(f"update_project_name: {exp}")
