import requests
from ..constants import BASE_URL

class Credentials:
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

    def list_user_credentials(self):
        response = requests.get(f'{self.url}/users/{self.user_id}/credentials',
                                headers=self.headers)
        response.raise_for_status()
        return response.json()

    def get_metadata(self):
        response = requests.get(f'{self.url}/credentials?userId={self.user_id}',
                                headers=self.headers)
        response.raise_for_status()
        return response.json()

    def delete(self, credential_id):
        response = requests.delete(f'{self.url}/users/{self.user_id}/credentials/{credential_id}',
                                   headers=self.headers)
        response.raise_for_status()
        return response.json()

    def create(self, data):
        response = requests.post(f'{self.url}/users/{self.user_id}/credentials',
                                 headers=self.headers, json=data)
        response.raise_for_status()
        return response.json()

    def generate_oauth_link(self, app, integration_id):
        response = requests.get(f'{self.url}/users/{self.user_id}/credentials/{app}?integrationId={integration_id}',
                                headers=self.headers)
        response.raise_for_status()
        return response.json()
