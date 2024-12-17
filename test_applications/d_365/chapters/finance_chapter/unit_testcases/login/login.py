from test_applications.d_365.core.object_provider import ObjectProvider
from test_applications.d_365.chapters.core.base_chapter import BaseChapter
from typing import Any
from test_applications.d_365.core.ii_f_a import IIFA

# --
# ...
# --


class Login(BaseChapter):
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

    # username=("Dummy365F1@redcare-pharmacy.com", True),
    # password=("TR5QWgRXqLOW", True),
    # username=("Dummy365F2@redcare-pharmacy.com", True),
    # password=("pVrg2q5z7mAx", True),

    def __prepare(
        self,
        username=("Dummy365F1@redcare-pharmacy.com", True),
        password=("TR5QWgRXqLOW", True),
    ) -> bool:

        try:

            if super().prepare():
                return True

            self.username = username
            self.password = password

            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False

    # --
    # ...
    # --

    @BaseChapter.wait_for(element_for_waiting_until_visible="frm_login")
    @BaseChapter.log
    def login(self, is_use_iifa=True, is_wait_for_stay_signed_in =True) -> bool:

        try:

            self.state["current_username"], _ = self.username
            current_user, _ = self.username
            self.state["current_user"]= current_user.split("@")[0]

            self.textbox(self.elements.txb_username, self.username)
            self.click(self.elements.btn_submit)

            self.textbox(self.elements.txb_password, self.password)
            self.click(self.elements.btn_submit)

            if is_use_iifa:
                self.authentication_iifa()

            if is_wait_for_stay_signed_in:
                self.wait_for_element_visibility_by_text(self.elements.txt_stay_signed_in)

                self.click(self.elements.btn_submit)

            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False

    # --
    # ...
    # --

    @BaseChapter.log
    def authentication_iifa(self) -> bool:

        try:

            if self.is_element_there(self.elements.txt_stay_signed_in):
                return

            authentication_nummer = self.read_textbox(
                self.elements.lbl_authentication_nummer, "text"
            )
            print(f"authentication_nummer: {authentication_nummer}")

            self.click(self.elements.hl_i_canot_use_ma)
            self.delay(500)

            self.click(self.elements.lbl_use_a_verification_code)
            self.delay(500)

            IIFA()

            self.textbox(
                self.elements.txb_verification_code, (self.state["iifa"], True)
            )
            print(f"2fa is: {self.state["iifa"]}")
            self.state.pop("iifa")

            self.click_button(self.elements.btn_verifi)

            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False
