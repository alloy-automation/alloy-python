# test/accounting/index.py
import json
import os
from alloy_python.uapi import UAPI
import uuid

# Retrieve API key from environment variable
api_key = os.environ.get('ALLOY_API_KEY')
connection_id = os.environ.get('ALLOY_CONNECTION_ID')

if not api_key:
    raise EnvironmentError("API key not found. Set the ALLOY_API_KEY environment variable.")

# Initialize with the retrieved API key
uapi = UAPI(api_key)
uapi.Accounting.connect("65878d9d61c4e7967cd99fa3")


# Create Account
create_account_data = {
    "accountName": f'myaccout{uuid.uuid4()}',
    "accountType": "OTHER_ASSET",
    "currency": "USD"
}
create_account_response = uapi.Accounting.create_account(create_account_data)

formatted_create_account = json.dumps(create_account_response, indent=4)
assert formatted_create_account is not None, "Create account failed"
print('[Accounting]: Create Account')
print(formatted_create_account)

# List Company Info
list_accounts_response = uapi.Accounting.list_accounts()

formatted_list_accounts = json.dumps(list_accounts_response, indent=4)
assert formatted_list_accounts is not None, "List accounts failed"
print('[Accounting]: List Accounts:')
print(formatted_list_accounts)

# Get Accounts Count
list_accounts_count_response = uapi.Accounting.get_account_count()

formatted_list_accounts_count = json.dumps(list_accounts_count_response, indent=4)
assert formatted_list_accounts_count is not None, "List accounts failed"
print('[Accounting]: List Accounts Count:')
print(formatted_list_accounts_count)




