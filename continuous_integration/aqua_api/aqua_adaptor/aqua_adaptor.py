from continuous_integration.aqua_api.aqua_adaptor.core.base_aqua_adapter import (
    BaseAquaAdapter,
)
from continuous_integration.aqua_api.aqua_adaptor.config.aqua_adapter_config import (
    AquaAdapterConfig,
)
from continuous_integration.aqua_api.aqua_adaptor.core.aqua_map_folder import (
    AquaMapFolder,
)
from continuous_integration.aqua_api.aqua_adaptor.core.aqua_map_testcase import (
    AquaMapTestcase,
)
from toolboxs.decorators import singleton


# --
# ...
# --


@singleton
class AquaAdaptor(BaseAquaAdapter):
    def __init__(self) -> None:
        self.test_application_address = self.instance.config_dictionary.get(
            "test_application_address"
        )

        self.__setup()
        print(__class__.__name__, id(__class__))

    # --
    # ...
    # --

    def __setup(self):
        self.aqua_map_folder = AquaMapFolder()
        self.aqua_map_testcase = AquaMapTestcase()

    # --
    # ...
    # --

    @classmethod
    def get_config_dictionary(cls):
        return AquaAdapterConfig().instance.dictionary

    # --
    # ... methods
    # --

    def complate_maping_from_framework_to_aqua(self):

        try:

            self.aqua_api.update_api()
            self.aqua_map_folder.get_test_application_folder_tree()
            self.aqua_map_folder.delete_all_folders_in_aqua()
            self.aqua_map_folder.map_folder_from_framework_to_aqua()
            self.aqua_map_testcase.update_intersect_framework_aqua_folder_file_tree()
            self.aqua_map_testcase.map_tastcase_from_framework_to_aqua()

        except Exception as exp:
            print(f"complate_maping_folder_from_framework_to_aqua: {exp}")

    # --
    # ... methods
    # --

    def complate_maping_folder_from_framework_to_aqua(self):

        try:

            self.aqua_map_folder.get_test_application_folder_tree()
            self.aqua_map_testcase.delete_all_testcase_in_aqua()
            self.aqua_map_folder.delete_all_folders_in_aqua()
            self.aqua_map_folder.map_folder_from_framework_to_aqua()

        except Exception as exp:
            print(f"complate_maping_folder_from_framework_to_aqua: {exp}")

    # --
    # ...
    # --

    def complate_maping_testcase_from_framework_to_aqua(self):

        try:

            self.aqua_map_testcase.get_test_application_file_tree()
            self.aqua_map_testcase.delete_all_testcase_in_aqua()
            self.aqua_map_testcase.update_intersect_framework_aqua_folder_file_tree()
            self.aqua_map_testcase.map_tastcase_from_framework_to_aqua()

        except Exception as exp:
            print(f"complate_maping_testcase_from_framework_to_aqua: {exp}")


# aqua_adaptor = AquaAdaptor()
# aqua_adaptor.complate_maping_testcase_from_framework_to_aqua()
