Stratégie ALM
=============

Objectif de la stratégie ALM
----------------------------

Pour rappel, la stratégie ALM :

* constate les augmentations de valeur comptable au passif et à l'actif avant la stratégie ALM
* agit sur les leviers de pilotage PPE et PMVL pour équilibrer le bilan in fine

Ceci est réalisé en prenant en compte que le résultat financier issu du compte de PB et les frais de placement sont extraits de la valeur comptable à l'actif post stratégie ALM

Inputs de la stratégie ALM
--------------------------

Afin de réaliser les calculs sous-jacents à la stratégie ALM, les inputs suivants sont nécessaires :

* les assiettes nécessaires au calcul de la PB pour les contrats en portefeuille, nommés :math:`MtPbAss`, sachant que :math:`MtPb = max(MtPbAss * TxServiNet - MtIcRest, 0)`
* les taux servis cible à tester (issus de la table HypAlmStrat)
* les différentes générations de PPE
* les produits financiers de l'année à l'actif nettés de la variation de réserve de capitalisation
* les PMVL disponibles (hors PMVL des titres obligataires)

Outputs de la stratégie ALM et du compte de résultat
----------------------------------------------------

La stratégie ALM vise à établir les outputs suivants :

* :math:`MtPfi` : Le montant de produits financiers de l'année. Ce montant est net de l'augmentation de Réserve de Capitalisation en entrée de l'algorithme ALM et contient en sortie les PMVR réalisés par l'ALM.
* :math:`MtPfiAssr = MtPfi * (1 - TxPfiAsseRepartPc)` : La part assureur des produits financiers 
* :math:`MtPfiAsse = MtPfi * TxPfiAsseRepartPc` : La part assuré des produits financiers 
* :math:`MtPfiAssePb = MtPfiAsse - MtFgxPlct - MtFgseEu` : La part assuré des produits financiers alimentant le compte de PB 

* :math:`MtResBrtAsse = MtPfiAssePb - MtPbBrt` : Le solde du compte de PB
* :math:`MtResBrt = MtPfiAssr + MtResBrtAsse` : Le résultat brut de l'année 

* :math:`TxServiBrt` : Le taux servi brut aux clients
* :math:`MtPbBrt` : Le montant de PB brute de CSG, en complément des intérêts crédités déjà versés
* :math:`MtPpeReprise` : La reprise de PPE déterminée par l'algorithme ALM. La dernière génération de PPE est forcément reprise.
* :math:`MtPpeDotation` : La dotation de PPE
* :math:`MtPmvr` : Le montant de plus ou moins values latentes réalisées lors de la stratégie ALM
* :math:`MtResIs` : Le montant d'impôts sur les sociétés
* :math:`MtResNet` : Le montant de résultat après impôts

Cohérence des outputs de la stratégie ALM
-----------------------------------------

Comme évoqué préalablement, l'objectif de l'algorithme ALM est d'aligner les augmentations de valeur comptable à l'actif et au passif en fin d'année.

Ainsi :

.. math::
    MtVc_{Passif}^{Fin} - MtVc_{Passif}^{Debut} = MtVc_{Actif}^{Fin} - MtVc_{Actif}^{Debut}

De cette équation initiale, on peut arriver à (cf détails des calculs plus bas) :

.. math::
    MtResBrtAsse
    =
    \left\{\begin{array}{l}
    MtPfiAssePb - MtIcRest - MtPbBrt 
    \\ - MtPpeDotation + MtPpeReprise
    \end{array}\right.

.. dropdown:: Cohérence des outputs de la stratégie ALM - Détails
    
    On cherche à vérifier

    .. math::
        MtVc_{Passif}^{Fin} - MtVc_{Passif}^{Debut} = MtVc_{Actif}^{Fin} - MtVc_{Actif}^{Debut}

    A l'actif, on peut prendre en compte les éléments suivants :

    :math:`MtVc_{Actif}^{Fin} = MtVc_{Actif}^{Av ResBrt} - MtFgxPlct - MtPfiAssr - MtResBrtAsse` 
    :math:`MtVc_{Actif}^{Av ResBrt} = MtVc_{Actif}^{Debut} + MtPfi - MtPrstTotBrt - MtFgseEu`
    :math:`MtPfi = MtPfiAsse + MtPfiAssr`
    :math:`MtPfiAssePb = MtPfiAsse - MtFgseEu - MtFgxPlct`

    On trouve alors :

    .. math::

        MtVc_{Passif}^{Fin} - MtVc_{Passif}^{Debut}
        =
        \left\{\begin{array}{l}
        MtPfiAssePb 
        \\ - MtPrstTotBrt 
        \\ - MtResBrtAsse 
        \end{array}\right.
    
    Au passif, prenant en compte :

    :math:`MtVc_{Passif}^{Fin} - MtVc_{Passif}^{Debut} = MtPm^{Fin} - MtPm^{Debut} + MtPpe^{Fin} - MtPpe^{Debut}`
    :math:`MtPm^{Fin} = MtPm^{Debut} - MtPrstTotBrt + MtIcRest + MtPbBrt`
    :math:`MtPpe^{Fin} - MtPpe^{Debut} = MtPpeDotation - MtPpeReprise`

    On trouve :

    .. math::
        \left\{\begin{array}{l}
        MtIcRest + MtPbBrt 
        \\ - MtPrstTotBrt 
        \\ + MtPpeDotation - MtPpeReprise
        \end{array}\right.
        =
        \left\{\begin{array}{l}
        MtPfiAssePb 
        \\ - MtPrstTotBrt 
        \\ - MtResBrtAsse 
        \end{array}\right.
 
    Simplifiant l'équation :

    .. math::
        MtResBrtAsse
        =
        \left\{\begin{array}{l}
        MtPfiAssePb - MtIcRest - MtPbBrt 
        \\ - MtPpeDotation + MtPpeReprise
        \end{array}\right.

Préparation des inputs de la stratégie ALM
------------------------------------------

Fonctions utilisées dans le calcul des outputs de la stratégie ALM
------------------------------------------------------------------

Calcul des outputs de la stratégie ALM à partir de taux servis bruts
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Calcul des outputs de la stratégie ALM à partir de taux servis bruts
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^



