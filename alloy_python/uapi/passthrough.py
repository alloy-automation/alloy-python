# alloy_python/uapi/passthrough.py
import requests
from ..constants import BASE_URL

class Passthrough:
    def __init__(self, api_key):
        if not api_key:
            raise ValueError("API key must be provided")
        
        self.api_key = api_key
        self.headers = {
            'Authorization': f'Bearer {api_key}',
        }
        self.url = BASE_URL
        self.connection_id = None

    def connect(self, connection_id):
        self.connection_id = connection_id

    def _api_request(self, method, endpoint, payload):
        url = f"{self.url}/{endpoint}?connectionId={self.connection_id}"
        try:
            response = requests.request(method, url, headers=self.headers, json=payload)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            return None

    def passthrough_request(self, method, endpoint, body=None, query=None, extra_headers=None):
        payload = {
            "method": method,
            "endpoint": endpoint,
            "body": body or None,
            "query": query or None,
            "extraHeaders": extra_headers or None
        }
        return self._api_request('POST', 'one/forward', payload)