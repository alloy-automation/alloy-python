# Logs SDK Documentation

## Overview

The Logs SDK provides functionality for retrieving error information, logs, and rerunning workflow executions.

## Get Workflow Errors

Retrieve error information for a specific workflow.

```python
from alloy_python.embedded import Embedded

# Initialize the Embedded SDK with your API key
api_key = 'YOUR_API_KEY'
embedded = Embedded(api_key)

# Set the user ID for which you want to retrieve workflow errors
user_id = "user123"
embedded.Logs.set_user_id(user_id)

# Specify the workflow ID for which you want to retrieve errors
workflow_id = "workflow123"
workflow_errors = embedded.Logs.get_workflow_errors(workflow_id=workflow_id)
```

## Get Workflow Logs

Retrieve logs for a specific workflow.

```python
from alloy_python.embedded import Embedded

# Initialize the Embedded SDK with your API key
api_key = 'YOUR_API_KEY'
embedded = Embedded(api_key)

# Set the user ID for which you want to retrieve workflow logs
user_id = "user123"
embedded.Logs.set_user_id(user_id)

# Specify the workflow ID for which you want to retrieve logs
workflow_id = "workflow123"
workflow_logs = embedded.Logs.get_workflow_logs(workflow_id=workflow_id)
```

## Rerun Workflow Execution

Rerun a specific workflow execution.

```python
from alloy_python.embedded import Embedded

# Initialize the Embedded SDK with your API key
api_key = 'YOUR_API_KEY'
embedded = Embedded(api_key)

# Set the user ID for which you want to rerun a workflow execution
user_id = "user123"
embedded.Logs.set_user_id(user_id)

# Specify the workflow ID and execution ID for the workflow execution you want to rerun
workflow_id = "workflow123"
execution_id = "execution123"
rerun_result = embedded.Logs.rerun_workflow_execution(workflow_id=workflow_id, execution_id=execution_id)
```
