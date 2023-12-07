import json
from alloy_python.embedded.users import User

user = User()

data = [{
       "users": [
         { "username": "user123", "fullName": "Joe Smoe" },
         { "username": "user456" },
         { "username": "janedoe", "fullName": "Jane Doe" }
       ]
     }]  # Replace with valid batch user data
response_data = user.create_batch_users(data)

print(json.dumps(response_data, indent=4))
