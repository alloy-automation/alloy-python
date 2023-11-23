# test_script.py
import json
from alloy_python.embedded.app import App

app = App()
response_data = app.get_apps()

# Pretty-print the JSON response
formatted_json = json.dumps(response_data, indent=4)
print(formatted_json)
