# test/crm/index.py
import json
import os
from alloy_python.uapi import UAPI
from alloy_python.uapi.crm import CRM

# Retrieve API key from environment variable
api_key = os.environ.get('ALLOY_API_KEY')
connection_id = os.environ.get('ALLOY_CONNECTION_ID')

if not api_key:
    raise EnvironmentError("API key not found. Set the ALLOY_API_KEY environment variable.")

# Initialize with the retrieved API key
crm = CRM(api_key)
crm.connect(connection_id)

# List Accounts
list_accounts_response = crm.list_accounts()

formatted_list_accounts = json.dumps(list_accounts_response, indent=4)
assert formatted_list_accounts is not None, "List accounts failed"
print('[CRM]: List Accounts:')
print(formatted_list_accounts)

# List Accounts Count
list_accounts_count_response = crm.get_accounts_count()

formatted_list_accounts_count = json.dumps(list_accounts_count_response, indent=4)
assert formatted_list_accounts_count is not None, "List accounts failed"
print('[CRM]: List Accounts Count:')
print(formatted_list_accounts_count)


# Create Account
create_account_data = {
    "accountName": "Mojica"
}
create_account_response = crm.create_account(create_account_data)

formatted_create_account = json.dumps(create_account_response, indent=4)
assert formatted_create_account is not None, "Create account failed"
print('[CRM]: Create Account:')
print(formatted_create_account)

