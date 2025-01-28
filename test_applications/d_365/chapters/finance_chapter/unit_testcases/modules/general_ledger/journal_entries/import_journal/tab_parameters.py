from typing import Any
from test_applications.d_365.core.object_provider import ObjectProvider
from test_applications.d_365.chapters.core.base_chapter import BaseChapter
from test_applications.d_365.abstrct_classes.tab.tab import Tab
from test_applications.windows_components.open_file_dialog import OpenFileDialog
import CONSTS

# --
# ...
# --


class TabParameters(BaseChapter, Tab):
    def __init__(
        self,
        *args,
        **kwargs,
    ) -> None:
        super().__init__(*args, **kwargs)

        self.elements = self.get_elements()
        self.__prepare(**kwargs)
        self.__setup()

        print(__class__.__name__, id(__class__))

    # --
    # ... call
    # --

    def __call__(self, action="", **kwargs) -> Any:

        try:

            if super_result := super().__call__(action, **kwargs):
                return super_result

            match action:
                case "":
                    self.tab_parameters()
                    
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

    def get_elements(self) -> str:
        return ObjectProvider()(__file__.replace(".py", ".json ", -1).replace("\\", "/").replace(" c", ""))

    # --
    # ... setup, teardown and prepare
    # --

    def __setup(self) -> bool:

        try:

            super().setup()

            self.open_file = OpenFileDialog()

            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False

    def __teardown(self) -> bool:

        try:

            super().teardown()

            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False

    def __prepare(
        self,
        file_address=(f"{CONSTS.ROOT_DIR}/.external_files/sample_files/import_journal_and_validate.csv",
            True,
        ),
    ) -> bool:

        try:

            if super().prepare():
                return True

            self.file_address = file_address,


            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False

    # --
    # ... methods
    # --
    @Tab.expand_tab
    @BaseChapter.wait_for(element_for_waiting_until_visible="btn_tab")
    @BaseChapter.log
    def tab_parameters(self, **kwargs) -> bool:

        try:

            self.click_button(self.elements.btn_browse)

            self.open_file(file_address = self.file_address[0])

            self.delay(220)

            # there is no longer btn_ok 
            # while self.is_element_there(self.elements.btn_ok):
            #     self.click_button(self.elements.btn_ok)
            #     self.delay(220)
                
            self.delay(220)

            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False
