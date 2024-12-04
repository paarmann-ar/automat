from typing import Any
from drivers.web.selenium.config.selenium_config import SeleniumConfig
from drivers.web.selenium.core.waits.waits import Waits
from drivers.web.selenium.core.action.chains import Chains
from drivers.web.selenium.core.action.single_actions import SingleActions
from drivers.web.selenium.core.action.browser_actions import BrowserActions
from drivers.web.selenium.core.action.complex_actions import ComplexActions
from drivers.web.selenium.core.dom_element_and_action.dom_element_and_action import DomElementAndAction
from drivers.web.selenium.core.action.property_attributs import PropertyAttributs
from drivers.web.selenium.core.dom_element_and_action.possible_appeared_objects_stack import PossibleAppearedObjectsStack

# --
# ...
# --

class SeleniumDriver(Waits, Chains, SingleActions, BrowserActions, ComplexActions, DomElementAndAction, PossibleAppearedObjectsStack, PropertyAttributs):
    def __init__(self) -> None:
        super().__init__()
        
        print(__class__.__name__, id(__class__))

    # --
    # ...
    # --

    def get_config_dictionary():
        return SeleniumConfig().instance.dictionary