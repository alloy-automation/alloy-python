import json
from alloy_python.embedded.credentials import Credentials

# Instantiate the Credentials class
credentials = Credentials()
credentials.set_user_id("651b7f858665f0e875a88a00")  # Replace with a valid user ID

# List user credentials
response_data = credentials.list_user_credentials()

# Pretty-print the response
print(json.dumps(response_data, indent=4))
