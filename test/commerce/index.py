# test/commerce/commerce.py
import json
import os
from alloy_python.uapi import UAPI
from alloy_python.uapi.commerce import Commerce

# Retrieve API key from environment variable
api_key = os.environ.get('ALLOY_API_KEY')
connection_id = os.environ.get('ALLOY_CONNECTION_ID')

if not api_key:
    raise EnvironmentError("API key not found. Set the ALLOY_API_KEY environment variable.")

# Initialize with the retrieved API key
commerce = Commerce(api_key, connection_id)

# Use the App service
response_data = commerce.list_customers()

# Pretty-print the JSON response
formatted_json = json.dumps(response_data, indent=4)
print(formatted_json)
