from typing import Any
from test_applications.d_365.core.object_provider import ObjectProvider
from test_applications.d_365.chapters.core.base_chapter import BaseChapter
from test_applications.d_365.abstrct_classes.tab.tab import Tab

# --
# ...
# --


class TabContactInformation(BaseChapter, Tab):
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
                    self.tab_contact_information()

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
        telephone=("017221026640", True),
        extension=("", True),
        mobile_phone=("017221026640", True),
        pager=("017221026640", True),
        fax=("017221026640", True),
        email=("b@b.com", True),
        sms=("017221026640", True),
        internet_address=("www.b.b", True),
        telex_number=("017221026640", True),
        name_of_person=("heer biee", True),
    ) -> bool:

        try:

            if super().prepare():
                return True

            self.telephone = telephone
            self.extension = extension
            self.mobile_phone = mobile_phone
            self.pager = pager
            self.fax = fax
            self.email = email
            self.sms = sms
            self.internet_address = internet_address
            self.telex_number = telex_number
            self.name_of_person = name_of_person
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
    def tab_contact_information(self) -> bool:

        try:

            self.textbox(self.elements.txb_telephone.self.telephone)
            self.textbox(self.elements.txb_extension.self.extension)
            self.textbox(self.elements.txb_mobile_phone.self.mobile_phone)
            self.textbox(self.elements.txb_pager.self.pager)
            self.textbox(self.elements.txb_fax.self.fax)
            self.textbox(self.elements.txb_email.self.email)
            self.textbox(self.elements.txb_sms.self.sms)
            self.textbox(self.elements.txb_internet_address.self.internet_address)
            self.textbox(self.elements.txb_telex_number.self.telex_number)
            self.textbox(self.elements.txb_name_of_person.self.name_of_person)

            self.delay(220)

            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False
