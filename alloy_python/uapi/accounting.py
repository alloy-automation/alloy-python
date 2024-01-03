import requests
from urllib.parse import urlencode
from ..constants import BASE_URL

class Accounting:
    def __init__(self, api_key):
        if not api_key:
            raise ValueError("API key must be provided")
        
        self.api_key = api_key
        self.headers = {
            'Authorization': f'Bearer {api_key}',
        }
        self.url = BASE_URL
        self.user_id = None
        self.connection_id = None

    def set_user(self, user_id):
        self.user_id = user_id

    def connect(self, connection_id):
        self.connection_id = connection_id

    def _api_request(self, method, endpoint, params=None, data=None):
        url = f'{self.url}/one/accounting/{endpoint}?connectionId={self.connection_id}'
        if params:
            url += f'&{urlencode(params)}'
        try:
            response = requests.request(method, url, headers=self.headers, json=data)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            return {"error": http_err.response.json().get('message', 'An error occurred'), "status_code": http_err.response.status_code}
        except requests.exceptions.RequestException as req_err:
            print(f"Error: {req_err}")
            return {"error": "Network or request error", "status_code": 500}

    def list_company_info(self, filter=None):
        params = filter if filter else {}
        return self._api_request('GET', 'company-info', params=params)

    def get_company_info_count(self):
        return self._api_request('GET', 'company-info/count')

    def get_company_info(self, company_info_id, filter=None):
        params = filter if filter else {}
        return self._api_request('GET', f'company-info/{company_info_id}', params=params)
    
    def create_account(self, data):
        return self._api_request('POST', 'accounts', data=data)

    def list_accounts(self, filter=None):
        params = filter if filter else {}
        return self._api_request('GET', 'accounts', params=params)

    def get_account_count(self):
        return self._api_request('GET', 'accounts/count')

    def get_account(self, account_id, filter=None):
        params = filter if filter else {}
        return self._api_request('GET', f'accounts/{account_id}', params=params)

    def update_account(self, account_id, data):
        return self._api_request('PUT', f'accounts/{account_id}', data=data)

    def delete_account(self, account_id):
        return self._api_request('DELETE', f'accounts/{account_id}')
    
    def create_customer(self, data):
        return self._api_request('POST', 'customers', data=data)

    def list_customers(self, filter=None):
        params = filter if filter else {}
        return self._api_request('GET', 'customers', params=params)

    def get_customer_count(self):
        return self._api_request('GET', 'customers/count')

    def get_customer(self, customer_id, filter=None):
        params = filter if filter else {}
        return self._api_request('GET', f'customers/{customer_id}', params=params)

    def update_customer(self, customer_id, data):
        return self._api_request('PUT', f'customers/{customer_id}', data=data)

    def delete_customer(self, customer_id):
        return self._api_request('DELETE', f'customers/{customer_id}')
    
    def create_vendor(self, data):
        return self._api_request('POST', 'vendors', data=data)

    def list_vendors(self, filter=None):
        params = filter if filter else {}
        return self._api_request('GET', 'vendors', params=params)

    def get_vendor_count(self):
        return self._api_request('GET', 'vendors/count')

    def get_vendor(self, vendor_id, filter=None):
        params = filter if filter else {}
        return self._api_request('GET', f'vendors/{vendor_id}', params=params)

    def update_vendor(self, vendor_id, data):
        return self._api_request('PUT', f'vendors/{vendor_id}', data=data)

    def delete_vendor(self, vendor_id):
        return self._api_request('DELETE', f'vendors/{vendor_id}')
    
    def list_tax_rates(self, filter=None):
        params = filter if filter else {}
        return self._api_request('GET', 'tax-rates', params=params)

    def get_tax_rate_count(self):
        return self._api_request('GET', 'tax-rates/count')

    def get_tax_rate(self, tax_rate_id, filter=None):
        params = filter if filter else {}
        return self._api_request('GET', f'tax-rates/{tax_rate_id}', params=params)

    def list_tracking_categories(self, filter=None):
        params = filter if filter else {}
        return self._api_request('GET', 'tracking-categories', params=params)

    def get_tracking_category_count(self):
        return self._api_request('GET', 'tracking-categories/count')

    def get_tracking_category(self, tracking_category_id, filter=None):
        params = filter if filter else {}
        return self._api_request('GET', f'tracking-categories/{tracking_category_id}', params=params)