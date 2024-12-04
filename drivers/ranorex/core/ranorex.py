from drivers.ranorex.config.ranorex_config import RanorexConfig
from drivers.core.base_driver import BaseDriver
from typing import Any
import subprocess

# --
# ...
# --


class Ranorex(BaseDriver):
    def __init__(self) -> None:
        super().__init__()

        self.ranorex_testsuit_address = "C:/Users/mpaarmann/Projects/ranorex/ax_md365_integration/ax_md365_integration/bin/Debug/ax_md365_integration.exe"
        print(__class__.__name__, id(__class__))

    # --
    # ...
    # --

    def get_config_dictionary():
        return RanorexConfig().instance.dictionary

    # --
    # ...
    # --

    def run_ranorex_testsuit(self, ranorex_testsuit_address=""):
        if ranorex_testsuit_address == "":
            ranorex_testsuit_address = self.ranorex_testsuit_address

        process = subprocess.Popen(ranorex_testsuit_address, shell=True)

        process.wait()
