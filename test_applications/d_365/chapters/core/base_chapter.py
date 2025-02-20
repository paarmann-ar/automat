from typing import Any
from abc import ABC, abstractmethod
from collections import namedtuple
from test_applications.d_365.core.base import Base
from test_applications.d_365.components.components_provider import ComponentsProvider
from services.log_.log_provider import LogProvider
from test_applications.d_365.abstrct_classes.lightbox.lightbox import Lightbox
from test_applications.d_365.abstrct_classes.tipbox.tipbox import Tipbox
from test_applications.d_365.abstrct_classes.blocking_message.blocking_message import (
    BlockingMessage,
)
from test_applications.d_365.abstrct_classes.context_menu.context_menu import (
    ContextMenu,
)
from test_applications.d_365.abstrct_classes.alert.alert import Alert
from test_applications.d_365.chapters.core.base_method.export_attribute_in_excel_format import (
    ExportAttributeInExcelFormat,
)
from test_applications.d_365.chapters.core.base_method.import_attribute_in_excel_format import (
    ImportAttributeInExcelFormat,
)
from test_applications.d_365.chapters.core.config.base_chapter_config import (
    BaseChapterConfig,
)
from continuous_integration.continuous_integration_provider import (
    ContinuousIntegrationProvider,
)

# --
# ...
# --


class BaseChapter(Base):
    def __init__(self, *args, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

        self.is_use_excel_attributs = self.config_dictionary["is_use_excel_attributs"]
        self.attributes_excel_file_address = self.config_dictionary[
            "attributes_excel_file_address"
        ]

        self.components = self.get_components()

        # self.aqua_description = f"this testcase is about: {self.__class__.__name__}"

        # self.aqua_source_code_filter = [
        #     "@BaseChapter.aqua",
        #     "@BaseChapter.log",
        #     "@BaseChapter.wait_for",
        #     "def",
        #     "try",
        #     "except",
        #     "return",
        #     "self.error",
        #     "return",
        # ]

    # --
    # ...
    # --

    @classmethod
    def get_config_dictionary(cls):
        return BaseChapterConfig().instance.dictionary

    # --
    # ...
    # --

    def __call__(self, action, **kwargs) -> bool:

        try:

            kwargs.update(dict(class_=self.__class__))

            match action:
                case "help_me":
                    print(dir(self.__class__))

                case "export_attribute_in_excel_format":
                    return ExportAttributeInExcelFormat(**kwargs).start()

                case "import_attribute_in_excel_format":
                    return ImportAttributeInExcelFormat(**kwargs).start()

                case _:
                    raise Exception(
                        f"class {__class__.__name__} have no method {action}."
                    )

            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False

    # --
    # ...
    # --

    def get_components(self) -> str:
        return ComponentsProvider().component

    # --
    # ...
    # --

    def setup(self) -> bool:

        try:

            self.alert = Alert()
            self.context_menu = ContextMenu()
            self.lightbox = Lightbox()
            self.tipbox = Tipbox()
            self.blocking_message = BlockingMessage()
            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False

    # --
    # ...
    # --

    def teardown(self) -> bool:

        try:

            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False

    # --
    # ...
    # --

    def prepare(self, *args, **kwargs: Any) -> None:

        try:

            if self.is_use_excel_attributs:
                ImportAttributeInExcelFormat(
                    class_=self.__class__,
                    excel_file_adress=self.attributes_excel_file_address,
                ).start()

                return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False

    # --
    # ... decorators
    # --

    def wait_for(**kwargs) -> bool:

        try:

            element_for_waiting_until_visible = kwargs.get(
                "element_for_waiting_until_visible", None
            )
            type_of_element = kwargs.get("type_of_element", "xpath")

            def decorator(
                function,
                element_for_waiting_until_visible=element_for_waiting_until_visible,
            ):

                def inner_function(*args, **kwargs):

                    nonlocal element_for_waiting_until_visible
                    nonlocal type_of_element

                    if element_for_waiting_until_visible:
                        if isinstance(element_for_waiting_until_visible, str):
                            element_for_waiting_until_visible = getattr(
                                args[0].elements, element_for_waiting_until_visible
                            )

                        args[0].wait_for_element_until_visibile(
                            element=element_for_waiting_until_visible,
                            type_of_element=type_of_element,
                        )

                    return function(*args, **kwargs)

                return inner_function

            return decorator

        except Exception as exp:
            print(f"{repr(exp)}")
            return False

    # --
    # ...
    # --

    def log(function) -> object:

        try:

            def inner_function(*args, **kwargs):
                args[0].info(f"{function.__module__}.{function.__name__}")
                return function(*args, **kwargs)

            return inner_function

        except Exception as exp:
            print(f"{repr(exp)}")
            return False

    # --
    # ...
    # --

    def aqua(function) -> object:

        try:

            def inner_function(*args, **kwargs):
                # testcase is hier
                element = ""
                class_name = args[0].__class__.__name__
                closure_name = [
                    closure.cell_contents for closure in function.__closure__
                ][0]

                if isinstance(closure_name, str):
                    closure_name = function.__qualname__

                else:
                    closure_name = closure_name.__name__

                result = function(*args, **kwargs)

                if isinstance(result, tuple):
                    element, result = result

                args[0].state["aqua"].update(
                    {f"{class_name}.{closure_name}": args[0].base_driver_state.copy()}
                )

                args[0].base_driver_state.clear()

                print(
                    f"!!!!!!!!!!!!!!!\n\ntestcase: {class_name}.{closure_name}\nelement: {element}\nresult: {result}\n\n!!!!!!!!!!!!!!!"
                )

                return result

            return inner_function

        except Exception as exp:
            print(f"{repr(exp)}")
            return False

    # --
    # ...
    # --

    def handel_tipbox(function) -> object:

        try:

            def inner_function(*args, **kwargs):

                Tipbox()()
                return function(*args, **kwargs)

            return inner_function

        except Exception as exp:
            print(f"{repr(exp)}")
            return False
