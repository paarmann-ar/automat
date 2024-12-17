from enum import Enum
from toolboxs.toolbox import Toolbox

# --
# ... Global Config
# --

ROOT_DIR = Toolbox.get_root_path().replace("\\", "/")
CONFIG_JSON = ROOT_DIR + "/config_dictionary/config.json"
EXTERNAL_FILES = ROOT_DIR + "/.external_files"

# --
# ... MD_365 Config
# --

class MD_365(Enum):
    TESTCASES_DIR = ROOT_DIR + "/MD_365/md_365/testcases"
    TESTKEYS_DIR = ROOT_DIR + "/MD_365/md_365/testcases/testkeys"
    TESTKEY_OBJECTS_DIR = ROOT_DIR + "/MD_365/md_365/testcases/testkey_objects"