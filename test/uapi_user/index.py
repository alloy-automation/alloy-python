# test/uapi_user/index.py
import json
import os
from alloy_python.uapi import UAPI
from alloy_python.uapi.user import User
import uuid

# Retrieve API key from environment variable
api_key = os.environ.get('ALLOY_API_KEY')
connection_id = os.environ.get('ALLOY_CONNECTION_ID')

if not api_key:
    raise EnvironmentError("API key not found. Set the ALLOY_API_KEY environment variable.")

# Initialize with the retrieved API key
user = User(api_key)
user.connect("6581c0f747dceb15541ad411")


# Create a User
create_user_data = {
    "username": f'user+{uuid.uuid4()}'
}
create_user_response = user.create_user(create_user_data)

formatted_create_user = json.dumps(create_user_response, indent=4)
assert formatted_create_user is not None, "Create user failed"
print(formatted_create_user)

# List all customers
# list_customers_response = commerce.list_customers()

# formatted_list_customers = json.dumps(list_customers_response, indent=4)
# assert formatted_list_customers is not None, "List customers failed"
# print(formatted_list_customers)
