Base de connaissances
=====================

Périmètre de la base de connaissances
-------------------------------------

La base de connaissance comprendra tous les éléments suivants. 

Cadrage du projet
^^^^^^^^^^^^^^^^^

La documentation associée au cadrage du projet inclut : 

* la formalisation des besoins des différentes parties prenantes
* les instructions de choix réalisées dans le cadre de la mise en place de la solution.

Gouvernance projet 
^^^^^^^^^^^^^^^^^^

Cette partie de la documentation comprend :

* Un référentiel des acteurs impliqués
* La comitologie associée au projet ou connexe à celui-ci
* L'organisation interne du projet
* Les supports & CR des comités afférents au SI Risques et Inventaire

Textes règlementaires et normes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Cette partie de la documentation comprend les textes règlementaires en vigeur ainsi que les normes calculatoires spécifiques à au groupe d'assurances.

Spécifications fonctionnelles
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Cette partie de la documentation comprend les spécifications fonctionnelles des différents modules calculatoires.

Description des données
^^^^^^^^^^^^^^^^^^^^^^^

Cette partie de la documentation comprend :

* la documentation du dictionnaire de données utilisé pour chaque version
* la documentation des formats des différents dataframes utilsés du bout en bout
* la documentation de la structure des différents éléments de configuration

Utilisation de la solution
^^^^^^^^^^^^^^^^^^^^^^^^^^

Cette partie de la documentation est destinée à expliquer aux utilisateurs comment utiliser la solution.

Documentation du code
^^^^^^^^^^^^^^^^^^^^^

Cette partie de la documentation vise à permettre un accès au code aux différents utilisateurs afin de faciliter la compréhension des calculs réalisés par les utilisateurs finaux.

Liens externes
^^^^^^^^^^^^^^

Cette partie est une simple liste de liens externes jugés intéressants par la communauté.

Exigences règlementaires associées à la gestion de la documentation
-------------------------------------------------------------------

Liens vers les exigences Solvabilté 2

Desciption des exigences S2 / standards DSI...

Exigences techniques
--------------------

Ci dessous la liste des exigences technico-fonctionnelles attendues vis à vis de la base documentaire.

Versioning de la base documentaire
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

De part la nature des indicateurs calculés par le SI Risques et Inventaire, celui-ci sera régulièrement audité par des entités internes ou externes.

Ces audits pourront ne pas concerner la toute dernière version de la chaîne de production et il convient donc de disposer de versions de la base documentaire pour chaque version de la chaîne de production utilisée à des fins de calculs règlementaires.

Il est aussi possible de vouloir décliner cette exigence aux calculs non réalisés dans le cadre de calculs règlementaires uniquement.

Point d'entrée unique
^^^^^^^^^^^^^^^^^^^^^

Le spectre de la documentation associée au SI Risques et Inventaire peut être assez large en fonction des choix réalisés quant à son périmètre.

Afin de faciliter l'accès de la documentation à l'ensemble des parties, un point d'accès unique est attendu.

Cela comprend la nécessité d'accéder aux différentes versions de la base documentaire comme vu plus haut.

Suivi des deltas
^^^^^^^^^^^^^^^^

Devra être possible de suivre qui a fait quels deltas dans la documentation.

Gestion de la documentation via branches
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Les développements étant réalisés via l'utilisation de branches, peut être considéré nécessaire que la documentation suive cette même logique.

Cette fonctionnalité est plus particulièrement prégnante pour la documentation des applicatifs de la chaîne de production. 

Formats attendus 
^^^^^^^^^^^^^^^^

Autant que faire se peut, est attendu que la documentation soit d'abord disponible / accessible en format web de sorte à faciliter le parcours de celle-ci.

Outre ce premier format, il devra être possible de disposer de sous parties de la documentation au format pdf et au format word, à destination d'acteurs internes ou externes.

Gestion de versions internes / externes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Autant que faire se peut, le système de gestion de la base documentaire permettra de disposer de versions à destination d'acteurs internes et de versions à destination d'acteurs externes (auditeurs par exemple)

Release notes
^^^^^^^^^^^^^

Le spectre de la documentation associée au SI Risques et Inventaire peut être assez large en fonction des choix réalisés quant à son périmètre.

Est donc attendu que des synthèses des deltas apportées entre deux versions de la base de connaissance soit mis à disposition, de manière automatique si cela est possible

Capacité de gérer de multiples contributeurs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Est attendu que les contributeurs à la base de connaissance soient multiples, avec des appétences diverses quant aux outils informatiques.

Accès aux référentiels
^^^^^^^^^^^^^^^^^^^^^^

Les processus calculatoires associés au SI Risques et Inventaire sont complexes et assis sur différents référentiels d'entreprise.

Autant que faire se peut, est attendu que les utilisateurs puissent parcourir ces référentiels.

A noter qu'au même titre que la base documentaire est versionnée, il doit être possible aux utilisateurs de visualiser 

Accès aux metadata
^^^^^^^^^^^^^^^^^^

La chaîne de production des indicateurs comprend un certain nombre d'applicatifs nécessitant divers inputs et générant divers outputs.

Pour une version donnée de la base de connaissance et de la chaîne de production associée, les utilisateurs ont besoin d'accéder :

* Aux différents dictionnaires de données utiliséS
* Aux formats des données en input et en outputs
* Eventuellement aux formats de certains intermédiaires de calculs


Intégration de formules mathématiques
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

De part les thématiques traitées au sein du SI Risques et Inventaire, le système de gestion de la base documentaire devra permettre d'intégrer 

Accès au code
^^^^^^^^^^^^^

Pour certains applicatifs de la chaîne de production (par exemple les modèles actuariels), peut être souhaité par les utilisateurs un accès en lecture seule au code en plus de l'accès aux spécifications. 

Gestion des identités et accès
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

L'ensemble de la base de connaissance n'a pas vocation à être accessible à l'ensemble des utilisateurs.

Est donc nécessaire de pouvoir gérer les accès des utlisateurs aux différents contenus de la base de connaissance.

