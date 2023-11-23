import json
from alloy_python.embedded.integrations import Integration

integration = Integration()
integration.set_user_id("651b7f858665f0e875a88a00")  # Replace with a valid user ID

integration_id = "65454632ca49e544e42ff292"  # Replace with a valid integration ID
response_data = integration.get_integration(integration_id)

print(json.dumps(response_data, indent=4))
