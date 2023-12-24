# User SDK Documentation

## Overview

The User SDK provides a client for interacting with user-related endpoints, enabling you to manage users through a specified API.

## Authentication

To use the User API, you need to instantiate the User class with a valid API key.

```python
from alloy_python.uapi import UAPI

api_key = "YOUR_API_KEY"
user = User(api_key)
```

### Methods

## List Users

Retrieve a list of users.

```python
users_data = user.list_users()
```

## Get User

Retrieve information about a specific user.

```python
user_data = user.get_user(user_id)
```

## Create User

Create a new user.

```python
user_data = {'username': 'john@example.com'}
user_data = user.create_user(user_data)
```

## Update User

Update information for a specific user.

```python
updated_user_data = {'username': 'jane@example.com'}
updated_data = user.update_user(user_id, updated_user_data)
```

## Delete User

Delete a specific user.

```python
deleted_data = user.delete_user(user_id)
```

## Error Handling

The User SDK provides error handling for API requests. If an error occurs, it prints an error message with status code and reason.

```python
try:
    response_data = user.list_users()
except ValueError as e:
    print(f"Error: {str(e)}")
```
