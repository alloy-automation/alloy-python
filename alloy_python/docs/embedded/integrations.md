# Integration SDK Documentation

## Overview

The Integration SDK provides functionalities for listing integrations and retrieving details for a specific integration associated with a user.

## List Integrations

Retrieve a list of integrations associated with a specific user.

```python
from alloy_python.embedded import Embedded

# Initialize the Embedded SDK with your API key
api_key = 'YOUR_API_KEY'
embedded = Embedded(api_key)

# Set the user ID for which you want to list integrations
user_id = "user123"
embedded.Integration.set_user_id(user_id)

# List integrations for the specified user
integrations_list = embedded.Integration.list_integrations()
```

## Get Integration Details

Retrieve detailed information for a specific integration associated with a user.

```python
from alloy_python.embedded import Embedded

# Initialize the Embedded SDK with your API key
api_key = 'YOUR_API_KEY'
embedded = Embedded(api_key)

# Set the user ID for which you want to retrieve integration details
user_id = "user123"
embedded.Integration.set_user_id(user_id)

# Specify the integration ID for which you want to retrieve details
integration_id = "integration123"
integration_details = embedded.Integration.get_integration(integration_id=integration_id)
```
