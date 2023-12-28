import requests
from ..constants import BASE_URL

class Webhooks:
    def __init__(self, api_key):
        if not api_key:
            raise ValueError("API key must be provided")

        self.api_key = api_key
        self.headers = {
            'Authorization': f'Bearer {api_key}',
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
        self.url = f"{BASE_URL}/one/webhooks"

    def create_subscription(self, topic, address):
        data = {
            'topic': topic,
            'address': address
        }
        response = requests.post(self.url, headers=self.headers, json=data)
        response.raise_for_status()
        return response.json()

    def list_subscriptions(self):
        response = requests.get(self.url, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def get_subscription(self, subscription_id):
        response = requests.get(f"{self.url}/{subscription_id}", headers=self.headers)
        response.raise_for_status()
        return response.json()

    def delete_subscription(self, subscription_id):
        response = requests.delete(f"{self.url}/{subscription_id}", headers=self.headers)
        response.raise_for_status()
        return response.json()
