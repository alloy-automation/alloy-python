# App SDK Documentation

## Overview

Retrieves a list of available apps.

## Get Apps

Retrieve a list of installed apps.

```python
from alloy_python.embedded import Embedded

# Initialize the Embedded SDK with your API key
api_key = 'YOUR_API_KEY'
embedded = Embedded(api_key)

# Get apps
apps_data = embedded.App.get_apps()
```
