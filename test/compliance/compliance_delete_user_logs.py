import json
import os
from alloy_python.embedded.embedded import Embedded

# Create an instance of the Compliance class using the default API key
api_key = os.environ.get('ALLOY_API_KEY')
if not api_key:
    raise EnvironmentError("API key not found. Set the ALLOY_API_KEY environment variable.")

# Initialize with the retrieved API key
embedded = Embedded(api_key)

# Set the user_id for the compliance instance
# Replace "example_user_id" with a valid user ID for your application
embedded.Compliance.set_user_id("6530c994e84e8b90693d6319")

# Call the delete_user_logs method
response_data = embedded.Compliance.delete_user_logs()

# Pretty-print the JSON response
formatted_json = json.dumps(response_data, indent=4)
print(formatted_json)
