from test_applications.d_365.core.object_provider import ObjectProvider
from test_applications.d_365.chapters.core.base_chapter import BaseChapter
from typing import Any
from test_applications.d_365.abstrct_classes.form.form import Form

# --
# ...
# --


class EmailParametersSmtpSetting(BaseChapter, Form):
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
                    self.email_parameters_smtp_setting()

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
        outgoing_mail_server=("smtp-qs.redteclab.de", True),
        smtp_port_number=("44587", True),
        is_ssl_tls_required=(True, True),
        environment_email_recipient=("viktoriia.shvydenko@redcare-pharmacy.com", True),
        environment_email_subject=("UAT", True),
        is_authentication_required=(True, True),
        username=("D365", True),
        password=("", False),
    ) -> bool:

        try:

            if super().prepare():
                return True

            self.outgoing_mail_server = outgoing_mail_server
            self.smtp_port_number = smtp_port_number
            self.is_ssl_tls_required = is_ssl_tls_required
            self.environment_email_recipient = environment_email_recipient
            self.environment_email_subject = environment_email_subject
            self.is_authentication_required = is_authentication_required
            self.username = username
            self.password = password

            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False

    # --
    # ... methods
    # --

    @BaseChapter.wait_for(
        element_for_waiting_until_visible="frm_email_parameters_smtp_setting",
        type_of_element="text_to_search",
    )
    @BaseChapter.log
    def email_parameters_smtp_setting(self, **kwargs) -> bool:

        try:

            self.textbox(
                self.elements.txb_outgoing_mail_server, self.outgoing_mail_server
            )
            self.textbox(self.elements.txb_smtp_port_number, self.smtp_port_number)
            self.chkbox(self.elements.chk_ssl_tls_required, self.is_ssl_tls_required)
            self.textbox(
                self.elements.txb_environment_email_recipient,
                self.environment_email_recipient,
            )
            self.textbox(
                self.elements.txb_environment_email_subject,
                self.environment_email_subject,
            )
            self.chkbox(
                self.elements.chk_authentication_required, self.is_authentication_required
            )
            self.textbox(self.elements.txb_username, self.username)
            self.textbox(self.elements.txb_password, self.password)

            self.delay(220)

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False
