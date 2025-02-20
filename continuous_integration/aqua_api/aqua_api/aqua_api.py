from continuous_integration.aqua_api.aqua_api.core.base_aqua_api import BaseAquaApi
from continuous_integration.aqua_api.aqua_api.config.aqua_api_config import (
    AquaApiConfig,
)
from continuous_integration.aqua_api.aqua_api.core.aqua_token_api import AquaTokenApi
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
from continuous_integration.aqua_api.aqua_api.core.aqua_test_execute_api import AquaTestExecuteApi

# --
# ...
# --


@singleton
class AquaApi(BaseAquaApi):
    def __init__(self, **kwargs) -> None:
        self.aqua_token_api = AquaTokenApi()
        self.aqua_token_api()

        self.project_api = AquaProjectApi(aqua_token_api=self.aqua_token_api)
        self.project_api.update_projects()

        self.folder_api = AquaFolderApi(aqua_token_api=self.aqua_token_api)
        self.subfolder_api = AquaSubfolderApi(
            current_project_id=self.project_api,
            current_folder_id=self.folder_api,
            aqua_token_api=self.aqua_token_api,
        )
        self.testcase_api = AquaTestcaseApi(aqua_token_api=self.aqua_token_api)
        self.test_execute_api = AquaTestExecuteApi(aqua_token_api=self.aqua_token_api)

        # self.update_api()

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

    def refresh_tocken(self) -> str:
        self.aqua_token_api.get_token()

    # --
    # ...
    # --

    def update_api(self, update_module=None) -> str:

        update_item = {
            "project": self.update_project,
            "folder": self.update_folder,
            "testcase": self.update_testcase,
            "testexecute": self.update_test_execute,
        }

        update_item.get(update_module, self.update_test_execute)()

        # self.project_api()

        # self.folder_api.current_project_id = self.project_api.current_project_id
        # self.folder_api()

        # self.subfolder_api.current_project_id = self.project_api.current_project_id
        # self.subfolder_api.current_folder_id = self.folder_api.current_folder_id
        # self.subfolder_api()

        # self.testcase_api.current_project_id = self.project_api.current_project_id
        # self.testcase_api()

        # self.execute_apo.current_project_id = self.project_api.current_project_id
        # self.execute_apo()

    def update_project(self):
        self.project_api()
        self.folder_api.current_project_id = self.project_api.current_project_id
        self.subfolder_api.current_project_id = self.project_api.current_project_id
        self.testcase_api.current_project_id = self.project_api.current_project_id
        self.test_execute_api.current_project_id = self.project_api.current_project_id

    def update_folder(self):
        self.update_project()
        self.folder_api()

    def update_subfolder(self):
        self.update_folder()
        self.subfolder_api.current_folder_id = self.folder_api.current_folder_id
        self.subfolder_api()

    def update_testcase(self):
        self.update_subfolder()
        self.testcase_api()

    def update_test_execute(self):
        self.update_testcase()
        self.test_execute_api()