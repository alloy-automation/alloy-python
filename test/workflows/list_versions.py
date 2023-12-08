import json
import os
from alloy_python.embedded import Embedded

api_key = os.environ.get('ALLOY_API_KEY')
if not api_key:
    raise EnvironmentError("API key not found. Set the ALLOY_API_KEY environment variable.")

embedded = Embedded(api_key)

embedded.Workflows.set_user_id("652f0b8852f08e6c8bb11834")
workflow_id = "65454636ca49e544e42ff2a1"
response_data = embedded.Workflows.list_versions(workflow_id)

print(json.dumps(response_data, indent=4))
