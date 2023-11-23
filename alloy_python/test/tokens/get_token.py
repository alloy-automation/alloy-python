import json
from alloy_python.embedded.tokens import Tokens

tokens = Tokens()
tokens.set_user_id("651b7f858665f0e875a88a00")  # Replace with a valid user ID

# Get token
response_data = tokens.get()

print(json.dumps(response_data, indent=4))
