# test/uapi_metadata/index.py
import json
import os
from alloy_python.uapi.metadata import Metadata

# Retrieve API key from environment variable
api_key = os.environ.get('ALLOY_API_KEY')

if not api_key:
    raise EnvironmentError("API key not found. Set the ALLOY_API_KEY environment variable.")

# Initialize with the retrieved API key
metadata = Metadata(api_key)

# Test list_operations
app_name = "shopify"
operations_response = metadata.list_operations(app_name)
formatted_operations = json.dumps(operations_response, indent=4)
assert formatted_operations is not None, "List operations failed"
print("Operations for App:", formatted_operations)

# Test list_fields
operation_name = "listOrders"
fields_response = metadata.list_fields(app_name, operation_name)
formatted_fields = json.dumps(fields_response, indent=4)
assert formatted_fields is not None, "List fields failed"
print("Fields for Operation:", formatted_fields)
