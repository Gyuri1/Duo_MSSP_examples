#!/usr/bin/env python
import json
import duo_client
import sys

# Import API credentials from Duo_Account.py
from DuoAccount import ikey, skey, host

# Ensure a parameter is provided for the new tenant name
if len(sys.argv) != 2:
    print("Usage: python DuoServiceHelath.py <tenant_name>")
    sys.exit(1)

# Retrieve the new tenant name from command-line argument
account_name = sys.argv[1]
#print(f"UnProvision tenant: {account_name}")

# Initialize Duo Accounts client with imported credentials
accounts = duo_client.Accounts(ikey, skey, host)
child_accounts=accounts.get_child_accounts()

account_id = next((item['account_id'] for item in child_accounts if item['name'] == account_name), None)

if account_id:
    print("up")
else:
    print("down")
    exit()
