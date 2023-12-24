# Link SDK Documentation

## Overview

The Link SDK provides functionality for generating installation URLs for integrations associated with a user.

## Generate Installation URL

Generate an installation URL for a specific integration associated with a user.

```python
from alloy_python.embedded import Embedded

# Initialize the Embedded SDK with your API key
api_key = 'YOUR_API_KEY'
embedded = Embedded(api_key)

# Set the user ID for which you want to generate an installation URL
user_id = "user123"
embedded.Link.set_user_id(user_id)

# Specify the integration ID for which you want to generate an installation URL
integration_id = "integration123"
installation_url = embedded.Link.generate(integration_id=integration_id)
```
