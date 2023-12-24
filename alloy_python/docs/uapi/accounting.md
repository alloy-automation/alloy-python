# Accounting SDK Documentation

## Overview

Aloy Unified API prpvides a client for interacting with our [Unified Accounting model](https://docs-uapi.runalloy.com/reference/accounts).

### Authentication

To use the Accounting API, you need to instantiate the `Accounting` class with your API key and establish a connection.

```python
from alloy_python.uapi import UAPI

api_key = "YOUR_API_KEY"
accounting = Accounting(api_key)
```

### Set the connectionId

Set the connectionId using the `connect()` method.

```python
accounting.connect("YOUR_CONNECTION_ID")
```

## Methods

### Company Information

#### List Company Info

List company information with an optional filter.

```python
company_info_data = accounting.list_company_info()
```

#### Get Company Info Count

Get the count of company information records.

```python
company_info_count = accounting.get_company_info_count()
```

#### Get Company Info

Get detailed company information by ID with an optional filter.

```python
detailed_company_info = accounting.get_company_info(companyId)
```

### Accounts

#### Create Account

Create an account with the provided data.

```python
account_data = {"accountName": "SampleAccount", "accountType": "EXPENSE", "currency": "USD"}
created_account = accounting.create_account(account_data)
```

#### List Accounts

List all accounts with an optional filter.

```python
all_accounts = accounting.list_accounts()
```

#### Get Account Count

Get the count of accounts.

```python
account_count = accounting.get_account_count()
```

#### Get Account

Get detailed account information by ID with an optional filter.

```python
detailed_account_info = accounting.get_account(accountId)
```

#### Update Account

Update an account with the provided data.

```python
update_data = {}
updated_account = accounting.update_account(accountId, update_data)
```

#### Delete Account

Delete an account by ID.

```python
accounting.delete_account(accountId)
```

### Customers

#### Create Customer

Create a customer with the provided data.

```python
customer_data = {
    "customerName": "Alloy",
    "addresses": [
        {   
            "addressType": "BILLING",
            "street1": "Beverly Hills",
            "zipCode": "90210",
            "country": "US"
        }
    ],
    "phoneNumbers": [
        {
            "phoneNumberType": "MOBILE",
            "phoneNumber": "09173210215"
        }
    ],
    ...
}
created_customer = accounting.create_customer(customer_data)
```

#### List Customers

List all customers with an optional filter.

```python
all_customers = accounting.list_customers()
```

#### Get Customer Count

Get the count of customers.

```python
customer_count = accounting.get_customer_count()
```

#### Get Customer

Get detailed customer information by ID with an optional filter.

```python
detailed_customer_info = accounting.get_customer(customerId)
```

#### Update Customer

Update a customer with the provided data.

```python
update_customer_data = {}
updated_customer = accounting.update_customer(customerId, update_customer_data)
```

#### Delete Customer

Delete a customer by ID.

```python
accounting.delete_customer(customerId)
```

### Vendors

#### Create Vendor

Create a vendor with the provided data.

```python
vendor_data = {
    "vendorName": "Alloy123",
    "vendorStatus": "ACTIVE",
    "addresses": [
        {
            "addressType": "BILLING",
            "street1": "Avenue of the Americas",
            "zipCode": "90210",
            "country": "US"
        }
    ],
    "phoneNumbers": [
        {
            "phoneNumberType": "MOBILE",
            "phoneNumber": "09173210215"
        }
    ]
}
created_vendor = accounting.create_vendor(vendor_data)
```

#### List Vendors

List all vendors with an optional filter.

```python
all_vendors = accounting.list_vendors()
```

#### Get Vendor Count

Get the count of vendors.

```python
vendor_count = accounting.get_vendor_count()
```

#### Get Vendor

Get detailed vendor information by ID with an optional filter.

```python
detailed_vendor_info = accounting.get_vendor(vendorId)
```

#### Update Vendor

Update a vendor with the provided data.

```python
update_vendor_data = {"vendorName": "UpdatedVendorName"}
updated_vendor = accounting.update_vendor(vendorId, update_vendor_data)
```

#### Delete Vendor

Delete a vendor by ID.

```python
accounting.delete_vendor(vendorId)
```

### Tax Rates

#### List Tax Rates

List all tax rates with an optional filter.

```python
all_tax_rates = accounting.list_tax_rates()
```

#### Get Tax Rate Count

Get the count of tax rates.

```python
tax_rate_count = accounting.get_tax_rate_count()
```

#### Get Tax Rate

Get detailed tax rate information by ID with an optional filter.

```python
detailed_tax_rate_info = accounting.get_tax_rate(taxRateId)
```

### Tracking Categories

#### List Tracking Categories

List all tracking categories with an optional filter.

```python
all_tracking_categories = accounting.list_tracking_categories()
```

#### Get Tracking Category

Get detailed tracking category information by ID with an optional filter.

```python
tracking_category_info = accounting.get_tracking_category(trackingCategoryId)
```

#### Get Tracking Category Count

Get the count of tracking categories.

```python
tracking_category_count = accounting.get_tracking_category_count()
```
