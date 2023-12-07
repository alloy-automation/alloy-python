import json
from alloy_python.embedded.users import User

user = User()
user.set_user_id("655eea40ea9303f27e958b75")  # Replace with a valid user ID

response_data = user.delete_user()

print(json.dumps(response_data, indent=4))
