# Credentials SDK Documentation

## Overview

The Credentials SDK provides functionalities for managing user credentials, including listing credentials, retrieving metadata, deleting, creating, and generating OAuth links.

## List User Credentials

Retrieve a list of credentials associated with a specific user.

```python
from alloy_python.embedded import Embedded

# Initialize the Embedded SDK with your API key
api_key = 'YOUR_API_KEY'
embedded = Embedded(api_key)

# Set the user ID for which you want to list credentials
user_id = "user123"
embedded.Credentials.set_user_id(user_id)

# List user credentials
user_credentials = embedded.Credentials.list_user_credentials()
```

## Get Credential Metadata

Retrieve metadata for all credentials associated with a specific user.

```python
from alloy_python.embedded import Embedded

# Initialize the Embedded SDK with your API key
api_key = 'YOUR_API_KEY'
embedded = Embedded(api_key)

# Set the user ID for which you want to get metadata
user_id = "user123"
embedded.Credentials.set_user_id(user_id)

# Get metadata for user credentials
credential_metadata = embedded.Credentials.get_metadata()
```

## Delete User Credential

Delete a specific credential associated with a user.

```python
from alloy_python.embedded import Embedded

# Initialize the Embedded SDK with your API key
api_key = 'YOUR_API_KEY'
embedded = Embedded(api_key)

# Set the user ID for which you want to delete a credential
user_id = "user123"
credential_id = "credential456"
embedded.Credentials.set_user_id(user_id)

# Delete the specified credential
deleted_credential = embedded.Credentials.delete(credential_id)
```

## Create User Credential

Create a new credential for a specific user.

```python
from alloy_python.embedded import Embedded

# Initialize the Embedded SDK with your API key
api_key = 'YOUR_API_KEY'
embedded = Embedded(api_key)

# Set the user ID for which you want to create a credential
user_id = "user123"
embedded.Credentials.set_user_id(user_id)

# Provide data for creating a new credential
credential_data = {"param": "value"}
created_credential = embedded.Credentials.create(data=credential_data)
```

## Generate OAuth Link

Generate an OAuth link for a specific app and integration ID.

```python
from alloy_python.embedded import Embedded

# Initialize the Embedded SDK with your API key
api_key = 'YOUR_API_KEY'
embedded = Embedded(api_key)

# Set the user ID for which you want to generate an OAuth link
user_id = "user123"
app_name = "example_app"
integration_id = "integration123"
embedded.Credentials.set_user_id(user_id)

# Generate an OAuth link for the specified app and integration ID
oauth_link = embedded.Credentials.generate_oauth_link(app=app_name, integration_id=integration_id)
```