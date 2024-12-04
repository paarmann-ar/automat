from toolboxs.decorators import singleton
from test_applications.d_365.components.component.form.form_match_found import (
    FormMatchFound,
)
from test_applications.d_365.components.component.form.form_vendor_name import (
    FormVendorName,
)
from test_applications.d_365.components.component.form.form_select_and_sort_item import (
    FormSelectAndSortItem,
)
from test_applications.d_365.components.component.combobox.combobox_type_2 import (
    ComboboxType2,
)
from test_applications.d_365.components.component_struct.component_struct import (
    ComponentStruct,
)
from test_applications.d_365.components.component.form.form_radio_button_and_select import FormRadioButtonAndSelect

@singleton
class ComponentsProvider:
    def __init__(self) -> None:
        print(__class__.__name__, id(__class__))

        # in ghablan toy indent aghbtar bod k ovordamesh jolo badan checkesh konam
        self.component = ComponentStruct(
            form_match_found=FormMatchFound(),
            form_vendor_name=FormVendorName(),
            form_select_and_sort_item=FormSelectAndSortItem(),
            combobox_type_2=ComboboxType2(),
            form_radio_button_and_select=FormRadioButtonAndSelect()
        )
