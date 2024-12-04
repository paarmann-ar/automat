from services.disk.core.base_disk import BaseDisk
from services.disk.file.config.file_config import FileConfig

# --
# ...
# --


class FileManager(BaseDisk):
    def __init__(self, **kwargs) -> None:
        super().__init__()

        self.mode = self.instance.config_dictionary["mode"]
        self.address = self.instance.config_dictionary["address"]
    # --
    # ...
    # --

    @classmethod
    def get_config_dictionary(cls):
        return FileConfig().instance.dictionary

    # --
    # ...
    # --

    def operation(self, mode="", address="", context="") -> str:

        try:

            if mode == "":
                mode = self.mode

            if address == "":
                address = self.address

            match mode:
                case 'r':
                    with open(address, mode) as file:
                        context = file.read()

                case _:
                    with open(address, mode) as file:
                        file.write(context)

        except Exception as exp:
            print(repr(exp))
            context = "Error"

        finally:
            file.close()
            return context
