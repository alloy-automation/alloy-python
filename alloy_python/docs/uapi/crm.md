# CRM SDK Documentation

## Overview

The CRM SDK provides a client for interacting with our [Customer Relationship Management (CRM) model](https://docs-uapi.runalloy.com/reference/crm).

## Authentication

To use the CRM API, you need to instantiate the CRM class with a valid API key.

```python
from alloy_python.uapi import UAPI

api_key = "YOUR_API_KEY"
crm = CRM(api_key)
```

### Set the connectionId

Set the connectionId using the `connect()` method.

```python
crm.connect("YOUR_CONNECTION_ID")
```

## Methods

### Accounts

#### List Accounts

List all accounts with an optional filter.

```python
all_accounts = crm.list_accounts()
```

#### Get Accounts Count

Get the count of accounts.

```python
accounts_count = crm.get_accounts_count()
```

#### Get Account

Get detailed account information by ID with an optional filter.

```python
detailed_account_info = crm.get_account(accountId)
```

#### Create Account

Create an account with the provided data.

```python
account_data = {"accountName": "Mojica"}
created_account = crm.create_account(account_data)
```

#### Update Account

Update an account by ID with the provided data.

```python
update_account_data = {"accountName": "UpdatedAccountName"}
updated_account = crm.update_account(accountId, update_account_data)
```

#### Delete Account

Delete an account by ID.

```python
crm.delete_account(accounrId)
```

### Contacts

#### List Contacts

List all contacts with an optional filter.

```python
all_contacts = crm.list_contacts()
```

#### Get Contacts Count

Get the count of contacts.

```python
contacts_count = crm.get_contacts_count()
```

#### Get Contact

Get detailed contact information by ID with an optional filter.

```python
detailed_contact_info = crm.get_contact(contactId)
```

#### Create Contact

Create a contact with the provided data.

```python
contact_data = { "firstName": "Gregg", "lastName": "Mojica" }
created_contact = crm.create_contact(contact_data)
```

#### Update Contact

Update a contact by ID with the provided data.

```python
update_contact_data = { "firstName": "Gregg", "lastName": "Jameson" }
updated_contact = crm.update_contact(contactId, update_contact_data)
```

#### Delete Contact

Delete a contact by ID.

```python
crm.delete_contact(contactId)
```

### Lead

#### List Leads

List all leads with an optional filter.

```python
all_leads = crm.list_leads()
```

#### Get Leads Count

Get the count of leads.

```python
leads_count = crm.get_leads_count()
```

#### Get Lead

Get detailed lead information by ID with an optional filter.

```python
detailed_lead_info = crm.get_lead(leadId)
```

#### Create Lead

Create a lead with the provided data.

```python
lead_data = { "lastName": "Mojica", "company": "Alloy" }
created_lead = crm.create_lead(lead_data)
```

#### Update Lead

Update a lead by ID with the provided data.

```python
update_lead_data = { "lastName": "Mojica", "company": "Alloy Automation" }
updated_lead = crm.update_lead(leadId, update_lead_data)
```

#### Delete Lead

Delete a lead by ID.

```python
crm.delete_lead(leadId)
```

### Notes

#### List Notes

List all notes with an optional filter.

```python
all_notes = crm.list_notes()
```

#### Get Notes Count

Get the count of notes.

```python
notes_count = crm.get_notes_count()
```

#### Get Note

Get detailed note information by ID with an optional filter.

```python
detailed_note_info = crm.get_note(noteId)
```

#### Create Note

Create a note with the provided data.

```python
note_data = {"noteTitle": "Meeting Notes", "content": "Discussed future plans."}
created_note = crm.create_note(note_data)
```

#### Update Note

Update a note by ID with the provided data.

```python
update_note_data = { "noteContent": "New Note", "noteTitle": "Test", "noteContact": "contactId" }
updated_note = crm.update_note(noteId, update_note_data)
```

#### Delete Note

Delete a note by ID.

```python
crm.delete_note(noteId)
```

### Task

#### List Tasks

List all tasks with an optional filter.

```python
all_tasks = crm.list_tasks()
```

#### Get Tasks Count

Get the count of tasks.

```python
tasks_count = crm.get_tasks_count()
```

#### Get Task

Get detailed task information by ID with an optional filter.

```python
detailed_task_info = crm.get_task(taskId)
```

#### Create Task

Create a task with the provided data.

```python
task_data = {"taskSubject": "Mappings"}
created_task = crm.create_task(data=task_data)
```

#### Update Task

Update a task by ID with the provided data.

```python
update_task_data = {"taskSubject": "New Mappings"}
updated_task = crm.update_task(taskId, update_task_data)
```

#### Delete Task

Delete a task by ID.

```python
crm.delete_task(taskId)
```

### Opportunity

#### List Opportunities

List all opportunities with an optional filter.

```python
all_opportunities = crm.list_opportunities()
```

#### Get Opportunities Count

Get the count of opportunities.

```python
opportunities_count = crm.get_opportunities_count()
```

#### Get Opportunity

Get detailed opportunity information by ID with an optional filter.

```python
detailed_opportunity_info = crm.get_opportunity(opportunityId)
```

#### Create Opportunity

Create an opportunity with the provided data.

```python
opportunity_data = {"opportunityName": "NewDeal", "amount": 5000.0}
created_opportunity = crm.create_opportunity(opportunity_data)
```

#### Update Opportunity

Update an opportunity by ID with the provided data.

```python
update_opportunity_data = { "opportunityName": "New Opportunity", "opportunityStage": "appointmentscheduled", "closeDate": "2026-11-17" }
updated_opportunity = crm.update_opportunity(opportunityId, update_opportunity_data)
```

#### Delete Opportunity

Delete an opportunity by ID.

```python
crm.delete_opportunity(opportunityId")
```

### User

#### List Users

List all users with an optional filter.

```python
all_users = crm.list_users()
```

#### List Users Count

Get the count of users.

```python
users_count = crm.list_users_count()
```

#### Get User

Get detailed user information by ID with an optional filter.

```python
detailed_user_info = crm.get_user(userId)
```

#### Create User

Create a user with the provided data.

```python
user_data = { "userFirstName": "Gregg", "userLastName": "Mojica", "userEmail": "gregg@runalloy.com" }
created_user = crm.create_user(user_data)
```

#### Update User

Update a user by ID with the provided data.

```python
update_user_data = { "userFirstName": "Hanna Grace" }
updated_user = crm.update_user(userId, update_user_data)
```

#### Delete User

Delete a user by ID.

```python
crm.delete_user(userId)
```
