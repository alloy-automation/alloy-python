import json
from alloy_python.embedded.workflows import Workflows

workflows = Workflows()
workflows.set_user_id("651b82608665f0e875a88e81")  # Replace with a valid user ID

response_data = workflows.deactivate_all()

print(json.dumps(response_data, indent=4))
