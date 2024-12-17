from test_applications.d_365.chapters.finance_chapter.unit_testcases.browser.browser import (
    Browser,
)
from test_applications.d_365.chapters.finance_chapter.unit_testcases.login.login import (
    Login,
)
from test_applications.d_365.chapters.finance_chapter.user_story.epics.invoice_workflow.invoice_workflow import (
    InvoiceWorkflow,
)


# --
# ...
# --

Browser().open_browser()
Login().login()

invoice_workflow = InvoiceWorkflow()
assert invoice_workflow.invoice_workflow()