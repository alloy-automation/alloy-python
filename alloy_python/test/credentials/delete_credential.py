import json
from alloy_python.embedded.credentials import Credentials

credentials = Credentials()
credentials.set_user_id("651b7f858665f0e875a88a00")  # Replace with a valid user ID

credential_id = "655edefb006fd89fc7165661"  # Replace with a valid credential ID
response_data = credentials.delete(credential_id)

print(json.dumps(response_data, indent=4))
