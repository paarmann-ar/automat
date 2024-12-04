from typing import Any
from test_applications.d_365.core.object_provider import ObjectProvider
from test_applications.d_365.core.base import Base

# --
# ...
# --


class Alert(Base):
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

            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False

    # --
    # ... make delay untis that messagebox dispaire
    # --

    def __call__(self, alert, operation="delay", is_log_exception=True) -> bool:

        try:

            match alert:
                case "please_wait_processing_your_request":
                    while self.wait_for_visibility(
                        self.elements.alert_please_wait_processing_your_request
                    ):
                        self.delay(220)

                case "is_please_wait_processing_your_request":
                    return self.driver.find_element(
                        *self.elements.alert_please_wait_processing_your_request
                    )

            if operation == "delay":
                return True

            raise Exception("alert notfound or have no this method")

        except Exception as exp:
            if is_log_exception:
                self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False
