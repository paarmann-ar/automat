from test_applications.d_365.core.object_provider import ObjectProvider
from test_applications.d_365.chapters.core.base_chapter import BaseChapter
from typing import Any

# --
# ...
# --


class Menu(BaseChapter):
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

    def __prepare(
        self,
        menu="main",
    ) -> bool:

        try:

            if super().prepare():
                return True

            self.menu = menu
            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False

    # --
    # ... methods
    # --

    @BaseChapter.wait_for()
    @BaseChapter.log
    def select_side_pannel_menu(self) -> bool:

        try:

            self.delay(220)

            match self.menu:
                case "main":
                    self.click(self.elements.mnu_side_panel_main)
                case "home":
                    self.click(self.elements.mnu_side_panel_home)
                case "recent":
                    self.click(self.elements.mnu_side_panel_recent)
                case "favorait":
                    self.click(self.elements.mnu_side_panel_favorait)
                case "workspace":
                    self.click(self.elements.mnu_side_panel_workspace)
                case "module":
                    self.click(self.elements.mnu_side_panel_module)
                case _:
                    pass

            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False

    # --
    # ...
    # --

    def pare_menu(self, menu="") -> bool:

        try:
            # I will dev this method in next
            menu.index(">")

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False
