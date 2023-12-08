import json
from alloy_python.embedded.users import User

user = User()

data = {
  "fullName": "jon doe",
  "username": "test@coolemail.com"
} 
response_data = user.create_user(data)

print(json.dumps(response_data, indent=4))
