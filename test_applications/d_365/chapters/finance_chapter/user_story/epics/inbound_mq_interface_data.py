from typing import Any
from test_applications.d_365.core.object_provider import ObjectProvider
from test_applications.d_365.chapters.core.base_chapter import BaseChapter
from test_applications.d_365.chapters.core.base_user_story import BaseUserStory
from test_applications.d_365.chapters.finance_chapter.unit_testcases.toolbars.toolbars import (
    Toolbars,
)
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.common.inquiries.mq.inbound_mq_interface_data_top_gadget import InboundMqInterfaceDataTopGadget
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.common.inquiries.mq.inbound_mq_interface_data_standard_view import InboundMqInterfaceDataStandardView
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.common.inquiries.mq.inbound_mq_messages_standard_view import InboundMqMessagesStandardView
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.common.inquiries.mq.inbound_mq_messages_top_gadget import InboundMqMessagesTopGadget


# --
# ...
# --


class InboundMqInterfaceData(BaseChapter, BaseUserStory):
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
            self.inbound_mq_interface_data_top_gadget = InboundMqInterfaceDataTopGadget()
            self.inbound_mq_interface_data_standard_view = InboundMqInterfaceDataStandardView()

            self.inbound_mq_messages_standard_view = InboundMqMessagesStandardView()
            self.inbound_mq_messages_top_gadget = InboundMqMessagesTopGadget()

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
    def collection_letter(self) -> bool:

        try:

            self.toolbars.change_mandant()
            self.toolbars.search_for_a_page = ("Inbound MQ interface data", True)
            self.toolbars.set_text_in_search_for_a_page()

            self.inbound_mq_interface_data_standard_view.incoming_message_id = None
            self.inbound_mq_interface_data_standard_view.select_incoming_message_id()

            self.inbound_mq_messages_standard_view.incoming_message_id = None
            self.inbound_mq_messages_standard_view.select_incoming_message_id()

            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False