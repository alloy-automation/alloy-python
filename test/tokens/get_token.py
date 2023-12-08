import json
import os
from alloy_python.embedded import Embedded

# Retrieve API key from environment variable
api_key = os.environ.get('ALLOY_API_KEY')
if not api_key:
    raise EnvironmentError("API key not found. Set the ALLOY_API_KEY environment variable.")

# Initialize the Embedded class with the API key
embedded = Embedded(api_key)

# Set user ID and get tokens
embedded.Tokens.set_user_id("651b7f858665f0e875a88a00")  # Replace with a valid user ID
response_data = embedded.Tokens.get()

print(json.dumps(response_data, indent=4))
