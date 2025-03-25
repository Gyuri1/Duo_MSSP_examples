#!/usr/bin/env python
import json
import duo_client
import sys


# Import API credentials from Duo_Account.py
from DuoAccount import ikey, skey, host

# Ensure a parameter is provided for the new tenant name
if len(sys.argv) != 2:
    print("Usage: python DuoUnProvision.py <new_tenant_name>")
    sys.exit(1)

# Retrieve the new tenant name from command-line argument
account_name = sys.argv[1]
#print(f"UnProvision tenant: {account_name}")

# Initialize Duo Accounts client with imported credentials
accounts = duo_client.Accounts(ikey, skey, host)


child_accounts=accounts.get_child_accounts()


account_id = next((item['account_id'] for item in child_accounts if item['name'] == account_name), None)

if not account_id:
    print("Error: Account not found.")
    exit()

# Delete the account and display the result
try:
    account_delete_info = accounts.delete_account(account_id)
    if account_delete_info=='':
    	print('OK')
    else:	
    	print(account_delete_info)
except Exception as e:
    print(f"Error deleting account: {e}")