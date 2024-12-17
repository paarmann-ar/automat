from typing import Any
from test_applications.d_365.core.object_provider import ObjectProvider
from test_applications.d_365.chapters.core.base_chapter import BaseChapter
from test_applications.d_365.chapters.core.base_user_story import BaseUserStory
from test_applications.d_365.chapters.finance_chapter.unit_testcases.toolbars.toolbars import (
    Toolbars,
)
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.credit_and_collections.collection_letter.review_and_process_collection_letters.review_and_process_collection_letters_manager import (
    ReviewAndProcessCollectionLettersManager,
)
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.credit_and_collections.collection_letter.create_collection_letters.create_collection_letters_manager import (
    CreateCollectionLettersManager,
)
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.credit_and_collections.collection_letter.customers.all_customers.all_customers_standard_view import (
    AllCustomersStandardView,
)
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.credit_and_collections.collection_letter.customers.all_customers.all_customers_top_gadget import (
    AllCustomersTopGadget,
)
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.system_administration.periodic_tasks.email_processing.email_distributor_batch.email_distributor_batch_manager import (
    EmailDistributorBatchManager,
)
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.system_administration.setup.email.inquiries.email_history.email_history_top_gadget import (
    EmailHistoryTopGadget,
)
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.system_administration.periodic_tasks.email_processing.batch_email_sending_status.batch_email_sending_status_standard_view import (
    BatchEmailSendingStatusStandardView,
)
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.system_administration.periodic_tasks.email_processing.batch_email_sending_status.batch_email_sending_status_top_gadget import (
    BatchEmailSendingStatusTopGadget,
)
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.system_administration.periodic_tasks.email_processing.batch_email_sending_status.email_identifier.email_identifier import (
    EmailIdentifier,
)


# --
# ...
# --


class CollectionLetter(BaseChapter, BaseUserStory):
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
        return ObjectProvider()(
            __file__.replace(".py", ".json ", -1).replace("\\", "/").replace(" c", "")
        )

    # --
    # ... setup, teardown and prepare
    # --

    def __setup(self) -> bool:

        try:

            super().setup()

            self.toolbars = Toolbars()
            self.create_collection_letters_manager = CreateCollectionLettersManager()

            self.review_and_process_collection_letters_manager = (
                ReviewAndProcessCollectionLettersManager()
            )
            self.email_distributor_batch_manager = EmailDistributorBatchManager()
            self.all_customers_standard_view = AllCustomersStandardView()
            self.all_customers_top_gadget = AllCustomersTopGadget()

            self.email_history_top_gadget = EmailHistoryTopGadget()

            self.batch_email_sending_status_standard_view = (
                BatchEmailSendingStatusStandardView()
            )
            self.batch_email_sending_status_top_gadget = (
                BatchEmailSendingStatusTopGadget()
            )

            self.email_identifier = EmailIdentifier()

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

            self.state["find_collection_letter_by_email_description"] = "find this description in Collection Letter"
            
            self.toolbars.change_mandant()

            self.create_collection_letters_manager(
                step_10="tab_parameters",
                step_20="tab_records_to_include",
                step_30="tab_run_in_the_background",
                step_40="save",
            )

            self.review_and_process_collection_letters_manager(
                step_10="select_customer_account",
                step_20="back",
            )

            self.email_distributor_batch_manager(
                step_10="tab_run_in_the_background",
                step_20="save",
            )

            self.toolbars.search_for_a_page = ("All customers", True)
            self.toolbars.full_address = "Accounts receivable > Customers"
            self.toolbars.set_full_address_in_search_for_a_page()
            
            self.delay(220)

            self.all_customers_standard_view.account_number = "D13900000016"
            self.all_customers_standard_view.select_customer_account_number()

            self.all_customers_top_gadget.all_customers_customer_email_history()
            self.email_history_top_gadget.email_detail()

            self.batch_email_sending_status_standard_view.select_email_description()
            self.batch_email_sending_status_top_gadget.show_message()

            self.email_identifier()

            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False