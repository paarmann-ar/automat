from services.disk.service_disk_provider import ServiceDiskProvider

# --
# ...
# --


class ImportAttributeInExcelFormat:
    def __init__(self, **kwargs) -> None:
        self.class_ = kwargs.get("class_", None)

        if self.class_:
            self.worksheet = self.class_.__name__
        else:
            self.worksheet = kwargs.get("worksheet", "")

        self.excel = ServiceDiskProvider().excel
        self.excel.mode = kwargs.get("mode", "r")
        self.excel.address = kwargs.get("excel_file_adress", None)

    # --
    # ...
    # --

    def start(self):

        try:

            self.excel.worksheet = self.worksheet

            imported_attributes = self.excel.operation()

            for attribute in imported_attributes[1:]:
                if attribute[1] != "-" and attribute[1] != "":
                    if attribute[2]:
                        setattr(self.class_.instance, attribute[0], (attribute[1], attribute[2]))
                    else:
                        setattr(self.class_.instance, attribute[0], (attribute[1]))

            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False
