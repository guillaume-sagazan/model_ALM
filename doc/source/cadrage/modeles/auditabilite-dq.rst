Auditabilité & Qualité des données
==================================

Auditabilité du modèle et gestion des outputs
---------------------------------------------

Est attendu que l'ensemble des spécifications puissent être recettées au travers de résultats écrits en output du modèle.

Est attendu que puissent être paramétrés en fonction des cas d'usage les outputs écrits.
Il est en effet impossible dans le contexte d'un run stochastique d'écrire en output tous les résultats de tous les calculs (volumétrie trop grande).

Est donc attendu 3 niveaux d'outputs :

* **Indicateurs :** Ecriture en output des BE à la maille nécessaire à l'analyse et à la suite du processus
* **Analyse déterministe :** Ecriture des outputs en base permettant la validation et l'analyse des résultats au niveau canton
* **Outputs de recette :** Pour un scenario donné, écriture d'outputs de recette au niveau le plus fin possible (actif unitaire, MP…)

Gestion de la qualité des données en entrée du modèle
-----------------------------------------------------

A défaut de gérer la qualité des données en amont du lancement des projections, est attendu que les données en entrée du modèle soient validées post chargement de celles ci.

Cela comprend :

* des validations simples telles que la vérification de contraintes sur les champs d'une table
* la validation de la cohérence des données entre elles afin d'éviter des erreurs en cours de projection

