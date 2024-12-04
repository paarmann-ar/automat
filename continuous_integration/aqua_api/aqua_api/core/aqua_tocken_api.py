from continuous_integration.aqua_api.aqua_api.core.base_aqua_api import BaseAquaApi
from continuous_integration.aqua_api.aqua_api.config.aqua_api_config import AquaApiConfig

# --
# ...
# --


class AquaTockenApi(BaseAquaApi):
    def __init__(self, **kwargs) -> None:
        self.base_url = self.instance.config_dictionary.get("base_url")
        self.token_url = self.instance.config_dictionary.get("token_url")
        self.username = self.instance.config_dictionary.get("username")
        self.password = self.instance.config_dictionary.get("password")

        self.access_token = None
        
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
    
    def __call__(self, project_name=None, folder_name=None) -> str:
        return self.get_tocken()

    # --
    # ... tocken
    # --

    def get_tocken(self, type="new"):

        try:

            if self.access_token is not None:
                return

            match type:
                case "new":
                    grant_type = "password"

                case "refresh":
                    grant_type = "refresh_token"

            response = self.request(
                method="post",
                url=f"{self.base_url}{self.token_url}",
                headers={"Content-Type": "application/x-www-form-urlencoded"},
                data={
                    "grant_type": grant_type,
                    "username": self.username,
                    "password": self.password,
                },
            )

            self.access_token = response.get("access_token", None)

            print(f"access Token is: {self.access_token}")
            return self.access_token

        except Exception as exp:
            print(f"get_tocken: {exp}")
