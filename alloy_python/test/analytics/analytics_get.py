import json
from alloy_python.embedded.analytics import Analytics

# Create an instance of the Analytics class using the default API key
analytics = Analytics()

# Example workflow ID - replace with a valid ID for your use case
workflow_id = "653bddcc28065599abd74ac0"

# Get analytics data
response_data = analytics.get(workflow_id)

# Pretty-print the JSON response
formatted_json = json.dumps(response_data, indent=4)
print(formatted_json)
