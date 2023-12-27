# Compliance SDK Documentation

## Overview

The Compliance SDK provides functionalities to manage user logs for compliance purposes.

## Delete User Logs

Delete logs associated with a specific user. Commonly used in conjunction with a GDPR request.

```python
from alloy_python.embedded import Embedded

# Initialize the Embedded SDK with your API key
api_key = 'YOUR_API_KEY'
embedded = Embedded(api_key)

# Delete logs for the specified user
deleted_logs = embedded.Compliance.delete_user_logs()
```
