from continuous_integration.aqua_api.aqua_api.core.base_aqua_api import BaseAquaApi
from continuous_integration.aqua_api.aqua_api.config.aqua_api_config import (
    AquaApiConfig,
)
import itertools
from continuous_integration.aqua_api.aqua_api.core.aqua_token_api import AquaTokenApi

# --
# ...
# --


class AquaTestExecuteApi(BaseAquaApi):
    def __init__(self, **kwargs) -> None:
        self.base_url = self.instance.config_dictionary.get("base_url")
        self.testexecute_url = self.instance.config_dictionary.get("testexecute_url")

        self.aqua_token_api = kwargs.get("aqua_token_api", None)
        self.aqua_access_token = self.aqua_token_api.aqua_access_token

        self.test_execute_id = 0
        self.test_execute_object = {}
        self.test_execute_dictionary = {}

        self.test_execute_teststep_object = []
        self.test_execute_teststep_index = 1
        self.test_execute_teststep_status = ""
        self.test_execute_teststep_result = True

        self.location = {}
        self.current_project_id = None
        self.folder_id = 0
        self.testcase_id = 0

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

    def __call__(self) -> str:
        pass

    # --
    # ...
    # --

    def create_test_execute_teststep_object(self):
        teststep_status = {
            "not_run": "NotRun",
            "pass": "Pass",
            "failed": "Failed",
            "blocked": "Blocked",
            "not_applicable": "NotApplicable",
        }

        self.test_execute_teststep_object.append(
            {
                "Index": self.test_execute_teststep_index,
                "Status": teststep_status.get(
                    self.test_execute_teststep_status, "Pass"
                ),
                "ActualResults": {
                    "PlainText": self.test_execute_teststep_result,
                },
            },
        )

    def clear_test_execute_teststep_object(self):
        self.test_execute_teststep_object.clear()

    # --
    # ...
    # --

    def create_test_execute_object(self):

        try:

            self.test_execute_object= {
                "TestCaseId": self.testcase_id,
                "Steps": self.test_execute_teststep_object
            }

        except Exception as exp:
            print(f"create_default_testcase_object: {str(exp)}")

    # --
    # ...
    # --

    def send_test_execute(self):

        try:

            self.aqua_token_api()
            self.aqua_access_token = self.aqua_token_api.aqua_access_token

            response = self.request(
                method="post",
                url=f"{self.base_url}{self.testexecute_url}",
                headers={
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {self.aqua_access_token}",
                },
                json=[self.test_execute_object],
            )

            self.test_execute_dictionary[response.get("Id")] = response

            print(
                "send test_execute id: ", response.get("Id"), response.get("Location")
            )

            return response.get("Id")

        except Exception as exp:
            print(f"create_testcases: {str(exp)}")
