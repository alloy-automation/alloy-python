import json
from alloy_python.embedded.logs import Logs

# Instantiate the Logs class
logs = Logs()
logs.set_user_id("651b7f858665f0e875a88a00")  # Replace with a valid user ID

workflow_id = "6512e1b62904e02be3b74bfa"  # Replace with a valid workflow ID
response_data = logs.get_workflow_errors(workflow_id)

# Pretty-print the response
print(json.dumps(response_data, indent=4))
