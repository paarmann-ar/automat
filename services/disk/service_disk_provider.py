from toolboxs.decorators import singleton
from services.disk.file.file_manager import FileManager
from services.disk.excel.excel_manager import ExcelManager

from services.disk.xml.xml_manager import XMLManager
from services.disk.json.json_manager import JSONManager

from services.log_.log_provider import LogProvider


# --
# ...
# --


@singleton
class ServiceDiskProvider:
    def __init__(self, **kwargs):
        log_info_class = LogProvider().info
        log_error_class = LogProvider().error

        self.json = JSONManager(
            log_info_class=log_info_class, log_error_class=log_error_class, **kwargs
        ).instance

        self.xml = XMLManager(
            log_info_class=log_info_class, log_error_class=log_error_class, **kwargs
        ).instance
        
        self.file = FileManager(
            log_info_class=log_info_class, log_error_class=log_error_class, **kwargs
        ).instance

        self.excel = ExcelManager(
            log_info_class=log_info_class, log_error_class=log_error_class, **kwargs
        ).instance
