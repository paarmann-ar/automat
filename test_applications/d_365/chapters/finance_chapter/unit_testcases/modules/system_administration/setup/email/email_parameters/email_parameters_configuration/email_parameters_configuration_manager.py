from test_applications.d_365.core.object_provider import ObjectProvider
from test_applications.d_365.chapters.core.base_chapter import BaseChapter
from typing import Any
from test_applications.d_365.abstrct_classes.form.form import Form
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.system_administration.setup.email.email_parameters.email_parameters_configuration.tab_general import TabGeneral
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.system_administration.setup.email.email_parameters.email_parameters_configuration.tab_enabled_interactive_email_providers import TabEnabledInteractiveEmailProviders
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.system_administration.setup.email.email_parameters.email_parameters_configuration.tab_email_history import TabEmailHistory
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.system_administration.setup.email.email_parameters.email_parameters_configuration.tab_throttling import TabThrottling
from test_applications.d_365.abstrct_classes.page.page import Page

# --
# ...
# --

class EmailParametersConfigurationManager(BaseChapter, Page):
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

            return self

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

            self.tab_general = TabGeneral()
            self.tab_enabled_interactive_email_providers = TabEnabledInteractiveEmailProviders()
            self.tab_email_history = TabEmailHistory()
            self.tab_throttling = TabThrottling()

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
    def email_parameters_configuration(self, **kwargs) -> bool:

        try:


            for _, tab in kwargs.items():
                match tab:
                    case "tab_general":
                        self.tab_general()
                        
                    case "tab_enabled_interactive_email_providers":
                        self.tab_enabled_interactive_email_providers()

                    case "tab_email_history":
                        self.tab_email_history()

                    case "tab_throttling":
                        self.tab_throttling()

                    case _:
                        pass

            self.delay(220)

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False