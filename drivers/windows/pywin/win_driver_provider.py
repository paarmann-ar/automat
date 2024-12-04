from drivers.windows.pywin.core.pywin import Pywin
from toolboxs.decorators import singleton


#--
#...
#--
@singleton
class WinDriverProvider:
    def __init__(self) -> None:
        print(__class__.__name__, id(__class__))
        self.pywin_driver = Pywin().instance