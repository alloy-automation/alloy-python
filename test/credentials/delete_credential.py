import json
import os
from alloy_python.embedded import Embedded

api_key = os.environ.get('ALLOY_API_KEY')
if not api_key:
    raise EnvironmentError("API key not found. Set the ALLOY_API_KEY environment variable.")

embedded = Embedded(api_key)
embedded.Credentials.set_user_id("652f0b8852f08e6c8bb11834")  # Replace with a valid user ID

credential_id = "6543def0ddbe54f5189b4c37"  # Replace with a valid credential ID
response_data = embedded.Credentials.delete(credential_id)

print(json.dumps(response_data, indent=4))
