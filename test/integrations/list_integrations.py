import json
import os
from alloy_python.embedded import Embedded

# Retrieve API key from environment variable
api_key = os.environ.get('ALLOY_API_KEY')
if not api_key:
    raise EnvironmentError("API key not found. Set the ALLOY_API_KEY environment variable.")

# Initialize the Embedded class with the API key
embedded = Embedded(api_key)

# Set user ID and list integrations
embedded.Integration.set_user_id("651b7f858665f0e875a88a00")  # Replace with a valid user ID
response_data = embedded.Integration.list_integrations()

# Pretty-print the JSON response
formatted_json = json.dumps(response_data, indent=4)
print(formatted_json)
