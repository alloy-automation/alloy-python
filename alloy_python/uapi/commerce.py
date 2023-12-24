# commerce.py
import requests
from urllib.parse import urlencode
from ..constants import BASE_URL

class Commerce:
    def __init__(self, api_key):
        if not api_key:
            raise ValueError("API key must be provided")
        self.url = BASE_URL
        self.api_key = api_key
        self.headers = {'Authorization': f'Bearer {api_key}'}

    def _api_request(self, method, endpoint, params=None, data=None):
        url = f'{self.url}/one/commerce/{endpoint}?connectionId={self.connection_id}'
        if params:
            url += f'&{urlencode(params)}'
        response = requests.request(method, url, headers=self.headers, json=data)
        if not response.ok:
            print(f"Error: {response.status_code} - {response.reason}")
            return
        
        # response.raise_for_status()
        return response.json()

    def set_user_id(self, user_id):
        self.user_id = user_id

    def connect(self, connection_id):
        self.connection_id = connection_id

    def list_customers(self, filter=None):
        params = filter if filter else {}
        return self._api_request('GET', 'customers', params=params)

    def get_customer(self, customer_id, filter=None):
        params = filter if filter else {}
        return self._api_request('GET', f'customers/{customer_id}', params=params)

    def create_customer(self, data):
        return self._api_request('POST', 'customers', data=data)

    def update_customer(self, customer_id, data):
        return self._api_request('PUT', f'customers/{customer_id}', data=data)

    def delete_customer(self, customer_id):
        return self._api_request('DELETE', f'customers/{customer_id}')

    def list_orders(self, filter=None):
        params = filter if filter else {}
        return self._api_request('GET', 'orders', params=params)

    def get_order(self, order_id, filter=None):
        params = filter if filter else {}
        return self._api_request('GET', f'orders/{order_id}', params=params)

    def create_order(self, data):
        return self._api_request('POST', 'orders', data=data)

    def update_order(self, order_id, data):
        return self._api_request('PUT', f'orders/{order_id}', data=data)

    def delete_order(self, order_id):
        return self._api_request('DELETE', f'orders/{order_id}')

    def list_products(self, filter=None):
        params = filter if filter else {}
        return self._api_request('GET', 'products', params=params)

    def get_product(self, product_id, filter=None):
        params = filter if filter else {}
        return self._api_request('GET', f'products/{product_id}', params=params)

    def create_product(self, data):
        return self._api_request('POST', 'products', data=data)

    def update_product(self, product_id, data):
        return self._api_request('PUT', f'products/{product_id}', data=data)

    def delete_product(self, product_id):
        return self._api_request('DELETE', f'products/{product_id}')

    def list_product_variants(self, product_id, filter=None):
        params = filter if filter else {}
        return self._api_request('GET', f'products/{product_id}/variants', params=params)

    def get_product_variant(self, product_id, variant_id, filter=None):
        params = filter if filter else {}
        return self._api_request('GET', f'products/{product_id}/variants/{variant_id}', params=params)

    def create_product_variant(self, product_id, data):
        return self._api_request('POST', f'products/{product_id}/variants', data=data)

    def update_product_variant(self, product_id, variant_id, data):
        return self._api_request('PUT', f'products/{product_id}/variants/{variant_id}', data=data)

    def delete_product_variant(self, product_id, variant_id):
        return self._api_request('DELETE', f'products/{product_id}/variants/{variant_id}')

    def list_fulfillments(self, order_id, filter=None):
        params = filter if filter else {}
        return self._api_request('GET', f'orders/{order_id}/fulfillments', params=params)

    def get_fulfillment_count(self, order_id):
        return self._api_request('GET', f'orders/{order_id}/fulfillments/count')

    def get_fulfillment(self, order_id, fulfillment_id, filter=None):
        params = filter if filter else {}
        return self._api_request('GET', f'orders/{order_id}/fulfillments/{fulfillment_id}', params=params)
