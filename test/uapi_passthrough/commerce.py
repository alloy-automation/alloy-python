# test/uapi_commerce/passthrough.py
import json
import os
from alloy_python.uapi.commerce import Commerce

api_key = os.environ.get('ALLOY_API_KEY')
connection_id = os.environ.get('ALLOY_CONNECTION_ID')

if not api_key or not connection_id:
    raise EnvironmentError("API key and Connection ID must be set.")

commerce = Commerce(api_key)
commerce.connect(connection_id)

# Example passthrough request to an external API endpoint
response = commerce.passthrough_request(
    method="GET",
    endpoint="/customers.json",  # Replace with a valid endpoint
    query={"limit": 10}
)

print(json.dumps(response, indent=4))
