from typing import Any
from test_applications.d_365.core.object_provider import ObjectProvider
from test_applications.d_365.chapters.core.base_chapter import BaseChapter
from test_applications.d_365.abstrct_classes.page.page import Page
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.accounts_payable.vendors.all_vendors.vendor_bank_accounts.tab_bank_general import (
    TabBankGeneral,
)
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.accounts_payable.vendors.all_vendors.vendor_bank_accounts.tab_prenotes import (
    TabPrenotes,
)
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.accounts_payable.vendors.all_vendors.vendor_bank_accounts.tab_setup import (
    TabSetup,
)
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.accounts_payable.vendors.all_vendors.vendor_bank_accounts.tab_address import (
    TabAddress,
)
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.accounts_payable.vendors.all_vendors.vendor_bank_accounts.tab_contact_information import (
    TabContactInformation,
)

# --
# ...
# --


class VendorBankAccounts(BaseChapter, Page):
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
        return ObjectProvider()(
            __file__.replace(".py", ".json ", -1).replace("\\", "/").replace(" c", "")
        )

    # --
    # ... setup and teardown and prepare
    # --

    def __setup(self) -> bool:

        try:

            super().setup()

            self.tab_bank_general = TabBankGeneral()
            self.tab_prenotes = TabPrenotes()
            self.tab_setup = TabSetup()
            self.tab_address = TabAddress()
            self.tab_contact_iInformation = TabContactInformation()

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
        bank_account=("01", True),
        name=("vendor test112", True),
    ) -> bool:

        try:

            if super().prepare():
                return True

            self.bank_account = (
                self.get_random(type="int"),
                bank_account[1] if bank_account[0] == "" else bank_account[1],
            )

            name, _ = name
            if name == "":
                name = self.state["vendor_name"]

            self.name = name
            
            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False

    # --
    # ... methods
    # --

    @BaseChapter.wait_for(
        element_for_waiting_until_visible="frm_vendor_bank_accounts",
        type_of_element="text_to_search",
    )
    @BaseChapter.log
    def add_new_bank_account(self, **kwargs) -> bool:

        try:

            self.click_button(self.elements.btn_new)

            self.textbox(self.elements.txb_bank_account, self.bank_account)
            self.textbox(
                self.elements.txb_name,
                self.name,
            )

            for _, tab in kwargs.items():
                match tab:
                    case "tab_bank_general":
                        self.tab_bank_general()

                    case "tab_prenotes":
                        self.tab_prenotes()

                    case "tab_setup":
                        self.tab_setup()

                    case "tab_address":
                        self.tab_address()

                    case "tab_contact_iInformation":
                        self.tab_contact_iInformation()

                    case _:
                        pass

            self.click_button(self.elements.btn_save)

            self.delay(220)

            self.lightbox()

            self.click_button(
                self.elements.btn_back, is_wait_for_not_uniqe_element_visibility=True
            )

            self.delay(220)

            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False

    # --
    # ...
    # --

    @BaseChapter.wait_for(
        element_for_waiting_until_visible="frm_vendor_bank_accounts",
        type_of_element="text_to_search",
    )
    @BaseChapter.log
    def delete(self) -> bool:

        try:

            self.click_button(self.elements.btn_delete)

            if self.lightbox(action="Yes"):
                self.click_button(self.elements.btn_back)

            self.delay(220)

            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False

    # --
    # ...
    # --

    @BaseChapter.wait_for(
        element_for_waiting_until_visible="frm_vendor_bank_accounts",
        type_of_element="text_to_search",
    )
    @BaseChapter.log
    def back(self) -> bool:

        try:

            self.click_button(self.elements.btn_back)

            if self.lightbox(action="Yes"):
                self.click_button(self.elements.btn_back)

            self.delay(220)

            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False
