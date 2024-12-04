from services.log_.log_provider import LogProvider
from toolboxs.decorators import singleton
from services.connection.request.request import Request


# --
# ...
# --
@singleton
class ConnectionProvider:
    def __init__(self, **kwargs) -> None:
        log_info_class = LogProvider().info
        log_error_class = LogProvider().error

        self.request = Request(
            log_info_class=log_info_class,
            log_error_class=log_error_class,
            **kwargs
        ).instance
