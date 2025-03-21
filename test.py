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

client_id = 'f6edd01f-6f0b-41b6-a653-24de534054b3'
client_secret = '3f3a44c8-ee76-40bf-ac41-3e1c9f1f6203'
url = 'https://sandbox-oauth.piste.gouv.fr/api/oauth/token'

client = LegiHandler()
client.token_url = url
client.api_url = "https://sandbox-api.piste.gouv.fr/dila/legifrance/lf-engine-app/"
client.set_api_keys(legifrance_api_key=client_id, legifrance_api_secret=client_secret)


# Obtenir l'article 7 du Code civil
resu = recherche_CODE(code_name="Code civil", search="7")
#pprint.pprint(resu)

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
#print(access_token)

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

data1 = "{\"recherche\":{\"filtres\":[{\"valeurs\":[\"LOI\",\"ORDONNANCE\",\"ARRETE\"],\"facette\":\"NATURE\"},{\"dates\":{\"start\":\"2020-01-01\",\"end\":\"2025-01-31\"},\"facette\":\"DATE_SIGNATURE\"}],\"sort\":\"SIGNATURE_DATE_DESC\",\"fromAdvancedRecherche\":false,\"secondSort\":\"ID\",\"champs\":[{\"criteres\":[{\"valeur\":\"information\",\"criteres\":[{\"valeur\":\"sécurité\",\"operateur\":\"ET\",\"typeRecherche\":\"UN_DES_MOTS\"}],\"operateur\":\"ET\",\"typeRecherche\":\"UN_DES_MOTS\"}],\"operateur\":\"ET\",\"typeChamp\":\"TITLE\"}],\"pageSize\":10,\"operateur\":\"ET\",\"typePagination\":\"DEFAUT\",\"pageNumber\":1},\"fond\":\"LODA_DATE\"}"

x = requests.post(url, headers=headers, data=data1)
pprint.pprint(x.text)

pprint.pprint(x)
f = open("res3.json", "w")
f.write(str(x.text))
f.close()

url = 'https://sandbox-api.piste.gouv.fr/dila/legifrance/lf-engine-app/search'

#data1 = "{\"recherche\":{\"filtres\":[{\"valeurs\":[\"LOI\",\"ORDONNANCE\",\"ARRETE\"],\"facette\":\"NATURE\"},{\"dates\":{\"start\":\"2015-01-01\",\"end\":\"2025-01-31\"},\"facette\":\"DATE_SIGNATURE\"}],\"sort\":\"SIGNATURE_DATE_DESC\",\"fromAdvancedRecherche\":false,\"secondSort\":\"ID\",\"champs\":[{\"criteres\":[{\"proximite\":1,\"valeur\":\"informatique\",\"criteres\":[{\"valeur\":\"informatique\",\"operateur\":\"ET\",\"typeRecherche\":\"TOUS_LES_MOTS_DANS_UN_CHAMP\"}],\"operateur\":\"ET\",\"typeRecherche\":\"TOUS_LES_MOTS_DANS_UN_CHAMP\"}],\"operateur\":\"ET\",\"typeChamp\":\"TITLE\"}],\"pageSize\":10,\"operateur\":\"ET\",\"typePagination\":\"DEFAUT\",\"pageNumber\":3},\"fond\":\"LODA_DATE\"}"
data1 = "{\"recherche\":{\"filtres\":[{\"valeurs\":[\"LOI\",\"ORDONNANCE\",\"ARRETE\"],\"facette\":\"NATURE\"},{\"dates\":{\"start\":\"2020-01-01\",\"end\":\"2025-01-31\"},\"facette\":\"DATE_SIGNATURE\"}],\"sort\":\"SIGNATURE_DATE_DESC\",\"fromAdvancedRecherche\":false,\"secondSort\":\"ID\",\"champs\":[{\"criteres\":[{\"valeur\":\"information\",\"criteres\":[{\"valeur\":\"sécurité\",\"operateur\":\"ET\",\"typeRecherche\":\"UN_DES_MOTS\"}],\"operateur\":\"ET\",\"typeRecherche\":\"UN_DES_MOTS\"}],\"operateur\":\"ET\",\"typeChamp\":\"TITLE\"}],\"pageSize\":10,\"operateur\":\"ET\",\"typePagination\":\"DEFAUT\",\"pageNumber\":1},\"fond\":\"LODA_DATE\"}"

x = requests.post(url, headers=headers, data=data1)
pprint.pprint(x.text)

pprint.pprint(x)
f = open("res3.json", "w")
f.write(str(x.text))
f.close()