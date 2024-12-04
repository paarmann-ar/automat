from typing import Any
from test_applications.d_365.core.object_provider import ObjectProvider
from test_applications.d_365.core.base import Base


# --
# ...
# --


class BlockingMessage(Base):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.elements = self.get_elements()
        print(__class__.__name__, id(__class__))

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
    # ...
    # --

    def __call__(
        self, is_visible_blocking_message=False, action="wait_for_disappeared"
    ) -> bool:

        try:

            if is_visible_blocking_message:
                if (
                    self.get_attribute_value(
                        self.elements.blocking_message_parent,
                        "style",
                        is_wait_for_visibility=False,
                    )
                    != "'display: true;'"
                ):
                    return True
                else:
                    raise Exception("blocking_message is not visible")

            match action:
                case "wait_for_disappeared":
                    while (
                        self.get_attribute_value(
                            self.elements.blocking_message_parent,
                            "style",
                            is_wait_for_visibility=False,
                        )
                        != "display: none;"
                    ):
                        self.delay(1000, '\n\n ***** \nwait for Blocking Message disappeared\n*****\n\n')

                    while (
                        self.get_attribute_value(
                            self.elements.blocking_message_child,
                            "style",
                            is_wait_for_visibility=False,
                        )
                        != "display: none;"
                    ):
                        self.delay(1000, '\n\n ***** \nwait for Blocking Message disappeared\n*****\n\n')

                    return True

            raise Exception("blocking_message notfound or have no this method")

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False
