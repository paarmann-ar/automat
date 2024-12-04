from components.comboboxes.combobox_components import ComboboxComponents
from toolboxs.decorators import singleton

#--
#...
#--
@singleton
class ComponentsProvider:
    def __init__(self) -> None:
        print(__class__.__name__, id(__class__))
        self.combobox_components = ComboboxComponents()