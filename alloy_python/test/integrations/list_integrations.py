import json
from alloy_python.embedded.integrations import Integration

# Instantiate the Integration class
integration = Integration()
integration.set_user_id("651b7f858665f0e875a88a00")  # Replace with a valid user ID

# List integrations
response_data = integration.list_integrations()

# Pretty-print the response
print(json.dumps(response_data, indent=4))
