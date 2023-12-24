# Events SDK Documentation

## Overview

The Events SDK provides functionalities for listing events and running specific events with associated data.

## List Events

Retrieve a list of events associated with a specific user.

```python
from alloy_python.embedded import Embedded

# Initialize the Embedded SDK with your API key
api_key = 'YOUR_API_KEY'
embedded = Embedded(api_key)

# Set the user ID for which you want to list events
user_id = "user123"
embedded.Events.set_user_id(user_id)

# List events for the specified user
events_list = embedded.Events.list()
```

## Run Event

Run a specific event with associated data.

```python
from alloy_python.embedded import Embedded

# Initialize the Embedded SDK with your API key
api_key = 'YOUR_API_KEY'
embedded = Embedded(api_key)

# Set the user ID for which you want to run an event
user_id = "user123"
embedded.Events.set_user_id(user_id)

# Specify the event and data for running the event
event_name = "My Event"
event_data = {"param": "value"}

# Run the specified event with the provided data
event_response = embedded.Events.run(event=event_name, data=event_data)
```
