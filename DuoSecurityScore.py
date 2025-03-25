#!/usr/bin/env python
import json
import duo_client
import sys

import random

import time
from datetime import datetime, timedelta


# Import API credentials from Duo_Admin.py
from DuoAdmin import admin_ikey, admin_skey, admin_host

# Ensure a parameter is provided for the tenant name
if len(sys.argv) != 2:
    print("Usage: python DuoSecurityScore.py <tenant_name>")
    sys.exit(1)

# Retrieve the new tenant name from command-line argument
account_name = sys.argv[1]
#print(f"UnProvision tenant: {account_name}")

# Initialize Duo Accounts client with imported credentials
admin_api = duo_client.Admin(admin_ikey, admin_skey, admin_host)


# Calculate time range (last 30 days)
now = datetime.now()
maxtime = int(now.timestamp() * 1000)  # Current time in milliseconds
mintime = int((now - timedelta(days=179)).timestamp() * 1000)



#security_score=admin.get_trust_monitor_events_iterator(mintime= date_30_days_ago_unix, maxtime=unix_timestamp_ms)
#print(security_score)

"""
try:
    # Hypothetical trust monitor events iterator
    for event in admin_api.get_trust_monitor_events_iterator(mintime=mintime,maxtime=maxtime):
        # Print event details
        print(f"Event Type: {event.get('eventtype', 'N/A')}")
        print(f"Timestamp: {datetime.fromtimestamp(event['ts']/1000).isoformat()}")
        print(f"Action: {event.get('action', 'N/A')}")
        print(f"Actor: {event.get('actor', {}).get('name', 'N/A')}")
        print(f"Target: {event.get('target', {}).get('name', 'N/A')}")
        print("-" * 50)

except AttributeError:
    print("Error: get_trust_monitor_events_iterator method not found in Admin API client")
"""
security_score =random.randint(0, 100)
print(security_score)