import requests
from ..constants import BASE_URL

class Analytics:
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

    def get(self, workflow_id):
        try:
            response = requests.get(f'{self.url}/workflows/{workflow_id}/analytics',
                                    headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as err:
            if err.response.status_code == 422:
                return err.response.json()
            else:
                raise ValueError(err.response.json().get('message'))
