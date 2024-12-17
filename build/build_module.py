import PyInstaller.__main__
import os, shutil
from CONSTS import ROOT_DIR
from build.build_config.build_config import build_directory
from build.build_config.build_config import target_exec_test_address
from build.core.refactor_config_json import RefactorConfigJson

# --
# ...
# --

class BuildModule:
    def __call__(self, test_file_full_address):

        rdc_home = f"{ROOT_DIR}/"

        source_adress = test_file_full_address
        source_py_file = source_adress.split("/")[-1]
        source_directory = "/".join(source_adress.split("/")[:-1]) + "/"

        print(f"************************ I am in build {source_py_file} ************************\n\n")
        
        PyInstaller.__main__.run(
            [
                f"{source_directory}{source_py_file}",
                "--clean",
                f"--icon={rdc_home}.external_files/resource/icon/rdc_automat.ico",
                f"--workpath={source_directory}build",
                f"--distpath={source_directory}exec",
                f"--specpath={source_directory}spec",
                f"--add-data={rdc_home}.external_execute_test:./.external_execute_test",
                f"--add-data={rdc_home}.external_files:./.external_files",
                f"--add-data={rdc_home}components:./components",
                f"--add-data={rdc_home}config_dictionary:./config_dictionary",
                f"--add-data={rdc_home}continuous_integration:./continuous_integration",
                f"--add-data={rdc_home}data_structure:./data_structure",
                f"--add-data={rdc_home}detectors:./detectors",
                f"--add-data={rdc_home}drivers:./drivers",
                f"--add-data={rdc_home}exception:./exception",
                f"--add-data={rdc_home}services:./services",
                f"--add-data={rdc_home}terminal:./terminal",
                f"--add-data={rdc_home}test_applications:./test_applications",
                f"--add-data={rdc_home}toolboxs:./toolboxs",
                f"--add-data={rdc_home}utility:./utility",
                f"--add-data={rdc_home}CONSTS.py:.",
            ]
        )

# --
# ...
# --

for directory in ["build","exec", "spec"]:
    rmtree_directory = f"{'/'.join(target_exec_test_address.split("/")[:-2])}/{directory}"
    
    try:
        
        shutil.rmtree(rmtree_directory)

    except FileNotFoundError:
        continue

for file in os.listdir(build_directory):

    if file[-2:] == "py":
        file = file[:-3]
        target_root_test_address = f"{target_exec_test_address}{file}/_internal/"
        refactor_config_json = RefactorConfigJson(
            target_root_test_address=target_root_test_address
        )

        refactor_config_json.refactor_json_config()

        build_module = BuildModule()
        build_module(f"{build_directory}{file}.py")

        refactor_config_json.reset_json_config()