import json
from alloy_python.embedded.users import User

user = User()
user.set_user_id("655eec40fddc8c4ffcbcdc39")  # Replace with a valid user ID

data = {
  "fullName": "jon dosse",
  "username": "test@coole222mail.com"
}   # Replace with valid update data
response_data = user.update_user(data)

print(json.dumps(response_data, indent=4))
