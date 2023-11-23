import json
from alloy_python.embedded.workflows import Workflows

workflows = Workflows()
workflows.set_user_id("651b7f858665f0e875a88a00")  # Replace with a valid user ID

response_data = workflows.list()

print(json.dumps(response_data, indent=4))
