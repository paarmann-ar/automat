from test_applications.d_365.core.object_provider import ObjectProvider
from test_applications.d_365.chapters.core.base_chapter import BaseChapter
from typing import Any
from test_applications.d_365.abstrct_classes.form.form import Form

# --
# ...
# --


class AttachmentsForVendorInvoiceDescription(BaseChapter, Form):
    def __init__(self, *args, **kwargs) -> None:
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
                    self.attachments_for_vendor_invoice_description()

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
        description=("description", True),
        type=("Note", True),
        attached=(True, True),
    ) -> bool:

        try:

            if super().prepare():
                return True

            self.description = description
            self.type = type
            self.attached = attached

            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False

    # --
    # ... methods
    # --

    @BaseChapter.wait_for(
        element_for_waiting_until_visible="frm_attachments_for_vendor_invoices",
        type_of_element="text_to_search",
    )
    @BaseChapter.log
    def attachments_for_vendor_invoice_description(self, **kwargs) -> bool:

        try:

            self.textbox(self.elements.txb_description, self.description)
            self.textbox(self.elements.txb_type, self.type)
            self.checkbox(self.elements.chk_attached, self.attached)

            self.delay(220)

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False
