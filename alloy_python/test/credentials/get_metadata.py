import json
from alloy_python.embedded.credentials import Credentials

credentials = Credentials()
credentials.set_user_id("example_user_id")  # Replace with a valid user ID

response_data = credentials.get_metadata()

print(json.dumps(response_data, indent=4))
