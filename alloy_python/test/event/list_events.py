import json
from alloy_python.embedded.events import Events

# Instantiate the Events class
events = Events()
events.set_user_id("651b7f858665f0e875a88a00")  # Replace with a valid user ID

# List events
response_data = events.list()

# Pretty-print the response
print(json.dumps(response_data, indent=4))
