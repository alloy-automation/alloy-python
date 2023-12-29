# test/uapi_passthrough/index.py
import json
import os
from alloy_python.uapi import UAPI
from alloy_python.uapi.passthrough import Passthrough

# Retrieve API key from environment variable
api_key = os.environ.get('ALLOY_API_KEY')
connection_id = os.environ.get('CONNECTION_ID')

if not api_key or not connection_id:
    raise EnvironmentError("API key or connection ID not found. Set the ALLOY_API_KEY and PASSTHROUGH_CONNECTION_ID environment variables.")

# Initialize with the retrieved API key
passthrough = Passthrough(api_key)
passthrough.connect(connection_id)

# Example Passthrough Request (Shopify List Customers)
method = "GET"
endpoint = "/customers.json"
response = passthrough.passthrough_request(method, endpoint)

formatted_response = json.dumps(response, indent=4)
print(formatted_response)
