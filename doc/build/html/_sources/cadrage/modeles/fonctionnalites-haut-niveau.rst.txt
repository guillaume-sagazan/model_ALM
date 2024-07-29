Fonctionnalités de haut niveau
==============================

Flexing vs Full ALM
-------------------

A écrire.

.. important:: 
    Dans le cas du modèle ALM Accenture, le choix retenu est de construire le modèle ALM en Full ALM.

    Faire évoluer le modèle de sorte qu'il gère aussi le flexing sera tout à fait possible 

Gestion des cantons & portefeuilles d'actifs
--------------------------------------------

On distinguera deux niveaux de regroupements d'actifs : les cantons et les portefeuilles d'actifs.

Un portefeuille d'actifs est un regroupement d'actifs unitaires en représentation d'engagements vis à vis des assurés.

Chaque portefeuille d'actif est soumis à une stratégie d'investissement propre, qui sera définie en input du modèle.

Un canton peut regrouper plusieurs portefeuilles d'actifs 

Peuvent être distingués trois types de cantons suivants :

* Les cantons de type "**canton assuré**", pour lesquels les actifs sont uniquement en représentation d'engagements vis à vis des assurés.
* Les cantons de type "**fonds propres**", pour lesquels les actifs sont uniquement en représentation des capitaux propres de la société.
* Les cantons de type "**fonds général**", pour lesquels les actifs sont en représentation d'engagements vis à vis des assurés et des capitaux propres de la société.

Finalement, le modèle pourrait être conçu pour : 

* traiter les cantons de manière totalement silotée 
* projeter l'ensemble des cantons et établir de compte de résultat au niveau de la société en prenant en compte les sources de marges issues de tous les cantons.

.. important:: 
    Dans le cas du modèle ALM Accenture, le choix retenu est de pouvoir modéliser l'établissement du compte de résultat au niveau de la société, prenant en compte les marges générées par l'ensemble des différents types de cantons, qui seront effectivement modélisés. 

Pas de temps du modèle ALM
--------------------------

Le pas de temps du modèle peut au choix être mensuel, trimestriel, annuel, ou peut être défini dans le paramétrage du modèle.

Ci dessous une synthèse des avantages et inconvénients de chaque choix et le choix retenu.

Pas de temps mensuel
^^^^^^^^^^^^^^^^^^^^

.. grid:: 2

    .. grid-item-card::  
        
        **Avantages**

        :octicon:`check;1em;sd-text-success` Permet une bonne finesse dans la projection des cashflows issus des actifs et des passifs
        
        :octicon:`check;1em;sd-text-success` Permet une bonne finesse pour l'intégration des affaires nouvelles
        
        :octicon:`check;1em;sd-text-success` Permet d'intégrer le vieillissement des contrats et des actifs dans le modèle, éventuellement à partir de n'importe quelle extraction de fin de mois
        
        :octicon:`check;1em;sd-text-success` Choix de pas de temps utilisé par au moins deux bancassureurs du marché

    .. grid-item-card::  
        
        **Inconvénients**

        :octicon:`alert;1em;sd-text-danger` Implique une utilisation plus intensive de la mémoire en cours de projection
        
        :octicon:`alert;1em;sd-text-danger` Implique un runtime plus important

        :octicon:`alert;1em;sd-text-danger` Pas de temps non strictement nécessaire du fait que les arrêtés S2 et Ifrs17 sont trimestriels

Pas de temps annuel
^^^^^^^^^^^^^^^^^^^

.. grid:: 2

    .. grid-item-card::  
        
        **Avantages**

        :octicon:`check;1em;sd-text-success` Simplifie le développement du modèle
        
        :octicon:`check;1em;sd-text-success` Améliore notablement le runtime du modèle
        
        :octicon:`check;1em;sd-text-success` Améliore notablement la mémoire nécessaire pour gérer les projections

    .. grid-item-card::  
        
        **Inconvénients**

        :octicon:`alert;1em;sd-text-danger` Modélisation des flux plus grossière
        
        :octicon:`alert;1em;sd-text-danger` Rend impossible l'utilisation du modèle pour les vieillissements 

Pas de temps trimestriel
^^^^^^^^^^^^^^^^^^^^^^^^

Ce choix pourrait être vu comme un compromis entre les deux choix précédents.

Pas de temps variable
^^^^^^^^^^^^^^^^^^^^^

.. grid:: 2

    .. grid-item-card::  
        
        **Avantages**

        :octicon:`check;1em;sd-text-success` Peut permettre de gérer les besoins de vieillissement en mensuel et les calculs de Best Estimate en trimestriel / annuel 

    .. grid-item-card::  
        
        **Inconvénients**

        :octicon:`alert;1em;sd-text-danger` Complexifie grandement les développements et la recette du modèle. Choix non recommandé pour cette raison.
        
