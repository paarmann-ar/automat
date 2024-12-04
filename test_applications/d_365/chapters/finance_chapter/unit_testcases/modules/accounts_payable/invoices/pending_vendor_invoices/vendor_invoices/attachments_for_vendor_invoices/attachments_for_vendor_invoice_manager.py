from test_applications.d_365.core.object_provider import ObjectProvider
from test_applications.d_365.chapters.core.base_chapter import BaseChapter
from typing import Any
from test_applications.d_365.abstrct_classes.form.form import Form
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.accounts_payable.invoices.pending_vendor_invoices.vendor_invoices.attachments_for_vendor_invoices.tab_attachment_for_vendor_invoice_general import (
    TabAttachmentForVendorInvoiceGeneral,
)
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.accounts_payable.invoices.pending_vendor_invoices.vendor_invoices.attachments_for_vendor_invoices.tab_attachment import (
    TabAttachment,
)
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.accounts_payable.invoices.pending_vendor_invoices.vendor_invoices.attachments_for_vendor_invoices.attachments_for_vendor_invoice_description import (
    AttachmentsForVendorInvoiceDescription,
)
# --
# ...
# --


class AttachmentsForVendorInvoiceManager(BaseChapter, Form):
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

            self.tab_attachment_for_vendor_invoice_general = (
                TabAttachmentForVendorInvoiceGeneral()
            )
            self.tab_attachment = TabAttachment()
            self.attachments_for_vendor_invoice_description = AttachmentsForVendorInvoiceDescription()
            self.Attachments_for_vendor_invoice_top_gadget = (
                AttachmentsForVendorInvoiceTopGadget()
            )
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

    @BaseChapter.wait_for(
        element_for_waiting_until_visible="frm_attachments_for_vendor_invoices",
        type_of_element="text_to_search",
    )
    @BaseChapter.log
    def attachments_for_vendor_invoice(self, **kwargs) -> bool:

        try:

            for _, tab in kwargs.items():
                match tab:
                    case "attachments_for_vendor_invoice_description":
                        self.attachments_for_vendor_invoice_description()
                        
                    case "tab_attachment_for_vendor_invoices_general":
                        self.tab_attachment_for_vendor_invoice_general()

                    case "tab_attachment":
                        self.tab_attachment()

                    case _:
                        pass

            self.delay(220)

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False