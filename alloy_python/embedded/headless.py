import requests
from ..constants import BASE_URL

class HeadlessInstallation:
    def __init__(self, api_key):
        if not api_key:
            raise ValueError("API key must be provided")
        self.api_key = api_key
        self.headers = {'Authorization': f'Bearer {api_key}'}
        self.url = BASE_URL
        self.user_id = None

    def set_user_id(self, user_id):
        self.user_id = user_id

    def set_username(self, username):
        self.username = username

    def start_installation(self, data):
        data['userId'] = self.user_id
        response = requests.post(f'{self.url}/headless/startInstallation',
                                 headers=self.headers, json=data)
        response.raise_for_status()
        return response.json()

    def complete_installation(self, data):
        response = requests.post(f'{self.url}/headless/completeInstallation',
                                 headers=self.headers, json=data)
        response.raise_for_status()
        return response.json()

