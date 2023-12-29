import requests
from urllib.parse import urljoin
from ..constants import BASE_URL

class User:
    def __init__(self, api_key):
        if not api_key:
            raise ValueError("API key must be provided")

        self.api_key = api_key
        self.headers = {
            'Authorization': f'Bearer {api_key}',
        }
        self.username = None
        self.user_id = None
        self.connection_id = None
        self.url = BASE_URL

    def connect(self, connection_id):
        self.connection_id = connection_id

    def list_users(self):
        url = f'{self.url}/one/users'
        response = self._api_request('GET', url)
        return response

    def get_user(self, user_id):
        url = f'{self.url}/one/users'
        response = self._api_request('GET', url)
        return response

    def create_user(self, data):
        url = f'{self.url}/one/users'
        response = self._api_request('POST', url, data=data)
        return response

    def update_user(self, user_id, data):
        url = f'{self.url}/one/users'
        response = self._api_request('PUT', url, data=data)
        return response

    def delete_user(self, user_id):
        url = f'{self.url}/one/users'
        response = self._api_request('DELETE', url)
        return response

    def _api_request(self, method, url, params=None, data=None):
        headers = self.headers.copy()
        try:
            response = requests.request(method, url, headers=headers, params=params, json=data)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            return {"error": http_err.response.json().get('message', 'An error occurred'), "status_code": http_err.response.status_code}
        except requests.exceptions.RequestException as req_err:
            print(f"Error: {req_err}")
            return {"error": "Network or request error", "status_code": 500}
