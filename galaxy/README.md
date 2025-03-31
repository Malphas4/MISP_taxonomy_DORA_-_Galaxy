
# Galaxy help

## Outils utilisé

> [!NOTE]
> [API Légifrance](https://piste.gouv.fr/index.php?option=com_apiportal&view=apitester&usage=api&apitab=tests&apiName=L%C3%A9gifrance&apiId=7e5a0e1d-ffcc-40be-a405-a1a5c1afe950&managerId=3&type=rest&apiVersion=2.4.2&Itemid=179&swaggerVersion=2.0&lang=fr)
> * API qui permet de récupérer les données juridiques de Légifrance
> 
> Python3
> * Pour le script qui récupère les informations utiles depuis Legifrance
> 
> [pylegifrance](https://github.com/rdassignies/pylegifrance/)
> * Librairie python qui utilise l'API Légifrance pour une utilisation simplifiée

## Comment récupérer les informations ?

### 1. Création d'un compte piste pour avoir accès à l'API Légifrance

Aller sur le site https://piste.gouv.fr/, puis créer un compte.

### 2. Accepter les consentements CGU pour utiliser l'API

Aller sur https://piste.gouv.fr/index.php?option=com_apiportal&view=cgu, puis dans la barre de recherche, taper *légifrance*.
Cocher ensuite les lignes correspondantes (PROD et SANDBOX), puis appuyer sur le bouton *Valider mes choix CGU*.

### 3. Sélection de l'API

Aller sur https://piste.gouv.fr/apps et sélectionner APP_SANDBOX_XXXXX, puis appuyer sur *Modifier l'application*, puis dans *Sélectionner les API*, cocher Légifrance. Faire ensuite *Appliquer les modifications*.

Il faut ensuite récupérer le *client_id* et le *client_secret* pour l'activation de l'API. Ils se trouvent dans la rubrique *Identifiants Oauth*. Pour voir le *client_secret*, il faut cliquer sur *Consulter le secret*.

### 4. Activer l'utilisation de l'API

Aller sur https://piste.gouv.fr/apimgt/api-center, sélectionner l'API *Légifrance*, puis dans la section *Documentation API*, appuyer sur le bouton *Authorize*.

Renseigner ensuite le *client_id* et le *client_secret*, et sélectionner comme scope *openid*. Cliquer ensuite sur *Authorize*.

### 5. Installation du module pylegifrance

Pour l'installer, il suffit de taper dans le terminal `pip install git+https://github.com/rdassignies/pylegifrance`.

### 6. Exécution du script python

Dans le script, renseigner son *client_id* et *client_secret*, puis lancer le script.