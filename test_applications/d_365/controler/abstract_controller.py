from terminal.server.server_api.terminal_api import Terminal_API
from multiprocessing import Process
from continuous_integration.continuous_integration_provider import (
    ContinuousIntegrationProvider,
)
import test_applications.d_365.controler.userstory_pytest as userstory_pytest

# --
# ...
# --

if __name__ == "__main__":
    ...
    screen_recorder = ContinuousIntegrationProvider().screen_recorder
    # terminal_api = Terminal_API()
    # terminal_api.start()

    start_recording = Process(target=screen_recorder.start_recording)
    stop_recording = Process(target=screen_recorder.stop_recording)

    # userstory_pytest = Process(target= userstory_pytest.run_pytest)
    
    start_recording.start()
    start_recording.join()

    # userstory_pytest.start()
    # userstory_pytest.join()

    stop_recording.start()
    stop_recording.join()