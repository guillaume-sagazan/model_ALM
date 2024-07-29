Versioning des sources
======================

Liste des tâches / issues
-------------------------

La liste des évolutions / anomalies est gérée via Gitlab en mode Kanban.

Sont distinguées dans le tableau de suivi les colonnes suivantes :

* Todo : Tâches à réaliser
* En cours : Tâches en cours de réalisation
* Done : Tâches réalisées

Gestion des branches
--------------------

**Branches principales**

* *main* : Branche principale pour les versions stables et en production.
* *develop* : Branche de développement intégrant les fonctionnalités avant la stabilisation.

**Branches de fonctionnalité**

Utilisez des branches de fonctionnalité (feature branches) pour développer de nouvelles fonctionnalités. Nommez-les *feature/nom-de-la-fonctionnalité*

**Branches bugfix**

Utilisez des branches de correctif (bugfix branches) pour corriger des bugs. Nommez-les *bugfix/nom-du-bug*

**Branches de release**

Utilisez des branches de version (release branches) pour préparer les nouvelles versions. Nommez-les ``release/x.y.z``.

**Branches de hotfix**

Utilisez des branches de hotfix pour corriger des bugs en production. Nommez-les *hotfix/x.y.z*.

Branches protégées
------------------

Au sein de gitlab, sont distingués pour chaque repository les rôles suivants 

* **owner :** Propriétaire du repository
* **maintainer :** Responsable de la maintenance du repository, en charge de la gestion des branches protégées
* **developer :** Développeur du repository, peut créer des branches de fonctionnalité et des MRs

Les branches *develop*, *main* et *release/** sont protégées, seuls les personnes en charge de la maintenance du repo peuvent merger sur ces branches.

Conventional Commits
--------------------

Les conventions de commit sont basées sur les [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/).

Dans le cas où les commits ne respectent pas les conventions, les MRs ne peuvent pas être fusionnées.

Merge requests (MR)
-------------------

**Exigences de révision**

Les MRs ne sont configurées à date pour nécessiter une approbation avant fusion.

**Pipeline CI/CD obligatoire**

Les MRs ne sont pas configurées à date pour exiger la réussite d'un pipelines CI/CD avant la fusion. 

GitLab CI/CD
------------

A faire un jour

*Fichier ``.gitlab-ci.yml``* :
  - Créez et configurez un fichier ``.gitlab-ci.yml`` pour automatiser les tests, les lintings, et les déploiements.
  - Exemples de stages : ``build``, ``test``, ``deploy``.

Etiquettes et milestones
------------------------

**Étiquettes**

Utilisez des étiquettes pour catégoriser les issues et les MRs (par exemple, ``bug``, ``enhancement``, ``documentation``).

**Milestones**

Utilisez des milestones pour planifier et suivre les progrès des versions et des sprints.
