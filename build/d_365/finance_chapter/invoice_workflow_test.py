from multiprocessing import Process
from toolboxs.toolbox import Toolbox
from continuous_integration.continuous_integration_provider import (
    ContinuousIntegrationProvider
)
from test_applications.d_365.chapters.finance_chapter.unit_testcases.browser.browser import (
    Browser
)
from test_applications.d_365.chapters.finance_chapter.unit_testcases.login.login import (
    Login
)
from test_applications.d_365.chapters.finance_chapter.user_story.epics.invoice_workflow.invoice_workflow import (
    InvoiceWorkflow,
)

# --
# ...
# --

def userstory():
    Browser().open_browser()
    Login().login()

    invoice_workflow = InvoiceWorkflow()
    invoice_workflow.state['dict_importet_moduls'] = Toolbox().get_import_moduls()
    invoice_workflow.invoice_workflow()

# --
# ...
# --

if __name__ == "__main__":
    screen_recorder = ContinuousIntegrationProvider().screen_recorder

    start_recording_process = Process(target=screen_recorder.start_recording)
    stop_recording_process = Process(target=screen_recorder.stop_recording)

    userstory_process = Process(target=userstory)

    start_recording_process.start()

    userstory_process.start()
    userstory_process.join()

    stop_recording_process.start()
    stop_recording_process.join()
