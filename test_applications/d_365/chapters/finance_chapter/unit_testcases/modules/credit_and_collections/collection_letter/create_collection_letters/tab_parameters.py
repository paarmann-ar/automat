from typing import Any
from test_applications.d_365.core.object_provider import ObjectProvider
from test_applications.d_365.chapters.core.base_chapter import BaseChapter
from test_applications.d_365.abstrct_classes.tab.tab import Tab
from datetime import date

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
        is_invoice=(True, True),
        is_credit_note=(True, True),
        is_payment=(False, True),
        is_interest=(False, True),
        collectionc_letter=("", False),
        collection_letter_date=("", True),
        use_posting_profile_from=("Account", False),
        posting_profile=("STD", False),
    ) -> bool:

        try:

            if super().prepare():
                return True

            self.is_invoice = is_invoice
            self.is_credit_note = is_credit_note
            self.is_payment = is_payment
            self.is_interest = is_interest
            self.collectionc_letter = collectionc_letter

            self.collection_letter_date = date.today().strftime(r"%m.%d.%Y"), (
                collection_letter_date[1]
                if collection_letter_date[0] == ""
                else collection_letter_date[1]
            )

            self.use_posting_profile_from = use_posting_profile_from
            self.posting_profile = posting_profile

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
    def tab_parameters(self) -> bool:

        try:

            self.checkbox(self.elements.chk_invoice, self.is_invoice)
            self.checkbox(self.elements.chk_credit_note, self.is_credit_note)
            self.checkbox(self.elements.chk_payment, self.is_payment)
            self.checkbox(self.elements.chk_interest, self.is_interest)
            self.textbox(self.elements.txb_collectionc_letter, self.collectionc_letter)
            self.textbox(
                self.elements.dt_collection_letter_date, self.collection_letter_date
            )
            self.textbox(
                self.elements.cmb_use_posting_profile_from,
                self.use_posting_profile_from,
                is_press_enter=True,
            )
            self.textbox(
                self.elements.cmb_posting_profile,
                self.posting_profile,
                is_press_enter=True,
            )

            self.delay(220)

            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False
