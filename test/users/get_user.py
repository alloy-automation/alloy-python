import json
from alloy_python.embedded.users import User

user = User()
user.set_user_id("651b7f858665f0e875a88a00")  # Replace with a valid user ID

response_data = user.get_user()

print(json.dumps(response_data, indent=4))
