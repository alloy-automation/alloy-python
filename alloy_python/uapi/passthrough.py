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
        except requests.exceptions.HTTPError as http_err:
            # Handles HTTP errors; returns error message and status code
            error_message = http_err.response.json().get('message', 'An error occurred')
            return {"error": error_message, "status_code": http_err.response.status_code}
        except requests.exceptions.RequestException as req_err:
            # Handles non-HTTP errors like network issues
            print(f"Error: {req_err}")
            return {"error": "Network or request error", "status_code": 500}


    def request(self, method, endpoint, body=None, query=None, extra_headers=None):
        payload = {
            "method": method,
            "endpoint": endpoint,
            "body": body or None,
            "query": query or None,
            "extraHeaders": extra_headers or None
        }
        return self._api_request('POST', 'one/forward', payload)