Conclusion
^^^^^^^^^^

.. Important::
    
    Dans le cas du modèle ALM développé par Accenture, le choix retenu est un pas de temps paramétrable en entrée du modèle.
    Gérant le cas le plus complexe, il pourra être adapté aux différents clients sans être réécrit en grande partie si le besoin client diffère du choix retenu chez Accenture.
    
    NB : A date le pas de temps du modèle est annuel. Le modèle doit évoluer pour intégrer la fonctionnalité de pas de temps variable à court terme.

Gestion des modes de projection
-------------------------------

Peut être décidé que le modèle devra gérer les modes de projection suivants :

* **ALM :** Dans ce mode de projection, les actifs et les passifs sont lancés simultanément et les interactions actif passif réalisées à chaque période.
* **Actif Seul :** Dans ce mode de projection, seul l’actif est projeté, pourra être inséré une hypothèse de chronique de flux de passif à intégrer.
* **Passif Seul :** Dans ce mode de projection seul le passif est projeté. Sera possible d’alimenter une chronique de taux servi bruts en entrée de ce mode de projection.

.. Important::
    
    Dans le cas du modèle ALM développé par Accenture, est retenu le choix de permettre le fonctionnement du modèle dans ces trois modes de projection.
    
    NB : Non fonctionnel à date

Utilisation des modèles pour les calculs d'indicateurs prospectifs
------------------------------------------------------------------

Le choix de l'utilisation du modèle pour le calcul des indicateurs prospectifs est un choix stucturant.

Cela implique que le modèle soit en capacité :

* de fonctionner en univers Real World
* de prendre en entrée des portefeuilles d'affaires nouvelles en plus des portefeuilles de contrats en stock à date d'arrêté
* de vieillir l'état de la société dans l'objectif que celui ci soit réutilisable dans d'autres projections servant à déterminer les différents indicateurs

Ci dessous les avantages et inconvénients associés :

.. grid:: 2

    .. grid-item-card::  
        
        **Avantages**

        :octicon:`check;1em;sd-text-success` Permet une meilleure compréhension des indicateurs prospectifs du fait que le même modèle et les mêmes mécanismes sont utilisés à date d'arrêté et en prospectif.
        
        :octicon:`check;1em;sd-text-success` Permet une rationalisation des technologies utilisées. En effet, si les indicateurs prospectifs ne sont pas calculés via le modèle, ils devront l'être via un autre software, impliquant des développements complémentaires à backtester par rapport aux résultats du modèle ALM

    .. grid-item-card::  
        
        **Inconvénients**

        :octicon:`alert;1em;sd-text-danger` Complexifie la recette du modèle.
        
        :octicon:`alert;1em;sd-text-danger` Nécessite un paramétrage efficace du modèle pour ne pas rendre ces processus complexes à gérer pour les utilisateurs.

.. Important::
    
    Dans le cas du modèle ALM développé par Accenture, est retenu le choix de permettre le calcul d'indicateurs prospectifs via les modèles.

Gestion des scenarios économiques & univers de projection
---------------------------------------------------------

En fonction des cas d'usage cibles, peut être attendu que le modèle :

* fonctionne en déterministe et en stochastique
* fonctionne en risque neutre et en monde réel
* puisse regénérer autoamtiquement le scenario CRN à partir de la courbe des taux sans risque de référence
* que la risque neutralisation soit traitée par le modèle à l'initialisation de celui ci

.. Important::
    
    Le modèle ALM développé par Accenture gèrera l'ensemble de ces fonctionnalités en cible.
    
    NB : A date, le modèle ne fonctionne pas en Monde Réel

Gestion de l'infra-annuel
-------------------------

Peut être souhaité que le modèle ALM soit en capacité de prendre en input un état de la société extrait en cours d'année.

.. Important::
    
    Le modèle ALM développé par Accenture permettra de gérer les dates de début de projection infra-annuelles.
    
    NB : Non fonctionnel à date

Intégration de calages automatisés
----------------------------------

Les modèles utilisent plutôt des taux pour diffuser les différents agrégats et ces taux doivent parfois être recalculés de sorte que les montants obtenus la première année de projection correspondent à des montants issus du contrôle de gestion.

Cela peut par exemple être le cas pour les primes, les prestations ou encore les frais généraux dont les cibles sont définies dans le cadre du Plan Moyen Terme.

Il est tout à fait possible d'utiliser le modèle pour regénérer l'hypothèse permettant de caler à ces montants.

.. Important::
    
    Le modèle ALM développé par Accenture gèrera ces calages en cible.
    
    NB : Aucun de ces calages n'est à date fonctionnel.
