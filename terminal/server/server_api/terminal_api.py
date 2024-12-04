from typing import Any
from flask import Flask, request, jsonify
from terminal.server.server_api.core.base_terminal_api import BaseTerminalApi
from terminal.server.server_api.config.terminal_api_config import TerminalApiConfig
import json

# --
# ...
# --


class Terminal_API(BaseTerminalApi):
    terminal_api = Flask("terminal_api")
    element_package = None
    element_package_file_address = ""
    element_package_file_mode = ""

    # --
    # ...
    # --

    def __init__(self, **kwargs: Any) -> None:
        __class__.element_package_file_address = self.instance.config_dictionary[
            "element_package_file_address"
        ]

        __class__.element_package_file_mode = self.instance.config_dictionary[
            "element_package_file_mode"
        ]
        __class__.aqua_config_file_address = self.instance.config_dictionary[
            "aqua_config_file_address"
        ]

    # --
    # ...
    # --

    @classmethod
    def get_config_dictionary(cls) -> str:
        return TerminalApiConfig().instance.dictionary

    # --
    # ...
    # --

    def start(self):
        __class__.terminal_api.run(debug=True)
        return True

    # --
    # ... Routes
    # --

    @terminal_api.route("/")
    def home():
        return "home"

    # --
    # ... Route, /api/google_extention
    # --

    @terminal_api.route("/api/google_extention", methods=["POST"])
    def api_google_extention():
        __class__.element_package = request.get_data()

        element_package_dictionary = __class__.instance.json.operation(
            context=__class__.element_package,
            is_get_dictionary=True,
            is_convert_context_to_json=True,
        )

        # prety dictionary
        element_package_dictionary = json.dumps(
            element_package_dictionary, sort_keys=True, indent=4, separators=(",", ":")
        )

        __class__.instance.file.operation(
            context=element_package_dictionary,
            address=__class__.element_package_file_address,
            mode=__class__.element_package_file_mode,
        )

        return __class__.element_package, 200