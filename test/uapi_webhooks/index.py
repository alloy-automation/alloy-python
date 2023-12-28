# test/webhooks/index.py
import json
import os
from alloy_python.uapi.webhooks import Webhooks

# Retrieve API key from environment variable
api_key = os.environ.get('ALLOY_API_KEY')
if not api_key:
    raise EnvironmentError("API key not found. Set the ALLOY_API_KEY environment variable.")

# Initialize the Webhooks class with the API key
webhooks = Webhooks(api_key)

# Create a webhook subscription
create_subscription_data = {
    "topic": ["commerce/customers", "sync/completed"],
    "address": "https://mysite.com/webhook"
}
create_subscription_response = webhooks.create_subscription(**create_subscription_data)
formatted_create_subscription = json.dumps(create_subscription_response, indent=4)
print("Created Subscription:", formatted_create_subscription)

# List all subscriptions
list_subscriptions_response = webhooks.list_subscriptions()
formatted_list_subscriptions = json.dumps(list_subscriptions_response, indent=4)
print("List of Subscriptions:", formatted_list_subscriptions)

# Retrieve a specific subscription
# Assuming the first subscription's ID from the list as an example
subscription_id = list_subscriptions_response['subscriptions'][0]['subscriptionId'] if list_subscriptions_response['subscriptions'] else None
if subscription_id:
    get_subscription_response = webhooks.get_subscription(subscription_id)
    formatted_get_subscription = json.dumps(get_subscription_response, indent=4)
    print("Specific Subscription:", formatted_get_subscription)

    # Delete the specific subscription
    delete_subscription_response = webhooks.delete_subscription(subscription_id)
    formatted_delete_subscription = json.dumps(delete_subscription_response, indent=4)
    print("Deleted Subscription:", formatted_delete_subscription)
else:
    print("No subscription found to retrieve or delete.")
