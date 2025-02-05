import requests
import pprint

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

url = 'https://sandbox-api.piste.gouv.fr/dila/legifrance/lf-engine-app/search'

data = {
    "recherche": {
        "champs": [
            {
                "typeChamp": "NUM_ARTICLE",
                "criteres": [
                    {
                        "typeRecherche": "EXACTE",
                        "valeur": "L36-11",
                        "operateur": "ET"
                    }
                ],
                "operateur": "ET"
            }
        ],
        "filtres": [
            {
                "facette": "NOM_CODE",
                "valeurs": [
                    "Code des postes et des communications électroniques"
                ]
            },
            {
                "facette": "DATE_VERSION",
                "singleDate": "1514802418000"
            }
        ],
        "pageNumber": "1",
        "pageSize": "10",
        "operateur": "ET",
    "sort": "PERTINENCE",
        "typePagination": "ARTICLE"
    },
   "fond": "CODE_DATE"
}

data1 = {
  "recherche": {
    "filtres": [
      {
        "valeurs": [
          "LOI",
          "ORDONNANCE",
          "ARRETE"
        ],
        "facette": "NATURE"
      },
      {
        "dates": {
          "start": "2015-01-01",
          "end": "2018-01-31"
        },
        "facette": "DATE_SIGNATURE"
      }
    ],
    "sort": "SIGNATURE_DATE_DESC",
    "fromAdvancedRecherche": "false",
    "secondSort": "ID",
    "champs": [
      {
        "criteres": [
          {
            "proximite": "2",
            "valeur": "dispositions",
            "criteres": [
              {
                "valeur": "soins",
                "operateur": "ET",
                "typeRecherche": "UN_DES_MOTS"
              },
              {
                "proximite": "3",
                "valeur": "fonction publique",
                "operateur": "ET",
                "typeRecherche": "TOUS_LES_MOTS_DANS_UN_CHAMP"
              }
            ],
            "operateur": "ET",
            "typeRecherche": "UN_DES_MOTS"
          }
        ],
        "operateur": "ET",
        "typeChamp": "TITLE"
      }
    ],
    "pageSize": "10",
    "operateur": "ET",
    "typePagination": "DEFAUT",
    "pageNumber": "1"
  },
  "fond": "LODA_DATE"
}

x = requests.post(url, headers=headers, data=data1)
pprint.pprint(x.text)