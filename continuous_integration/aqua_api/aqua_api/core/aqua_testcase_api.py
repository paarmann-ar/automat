from continuous_integration.aqua_api.aqua_api.core.base_aqua_api import BaseAquaApi
from continuous_integration.aqua_api.aqua_api.config.aqua_api_config import (
    AquaApiConfig,
)
import itertools


# --
# ...
# --


class AquaTestcaseApi(BaseAquaApi):
    def __init__(self, **kwargs) -> None:
        self.base_url = self.instance.config_dictionary.get("base_url")
        self.testcase_url = self.instance.config_dictionary.get("testcase_url")

        self.access_token = None
        self.testcase_id = 0
        self.testcase_object = {}
        self.testcases_dictionary = {}
        self.parsed_testcase = {}

        self.location = {}
        self.current_project_id = None
        self.folder_id = 0

        self.details = []
        self.testcase_name = {
            "FieldId": "Name",
            "Value": "",
        }
        self.automatisiert = {
            # 02 Automatisiert?
            "FieldId": "CustomInt00",
            "Value": 10465,
        }
        self.status = {
            # 21 Status
            "FieldId": "Status",
            "Value": 10440,
        }
        self.test_level = {
            # 22 TestLevel
            "FieldId": "TestLevel",
            "Value": 10464,
        }

        self.description = "Testcase description"

        self.test_data = {}
        self.test_step_index = itertools.count(1)
        self.test_step_name = "test_step_name"
        self.test_step_description = {
            "Html": "Teststep description",
        }
        self.test_step_expexted_result = {
            "PlainText": "Teststep expexted result",
        }

        self.test_steps_object = []

        print(__class__.__name__, id(__class__))

    # --
    # ...
    # --

    def description_object(self):
        return {
            "Html": self.description,
        }

    # --
    # ...
    # --

    def create_test_steps_object(self):
        test_step_object = self.test_step_object()
        self.test_steps_object.append(test_step_object)

    def test_step_object(self):
        test_step_index = next(self.test_step_index)
        return {
            "Index": test_step_index,
            "Name": self.test_step_name,
            "Description": self.test_step_description,
            "ExpectedResult": self.test_step_expexted_result,
            "StepType": "Step",
        }

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
        self.update_testcases()

    # --
    # ...
    # --

    def create_testcase_object(self):

        try:

            self.testcase_object = {
                "Location": {
                    "ProjectId": self.current_project_id,
                    "FolderId": self.folder_id,
                },
                "Details": [
                    self.testcase_name,
                    self.automatisiert,
                    self.status,
                    self.test_level,
                ],
                "Attachments": None,
                "Description": self.description_object(),
                "TestSteps": self.test_steps_object,
                "TestData": None,
            }

        except Exception as exp:
            print(f"create_default_testcase_object: {str(exp)}")

    # --
    # ...
    # --

    def update_testcases(self):

        try:

            response = self.request(
                method="get",
                url=f"{self.base_url}{self.testcase_url}/ItemList",
                headers={
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {self.access_token}",
                },
                params={
                    "projectId": self.current_project_id,
                },
                delay=0.1,
            )

            if not response:
                return

            for testcase in response["Items"]:
                id = testcase.get("Id")
                name = testcase.get("Name")
                formatted_id = testcase.get("FormattedId")

                self.testcases_dictionary[id] = {
                    "name": name,
                    "formatted_id": formatted_id,
                }

            print(f"testcase id: {self.testcases_dictionary}")

        except Exception as exp:
            print(f"update_testcases: {str(exp)}")

    # --
    # ...
    # --

    def create_testcases(self):

        try:

            response = self.request(
                method="post",
                url=f"{self.base_url}{self.testcase_url}",
                headers={
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {self.access_token}",
                },
                json=self.testcase_object,
            )

            self.testcases_dictionary[response.get("Id")] = response

            print("created testcase id: ", response.get("Id"), response.get("Location"))

        except Exception as exp:
            print(f"create_testcases: {str(exp)}")

    # --
    # ...
    # --

    def delete_testcase(self):

        try:

            response = self.request(
                method="delete",
                url=f"{self.base_url}{self.testcase_url}/{self.testcase_id}",
                headers={
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {self.access_token}",
                },
            )

        except Exception as exp:
            print(f"delete_testcase: {str(exp)}")
