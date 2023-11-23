import json
from alloy_python.embedded.logs import Logs

logs = Logs()
logs.set_user_id("example_user_id")  # Replace with a valid user ID

workflow_id = "example_workflow_id"  # Replace with a valid workflow ID
execution_id = "example_execution_id"  # Replace with a valid execution ID
response_data = logs.rerun_workflow_execution(workflow_id, execution_id)

print(json.dumps(response_data, indent=4))
