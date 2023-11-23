import requests
from ..constants import BASE_URL, API_KEY

class Logs:
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

    def get_workflow_errors(self, workflow_id):
        try:
            response = requests.get(f'{self.url}/workflows/{workflow_id}/errors?userId={self.user_id}',
                                    headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as err:
            if err.response.status_code == 422:
                return err.response.json()
            else:
                raise ValueError(err.response.json().get('message'))

    def get_workflow_logs(self, workflow_id):
        try:
            response = requests.get(f'{self.url}/workflows/{workflow_id}/logs?userId={self.user_id}',
                                    headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as err:
            if err.response.status_code == 422:
                return err.response.json()
            else:
                raise ValueError(err.response.json().get('message'))

    def rerun_workflow_execution(self, workflow_id, execution_id):
        try:
            response = requests.post(f'{self.url}/workflows/{workflow_id}/rerun/{execution_id}?userId={self.user_id}',
                                     headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as err:
            if err.response.status_code == 422:
                return err.response.json()
            else:
                raise ValueError(err.response.json().get('message'))
