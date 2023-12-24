
# Alloy Python SDK

This SDK provides a Python interface for interacting with Alloy APIs. It's designed for flexibility and easy integration into Python projects and is distributed via PyPI.

## Installation

The Alloy Python SDK can be easily installed using pip:

```bash
pip install alloy-python-sdk
```

## Usage

The package needs to be configured with your account's API key, which is available in the Alloy Dashboard under settings. You must supply the API key with each instantiation of the module.


### Unified API

To use thie SDK with Alloy's Unified API, use the code snippet below:

```python
from alloy_python.uapi import UAPI
uapi = UAPI('YOUR_API_KEY')
````

### Creating a User

To make API calls to Unified API, you must first [create a user](https://docs-uapi.runalloy.com/reference/create-user). To create a user, call the `User.create_user()` method as seen below. You must pass a unique username.


```python
user_data = {'username': 'john@example.com'}
user_data = user.create_user(user_data)
```


Before you make your first API call, you will need to obtain a `connectionId`. A connectionId represents the unique identifier of an app you plan to make API calls to. You can obtain a connectionId by using the frontend SDK. Read more [here](https://docs-uapi.runalloy.com/docs/unified-api-quick-start).



### Making requests to Alloy Unified API's SDK

Once you have a `connectionId`, you can start making calls to Alloy Unified API. See the example below for making a request to the Commerce Unified API:

```python
from alloy_python.uapi.commerce import Commerce

commerce = Commerce('YOUR_API_KEY')
list_customers_response = commerce.list_customers()
```


### Alloy Embedded

To set up Alloy's Embedded iPaaS, use the code snippet below:

```python
from alloy_python.embedded import Embedded

# Initialize with your API key
embedded = Embedded('YOUR_API_KEY')

# Example usage with the App class
response = embedded.App.get_apps()
print(response)
```






## Testing

### API Key for Testing

To test the SDK, you'll need to set the `ALLOY_API_KEY` environment variable. This can be done in your terminal session:

```bash
export ALLOY_API_KEY="your_api_key_here"
```

### Running Test Scripts

The SDK includes a set of test scripts that you can use to verify its functionality. Before running these scripts, ensure that the `ALLOY_API_KEY` environment variable is set as described above. You may need to replace user IDs, workflow IDs, integration IDs, etc., in the test scripts with those specific to your Alloy account.

Run a test script using:

```bash
python3 test/path_to_test_script.py
```

For example:

```bash
python3 test/apps/get_apps.py
```

## Contributing

Contributions to the SDK are welcome. Please ensure to follow the coding standards and write tests for new features.

