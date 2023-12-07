import json
from alloy_python.embedded.compliance import Compliance

# Create an instance of the Compliance class using the default API key
compliance = Compliance()

# Set the user_id for the compliance instance
# Replace "example_user_id" with a valid user ID for your application
compliance.set_user_id("6530c994e84e8b90693d6319")

# Call the delete_user_logs method
response_data = compliance.delete_user_logs()

# Pretty-print the JSON response
formatted_json = json.dumps(response_data, indent=4)
print(formatted_json)
