import json
from alloy_python.embedded.workflows import Workflows

workflows = Workflows()
workflows.set_user_id("652f0b8852f08e6c8bb11834")  # Replace with a valid user ID

workflow_id = "65454636ca49e544e42ff2a1"  # Replace with a valid workflow ID
response_data = workflows.activate(workflow_id)

print(json.dumps(response_data, indent=4))
