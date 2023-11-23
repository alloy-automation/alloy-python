import json
from alloy_python.embedded.credentials import Credentials

credentials = Credentials()
credentials.set_user_id("651b7f858665f0e875a88a00")  # Replace with a valid user ID

app = "shopify"
integration_id = "6509d140571419e3633878e8"
response_data = credentials.generate_oauth_link(app, integration_id)

print(json.dumps(response_data, indent=4))
