# Commerce SDK Documentation

## Overview

The Commerce SDK provides a client for interacting with our [Unified Commerce model](https://docs-uapi.runalloy.com/reference/commerce).

## Authentication

To use the Commerce API, you need to instantiate the Commerce class with a valid API key.

```python
from alloy_python.uapi import UAPI

api_key = 'YOUR_API_KEY'
uapi = UAPI(api_key)
```

### Set the connectionId

Set the connectionId using the `connect()` method.

```python
uapi.Commerce.connect('YOUR_CONNECTION_ID')
```

## Methods

### List Customers

List all customers with an optional filter.

```python
all_customers = uapi.Commerce.list_customers()
```

### Get Customer

Get detailed customer information by ID with an optional filter.

```python
detailed_customer_info = uapi.Commerce.get_customer(customerId)
```

### Create Customer

Create a customer with the provided data.

```python
customer_data = { "firstName": "Alloy", "lastName": "Tester", "email": "testing@runalloy.com", "phone": "+639173220218" }
created_customer = uapi.Commerce.create_customer(customer_data)
```

### Update Customer

Update a customer by ID with the provided data.

```python
update_customer_data = {"customerName": "UpdatedCustomerName"}
updated_customer = uapi.Commerce.update_customer(customerId, update_customer_data)
```

### Delete Customer

Delete a customer by ID.

```python
uapi.Commerce.delete_customer(customerId)
```

### List Orders

List all orders with an optional filter.

```python
all_orders = uapi.Commerce.list_orders()
```

### Get Order

Get detailed order information by ID with an optional filter.

```python
detailed_order_info = uapi.Commerce.get_order(orderId)
```

### Create Order

Create an order with the provided data.

```python
order_data = {"orderNumber": "ORD-001", "totalAmount": 100.0, "customerId": "customer123"}
created_order = uapi.Commerce.create_order(order_data)
```

### Update Order

Update an order by ID with the provided data.

```python
update_order_data = {"orderNumber": "UpdatedORD-001"}
updated_order = uapi.Commerce.update_order(orderId, update_order_data)
```

### Delete Order

Delete an order by ID.

```python
uapi.Commerce.delete_order(orderId)
```

### List Products

List all products with an optional filter.

```python
all_products = uapi.Commerce.list_products()
```

### Get Product

Get detailed product information by ID with an optional filter.

```python
detailed_product_info = uapi.Commerce.get_product(productId)
```

### Create Product

Create a product with the provided data.

```python
product_data = {"productName": "SampleProduct", "price": 50.0, "category": "Electronics"}
created_product = uapi.Commerce.create_product(product_data)
```

### Update Product

Update a product by ID with the provided data.

```python
update_product_data = {"productName": "UpdatedProduct"}
updated_product = uapi.Commerce.update_product(productId, update_product_data)
```

### Delete Product

Delete a product by ID.

```python
uapi.Commerce.delete_product(productId)
```

### List Product Variants

List all variants of a product with an optional filter.

```python
all_product_variants = uapi.Commerce.list_product_variants(productId)
```

### Get Product Variant

Get detailed information about a product variant by ID with an optional filter.

```python
detailed_variant_info = uapi.Commerce.get_product_variant(productId, variantId)
```

### Create Product Variant

Create a variant for a product with the provided data.

```python
variant_data = {"variantName": "SampleVariant", "price": 60.0, "color": "Blue"}
created_variant = uapi.Commerce.create_product_variant(productId, variant_data)
```

### Update Product Variant

Update a variant of a product by ID with the provided data.

```python
update_variant_data = {"variantName": "UpdatedVariant"}
updated_variant = uapi.Commerce.update_product_variant(productId, variantId, update_variant_data)
```

### Delete Product Variant

Delete a variant of a product by ID.

```python
uapi.Commerce.delete_product_variant(productId, variantId)
```

### List Fulfillments

List all fulfillments for an order with an optional filter.

```python
all_fulfillments = uapi.Commerce.list_fulfillments(orderId)
```

### Get Fulfillment Count

Get the count of fulfillments for an order.

```python
fulfillment_count = uapi.Commerce.get_fulfillment_count(orderId)
```

### Get Fulfillment

Get detailed information about a fulfillment by ID for a specific order with an optional filter.

```python
detailed_fulfillment_info = uapi.Commerce.get_fulfillment(orderId, fulfillmentId)
```

