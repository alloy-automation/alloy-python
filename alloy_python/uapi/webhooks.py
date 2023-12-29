# alloy_python/uapi/webhooks.py
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

    def _api_request(self, method, endpoint, data=None):
        url = f"{self.url}/{endpoint}" if endpoint else self.url
        try:
            response = requests.request(method, url, headers=self.headers, json=data)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            return None

    def create_subscription(self, topic, address):
        data = {
            'topic': topic,
            'address': address
        }
        return self._api_request('POST', '', data)

    def list_subscriptions(self):
        return self._api_request('GET', '')

    def get_subscription(self, subscription_id):
        return self._api_request('GET', str(subscription_id))

    def delete_subscription(self, subscription_id):
        return self._api_request('DELETE', str(subscription_id))
