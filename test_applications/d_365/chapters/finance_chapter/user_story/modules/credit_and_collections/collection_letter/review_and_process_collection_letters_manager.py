from typing import Any
from test_applications.d_365.core.object_provider import ObjectProvider
from test_applications.d_365.chapters.core.base_chapter import BaseChapter
from test_applications.d_365.chapters.core.base_user_story import BaseUserStory
from test_applications.d_365.chapters.finance_chapter.unit_testcases.toolbars.toolbars import (
    Toolbars,
)
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.credit_and_collections.collection_letter.review_and_process_collection_letters.review_and_process_collection_letters_standard_view import (
    ReviewAndProcessCollectionLettersStandardView,
)
from test_applications.d_365.chapters.finance_chapter.unit_testcases.modules.credit_and_collections.collection_letter.review_and_process_collection_letters.review_and_process_collection_letters_top_gadget import (
    ReviewAndProcessCollectionLettersTopGadget,
)


# --
# ...
# --

class ReviewAndProcessCollectionLettersManager(BaseChapter, BaseUserStory):
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
            self.review_and_process_collection_letters_standard_view = (
                ReviewAndProcessCollectionLettersStandardView()
            )
            self.review_and_process_collection_letters_top_gadget = (
                ReviewAndProcessCollectionLettersTopGadget()
            )

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
    def review_and_process_collection_letters(self) -> bool:

        try:

            self.toolbars.change_mandant(mandant=("139", True))

            self.toolbars.search_for_a_page = (
                "Review and process collection letters",
                True,
            )
            self.toolbars.set_text_in_search_for_a_page()

            self.delay(220)

#----
            self.review_and_process_collection_letters_standard_view.select_customer_account()
            self.review_and_process_collection_letters_top_gadget.back()

            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False
