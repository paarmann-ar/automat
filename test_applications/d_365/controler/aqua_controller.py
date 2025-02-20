from continuous_integration.continuous_integration_provider import (
    ContinuousIntegrationProvider,
)


aqua_api = ContinuousIntegrationProvider().aqua_api
aqua_adapter = ContinuousIntegrationProvider().aqua_adapter

#################################

aqua_adapter.complate_maping_from_framework_to_aqua()

#################################

# test execute
# aqua_api.update_api("project")

# test_execute_api = aqua_api.test_execute_api

# test_execute_api.test_execute_teststep_index = 1
# test_execute_api.testcase_id = 48952

# test_execute_api.create_test_execute_teststep_object()
# test_execute_api.create_test_execute_object()

# test_execute_api.send_test_execute()