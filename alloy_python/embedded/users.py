import requests
from ..constants import BASE_URL, API_KEY

class User:
    def __init__(self, api_key=API_KEY):
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

    def get_user(self):
        response = requests.get(f'{self.url}/users/{self.user_id}',
                                headers=self.headers)
        response.raise_for_status()
        return response.json()

    def list_users(self):
        response = requests.get(f'{self.url}/users', headers=self.headers)
        response.raise_for_status()
        return response.json()

    def create_user(self, data):
        response = requests.post(f'{self.url}/users', json=data,
                                 headers=self.headers)
        response.raise_for_status()
        return response.json()

    def create_batch_users(self, data):
        response = requests.post(f'{self.url}/users/batch', json=data,
                                 headers=self.headers)
        response.raise_for_status()
        return response.json()

    def update_user(self, data):
        response = requests.put(f'{self.url}/users/{self.user_id}', json=data,
                                headers=self.headers)
        response.raise_for_status()
        return response.json()

    def delete_user(self):
        response = requests.delete(f'{self.url}/users/{self.user_id}',
                                   headers=self.headers)
        response.raise_for_status()
        return response.json()
