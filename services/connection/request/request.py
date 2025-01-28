import asyncio.tasks
from services.connection.request.config.request_config import RequestConfig
from services.connection.core.base_connection import BaseConnection
import requests
import time
import asyncio

# --
# ...
# --


class Request(BaseConnection):
    def __init__(self, **kwargs) -> None:

        try:
            self.url = kwargs.get("url", None)
            self.headers = kwargs.get("headers", None)
            self.params = kwargs.get("params")
            self.data = kwargs.get("data", None)
            self.json = kwargs.get("json", None)
            self.auth = kwargs.get("auth")

            self.method = kwargs.get("method", "get")
            self.is_response_json = kwargs.get("is_response_json", True)

        except Exception as exp:
            self.error(f"{__file__}--->{__name__}: {str(exp)}")

    # --
    # ...
    # --

    @classmethod
    def get_config_dictionary(cls):
        return RequestConfig().instance.dictionary

    # --
    # ...
    # --

    def __call__(self, **kwargs) -> str:
        self.url = kwargs.get("url", None)
        self.headers = kwargs.get("headers", None)
        self.params = kwargs.get("params", None)
        self.data = kwargs.get("data", None)
        self.json = kwargs.get("json", None)
        self.auth = kwargs.get("auth", None)

        self.method = kwargs.get("method", "get")
        self.is_response_json = kwargs.get("is_response_json", True)

        self.request_package = {
            "url": self.url,
            "auth": self.auth,
            "headers": self.headers,
            "params": self.params,
            "data": self.data,
            "json": self.json,
            "timeout": (10, 10),
        }

        self.delay = kwargs.get("delay", 0.5)
        return self.get_response()

    # --
    # ...
    # --

    async def get_response(self): ...

    def get_response(self):

        try:

            match self.method.lower():
                case "get":
                    response = requests.get(**self.request_package)

                case "post":
                    response = requests.post(**self.request_package)

                case "patch":
                    response = requests.patch(**self.request_package)

                case "delete":
                    response = requests.delete(**self.request_package)

            time.sleep(self.delay)

            if response.status_code == 401:
                print('The current user is not correctly authenticated or the session or authentication token has expired.')
                return 'expired token'

            response = (
                response if response.status_code in [204, 200] else print(response.text)
            )

            if response.status_code == 204:
                return True
            
            elif self.is_response_json and response:
                response = response.json()

            return response

        except ValueError as v_exp:
            print(f"{v_exp}")
            
        except Exception as exp:
            print(f"{exp}")
