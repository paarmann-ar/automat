from test_applications.d_365.chapters.finance_chapter.unit_testcases.browser.browser import (
    Browser,
)
from test_applications.d_365.chapters.finance_chapter.unit_testcases.login.login import (
    Login,
)
from test_applications.d_365.chapters.finance_chapter.user_story.epics.import_and_post_free_text_invoice import (
    ImportAndPostFreeTextInvoice,
)

# --
# ...
# --

if __name__ == "__main__":
    Browser().open_browser()
    Login().login()

    import_free_text_invoice = ImportAndPostFreeTextInvoice()
    import_free_text_invoice.import_and_post_free_text_invoice()