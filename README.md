# PythonSdk
This is a basic wrapper package for sending events to the [Alloy](https://runalloy.com/) API. It exposes a single class module, that you can use across your Python controllers.

## Installation

Install the PyPI and add to the application:

pip install alloy


## Usage

from alloy import run_alloy
run_alloy(
   apiKey=API_KEY,
   workflowId =workflowID,
   data = {parameterName: 'Parameter Value'},
   returnExecutionData = False
)


## Contributing
Bug reports and pull requests are welcome on GitHub at https://github.com/alloy-automation/alloy-python.

pip install calculato
