import json
from alloy_python.embedded.users import User

user = User()

response_data = user.list_users()

print(json.dumps(response_data, indent=4))
