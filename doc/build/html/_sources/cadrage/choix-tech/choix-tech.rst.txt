Choix techniques
================

Au vu des besoins exprimés, plusieurs types de réponses peuvent être imaginées :

* la construction d'une solution basée sur une data platform telle que GCP Snowflake ou encore Databricks, avec un front web réutilisant différents composants disponibles sur le marché
* l'utilisation des fonctionnalités offertes par des solutions de type Dataiku, Alteryx

La démarche de déterminisation de la cible consiste donc à formaliser les instructions de choix permettant d'aboutir à une solution du premier type puis de comparer cette solution à une solution du second type.

Les dossiers de choix communs aux deux solutions sont les suivants :

* le prime d'implémentation retenu pour le modèle ALM (commun aux deux types de solutions)
* le framework utilisé dans le cadre des développements (commun aux deux types de solutions)
* les bonnes pratiques d'implémentation des modèles

Les dossiers de choix spécifiques au premier type de solution :

* le framework de gestion des pipelines de données 
* le framework utilisé pour la gestion de la qualité des données
* le choix de la solution utilisée pour la documentation

Finalement, la solution retenue sera comparée à la solution Dataiku / Alteryx.

.. toctree::
   :maxdepth: 6
   :hidden:
   :caption: Dossiers de choix

   framework-df2df
   prisme-modelisation
   gestion-pipelines
   framework-dq
   solution-doc-projet
   