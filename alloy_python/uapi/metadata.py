# uapi/metadata.py
import requests
from ..constants import BASE_URL

class Metadata:
    def __init__(self, api_key):
        if not api_key:
            raise ValueError("API key must be provided")

        self.api_key = api_key
        self.headers = {
            'Authorization': f'Bearer {api_key}',
            'accept': 'application/json'
        }
        self.base_url = BASE_URL

    def list_operations(self, app):
        url = f'{self.base_url}/one/metadata/operations/?app={app}'
        return self._api_request('GET', url)

    def list_fields(self, app, operation):
        url = f'{self.base_url}/one/metadata/fields?app={app}&operation={operation}'
        return self._api_request('GET', url)

    def _api_request(self, method, url, params=None):
        try:
            response = requests.request(method, url, headers=self.headers, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            return {"error": http_err.response.json().get('message', 'An error occurred'), "status_code": http_err.response.status_code}
        except requests.exceptions.RequestException as req_err:
            print(f"Error: {req_err}")
            return {"error": "Network or request error", "status_code": 500}

