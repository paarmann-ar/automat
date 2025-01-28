from typing import Any
from test_applications.d_365.core.object_provider import ObjectProvider
from test_applications.d_365.chapters.core.base_chapter import BaseChapter
from test_applications.d_365.abstrct_classes.tab.tab import Tab

# --
# ...
# --


class TabAttachmentForVendorInvoiceGeneral(BaseChapter, Tab):
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
                    self.tab_general()
                    return True

                case _:
                    raise Exception(
                        f"class {__class__.__name__} have no method {action}."
                    )

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
        notes=("notes", True),
        is_default_attachment=(False, False),
        created_by=("", False),
        restriction=("", False),
        created_date_and_time=("", False),
    ) -> bool:

        try:

            if super().prepare():
                return True

            self.notes = notes
            self.is_default_attachment = is_default_attachment
            self.created_by = created_by
            self.restriction = restriction
            self.created_date_and_time = created_date_and_time

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
    def tab_general(self) -> bool:

        try:

            self.textbox(self.elements.txb_notes, self.notes)
            self.textbox(
                self.elements.chk_is_default_attachment, self.is_default_attachment
            )
            self.textbox(self.elements.txb_created_by, self.created_by)
            self.textbox(self.elements.txb_restriction, self.restriction)
            self.textbox(
                self.elements.txb_created_date_and_time, self.created_date_and_time
            )

            self.delay(220)

            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False