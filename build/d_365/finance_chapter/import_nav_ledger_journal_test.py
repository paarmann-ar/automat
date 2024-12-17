from multiprocessing import Process
from continuous_integration.continuous_integration_provider import (
    ContinuousIntegrationProvider,
)
from test_applications.d_365.chapters.finance_chapter.unit_testcases.browser.browser import (
    Browser,
)
from test_applications.d_365.chapters.finance_chapter.unit_testcases.login.login import (
    Login,
)

# --
# ...
# --

def userstory():
    Browser().open_browser()
    Login().login()

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
