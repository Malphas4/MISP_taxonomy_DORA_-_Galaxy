import requests
import pprint
import json

from pylegifrance import LegiHandler
from pylegifrance import recherche_CODE
from pylegifrance import recherche_LODA

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

client = LegiHandler()
client.token_url = url
client.api_url = "https://sandbox-api.piste.gouv.fr/dila/legifrance/lf-engine-app/"
client.set_api_keys(legifrance_api_key=client_id, legifrance_api_secret=client_secret)


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

#data1 = "{\"ancienId\":\"MCN97020008A\"}"

#x = requests.post(url, headers=headers, data=data1)
#pprint.pprint(x.text)

resu = recherche_LODA(search="cybersécurité", champ='ALL', type_recherche='TOUS_LES_MOTS_DANS_UN_CHAMP', nature=['DECRET'], date_signature=["2017-01-01", "2025-01-01"], page_size=1)
pprint.pprint(resu)
f = open("res1.json", "w")
f.write(str(resu[0]))
f.close()

print("\n\n\n")

resu = recherche_LODA(search="RGPD", champ='ALL', type_recherche='TOUS_LES_MOTS_DANS_UN_CHAMP', nature=['DECRET'], date_signature=["2018-01-01", "2025-01-01"], page_size=3)
pprint.pprint(resu)
f = open("res2.json", "w")
f.write(str(resu[0]))
f.close()