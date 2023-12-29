
# Metadata SDK Documentation

## Overview

The Metadata SDK provides a client for interacting with metadata endpoints, enabling you to retrieve information about operations and fields for different apps.

## Authentication

To use the Metadata API, you need to instantiate the Metadata class with a valid API key.

```
from alloy_python.uapi import UAPI

api_key = 'YOUR_API_KEY'
uapi = UAPI(api_key)
``` 

## Methods

### List Operations for an App

Retrieve a list of operations for a specified app.

`operations_data = uapi.Metadata.list_operations(app="shopify")` 

### List Fields for an Operation

Retrieve a list of fields for a specified operation in an app.

`fields_data = uapi.Metadata.list_fields(app="shopify", operation="listOrders")` 

## Error Handling

The Metadata SDK provides error handling for API requests. If an error occurs, it returns a JSON with status code and error message.

```
{
    "error": "Invalid connectionId",
    "status_code": 400
}
```