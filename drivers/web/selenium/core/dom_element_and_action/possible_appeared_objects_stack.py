from drivers.web.selenium.core.base_selenium import BaseSelenium
from selenium.webdriver.common.keys import Keys
from typing import Any
import inspect

# --
# ...
# --


class PossibleAppearedObjectsStack(BaseSelenium):
    def __init__(self) -> None:
        super().__init__()

        # {element_name: ({type:element}, function)}
        self.possible_appeared_objects_stack = {}

        print(__class__.__name__, id(__class__))

    # --
    # ... call
    # --

    @BaseSelenium.log
    def is_object_in_possible_appeared_objects_appeared(
        self,
    ):

        try:

            for (
                element_name,
                element_data,
            ) in self.possible_appeared_objects_stack.items():
                
                for k,v in element_data[0].items():
                    element_tuple = k,v 
                find_element = self.is_element_there(element_tuple)

                print(find_element)

                if find_element:
                    element_data[1]()

                print(f"{element_name}:{element_data}")

                return find_element

        except Exception as exp:
            self.error(
                f"faild on: {__class__}.{repr(exp)}\n{__class__}.{str(exp)}\n{self.stack()} => "
            )
            return False

    # --
    # ... add element
    # --

    @BaseSelenium.log
    def add_object_to_possible_appeared_objects_stack(self, element):

        try:

            self.possible_appeared_objects_stack.update(element)

        except Exception as exp:
            self.error(
                f"faild on: {__class__}.{repr(exp)}\n{__class__}.{str(exp)}\n{self.stack()} => {element}"
            )
            return False

    # --
    # ... delete element
    # --

    @BaseSelenium.log
    def delete_object_to_possible_appeared_objects_stack(self, element_name):

        try:

            self.possible_appeared_objects_stack.pop(element_name)

        except Exception as exp:
            self.error(
                f"faild on: {__class__}.{repr(exp)}\n{__class__}.{str(exp)}\n{self.stack()} => {element_name}"
            )
            return False
