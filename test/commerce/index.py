# test/commerce/index.py
import json
import os
from alloy_python.uapi import UAPI
from alloy_python.uapi.commerce import Commerce
import uuid
import random

# Retrieve API key from environment variable
api_key = os.environ.get('ALLOY_API_KEY')
connection_id = os.environ.get('ALLOY_CONNECTION_ID')

if not api_key:
    raise EnvironmentError("API key not found. Set the ALLOY_API_KEY environment variable.")

uapi = UAPI(api_key)
uapi.Commerce.connect('6581c0f747dceb15541ad411')

# Initialize with the retrieved API key
# commerce = Commerce(api_key)
# commerce.connect("6581c0f747dceb15541ad411")


# Create a Customer
phone_number = ''.join(str(random.randint(0, 9)) for _ in range(10))
create_customer_data = {
    "firstName": "Alloy",
    "lastName": "Test User",
    "email": f'user+{uuid.uuid4()}@runalloy.com',
    "phone": f'+1{phone_number}'
}
create_customers_response = uapi.Commerce.create_customer(create_customer_data)

formatted_create_customers = json.dumps(create_customers_response, indent=4)
assert formatted_create_customers is not None, "Create customer failed"


# List all customers
list_customers_response = uapi.Commerce.list_customers()

formatted_list_customers = json.dumps(list_customers_response, indent=4)
assert formatted_list_customers is not None, "List customers failed"
print(formatted_list_customers)
