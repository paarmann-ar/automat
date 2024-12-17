from services.disk.file.file_manager import FileManager
from build.build_config.build_config import source_const_root_dir_in_local_dev_computer
import CONSTS

# --
# ...
# --

class RefactorConfigJson:
    def __init__(self, **kwargs):
        self.target_root_test_address = kwargs.get("target_root_test_address","")
        self.file = FileManager()
        self.file.address = CONSTS.CONFIG_JSON

    # --
    # ...
    # --

    def refactor_json_config(self):
        config_json = self.file.operation("r").replace(
            source_const_root_dir_in_local_dev_computer, self.target_root_test_address
        )
        self.file.operation("w", context=config_json)

        print("************************ refactor_json_config ************************\n\n")
        print(config_json)

    # --
    # ...
    # --

    def reset_json_config(self):
        config_json = self.file.operation("r").replace(
            self.target_root_test_address, source_const_root_dir_in_local_dev_computer
        )
        self.file.operation("w", context=config_json)
        
        print("************************ reset_json_config ************************\n\n")
        print(config_json)
