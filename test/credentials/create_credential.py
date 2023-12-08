import json
from alloy_python.embedded.credentials import Credentials

credentials = Credentials()
credentials.set_user_id("651b7f858665f0e875a88a00")  # Replace with a valid user ID

data = {
  "credential": {
    "type": "httpHeaderAuth",
    "data": {
      "fieldName": "Authorization",
      "value": "bearer 9876543210"
    }
  }
}  # Replace with valid data for creating a credential
response_data = credentials.create(data)

print(json.dumps(response_data, indent=4))
