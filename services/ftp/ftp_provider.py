from services.ftp.core.ftp import FTP
from services.log_.log_provider import LogProvider
from toolboxs.decorators import singleton

# --
# ...
# --
@singleton
class FTPProvider:
    def __init__(self, domain='aqc', current_working_directory=None, file_to_download=None, temp_location_for_download=None, **kwargs) -> None:
        log_info_class = LogProvider().info
        log_error_class = LogProvider().error
        
        self.ftp = FTP(domain=domain, log_info_class=log_info_class, log_error_class=log_error_class, **kwargs).instance