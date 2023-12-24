import requests
from ..constants import BASE_URL

class Accounting:
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

    def list_company_info(self, filter=None):
        params = filter if filter else {}
        return self._api_request('GET', 'accounting/company-info', params=params)

    def get_company_info_count(self):
        return self._api_request('GET', 'accounting/company-info/count')

    def get_company_info(self, company_info_id, filter=None):
        params = filter if filter else {}
        return self._api_request('GET', f'accounting/company-info/{company_info_id}', params=params)
    
    def create_account(self, data):
        return self._api_request('POST', 'accounting/accounts', data=data)

    def list_accounts(self, filter=None):
        params = filter if filter else {}
        return self._api_request('GET', 'accounting/accounts', params=params)

    def get_account_count(self):
        return self._api_request('GET', 'accounting/accounts/count')

    def get_account(self, account_id, filter=None):
        params = filter if filter else {}
        return self._api_request('GET', f'accounting/accounts/{account_id}', params=params)

    def update_account(self, account_id, data):
        return self._api_request('PUT', f'accounting/accounts/{account_id}', data=data)

    def delete_account(self, account_id):
        return self._api_request('DELETE', f'accounting/accounts/{account_id}')
    
    def create_customer(self, data):
        return self._api_request('POST', 'accounting/customers', data=data)

    def list_customers(self, filter=None):
        params = filter if filter else {}
        return self._api_request('GET', 'accounting/customers', params=params)

    def get_customer_count(self):
        return self._api_request('GET', 'accounting/customers/count')

    def get_customer(self, customer_id, filter=None):
        params = filter if filter else {}
        return self._api_request('GET', f'accounting/customers/{customer_id}', params=params)

    def update_customer(self, customer_id, data):
        return self._api_request('PUT', f'accounting/customers/{customer_id}', data=data)

    def delete_customer(self, customer_id):
        return self._api_request('DELETE', f'accounting/customers/{customer_id}')
    
    def create_vendor(self, data):
        return self._api_request('POST', 'accounting/vendors', data=data)

    def list_vendors(self, filter=None):
        params = filter if filter else {}
        return self._api_request('GET', 'accounting/vendors', params=params)

    def get_vendor_count(self):
        return self._api_request('GET', 'accounting/vendors/count')

    def get_vendor(self, vendor_id, filter=None):
        params = filter if filter else {}
        return self._api_request('GET', f'accounting/vendors/{vendor_id}', params=params)

    def update_vendor(self, vendor_id, data):
        return self._api_request('PUT', f'accounting/vendors/{vendor_id}', data=data)

    def delete_vendor(self, vendor_id):
        return self._api_request('DELETE', f'accounting/vendors/{vendor_id}')
    
    def list_tax_rates(self, filter=None):
        params = filter if filter else {}
        return self._api_request('GET', 'accounting/tax-rates', params=params)

    def get_tax_rate_count(self):
        return self._api_request('GET', 'accounting/tax-rates/count')

    def get_tax_rate(self, tax_rate_id, filter=None):
        params = filter if filter else {}
        return self._api_request('GET', f'accounting/tax-rates/{tax_rate_id}', params=params)

    def list_tracking_categories(self, filter=None):
        params = filter if filter else {}
        return self._api_request('GET', 'accounting/tracking-categories', params=params)

    def get_tracking_category_count(self):
        return self._api_request('GET', 'accounting/tracking-categories/count')

    def get_tracking_category(self, tracking_category_id, filter=None):
        params = filter if filter else {}
        return self._api_request('GET', f'accounting/tracking-categories/{tracking_category_id}', params=params)