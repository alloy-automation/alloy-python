from .accounting import Accounting
from .commerce import Commerce
from .crm import CRM

class UAPI:
    def __init__(self, api_key):
        if not api_key:
            raise ValueError("API key must be provided")
        
        self.api_key = api_key

        # Initialize all other classes with the API key
        self.Accounting = Accounting(api_key)
        self.Commerce = Commerce(api_key)
        self.CRM = CRM(api_key)

    def identify(self, username):
        # Implementation for identifying a user
        pass

    def clear(self):
        # Implementation to clear stored data
        pass
