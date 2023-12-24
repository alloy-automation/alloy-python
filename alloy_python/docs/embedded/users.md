# User SDK Documentation

## Overview

The User SDK provides functionality for managing user information, including retrieving user details, listing users, creating users, updating user information, and deleting users.

## Set User ID

Set the user ID for the User SDK instance. Once you have set the user Id you do not need to interact with it again.

```python
from alloy_python.embedded import Embedded

# Initialize the Embedded SDK with your API key
api_key = 'YOUR_API_KEY'
embedded = Embedded(api_key)

# Set the user ID for the User SDK instance
user_id = "user123"
embedded.User.set_user_id(user_id)
```

## Get User

Retrieve detailed information for a specific user.

```python
from alloy_python.embedded import Embedded

# Initialize the Embedded SDK with your API key
api_key = 'YOUR_API_KEY'
embedded = Embedded(api_key)

# Set the user ID for which you want to retrieve details
user_id = "user123"
embedded.User.set_user_id(user_id)

# Retrieve user details
user_info = embedded.User.get_user()
```

## List Users

Retrieve a list of all users.

```python
from alloy_python.embedded import Embedded

# Initialize the Embedded SDK with your API key
api_key = 'YOUR_API_KEY'
embedded = Embedded(api_key)

# Retrieve a list of all users
user_list = embedded.User.list_users()
```

## Create User

Create a new user.

```python
from alloy_python.embedded import Embedded

# Initialize the Embedded SDK with your API key
api_key = 'YOUR_API_KEY'
embedded = Embedded(api_key)

# User data to create a new user
user_data = {"username": "new_user"}

# Create a new user
created_user = embedded.User.create_user(data=user_data)
```

## Create Batch Users

Create multiple users in batch.

```python
from alloy_python.embedded import Embedded

# Initialize the Embedded SDK with your API key
api_key = 'YOUR_API_KEY'
embedded = Embedded(api_key)

# User data for multiple users
batch_user_data = [
    {"username": "user1"},
    {"username": "user2"},
    # ... add more user data as needed
]

# Create batch users
created_users = embedded.User.create_batch_users(data=batch_user_data)
```

## Update User

Update information for a specific user.

```python
from alloy_python.embedded import Embedded

# Initialize the Embedded SDK with your API key
api_key = 'YOUR_API_KEY'
embedded = Embedded(api_key)

# User data to update
update_data = {"username": "new_user_1"}

# Update user information
updated_user = embedded.User.update_user(data=update_data)
```

## Delete User

Delete a specific user.

```python
from alloy_python.embedded import Embedded

# Initialize the Embedded SDK with your API key
api_key = 'YOUR_API_KEY'
embedded = Embedded(api_key)

# Delete the user with the set user ID
user_id = '123'
deleted_user = embedded.User.delete_user()
```
