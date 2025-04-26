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
