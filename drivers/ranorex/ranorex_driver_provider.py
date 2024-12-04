from drivers.ranorex.core.ranorex import Ranorex
from toolboxs.decorators import singleton


# --
# ...
# --
@singleton
class RanorexDriverProvider:
    def __init__(self) -> None:
        print(__class__.__name__, id(__class__))
        self.ranorex_driver = Ranorex().instance
