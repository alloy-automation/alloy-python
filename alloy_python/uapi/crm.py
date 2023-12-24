import requests
from ..constants import BASE_URL

class CRM:
    def __init__(self, api_key):
        self.api_key = api_key
        self.headers = {
            'Authorization': f'Bearer {api_key}',
        }
        self.user_id = None
        self.connection_id = None
        self.base_url = BASE_URL

    def set_user(self, user_id):
        self.user_id = user_id

    def connect(self, connection_id):
        self.connection_id = connection_id

    def _api_request(self, method, endpoint, params=None, data=None):
        url = f'{self.base_url}/{endpoint}?connectionId={self.connection_id}'
        response = requests.request(
            method,
            url,
            headers=self.headers,
            params=params,
            json=data,
        )
        response.raise_for_status()
        return response.json()

    # Account-related methods
    def list_accounts(self, filter=None):
        return self._api_request('GET', 'one/crm/accounts', params=filter)

    def get_accounts_count(self):
        return self._api_request('GET', 'one/crm/accounts/count')

    def get_account(self, account_id, filter=None):
        return self._api_request('GET', f'one/crm/accounts/{account_id}', params=filter)

    def create_account(self, data):
        return self._api_request('POST', 'one/crm/accounts', data=data)

    def update_account(self, account_id, data):
        return self._api_request('PUT', f'one/crm/accounts/{account_id}', data=data)

    def delete_account(self, account_id):
        return self._api_request('DELETE', f'one/crm/accounts/{account_id}')

    # Contact-related methods
    def list_contacts(self, filter=None):
        return self._api_request('GET', 'one/crm/contacts', params=filter)

    def get_contacts_count(self):
        return self._api_request('GET', 'one/crm/contacts/count')

    def get_contact(self, contact_id, filter=None):
        return self._api_request('GET', f'one/crm/contacts/{contact_id}', params=filter)

    def create_contact(self, data):
        return self._api_request('POST', 'one/crm/contacts', data=data)

    def update_contact(self, contact_id, data):
        return self._api_request('PUT', f'one/crm/contacts/{contact_id}', data=data)

    def delete_contact(self, contact_id):
        return self._api_request('DELETE', f'one/crm/contacts/{contact_id}')

    # Lead-related methods
    def list_leads(self, filter=None):
        return self._api_request('GET', 'one/crm/leads', params=filter)

    def get_leads_count(self):
        return self._api_request('GET', 'one/crm/leads/count')

    def get_lead(self, lead_id, filter=None):
        return self._api_request('GET', f'one/crm/leads/{lead_id}', params=filter)

    def create_lead(self, data):
        return self._api_request('POST', 'one/crm/leads', data=data)

    def update_lead(self, lead_id, data):
        return self._api_request('PUT', f'one/crm/leads/{lead_id}', data=data)

    def delete_lead(self, lead_id):
        return self._api_request('DELETE', f'one/crm/leads/{lead_id}')

    # Note-related methods
    def list_notes(self, filter=None):
        return self._api_request('GET', 'one/crm/notes', params=filter)

    def get_notes_count(self):
        return self._api_request('GET', 'one/crm/notes/count')

    def get_note(self, note_id, filter=None):
        return self._api_request('GET', f'one/crm/notes/{note_id}', params=filter)

    def create_note(self, data):
        return self._api_request('POST', 'one/crm/notes', data=data)

    def update_note(self, note_id, data):
        return self._api_request('PUT', f'one/crm/notes/{note_id}', data=data)

    def delete_note(self, note_id):
        return self._api_request('DELETE', f'one/crm/notes/{note_id}')

    # Task-related methods
    def list_tasks(self, filter=None):
        return self._api_request('GET', 'one/crm/tasks', params=filter)

    def get_tasks_count(self):
        return self._api_request('GET', 'one/crm/tasks/count')

    def get_task(self, task_id, filter=None):
        return self._api_request('GET', f'one/crm/tasks/{task_id}', params=filter)

    def create_task(self, data):
        return self._api_request('POST', 'one/crm/tasks', data=data)

    def update_task(self, task_id, data):
        return self._api_request('PUT', f'one/crm/tasks/{task_id}', data=data)

    def delete_task(self, task_id):
        return self._api_request('DELETE', f'one/crm/tasks/{task_id}')

    # Opportunity-related methods
    def list_opportunities(self, filter=None):
        return self._api_request('GET', 'one/crm/opportunities', params=filter)

    def get_opportunities_count(self):
        return self._api_request('GET', 'one/crm/opportunities/count')

    def get_opportunity(self, opportunity_id, filter=None):
        return self._api_request('GET', f'one/crm/opportunities/{opportunity_id}', params=filter)

    def create_opportunity(self, data):
        return self._api_request('POST', 'one/crm/opportunities', data=data)

    def update_opportunity(self, opportunity_id, data):
        return self._api_request('PUT', f'one/crm/opportunities/{opportunity_id}', data=data)

    def delete_opportunity(self, opportunity_id):
        return self._api_request('DELETE', f'one/crm/opportunities/{opportunity_id}')

    # User-related methods
    def list_users(self, filter=None):
        return self._api_request('GET', 'one/crm/users', params=filter)

    def list_users_count(self):
        return self._api_request('GET', 'one/crm/users/count')

    def get_user(self, user_id, filter=None):
        return self._api_request('GET', f'one/crm/users/{user_id}', params=filter)

    def create_user(self, data):
        return self._api_request('POST', 'one/crm/users', data=data)

    def update_user(self, user_id, data):
        return self._api_request('PUT', f'one/crm/users/{user_id}', data=data)

    def delete_user(self, user_id):
        return self._api_request('DELETE', f'one/crm/users/{user_id}')
