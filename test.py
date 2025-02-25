import requests
import pprint

# https://github.com/rdassignies/pylegifrance

# HOW TO GET client_id AND client_secret ?
#
# 1) Sign in on https://piste.gouv.fr/
# 2) Go on applications
# 3) Select the APP_SANDOX
# 4) On the OAuth Credentials raw:
#   a) For client_id: select the id below 'Client ID'
#   b) For client_secret: click on 'View secret' and copy the key

client_id = 'xxx'
client_secret = 'xxx'

url = 'https://sandbox-oauth.piste.gouv.fr/api/oauth/token'

from pylegifrance import LegiHandler
client = LegiHandler()
client.token_url = url
client.api_url = "https://sandbox-api.piste.gouv.fr/dila/legifrance/lf-engine-app/"
client.set_api_keys(legifrance_api_key=client_id, legifrance_api_secret=client_secret)

from pylegifrance import recherche_CODE

# Obtenir l'article 7 du Code civil
resu = recherche_CODE(code_name="Code civil", search="7")
pprint.pprint(resu)

headers = {
        'Accept-Encoding' : 'gzip,deflate',
        'Content-Type' : 'application/x-www-form-urlencoded',
        'Content-Length' : '140',
        'Host' : 'sandbox-oauth.piste.gouv.fr',
        'Connection' : 'Keep-Alive',
        'User-Agent' : 'Apache-HttpClient/4.1.1 (java 1.5)'
    }

data = {
        'grant_type' : 'client_credentials',
        'client_id' : client_id,
        'client_secret' : client_secret,
        'scope' : 'openid'
    }

x = requests.post(url, data=data, headers=headers)
access_token = str(x.json()['access_token'])
print(access_token)

#######

##url = 'https://sandbox-api.piste.gouv.fr/dila/legifrance/lf-engine-app/list/ping'

headers = {
        'Authorization' : 'Bearer ' + access_token,
        'Content-Type' : 'application/json',
        'accept': 'application/json'
    }

##x = requests.post(url, headers=headers)
##pprint.pprint(x.text)

########

url = 'https://sandbox-api.piste.gouv.fr/dila/legifrance/lf-engine-app/consult/getCnilWithAncienId'

data1 = "{\"ancienId\":\"MCN97020008A\"}"

x = requests.post(url, headers=headers, data=data1)
#pprint.pprint(x.text)

resu = recherche_CODE(code_name="Code civil", search="7", formatter=True)
pprint.pprint(resu)