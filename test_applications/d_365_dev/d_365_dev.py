from test_applications.d_365_dev.dev_export_attribute_in_excel_format import (
    DevExportAttributeInExcelFormat,
)

# --
# ... create file of attributes in excel format
# --

dev_export_attribute_in_excel_format = DevExportAttributeInExcelFormat()
dev_export_attribute_in_excel_format.run_export_attribute_in_excel_format_in_all_class(
    export_file_name=f"/all_class_attributs.xlsx"
)
