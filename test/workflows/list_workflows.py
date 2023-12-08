import json
import os
from alloy_python.embedded import Embedded

api_key = os.environ.get('ALLOY_API_KEY')
if not api_key:
    raise EnvironmentError("API key not found. Set the ALLOY_API_KEY environment variable.")

embedded = Embedded(api_key)

embedded.Workflows.set_user_id("651b7f858665f0e875a88a00")
response_data = embedded.Workflows.list()

print(json.dumps(response_data, indent=4))
