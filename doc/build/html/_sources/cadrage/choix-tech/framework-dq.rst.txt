Gestion de la qualité des données
=================================

Cette instruction de choix a été réalisée en juin 2024.

Solutions envisagées
--------------------

**Great expectations**

Great Expectations est une bibliothèque open source de validation de données en Python qui permet de définir, exécuter et documenter des attentes sur la qualité des données. Elle offre des outils pour créer des tests automatisés et générer des rapports de validation de données.

**Deequ**

Développé par Amazon, Deequ est une bibliothèque Scala pour vérifier la qualité des données. Elle permet de définir des contraintes de qualité des données, de profiler les données, et de produire des métriques de qualité.

**DBT (Data Build Tool)**

DBT est un outil qui permet de transformer des données dans des entrepôts de données en utilisant du SQL. Il permet également de tester la qualité des données avec des tests unitaires.

**Apache Griffin**

Apache Griffin est un framework open source pour mesurer la qualité des données. Il permet la définition de règles de qualité des données et la génération de métriques de qualité des données.

**Pandera**

Pandera est une bibliothèque Python qui utilise les dataframes Pandas pour la validation des données. Elle permet de définir des schémas de validation pour les dataframes et d'automatiser la validation des données.

**Cerberus**

Cerberus est une bibliothèque légère de validation de schémas de données pour Python. Elle est flexible et facile à utiliser pour valider des structures de données JSON et des dictionnaires.

**Tidy Data Validator (TDV)**

TDV est un outil pour la validation des données dans les pipelines de données. Il permet de définir des règles de validation et de produire des rapports de validation.

**Data-QA**

Data-QA est une solution intégrée pour surveiller et gérer la qualité des données. Elle permet de définir des règles de validation et de suivre les métriques de qualité des données.

**Datafold**

Datafold propose des outils pour la gestion de la qualité des données et la détection des anomalies. Il offre des fonctionnalités pour la validation des pipelines de données et le monitoring des modifications de données.

**Cerberus**

    Une bibliothèque légère pour la validation de schémas sur des dictionnaires.
    Flexible avec des règles de validation personnalisées.
    Bien adapté pour des structures de données simples.

**Voluptuous**

Une autre option légère pour la validation de schémas sur des dictionnaires.
Offre une bonne flexibilité avec des validateurs personnalisés.
Idéal pour des besoins de validation simples et rapides.

**Soda**

Conçu pour la surveillance et la gestion de la qualité des données.
Offre des fonctionnalités de profiling de données et de monitoring des pipelines.
Supporte les DataFrames pandas et les bases de données SQL.
Utilise YAML/JSON pour la définition des schémas et des règles de validation.

Critères de choix
-----------------

Les critères de choix suivants sont retenus :

* **Type de données** : Les solutions doivent être capables de valider des données structurées et non structurées.

Comparaison des solutions envisagées
------------------------------------

.. list-table:: Comparaison des solutions de validation des données
   :header-rows: 1
   :widths: 20 15 15 10 10 15 15 15 20

   * - Solution
     - Langage
     - Type de Données
     - Tests Automatisés
     - Rapports de Validation
     - Surveillance en Temps Réel
     - Intégration Pipeline
     - Flexibilité des Règles
     - Licence
   * - Great Expectations
     - Python
     - Structurées/Non-structurées
     - Oui
     - Oui
     - Oui
     - Oui
     - Élevée
     - Open Source (MIT)
   * - Soda
     - Python
     - Structurées/Non-structurées
     - Oui
     - Oui
     - Oui
     - Oui
     - Élevée
     - Open Source (Apache 2.0)
   * - Voluptuous
     - Python
     - Structurées
     - Non
     - Non
     - Non
     - Non
     - Moyenne
     - Open Source (BSD)
   * - Datafold
     - Python
     - Structurées/Non-structurées
     - Oui
     - Oui
     - Oui
     - Oui
     - Élevée
     - Propriétaire
   * - Data-QA
     - N/A
     - Structurées/Non-structurées
     - Oui
     - Oui
     - Oui
     - Oui
     - Élevée
     - Propriétaire
   * - Tidy Data Validator (TDV)
     - N/A
     - Structurées/Non-structurées
     - Oui
     - Oui
     - Oui
     - Oui
     - Élevée
     - Propriétaire
   * - Cerberus
     - Python
     - JSON/Dictionnaires
     - Oui
     - Non
     - Non
     - Non
     - Moyenne
     - Open Source (ISC)
   * - Pandera
     - Python
     - Structurées (Pandas)
     - Oui
     - Oui
     - Non
     - Oui
     - Élevée
     - Open Source (MIT)
   * - Apache Griffin
     - Java/Scala
     - Structurées/Non-structurées
     - Oui
     - Oui
     - Oui
     - Oui
     - Élevée
     - Open Source (Apache 2.0)
   * - DBT (Data Build Tool)
     - SQL
     - Structurées
     - Oui
     - Oui
     - Non
     - Oui
     - Moyenne
     - Open Source (Apache 2.0)
   * - Deequ
     - Scala
     - Structurées
     - Oui
     - Oui
     - Oui
     - Oui
     - Élevée
     - Open Source (Apache 2.0)
