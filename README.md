# MISP_taxonomy_DORA

## Description

Le but de ce projet est de créer une taxonomie pour DORA.
Nous nous sommes basés sur l'article de loi officiel accessible [ici](https://eur-lex.europa.eu/eli/reg/2022/2554/oj/eng)
Plusiers méthodes ont été utilisées :
1. Manuellement 
2. parsing textuel
3. IA avec contrôle humain et le json fait à la main en entrée
### Méthode manuelle
Une première version manuelle a été faite pour la liste des entités et leur définition.
Le json respectant le modèle et la documentqtion disponible [ici](https://www.circl.lu/doc/misp/taxonomy/)
### Parsing
Nous avons copié DORA dans un document .txt puis avons mis en forme le texte. Obtenir le json de l'étape 1 était relativement simple mais l'enrichir par cette méthode afin d'obtenir un json cohérent et structuré n'était pas possible. Une réflexion humaien est nécessaire afin de sélectionner les parties à intégrer. De plus, le texte n'évoluera pas dans le temps et si un changement est fait, nous estimons que la l'évolution de NIS  à NIS 2 est un bon exemple, les fonctions seront à refaire. 
Ainsi cette approche a été abandonné en cours de route car peu efficace.
### IA
L'utilisation d'une IA bureautique (Claude, Copilot, ChatGPT) a été essayé. Une limite de texte est imposé  et empêche le traitement de l'article en entier.
De ce fait un travail humain de sélection des parties à intégrer et de réflection reste nécessaire, par contre l'ajout dans le json obtenu manuellement est très efficace. 
De plus, un contrôle humain est obligatoire mais reste peu chronophage et plus précis que des scripst de parsing
### Fusion IA et parsing
Une piste possible serait du parsing pour sélectionner les parties intéressantes puis de les transformer en JSOn par IA mais cela n'a aps été fait par manque de temps et et volonté de passer à la galaxie.
## Vérification 
Nous avons installé une instance locale de MISP  avec [docker](https://github.com/MISP/misp-docker) afin de texter la taxonomie.
Une requête pour l'ajouter au github MISP reste à faire, des réflexions pour l'améliorer sont encore présentes.

# Galaxy_French_Law

### Description

Le but de ce projet est de créer une galaxie en liant des textes de loi avec des termes d'incident de cybersécurité tel que "cyberharcèlement, DDoS, rançonlogiciel ..."  

### Méthode API
Nous avons rassemblés toutes nos fonctions de scraping dans un fichier écrit en Python nommé "scraping.py".
Nous nous sommes tournées dans un premier temps vers l'API officiel du gouvernement francais [piste](https://piste.gouv.fr/?view=home)
le code présent est notre essai de récupérer les lois françaises selon un conetxte dédié.

Le premier problème que nous avons rencontré est que seul un nombre limité de loi ressortent. 
le second est que parmis les différentes option de recherche, la recherche dynamique présent sur le site que nous voulions utiliser n'est pas utilisable avec l'API. La recherche faite prend en compte les mots recheché dans les textes de loi avec un langague juridique et nous n'avons pas les compétences afin de faire les requêtes correctement.  
De plus, selon la zone de juridiction, les jurisprudence diffèrent, donnant un résultat différent à lier si nous vouliosn donner une estimation des peines ou ammendes.

Une alternative a été d'utiliser un projet open source sur Github mais la limite technique subsistait.
La recherche dynamique a projet d'être ajouté à l'API mais ne l'est pas encore.

### Solution alernative
Face à l'impossibilité d'utiliser l'API pour générer des json utilisable pour la galaxy, nous avons cherché d'autres alternatives, en vain.
Une piste possible mais envisagée trop tard pour la deadline de la faculté est dans les axes d'améliorations, AF dans notre temps libre après.
## Références

## Axes d'améliorations et réalisations restantes
1. Améliorer la taxonomie
2. Réessayer lors de l'ajout de la recherche dynamique 
3. Utiliser le [projet](https://github.com/louisbrulenaudet/legalkit-pipeline) afin d'entrainer une IA ou du Scrapping pour faire la galaxy
4.  Ajouter la taxonomie à MISP quand nous serons satisfait (avant la fin de l'année mais le stage est chronophage) 

## Comment lancer le projet

Pour lancer le projet, il suffit d'exécuter avec Python notre script.
Il utilise directement l'API [pylegifrance](https://github.com/rdassignies/pylegifrance) qui permet d'avoir accès aux informations sur les textes de lois français. Plus d'informations sur le site https://dassignies.law/blog/utilisation-de-lapi-legifrance.

Des information supplémentaires sont dasn le README.MD de la galaxy pour l'API rest
