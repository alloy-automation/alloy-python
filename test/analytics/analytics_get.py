import json
import os
from alloy_python.embedded.analytics import Analytics

# Retrieve API key from environment variable
api_key = os.environ.get('ALLOY_API_KEY')
if not api_key:
    raise EnvironmentError("API key not found. Set the ALLOY_API_KEY environment variable.")

# Create an instance of the Analytics class using the API key
analytics = Analytics(api_key)

# Example workflow ID - replace with a valid ID for your use case
workflow_id = "653bddcc28065599abd74ac0"

# Get analytics data
response_data = analytics.get(workflow_id)

# Pretty-print the JSON response
formatted_json = json.dumps(response_data, indent=4)
print(formatted_json)
