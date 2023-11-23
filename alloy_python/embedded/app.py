import requests
from ..constants import BASE_URL, API_KEY

class App:
    def __init__(self, api_key=API_KEY):
        self.api_key = api_key
        self.headers = {'Authorization': f'Bearer {api_key}'}
        self.url = BASE_URL

    def get_apps(self):
        response = requests.get(f'{self.url}/apps', headers=self.headers)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 422:
            return response.json()
        else:
            response.raise_for_status()

if __name__ == "__main__":
    app = App()
    print(app.get_apps())
