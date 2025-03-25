Duo MSSP Examples scripts
====

These scripts show how to use Duo Account API.


How to install:
===

Please install `requests` and `duo_client` python modules:


`pip install requests`  
`pip install duo_clients`  

Please update DuoAccount.py data with Your Duo Account API credentials!

More info:
https://duo.com/docs/accountsapi#using-accounts-api-with-admin-api



How to run:
===

1. This script creates a new tenant with the name of NewAccount:
   
  `python DuoProvision.py NewAccount`  

  It gives back `OK` if everything is successful or provides the error message.   


2. This script deletes the NewAccount tenant:
   
  `python DuoUnProvision.py NewAccount` 
  
   It gives back `OK` if everything is successful or provides the error message.   


3. This script shows the status of a given tenant, like `NewAccount` here:
   
  `python DuoServiceHealth.py NewAccount`  
  
  It gives back `up` message if this is a valid tenant or 'down' if not.   

