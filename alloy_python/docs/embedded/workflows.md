# Workflows SDK Documentation

## Overview

The Workflows SDK provides functionality for managing workflows, including listing workflows, retrieving workflow details, listing versions of a workflow, activating, deactivating, upgrading, and deleting workflows.

## Set User ID

Set the user ID for the Workflows SDK instance.

```python
from alloy_python.embedded import Embedded

# Initialize the Embedded SDK with your API key
api_key = 'YOUR_API_KEY'
embedded = Embedded(api_key)

# Set the user ID for the Workflows SDK instance
user_id = "user123"
embedded.Workflows.set_user_id(user_id)
```

## List Workflows

Retrieve a list of all workflows associated with the user.

```python
from alloy_python.embedded import Embedded

# Initialize the Embedded SDK with your API key
api_key = 'YOUR_API_KEY'
embedded = Embedded(api_key)

# Retrieve a list of all workflows
workflow_list = embedded.Workflows.list()
```

## List Workflow Versions

Retrieve a list of versions for a specific workflow.

```python
from alloy_python.embedded import Embedded

# Initialize the Embedded SDK with your API key
api_key = 'YOUR_API_KEY'
embedded = Embedded(api_key)

# Set the user ID for which you want to list workflow versions
user_id = "user123"
embedded.Workflows.set_user_id(user_id)

# Workflow ID for which to list versions
workflow_id = "workflow123"
version_list = embedded.Workflows.list_versions(workflow_id)
```

## Get Workflow

Retrieve detailed information for a specific workflow.

```python
from alloy_python.embedded import Embedded

# Initialize the Embedded SDK with your API key
api_key = 'YOUR_API_KEY'
embedded = Embedded(api_key)

# Set the user ID for which you want to retrieve workflow details
user_id = "user123"
embedded.Workflows.set_user_id(user_id)

# Workflow ID for which to retrieve details
workflow_id = "workflow123"
workflow_info = embedded.Workflows.get(workflow_id)
```

## Deactivate All Workflows

Deactivate all workflows associated with the user.

```python
from alloy_python.embedded import Embedded

# Initialize the Embedded SDK with your API key
api_key = 'YOUR_API_KEY'
embedded = Embedded(api_key)

# Deactivate all workflows
deactivation_result = embedded.Workflows.deactivate_all()
```

## Activate Workflow

Activate a specific workflow.

```python
from alloy_python.embedded import Embedded

# Initialize the Embedded SDK with your API key
api_key = 'YOUR_API_KEY'
embedded = Embedded(api_key)

# Workflow ID to activate
workflow_id = "workflow123"
activation_result = embedded.Workflows.activate(workflow_id)
```

## Deactivate Workflow

Deactivate a specific workflow.

```python
from alloy_python.embedded import Embedded

# Initialize the Embedded SDK with your API key
api_key = 'YOUR_API_KEY'
embedded = Embedded(api_key)

# Workflow ID to deactivate
workflow_id = "workflow123"
deactivation_result = embedded.Workflows.deactivate(workflow_id)
```

## Upgrade Workflow

Upgrade a specific workflow to the latest version.

```python
from alloy_python.embedded import Embedded

# Initialize the Embedded SDK with your API key
api_key = 'YOUR_API_KEY'
embedded = Embedded(api_key)

# Workflow ID to upgrade
workflow_id = "workflow123"
upgrade_result = embedded.Workflows.upgrade(workflow_id)
```

## Delete Workflow

Delete a specific workflow.

```python
from alloy_python.embedded import Embedded

# Initialize the Embedded SDK with your API key
api_key = 'YOUR_API_KEY'
embedded = Embedded(api_key)

# Workflow ID to delete
workflow_id = "workflow123"
deletion_result = embedded.Workflows.delete(workflow_id)
```
