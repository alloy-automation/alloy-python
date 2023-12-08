import json
import os
from alloy_python.embedded import Embedded

api_key = os.environ.get('ALLOY_API_KEY')
if not api_key:
    raise EnvironmentError("API key not found. Set the ALLOY_API_KEY environment variable.")

embedded = Embedded(api_key)

embedded.Workflows.set_user_id("651b82608665f0e875a88e81")
response_data = embedded.Workflows.deactivate_all()

print(json.dumps(response_data, indent=4))
