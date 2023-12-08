
# Alloy Python SDK

This SDK provides a Python interface for interacting with Alloy APIs. It's designed for flexibility and easy integration into Python projects and is distributed via PyPI.

## Installation

The Alloy Python SDK can be easily installed using pip:

```bash
pip install alloy-python-sdk
```

## Usage

After installation, you can use the SDK in your Python projects by importing the `Embedded` class and initializing it with your API key. Here's an example:

```python
from alloy_python.embedded import Embedded

# Initialize with your API key
embedded = Embedded("your_alloy_api_key")

# Example usage with the App class
response = embedded.App.get_apps()
print(response)

# You can also access other services in a similar manner
# response = embedded.User.get_user()
# response = embedded.Workflows.list()
# ... and so on
```

Replace `"your_alloy_api_key"` with your actual Alloy API key. The `Embedded` class provides access to various services like Apps, Users, Workflows, etc.

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

## License

Specify the license under which your SDK is distributed. This can be MIT, Apache, GPL, or any other open-source license you choose.
