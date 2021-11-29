import requests,json
import urllib3
urllib3.disable_warnings()

###  Step 1 - Define auth URL, Endpoint URL, Payload and Credentials  ###

# PU + OT - Replace with your tenants token URL
token_url = "https://mingle-sso.inforcloudsuite.com:443/NSACOM_DEM/as/token.oauth2"

# Endpoint URL - Can get from swagger documentation in IONAPI - Replace with your tenants API URL
test_api_url = "https://mingle-ionapi.inforcloudsuite.com/NSACOM_DEM/SX/rest/serviceinterface/proxy/FetchWhere"

# IONAPI Request - Replace payload with your own request
payload = """{
              "CompanyNumber": 1,
              "Operator": "RT01",
              "TableName": "sasp",
              "WhereClause": "",
              "BatchSize": 0,
              "RestartRowID": ""
             }"""

#SAAK
saak_user = "<< SAAK value from .ionapi >>"
#SASK
sask_password = "<< SASK value from .ionapi >>"
#CI
client_id = '<< CI value from .ionapi >>'
#CS
client_secret = '<< CS value from .ionapi >>'

###  ____________________________________________________________________________________  ###


###  Step 2 - single call with resource owner credentials in the body and client credentials as the basic auth header  ###

data = {
        'grant_type': 'password',
        'username': saak_user, 
        'password': sask_password
        }

access_token_response = requests.post(token_url, 
                        data=data, verify=False, allow_redirects=False, 
                        auth=(client_id, client_secret))
tokens = json.loads(access_token_response.text)

print ("access token: " + tokens['access_token'])

###  ____________________________________________________________________________________  ###


###  Step 3 - now we can use the access_token to make as many calls as we want until token expires.  ###

api_call_headers = {'Authorization': 'Bearer ' + tokens['access_token']}
api_call_response = requests.request("POST", test_api_url, headers=api_call_headers, data = payload, verify=False)

print (api_call_response.text.encode('utf8'))

###  ____________________________________________________________________________________  ###