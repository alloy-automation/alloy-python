import json
import os
from alloy_python.embedded import Embedded

api_key = os.environ.get('ALLOY_API_KEY')
if not api_key:
    raise EnvironmentError("API key not found. Set the ALLOY_API_KEY environment variable.")

embedded = Embedded(api_key)
embedded.Events.set_user_id("651b7f858665f0e875a88a00")  # Replace with a valid user ID

event = "isv_app_order_created"  # Replace with actual event
data = {"key": "value"}  # Replace with actual data

response_data = embedded.Events.run(event, data)

print(json.dumps(response_data, indent=4))
