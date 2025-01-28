from test_applications.d_365.core.object_provider import ObjectProvider
from test_applications.d_365.chapters.core.base_chapter import BaseChapter
from typing import Any
import subprocess

# --
# ...
# --


class CreateCustomer(BaseChapter):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.file_address = ""

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
                    self.create_customer(**kwargs)

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
        return ObjectProvider()(
            __file__.replace(".py", ".json ", -1).replace("\\", "/").replace(" c", "")
        )

    # --
    # ... setup and teardown and prepare
    # --

    def __setup(self) -> bool:

        try:

            super().setup()

            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False

    # --
    # ...
    # --

    def __teardown(self) -> bool:

        try:

            super().teardown()

            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False

    # --
    # ...
    # --

    def __prepare(self) -> bool:

        try:

            if super().prepare():
                return True

            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False

    # --
    # ... methods
    # --

    def create_customer(self, **kwargs) -> bool:

        try:

            self.run_ax2009()

            self.instance.windriver_connect(self.elements.frm_ax2009)
            self.instance.windriver_click(self.elements.frm_address_bar)

            self.instance.windriver_click(self.elements.txb_address_bar)

            self.instance.txb_address_bar(
                self.elements.txb_address_bar,
                text="140/Debitoren/Debitoren Bereich5",
                is_set_focus=False
            )

            # self.instance.windriver_click(self.elements.btn_folder_address)
            # self.instance.windriver_textbox(
            #     self.elements.txb_folder_address,
            #     text=file_directory,
            #     is_press_enter=True,
            #     is_back_space=True,
            # )

            # self.instance.windriver_textbox(self.elements.txb_file_name, text=file_name)

            # self.instance.windriver_click_button(self.elements.btn_open)

            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False

    # --
    # ...
    # --

    def run_ax2009(self, **kwargs) -> bool:

        try:

            import CONSTS

            process = subprocess.Popen(
                CONSTS.ROOT_DIR
                + "/test_applications/d_365/chapters/finance_chapter/unit_testcases/ax_2009/start_ax.bat",
                shell=True,
            )
            process.wait()

            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False