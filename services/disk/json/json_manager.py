from services.disk.core.base_disk import BaseDisk
import json
from typing import Any

# --
# ...
# --


class JSONManager(BaseDisk):
    def __init__(self, **kwargs) -> None:
        super().__init__()

    # --
    # ...
    # --

    def operation(
        self,
        address="",
        context="",
        is_get_dictionary=True,
        is_convert_context_to_json=False,
        is_json_data_has_unexpected_char=False
    ) -> Any:

        try:
            json_data = None

            if context == "":
                with open(address, "r", encoding="utf8") as file:
                    readed_file = file.read()
                    corrected_file_string = self.__fix_json_error(readed_file)
                    json_data = json.loads(corrected_file_string)

                    if is_get_dictionary:
                        json_data = dict(json_data)

                    if is_json_data_has_unexpected_char:
                        for key,value_dictionary in json_data.items():
                            for key_,value_ in value_dictionary.items():
                                value_ = value_.replace("*******", "\"")
                                value_=dict({key_:value_})
                            json_data[key]=value_


            elif is_convert_context_to_json:
                json_data = json.loads(context)

                if is_get_dictionary:
                    json_data = dict(json_data)

            else:
                with open(address, "w") as file:
                    corrected_file_string = self.__fix_json_error(context)
                    json.dumps(corrected_file_string, indent=4)
                    file.write(corrected_file_string)
                    json_data = True

            return json_data

        except Exception as exp:
            print(repr(f"{exp} -> {address}"))

    # --
    # ...
    # --

    def __fix_json_error(self, context="") -> str:

        try:

            context = context.replace(chr(92), chr(47))
            context = context.replace(chr(39), chr(34))
            context = context.replace("/\"", "*******")

            return context

        except Exception as exp:
            print(repr(exp))
