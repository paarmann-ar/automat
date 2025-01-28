from toolboxs.decorators import singleton
from continuous_integration.screen_recorder.controller.screen_recorder_controller import (
    ScreenRecoderController,
)
from continuous_integration.aqua_api.aqua_adaptor.aqua_adaptor import AquaAdaptor
from continuous_integration.aqua_api.aqua_api.aqua_api import AquaApi
# --
# ...
# --
@singleton
class ContinuousIntegrationProvider:
    def __init__(self):

        self.screen_recorder = ScreenRecoderController().instance
        self.aqua_adapter = AquaAdaptor().instance
        self.aqua_api = AquaApi().instance

