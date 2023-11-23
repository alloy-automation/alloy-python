import json
from alloy_python.embedded.workflows import Workflows

workflows = Workflows()
workflows.set_user_id("example_user_id")  # Replace with a valid user ID

workflow_id = "example_workflow_id"  # Replace with a valid workflow ID
response_data = workflows.upgrade(workflow_id)

print(json.dumps(response_data, indent=4))
