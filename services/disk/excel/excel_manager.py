from services.disk.core.base_disk import BaseDisk
from services.disk.excel.config.excel_config import excelConfig
import xlsxwriter
import xlwings
import random

# --
# ...
# --


class ExcelManager(BaseDisk):
    def __init__(self, **kwargs) -> None:
        super().__init__()
        
        self.mode = kwargs.get("mode", self.instance.config_dictionary["default_mode"])
        self.address = kwargs.get(
            "address", self.instance.config_dictionary["default_address"]
        )

        # self.workbook = [
        #     {
        #         "worksheet_1": [
        #             [
        #                 {
        #                     (0, 0): "Set name",
        #                 },
        #                 {(0, 1): "Tax Exempt Number"},
        #             ],
        #             [{(1, 0): "country"}, {(1, 1): "ITA"}],
        #             [{(2, 0): "tax_exempt_number"}, {(2, 1): "47510326"}],
        #         ]
        #     }
        # ]

        self.workbook = []
        self.worksheet = None

    # --
    # ...
    # --

    @classmethod
    def get_config_dictionary(cls):
        return excelConfig().instance.dictionary

    # --
    # ...
    # --

    def operation(self, mode="", address="", file_name="") -> str:

        try:

            if mode == "":
                mode = self.mode

            if address == "":
                address = self.address

                if file_name:
                    address = address.replace(address[address.rfind("/") :], file_name)

            if mode == "w":

                with xlsxwriter.Workbook(address) as workbook:
                    format_first_row = workbook.add_format(
                        {"bg_color": "#c6e2ff", "border": 1}
                    )
                    format_rest_rows = workbook.add_format(
                        {"bg_color": "#ffefd5", "border": 1}
                    )
                    format_first_row.set_center_across()
                    format_rest_rows.set_center_across()

                    temp_list_worksheet_name = []

                    for index, worksheet in enumerate(self.workbook):
                        temp_worksheet_name = list(worksheet.keys())[0]

                        if temp_worksheet_name in temp_list_worksheet_name:
                            temp_new_worksheet_name = (
                                f"{temp_worksheet_name}_{random.randint(1, 10000)}")
                            
                            temp = self.workbook.pop(index)
                            temp[temp_new_worksheet_name]=temp.pop(temp_worksheet_name)
                            self.workbook.insert(index, temp)

                        temp_list_worksheet_name.append(temp_worksheet_name)

                    for worksheet in self.workbook:
                        for worksheet_name, worksheet_value in worksheet.items():
                            worksheet = workbook.add_worksheet(worksheet_name)

                            for row_data in worksheet_value:
                                for data in row_data:
                                    for item, value in data.items():

                                        try:

                                            row_format = (
                                                format_rest_rows
                                                if item[0] != 0
                                                else format_first_row
                                            )

                                            worksheet.write(
                                                item[0], item[1], value, row_format
                                            )
                                        # I have change this exp to bestimmt exception
                                        except Exception as exp:
                                            print(repr(exp))

                        worksheet.autofit()

            elif mode == "r":
                worksheets = []
                workbook = xlwings.Book(address)

                if self.worksheet:
                    worksheets = (
                        workbook.sheets[self.worksheet].range("A1").expand() .value
                    )

                else:
                    for worksheet in workbook.sheets:
                        worksheets.append(worksheet.range("A1").expand().value)

                print(worksheets)
                return worksheets

        except Exception as exp:
            print(repr(exp))
            return False
