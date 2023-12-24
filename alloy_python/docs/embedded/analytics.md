# Analytics SDK Documentation

## Overview

The Analytics SDK provides a client for retrieving analytics data related to workflows.

## Get Analytics Data

Retrieve analytics data for a specific workflow.

```python
from alloy_python.embedded import Embedded

# Initialize the Embedded SDK with your API key
api_key = 'YOUR_API_KEY'
embedded = Embedded(api_key)

# Get analytics for a workflow
workflow_id = "workflow123"
analytics_data = embedded.Analytics.get(workflow_id)
```