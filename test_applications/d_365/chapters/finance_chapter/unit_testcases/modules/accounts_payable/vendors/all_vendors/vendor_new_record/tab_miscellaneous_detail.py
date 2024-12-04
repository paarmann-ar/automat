from typing import Any
from test_applications.d_365.core.object_provider import ObjectProvider
from test_applications.d_365.chapters.core.base_chapter import BaseChapter
from test_applications.d_365.abstrct_classes.tab.tab import Tab

# --
# ...
# --


class TabMiscellaneousDetail(BaseChapter, Tab):
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
                    self.tab_miscellaneous_detail()

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
        Credit_rating=("", True),
        creadit_limit=("", True),
        buyer_group=("", True),
        vendor_hold=("", True),
        reason_code=("", True),
        is_intercompany_active=(True, True),
        company=("", True),
        customer_account=("", True),
        vendor_rebate_group=("", True),
        is_public_sector=(True, True),
        Procurement_category=("1370600", True),
    ) -> bool:

        try:

            if super().prepare():
                return True

            self.Credit_rating = (
                self.get_random(type="int"),
                Credit_rating[1] if Credit_rating[0] == "" else Credit_rating[1],
            )
            self.creadit_limit = (
                self.get_random(type="int"),
                creadit_limit[1] if creadit_limit[0] == "" else creadit_limit[1],
            )
            self.buyer_group = buyer_group
            self.vendor_hold = vendor_hold
            self.reason_code = reason_code
            self.is_intercompany_active = is_intercompany_active
            self.company = company
            self.customer_account = customer_account
            self.vendor_rebate_group = vendor_rebate_group
            self.is_public_sector = is_public_sector
            self.Procurement_category = Procurement_category
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
    def tab_miscellaneous_detail(self) -> bool:

        try:

            self.textbox(self.elements.txb_Credit_rating, self.Credit_rating)
            self.textbox(self.elements.txb_creadit_limit, self.creadit_limit)
            self.components.combobox_type_2(
                self.elements.cmb_buyer_group, self.buyer_group
            )
            self.textbox(self.elements.txb_vendor_hold, self.vendor_hold)
            self.textbox(self.elements.txb_reason_code, self.reason_code)
            self.checkbox(
                self.elements.chk_intercompany_active, self.is_intercompany_active
            )
            self.textbox(self.elements.txb_company, self.company)
            self.textbox(self.elements.txb_customer_account, self.customer_account)
            self.components.combobox_type_2(
                self.elements.cmb_vendor_rebate_group, self.vendor_rebate_group
            )
            self.checkbox(self.elements.chk_public_sector, self.is_public_sector)
            self.textbox(
                self.elements.cmb_Procurement_category,
                self.Procurement_category,
                is_press_enter=True,
            )

            self.delay(220)

            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False
