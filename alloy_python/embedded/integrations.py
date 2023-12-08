import requests
from ..constants import BASE_URL

class Integration:
    def __init__(self, api_key):
        if not api_key:
            raise ValueError("API key must be provided")
        self.api_key = api_key
        self.headers = {'Authorization': f'Bearer {api_key}'}
        self.url = BASE_URL
        self.username = None
        self.user_id = None
        self.connection_id = None

    def set_user_id(self, user_id):
        self.user_id = user_id

    def set_username(self, username):
        self.username = username

    def list_integrations(self):
        response = requests.get(f'{self.url}/integrations?userId={self.user_id}',
                                headers=self.headers)
        response.raise_for_status()
        return response.json()

    def get_integration(self, integration_id):
        response = requests.get(f'{self.url}/integrations/{integration_id}?userId={self.user_id}',
                                headers=self.headers)
        response.raise_for_status()
        return response.json()
