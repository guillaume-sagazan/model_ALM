Configuration d'un traitement
=============================

Configuration de la projection
------------------------------

La configuration des projections à réaliser inclut les paramètres suivants :

* **chocS2List :** Liste des chocs Solvabilité à lancer dans le cadre du traitement
* **projModeProjection :** Mode de projection. Peut prendre les valeurs ["ALM", "ACTIF_SEUL", "PASSIF_SEUL"]
* **projHorizon :** Horizon de projection en année
* **societe :** Société à prendre en compte dans le cadre de la projection
* **projDateDebut :** Date de début de la projection (format iso : "YY-MM-DD")

* **gseScUnivers ["RN", "RW"] :** Précise l'univers de projection
* **gseScCrnAutoBuild ["True","False"] :** Précise l'univers de projection
* **gseScEcoListStr :** Chaine de caractère précisant les
* **gseObligMaturiteMaxAutoDetect ["True","False"] :** Précise si la maturité maximum des courbes des taux
* **gseObligMaturiteMax :** Si gseObligMaturiteMaxAutoDetect = False, précise la maturité maximum dans le cas des courbes des taux projetées

* **methodeInitEquilibreBilan :** Méthode utilisée pour équilibrer le bilan en t=0. Peut prendre les valeurs ["CASH","FONDS_PROPRES"]
* **methodeProjEquilibreBilan :** Méthode utilisée pour équilibrer le bilan en cours de projection. Peut prendre les valeurs ["CASH","FONDS_PROPRES"]

* **techNbProcesses :** Paramètre indiquant le nombre de processus à lancer en parallèle pour gérer les scenarios économiques

.. note::
    A noter qu'un test de cohérence doit être effectué afin de vérifier que si gseScCrnAutoBuild = True alors gseScUnivers = "RN" et gseScEcoListStr = "1"

A noter que se déduisent de ces paramètres :

* **chocS2GseSet :** Liste des chocs S2 impactant les variables économiques
* **chocS2PassifPmEvolSet :** Liste des chocs S2 impactant l'évolution des PM
* **chocS2PassifIcFgxSet :** Liste des chocs S2 impactant les frais généraux intérêts crédités des UC
* **gseScEcoList :** Liste de scenarios économiques au format liste d'entiers
* **projDateDebutAnnee :** Année de début de projection
* **projDtImage :** Date de début de projection au format string

.. note::
    Dans la suite des spécifications, on pourra faire référence à ces paramètres comme suit : projCfg. "Nom du paramètre"


Configuration des outputs souhaités
-----------------------------------

* **genererOutputDebug :** Booléen d'activation des outputs de Debug
* **genererOutputDebugScListStr :** Liste des scenarios pour lesquels les outputs de debug seront écrits.
* **genererOutputRctLoad :** Booléen d'activation des outputs post chargement des données
* **genererOutputRctInitGse :** Booléen d'activation des outputs de recette relatifs aux variables économiques après initialisation
* **genererOutputRctInitActif :** Booléen d'activation des outputs de recette relatifs aux actifs après initialisation
* **genererOutputRctInitPassif :** Booléen d'activation des outputs de recette relatifs au passif après initialisation
* **genererOutputRctProjActif :** Booléen d'activation des outputs de recette relatifs aux actifs
* **genererOutputRctProjPassif:** Booléen d'activation des outputs de recette relatifs aux passifs
* **genererOutputRctProjStratInv** : Booléen d'activation des outputs de recette relatifs à la stratégie d'investissement
* **genererOutputRctProjProv :** Booléen d'activation des outputs de recette relatifs aux provisions comptables
* **genererOutputRctProjAlmCr :** Booléen d'activation des outputs de recette relatifs à la stratégie ALM
* **genererOutputRctScListStr :** Liste des scenarios pour lesquels les outputs de recette seront écrits.
* **genererOutputPrdAd :** Booléen d'activation des outputs alimentant l'analyse déterministe
* **genererOutputPrdAdScListStr :** Liste des scenarios pour lesquels les outputs alimentant l'analyse déterministe seront écrits.
* **genererOutputPrdQrt :** Booléen d'activation des outputs alimentant l'analyse déterministe

.. note::
    Dans la suite des spécifications, on pourra faire référence à ces paramètres comme suit : outputCfg. "Nom du paramètre"

Configuration de la gestion des erreurs
---------------------------------------

La configuration des erreurs du modèle inclut les paramètres suivants :

* **errorZero :** Définition du zéro absolu. Tout nombre en valeur absolue inférieur à ce montant est considéré comme nul. La valeur par défaut de ce paramètre est 0.000000000001
* **errorZeroRelatif :** Définition du zéro relatif. Deux nombres sont considérés égaux si l'écart absolu entre ces deux nombres est inférieur en valeur absolu à ce montant.  La valeur par défaut de ce paramètre est 0.0000000001
* **initPassifErrorStrategy ["CONTINUER", "LANCER_EXCEPTION"]:** Stratégie adoptée quand une erreur est détectée dans la projection du passif
* **initActifObligTraIterMax :** Nombre d'itération maximum pour l'initialisation du TRA. La valeur par défaut de ce paramètre est de 10000
* **initActifErrorStrategy ["CONTINUER", "LANCER_EXCEPTION"]:** Stratégie adoptée quand une erreur est détectée dans la projection de l'actif
* **equilibreBilanErrorStrategy ["CONTINUER", "LANCER_EXCEPTION"]:** Stratégie adoptée quand une erreur bilan est détectée au cours de la projection. A noter que si "CONTINUER" est choisi,
* **equilibreBilanErrorMax :** Erreur Bilan maximum acceptée. Au dessus de ce montant, une erreur est reportée, selon la stratégie définie. La valeur par défaut de ce paramètre est 20 euros.

.. note::
    Dans la suite des spécifications, on pourra faire référence à ces paramètres comme suit : errCfg. "Nom du paramètre"