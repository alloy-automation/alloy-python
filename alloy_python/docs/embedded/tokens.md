# Tokens SDK Documentation

## Overview

The Tokens SDK provides functionality for managing user tokens and retrieving information about integrations.

## List Integrations

Retrieve a list of integrations associated with a user.

```python
from alloy_python.embedded import Embedded

# Initialize the Embedded SDK with your API key
api_key = 'YOUR_API_KEY'
embedded = Embedded(api_key)

# Set the user ID for which you want to list integrations
user_id = "user123"
embedded.Tokens.set_user_id(user_id)

# Retrieve a list of integrations
integration_list = embedded.Tokens.list_integrations()
```

## Get User Token

Retrieve the user token for a specific user.

```python
from alloy_python.embedded import Embedded

# Initialize the Embedded SDK with your API key
api_key = 'YOUR_API_KEY'
embedded = Embedded(api_key)

# Set the user ID for which you want to retrieve the token
user_id = "user123"
embedded.Tokens.set_user_id(user_id)

# Retrieve the user token
user_token = embedded.Tokens.get()
```
