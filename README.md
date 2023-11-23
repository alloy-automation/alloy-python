# Alloy Python SDK

This SDK provides a Python interface for interacting with Alloy APIs. It's designed for flexibility and easy integration into Python projects. This package will be distributed via PyPI and will be available via `pip install alloy-xxx`.

## Installation

### Clone the repository

Clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/alloy_python.git
```

### Install dependencies and the package

Install the required dependencies and the SDK itself:

```bash
pip install -r requirements.txt
pip install .
```

## Usage

After installation, you can import and use the SDK in your Python projects:

```python
from alloy_python import Embedded

# Initialize with your API key
embedded = Embedded("your_api_key_here")

# Example usage with the App class
response = embedded.App.get_apps()
print(response)

# Example usage with other classes
# response = embedded.User.get_user()
# response = embedded.Workflows.list()
# ... and so on
```

Replace `"your_api_key_here"` with your actual API key. The `Embedded` class provides access to all the features of the Alloy Python SDK.

### Testing
## API Key Configuration

Before using the SDK, set your API key in the `constants.py` file:

```python
# constants.py

BASE_URL = "https://embedded.runalloy.com/2023-12"
API_KEY = "your_api_key_here"
# Other constants...
```

Replace `"your_api_key_here"` with your actual API key.### API Key Configuration

Before using the SDK, set your API key in the `constants.py` file:

```python
# constants.py

BASE_URL = "https://embedded.runalloy.com/2023-12"
API_KEY = "your_api_key_here"
# Other constants...
```

For running test scripts, ensure to set the `PYTHONPATH` environment variable and configure the API key in `constants.py`.

```
export PYTHONPATH="/Users/kellygold/code/alloy_python:$PYTHONPATH"
```

## Contributing

Contributions to the SDK are welcome. Please ensure to follow the coding standards and write tests for new features.

## License

Specify the license under which your SDK is distributed.
