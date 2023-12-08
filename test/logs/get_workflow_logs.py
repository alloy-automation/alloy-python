import json
import os
from alloy_python.embedded import Embedded

# Retrieve API key from environment variable
api_key = os.environ.get('ALLOY_API_KEY')
if not api_key:
    raise EnvironmentError("API key not found. Set the ALLOY_API_KEY environment variable.")

# Initialize the Embedded class with the API key
embedded = Embedded(api_key)

# Set user ID and get workflow logs
embedded.Logs.set_user_id("652f0b8852f08e6c8bb11834")  # Replace with a valid user ID
workflow_id = "65454636ca49e544e42ff2a1"  # Replace with a valid workflow ID
response_data = embedded.Logs.get_workflow_logs(workflow_id)

print(json.dumps(response_data, indent=4))
