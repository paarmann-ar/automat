from continuous_integration.aqua_api.aqua_api.core.base_aqua_api import BaseAquaApi
from continuous_integration.aqua_api.aqua_api.config.aqua_api_config import (
    AquaApiConfig,
)
import time

# --
# ...
# --


class AquaTokenApi(BaseAquaApi):
    def __init__(self, **kwargs) -> None:
        self.base_url = self.instance.config_dictionary.get("base_url")
        self.token_url = self.instance.config_dictionary.get("token_url")
        self.username = self.instance.config_dictionary.get("username")
        self.password = self.instance.config_dictionary.get("password")

        self.aqua_access_token = None
        self.expires_in_token = 0
        self.expires_get_time = time.time()

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

    def __call__(self, **kwargs) -> str:
        return self.get_token(**kwargs)

    # --
    # ... tocken
    # --

    def get_token(self, **kwargs):

        try:

            if self.expires_in_token - 30 > time.time() - self.expires_get_time:
                return

            data = {
                "grant_type": "password",
                "username": self.username,
                "password": self.password,
            }

            if self.aqua_access_token:
                data["refresh_token"] = self.aqua_access_token

            response = self.request(
                method="post",
                url=f"{self.base_url}{self.token_url}",
                headers={"Content-Type": "application/x-www-form-urlencoded"},
                data=data,
            )

            self.aqua_access_token = response.get("access_token", None)
            self.expires_in_token = response.get("expires_in", 0)
            self.expires_get_time = time.time()

            print(f"access Token is: {self.aqua_access_token}")
            return self.aqua_access_token

        except Exception as exp:
            print(f"get_token: {exp}")
