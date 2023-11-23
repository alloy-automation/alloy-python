from alloy_python.embedded.embedded import Embedded

# Initialize with a specific API key
embedded = Embedded("laON7aWuiCDHyYQof42AT")

# Use the services
response = embedded.App.get_apps()
print(response)
