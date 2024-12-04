from continuous_integration.aqua_api.aqua_api.core.base_aqua_api import BaseAquaApi
from continuous_integration.aqua_api.aqua_api.config.aqua_api_config import AquaApiConfig
from continuous_integration.aqua_api.aqua_api.core.aqua_tocken_api import AquaTockenApi
from continuous_integration.aqua_api.aqua_api.core.aqua_project_api import (
    AquaProjectApi,
)
from continuous_integration.aqua_api.aqua_api.core.aqua_folder_api import AquaFolderApi
from continuous_integration.aqua_api.aqua_api.core.aqua_subfolder_api import (
    AquaSubfolderApi,
)
from continuous_integration.aqua_api.aqua_api.core.aqua_testcase_api import (
    AquaTestcaseApi,
)
from toolboxs.decorators import singleton

# --
# ...
# --

@singleton
class AquaApi(BaseAquaApi):
    def __init__(self, **kwargs) -> None:
        self.access_token_api = AquaTockenApi()()
        self.project_api = AquaProjectApi(access_token=self.access_token_api)
        self.folder_api = AquaFolderApi(access_token=self.access_token_api)
        self.subfolder_api = AquaSubfolderApi(
            access_token=self.access_token_api,
            current_project_id=self.project_api,
            current_folder_id=self.folder_api,
        )
        self.testcase_api = AquaTestcaseApi(access_token=self.access_token_api)
        
        self.update_api()

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

    def update_api(self) -> str:
        self.project_api.access_token = self.access_token_api
        self.project_api()

        self.folder_api.access_token = self.access_token_api
        self.folder_api.current_project_id = self.project_api.current_project_id
        self.folder_api()

        self.subfolder_api.access_token = self.access_token_api
        self.subfolder_api.current_project_id = self.project_api.current_project_id
        self.subfolder_api.current_folder_id = self.folder_api.current_folder_id
        self.subfolder_api()

        self.testcase_api.access_token = self.access_token_api
        self.testcase_api.current_project_id = self.project_api.current_project_id
        self.testcase_api()