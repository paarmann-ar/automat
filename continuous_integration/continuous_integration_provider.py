from toolboxs.decorators import singleton
from continuous_integration.screen_recorder.controller.screen_recorder_controller import (
    ScreenRecoderController,
)
import time
from multiprocessing import Process

# --
# ...
# --
@singleton
class ContinuousIntegrationProvider:
    def __init__(self):

        self.screen_recorder = ScreenRecoderController().instance

