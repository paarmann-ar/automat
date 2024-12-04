from test_applications.d_365.core.object_provider import ObjectProvider
from test_applications.d_365.chapters.core.base_chapter import BaseChapter
from typing import Any
from test_applications.d_365.abstrct_classes.form.form import Form
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.system_administration.setup.email.email_parameters.email_parameters_top_gadget import EmailParametersTopGadget
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.system_administration.setup.email.email_parameters.email_parameters_microsoft_graph_settings import EmailParametersMicrosoftGraphSettings
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.system_administration.setup.email.email_parameters.email_parameters_side_gadget import EmailParametersSideGadget
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.system_administration.setup.email.email_parameters.email_parameters_smtp_setting import EmailParametersSmtpSetting
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.system_administration.setup.email.email_parameters.email_parameters_test_email import EmailParametersTestEmail


# --
# ...
# --


class EmailParametersManager(BaseChapter, Form):
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
                    self.email_parameters_configuration()

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

            self.email_parameters_top_gadget = EmailParametersTopGadget()
            self.email_parameters_microsoft_graph_settings = EmailParametersMicrosoftGraphSettings()
            self.email_parameters_side_gadget = EmailParametersSideGadget()
            self.email_parameters_smtp_setting = EmailParametersSmtpSetting()
            self.email_parameters_test_email = EmailParametersTestEmail()
        
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
    ) -> bool:

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
        element_for_waiting_until_visible="frm_email_parameters",
        type_of_element="text_to_search",
    )
    @BaseChapter.log
    def email_parameters(self, **kwargs) -> bool:

        try:

            for _, tab in kwargs.items():
                match tab:
                    case "email_parameters_top_gadget":
                        self.email_parameters_top_gadget()

                    case "email_parameters_side_gadget":
                        self.email_parameters_side_gadget()
                        
                    case "email_parameters_microsoft_graph_settings":
                        self.email_parameters_microsoft_graph_settings.email_parameters_microsoft_graph_settings()

                    case "email_parameters_smtp_setting":
                        self.email_parameters_smtp_setting.email_parameters_smtp_setting()

                    case "email_parameters_test_email":
                        self.email_parameters_test_email.email_parameters_test_email()
            
                    case _:
                        pass

            self.delay(220)

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False
