import json
import os
from alloy_python.embedded import Embedded

api_key = os.environ.get('ALLOY_API_KEY')
if not api_key:
    raise EnvironmentError("API key not found. Set the ALLOY_API_KEY environment variable.")

embedded = Embedded(api_key)
embedded.Credentials.set_user_id("651b7f858665f0e875a88a00")  # Replace with a valid user ID

app = "shopify"
integration_id = "6509d140571419e3633878e8"
response_data = embedded.Credentials.generate_oauth_link(app, integration_id)

print(json.dumps(response_data, indent=4))
