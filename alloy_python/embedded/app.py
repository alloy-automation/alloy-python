# app.py
import requests
from ..constants import BASE_URL

class App:
    def __init__(self, api_key):
        self.headers = {'Authorization': f'Bearer {api_key}'}
        self.url = BASE_URL

    def get_apps(self):
        response = requests.get(f'{self.url}/metadata/apps', headers=self.headers)
        response.raise_for_status()  # Raise an exception for HTTP error responses
        return response.json()

# The __name__ == "__main__" block can be used for testing this class directly
if __name__ == "__main__":
    # For local testing, replace 'your_api_key_here' with your actual API key
    app = App('your_api_key_here')
    print(app.get_apps())
