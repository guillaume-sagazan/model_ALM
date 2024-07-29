Orchestration des calculs & data quality
========================================

Orchestration des calculs
-------------------------

**Orchestration des pipelines :**

La solution permettra de définir et d'orchestrer des pipelines de données complexes, comprenant des dépendances explicites entre les différentes étapes (ou nœuds) du pipeline.

**Conception des pipeline :**

La solution retenue permettra une grande réutilisation des différents pipelines et permettra de définir les assets de données produits et consommés par les pipelines, facilitant la traçabilité et la gestion des dépendances des données.

**Gestion des configurations :**

La solution permettra de gérer les paramètres et les options des pipelines, facilitant ainsi le passage d'un environnement à un autre (développement, test, production).

**Observabilité et monitoring :**

La solution retenue mettra à disposition des outils d'observabilité pour surveiller l'exécution des pipelines, y compris des journaux détaillés, des métriques, et des visualisations des pipelines.

**Intégration avec d'autres outils :**

La solution permettra de s'intègrer avec :

* une variété de langages Pandas, Spark, SQL
* d'autres orchestrateurs comme Apache Airflow
* des systèmes de gestion de qualité de données

**Gestion des erreurs et reprise :**

Les pipelines doivent pouvoir être configurés pour gérer les erreurs de manière granulaire, permettant la reprise partielle des pipelines en cas d'échec.

**Exécution locale et distante :**

La solution retenue permettra l'exécution des pipelines en local pour le développement et les tests, ainsi qu'en environnement distribué pour la production.

**Planification & Gestion des évènements :**

Les pipelines peuvent être planifiés pour s'exécuter à des horaires spécifiques ou déclenchés par des événements, facilitant l'automatisation des workflows de données.

**Composition de pipelines :**

La solution supportera la composition de pipelines, permettant de combiner plusieurs pipelines en workflows plus complexes.

**Backfills :**

La solution permettra de ré-exécuter des portions de données historiques (backfills) facilement, facilitant la correction et la ré-analyse des données passées.

**Types personnalisés et validation des données :**

Vous pouvez définir des types de données personnalisés et des validations pour garantir l'intégrité des données à chaque étape du pipeline.

**Interface utilisateur et tableau de bord :**

La solution offrira une interface utilisateur riche pour la gestion et le monitoring des pipelines, permettant aux utilisateurs de visualiser les exécutions, de planifier les tâches et de consulter les logs.
Celle ci sera personnalisable. 

**Support des ressources externes :**

Les pipelines peuvent être configurés pour utiliser des ressources externes telles que des bases de données, des services web, et des systèmes de fichiers, avec des hooks pour gérer leur cycle de vie.

Gestion de la qualité des données
---------------------------------

**Définition des attentes :**

Vous pouvez définir des attentes spécifiques concernant vos données. Les attentes peuvent être des règles simples, comme "la colonne A ne doit pas avoir de valeurs nulles", ou plus complexes, comme "la somme des valeurs de la colonne B doit être égale à un certain total".

**Validation des données :**

Great Expectations permet de valider les données en fonction des attentes définies. Cela peut se faire sur des données historiques ou en temps réel, intégrées dans vos pipelines de données.

**Documentation automatique des attentes :**

Les attentes définies sont automatiquement documentées sous forme de pages HTML, ce qui facilite la compréhension et la communication des règles de validation des données aux autres membres de l'équipe.

**Intégration avec différents outils et plateformes :**

Great Expectations s'intègre avec de nombreuses sources de données et outils de traitement des données comme Pandas, SQLAlchemy, Spark, etc. Cela permet de valider des données provenant de diverses sources de manière homogène.

**Profilage des données :**

L'outil permet de générer des profils de données, fournissant un aperçu des distributions de colonnes, des types de données et des valeurs inhabituelles, facilitant ainsi la compréhension des caractéristiques de vos données.

**Checkpoints :**

Les checkpoints permettent de regrouper plusieurs validations de données et de les exécuter ensemble. Cela permet de structurer et de planifier les validations de manière cohérente.

**Alertes et notifications :**

En cas d'échec de validation, Great Expectations peut envoyer des alertes et des notifications, permettant de réagir rapidement aux problèmes de qualité des données.

**Flexibilité et extensibilité :**

Vous pouvez personnaliser et étendre les attentes et les validations en fonction de vos besoins spécifiques, grâce à la possibilité d'écrire des attentes personnalisées.

**Intégration CI/CD :**

Great Expectations peut être intégré dans les pipelines de CI/CD, permettant de vérifier la qualité des données à chaque étape de développement et de déploiement.

**Visualisation des résultats de validation :**

Les résultats des validations sont présentés de manière visuelle et détaillée, permettant d’identifier facilement les problèmes et de prendre des mesures correctives.

