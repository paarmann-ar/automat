from test_applications.d_365.core.object_provider import ObjectProvider
from test_applications.d_365.chapters.core.base_chapter import BaseChapter
from typing import Any
from test_applications.d_365.abstrct_classes.form.form import Form

# --
# ...
# --


class WorkflowForVendorInvoice(BaseChapter, Form):
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
                    self.attachments_for_vendor_invoice()

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
        name=("", False),
        pervious_comment=("", False),
        comment=("comment", True),
    ) -> bool:

        try:

            if super().prepare():
                return True

            self.name = name
            self.pervious_comment = pervious_comment
            self.comment = comment

            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False

    # --
    # ... methods
    # --

    @BaseChapter.wait_for(
        element_for_waiting_until_visible="frm_workflow_for_vendor_invoices",
        type_of_element="text_to_search",
    )
    @BaseChapter.log
    def workflow_for_vendor_invoice(self, **kwargs) -> bool:

        try:

            self.textbox(self.elements.txb_name, self.name)
            self.textbox(self.elements.txb_pervious_comment, self.pervious_comment)
            self.textbox(self.elements.txb_comment, self.comment)

            self.click_button(self.elements.btn_startworkflow)
            self.delay(220)

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False

    # --
    # ...
    # --

    @BaseChapter.wait_for(
        element_for_waiting_until_visible="frm_workflow_for_vendor_invoices",
        type_of_element="text_to_search",
    )
    @BaseChapter.log
    def approve_workflow_for_vendor_invoice(self, **kwargs) -> bool:

        try:

            self.textbox(self.elements.txb_name, self.name)
            self.textbox(self.elements.txb_pervious_comment, self.pervious_comment)
            self.textbox(self.elements.txb_comment, self.comment)

            self.click_button(self.elements.btn_approve)
            self.delay(220)

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False