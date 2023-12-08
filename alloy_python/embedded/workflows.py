import requests
from ..constants import BASE_URL

class Workflows:
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

    def list(self):
        response = requests.get(f'{self.url}/workflows?userId={self.user_id}',
                                headers=self.headers)
        response.raise_for_status()
        return response.json()

    def list_versions(self, workflow_id):
        response = requests.get(f'{self.url}/workflows/{workflow_id}/versions?userId={self.user_id}',
                                headers=self.headers)
        response.raise_for_status()
        return response.json()

    def get(self, workflow_id):
        response = requests.get(f'{self.url}/workflows/{workflow_id}?userId={self.user_id}',
                                headers=self.headers)
        response.raise_for_status()
        return response.json()

    def deactivate_all(self):
        response = requests.put(f'{self.url}/users/{self.user_id}/deactivate-workflows',
                                headers=self.headers)
        response.raise_for_status()
        return response.json()

    def activate(self, workflow_id):
        data = {'workflowId': workflow_id, 'userId': self.user_id}
        response = requests.put(f'{self.url}/workflows/activate', json=data,
                                headers=self.headers)
        response.raise_for_status()
        return response.json()

    def deactivate(self, workflow_id):
        data = {'workflowId': workflow_id, 'userId': self.user_id}
        response = requests.put(f'{self.url}/workflows/deactivate', json=data,
                                headers=self.headers)
        response.raise_for_status()
        return response.json()

    def upgrade(self, workflow_id):
        response = requests.put(f'{self.url}/workflows/{workflow_id}/upgrade?userId={self.user_id}',
                                headers=self.headers)
        response.raise_for_status()
        return response.json()

    def delete(self, workflow_id):
        response = requests.delete(f'{self.url}/workflows/{workflow_id}?userId={self.user_id}',
                                   headers=self.headers)
        response.raise_for_status()
        return response.json()
