import requests
from ..constants import BASE_URL

class Events:
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
        try:
            response = requests.get(f'{self.url}/events?userId={self.user_id}',
                                    headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as err:
            if err.response.status_code == 422:
                return err.response.json()
            else:
                raise ValueError(err.response.json().get('message'))

    def run(self, event, data):
        body_data = {
            "event": event,
            "userId": self.user_id,
            "data": data,
        }
        try:
            response = requests.post(f'{self.url}/run/event', headers=self.headers,
                                     json=body_data)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as err:
            if err.response.status_code == 422:
                return err.response.json()
            else:
                raise ValueError(err.response.json().get('message'))
