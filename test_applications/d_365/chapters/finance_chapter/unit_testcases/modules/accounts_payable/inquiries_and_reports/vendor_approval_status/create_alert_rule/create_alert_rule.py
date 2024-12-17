from test_applications.d_365.core.object_provider import ObjectProvider
from test_applications.d_365.chapters.core.base_chapter import BaseChapter
from typing import Any
from test_applications.d_365.abstrct_classes.form.form import Form

# --
# ...
# --


class CreateAlertRule(BaseChapter, Form):
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
                    self.create_alert_rule()

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
        return ObjectProvider()(
            __file__.replace(".py", ".json ", -1).replace("\\", "/").replace(" c", "")
        )

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

    def __prepare(
        self,
        table_name=("Vendor Release Status Table", True),
        event=("Record has been created", True),
        subject=("Record has been created in Vendor Release Status Table", True),
        message=("pleas approve second approval", True),
        email_recipients=("Mohammad.Paarmann@redcare-pharmacy.com", True),
        is_send_email=(True, True),
    ) -> bool:

        try:

            if super().prepare():
                return True

            self.table_name = table_name
            self.event = event
            self.subject = subject
            self.message = message
            self.email_recipients = email_recipients
            self.is_send_email = is_send_email
            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False

    # --
    # ... methods
    # --

    @BaseChapter.wait_for(
        element_for_waiting_until_visible="frm_create_alert_rule",
        type_of_element="text_to_search",
    )
    @BaseChapter.log
    def create_alert_rule(self, **kwargs) -> bool:

        try:

            self.textbox(self.elements.cmb_table_name, self.table_name)
            self.textbox(self.elements.cmb_event, self.event)

            self.textbox(self.elements.txb_subject, self.subject)
            self.textbox(self.elements.txa_message, self.message)
            self.textbox(self.elements.txb_email_recipients, self.email_recipients)
            self.textbox(self.elements.chk_send_email, self.is_send_email)

            self.click_button(self.elements.btn_ok)
            self.delay(220)

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False
