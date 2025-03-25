#!/usr/bin/env python
import json
import duo_client
import sys


# Import API credentials from Duo_Account.py
from DuoAccount import ikey, skey, host

# Ensure a parameter is provided for the new tenant name
if len(sys.argv) != 2:
    print("Usage: python DuoProvision.py <new_tenant_name>")
    sys.exit(1)

# Retrieve the new tenant name from command-line argument
account_name = sys.argv[1]
#print(f"Creating new tenant: {account_name}")

# Initialize Duo Accounts client with imported credentials
accounts = duo_client.Accounts(ikey, skey, host)

# Create the account and display the result
try:
    account_create_info = accounts.create_account(account_name)
    if 'account_id' in account_create_info:
        print('OK')
    else:    
        print(account_create_info)
except Exception as e:
    print(f"Error creating account: {e}")