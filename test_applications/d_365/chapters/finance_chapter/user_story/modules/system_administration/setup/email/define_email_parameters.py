from typing import Any
from test_applications.d_365.core.object_provider import ObjectProvider
from test_applications.d_365.chapters.core.base_chapter import BaseChapter
from test_applications.d_365.chapters.core.base_user_story import BaseUserStory
from test_applications.d_365.chapters.finance_chapter.unit_testcases.toolbars.toolbars import (
    Toolbars,
)
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.system_administration.setup.email.email_parameters.email_parameters_configuration.email_parameters_configuration_manager import (
    EmailParametersConfigurationManager,
)
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.system_administration.setup.email.email_parameters.email_parameters_side_gadget import (
    EmailParametersSideGadget,
)
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.system_administration.setup.email.email_parameters.email_parameters_smtp_setting import (
    EmailParametersSmtpSetting,
)
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.system_administration.setup.email.email_parameters.email_parameters_microsoft_graph_settings import (
    EmailParametersMicrosoftGraphSettings,
)
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.system_administration.setup.email.email_parameters.email_parameters_test_email import (
    EmailParametersTestEmail,
)
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.system_administration.setup.email.email_parameters.email_parameters_top_gadget import (
    EmailParametersTopGadget,
)
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.system_administration.setup.email.email_parameters.email_parameters_manager import (
    EmailParametersManager,
)

# --
# ...
# --


class DefineEmailParameters(BaseChapter, BaseUserStory):
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

            self.toolbars = Toolbars()
            self.email_parameters_top_gadget = EmailParametersTopGadget()
            self.email_parameters_side_gadget = EmailParametersSideGadget()
            self.email_parameters_manager = EmailParametersManager()
            self.email_parameters_configuration_manager = (
                EmailParametersConfigurationManager()
            )
            self.email_parameters_smtp_setting = EmailParametersSmtpSetting()
            self.email_parameters_microsoft_graph_settings = (
                EmailParametersMicrosoftGraphSettings()
            )
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

    @BaseChapter.log
    def define_email_parameters(self) -> bool:

        try:

            self.toolbars.change_mandant()

            self.toolbars.search_for_a_page = ("Email parameters", True)
            self.toolbars.set_text_in_search_for_a_page()

            self.delay(220)

            self.email_parameters_side_gadget.email_parameters_configuration()
            self.delay(220)
            self.email_parameters_configuration_manager.email_parameters_configuration(
                    step_10 = "tab_general",
                    step_20 = "tab_enabled_interactive_email_providers",
                    step_30 = "tab_email_history",
                    step_40 = "tab_throttling",
            )

            self.email_parameters_side_gadget.email_parameters_smtp_setting()
            self.email_parameters_smtp_setting.email_parameters_smtp_setting()
            self.delay(220)

            self.email_parameters_side_gadget.email_parameters_microsoft_graph_settings()
            self.email_parameters_microsoft_graph_settings.email_parameters_microsoft_graph_settings()
            self.delay(220)

            self.email_parameters_side_gadget.email_parameters_test_email()
            self.email_parameters_test_email.email_parameters_test_email()
            self.delay(220)

            self.email_parameters_top_gadget.save_email_parameters()
            self.delay(220)

            self.email_parameters_top_gadget.back_email_parameters()
            self.delay(220)

            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False
