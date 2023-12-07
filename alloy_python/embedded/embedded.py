from .users import User
from .app import App
from .integrations import Integration
from .tokens import Tokens
from .workflows import Workflows
from .events import Events
from .compliance import Compliance
from .logs import Logs
from .credentials import Credentials
from .link import Link
from .analytics import Analytics

class Embedded:
    def __init__(self, api_key):
        self.api_key = api_key

        # Initialize all other classes with the API key
        self.User = User(api_key)
        self.App = App(api_key)
        self.Integration = Integration(api_key)
        self.Tokens = Tokens(api_key)
        self.Workflows = Workflows(api_key)
        self.Events = Events(api_key)
        self.Compliance = Compliance(api_key)
        self.Logs = Logs(api_key)
        self.Credentials = Credentials(api_key)
        self.Link = Link(api_key)
        self.Analytics = Analytics(api_key)

        # Additional setup as needed...

    def identify(self, username):
        # Implementation for identifying a user
        pass

    def clear(self):
        # Implementation to clear stored data
        pass
