from test_applications.d_365.chapters.finance_chapter.unit_testcases.browser.browser import (
    Browser,
)
from continuous_integration.continuous_integration_provider import ContinuousIntegrationProvider
from continuous_integration.continuous_integration_provider import ContinuousIntegrationProvider


aqua_api = ContinuousIntegrationProvider().aqua_api
aqua_adapter = ContinuousIntegrationProvider().aqua_adapter


browser = Browser()
# aqua_api.update_api()
# aqua_adapter.complate_maping_folder_from_framework_to_aqua()
aqua_adapter.complate_maping_from_framework_to_aqua()

browser.open_browser()