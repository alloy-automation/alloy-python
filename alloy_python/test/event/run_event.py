import json
from alloy_python.embedded.events import Events

events = Events()
events.set_user_id("651b7f858665f0e875a88a00")  # Replace with a valid user ID

# Example event and data - replace with actual event and data
event = "isv_app_order_created"
data = {"key": "value"}

response_data = events.run(event, data)

print(json.dumps(response_data, indent=4))
