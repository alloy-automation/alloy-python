import json
import os
from alloy_python.embedded import Embedded

# Retrieve API key from environment variable
api_key = os.environ.get('ALLOY_API_KEY')
if not api_key:
    raise EnvironmentError("API key not found. Set the ALLOY_API_KEY environment variable.")

# Initialize the Embedded class with the API key
embedded = Embedded(api_key)

# Set user ID and rerun workflow execution
embedded.Logs.set_user_id("example_user_id")  # Replace with a valid user ID
workflow_id = "example_workflow_id"  # Replace with a valid workflow ID
execution_id = "example_execution_id"  # Replace with a valid execution ID
response_data = embedded.Logs.rerun_workflow_execution(workflow_id, execution_id)

print(json.dumps(response_data, indent=4))
