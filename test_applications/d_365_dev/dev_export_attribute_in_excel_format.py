import importlib.util
import os
import glob
import importlib
from services.disk.service_disk_provider import ServiceDiskProvider
from continuous_integration.aqua_api.aqua_adaptor.core.get_all_class_in_test_application import GetAllClassInTestApplication

# --
# ...
# --


class DevExportAttributeInExcelFormat:
    def __init__(self) -> None:
        self.get_all_class_in_test_application = GetAllClassInTestApplication()

    # --
    # ...
    # --

    # def get_list_of_object_from_all_classes_in_unit_testcases(self):
    #     self.get_list_of_all_classes_in_unit_testcases()

    #     self.Objects_of_classes = [class_() for class_ in self.classes]

    # # --
    # # ...
    # # --

    # def get_list_of_all_classes_in_unit_testcases(self):
    #     for file in glob.glob(
    #         f"C:/Users/mpaarmann/Projects/rdc_automat/test_applications/md_365/chapters/finance_chapter/unit_testcases/**/*.py",
    #         recursive=True,
    #     ):
    #         name = file.split("\\")[-1][:-3]

    #         spec = importlib.util.spec_from_file_location(name, file)
    #         module = importlib.util.module_from_spec(spec)
    #         spec.loader.exec_module(module)

    #         class_name = "".join([word.capitalize() for word in name.split("_")])

    #         class_ = getattr(module, class_name)
    #         self.classes.append(class_)

    # --
    # ... export_attribute_in_excel_format
    # --

    def run_export_attribute_in_excel_format_in_all_class(
        self, export_file_name=f"/all_class_attributs.xlsx"
    ):
        action = "export_attribute_in_excel_format"
        excel = ServiceDiskProvider().excel

        self.get_all_class_in_test_application.get_list_of_object_from_all_classes_in_unit_testcases()

        for object_ in self.get_all_class_in_test_application.Objects_of_classes:
            excel.workbook.append(object_(action=action, is_create_excel_file=False)[0])

        excel.operation(file_name=export_file_name)
