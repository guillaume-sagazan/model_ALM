Modélisation des actifs
=======================

Initialisation
--------------

L'évolution des valeurs de marché des actifs indiciels prendra en input un taux de performance brut issu des jeux de scenarios économiques.

Un taux de dividendes, permettant potentiellement de simuler des cashflows et produits financiers pour les actifs indiciels, existe dans le modèle mais est défini à zéro à date.

Titres Obligataires - Risque Neutralisation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Les titres obligataires sont risque neutralisés à l'initialisation du modèle sur la base de la courbe des taux de référence de l'arrêté.

Cette risque neutralisation est réalisée en ajustant le nominal des obligations et donc les cashflows futurs des obligations.

Titres Obligataires - Initialisation du TRA
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A l'initialisation du modèle, le taux de rendement actuariel des obligations est recalculé de sorte que :

.. math::
    MtVc(t=0) =
    \sum_{t=1}^{maturiteOblig}{\frac{MtNominal*TxCoupon}{(1+TRA)^{t}}}
    + \frac{MtNominal * TxRemboursement}{(1+TRA)^{maturiteOblig}}

Ce recalcul du TRA permet de lisser les produits financiers sur la durée de vie de l'obligation.

Les produits financiers générés par les obligations sont dès lors calculés comme :

.. math::
    MtPfi(t) = TRA * MtVc(t-1)

Performance
-----------

Actifs Indiciels
^^^^^^^^^^^^^^^^

Pour les actifs indiciels, les formules suivantes s'appliquent.

**Calcul de la valeur de marché**

.. math::
    MtVm^{ApPerf}(t) = MtVm^{AvPerf}(t) * facteurPerfTotIndice(typeIndice, chocS2Gse, scenario, t)

**Calcul de la valeur comptable**

.. math::
    MtVc^{ApPerf}(t) = MtVc^{AvPerf}(t)

**Calcul des produits financiers**

.. math::
    MtPfi^{Perf}(t) = 0.0

**Calcul des cashflows**

.. math::
    MtCf^{Perf}(t) = 0.0

Titres obligataires
^^^^^^^^^^^^^^^^^^^

**Calcul de la valeur de marché**

.. math::
    MtVm^{ApPerf}(t) =
    \left\{\begin{array}{l}
    \sum_{mat=1}^{maturiteOblig}{MtNominal * TxCoupon * pzc(CT(chocS2Gse, scenario, t), mat)}
    \\ + MtNominal * TxRemboursement * pzc(CT(chocS2Gse, scenario, t), maturiteOblig)
    \end{array}\right.

**Calcul des produits financiers**

.. math::
    MtPfi^{Perf}(t) = MtVc^{AvPerf}(t) * TRA

**Calcul du cashflow**

Si t < date de maturité de l'obligation :

.. math::
    MtCf^{Perf}(t) = MtNominal * TxCoupon

Si t = date de maturité de l'obligation :

.. math::
    MtCf^{Perf}(t) = MtCf^{Perf}(t) + MtNominal * TxRemboursement

**Calcul de la valeur comptable**

.. math::
    MtVc^{ApPerf}(t) = MtVc^{AvPerf}(t) + MtPfi^{Perf}(t) - MtCf^{Perf}(t)

Cash
^^^^

Le cash est le réceptacle des cash flows issus des contrats supports euro d'une part et des cashflows issus des actifs sous gestion d'autre part.

L'ensemble des cashflows sont préparés en amont dans un dataframe :math:`pfarisCashPerfInputCf` (au format :df:`ProjActifCashInputCf`)

A noter que le cash est revalorisé sur la base de :math:`facteurPerfCash(chocS2Gse, scenario, t, intraperiod)` explicité précédemment.

**Calcul des produits financiers**

Soit la jointure entre pfarisCashPerfInputCf et igseCashPerf.

Cette jointure permet de calculer les produits financiers issus des différents cashflows ainsi :

.. math::
    MtPfi^{Perf}(t) = pfarisCashPerfInputCf.MtCf * facteurPerfCash

A ceci s'ajoute les produits financiers issus du stock de cash présent au début de la période.

.. math::
    MtPfi^{Perf}(t) = MtPfi^{Perf}(t) + MtVm^{AvPerf}(t) * facteurPerfCash(chocS2Gse, scenario, t, BEG)

**Calcul des cashflows intégrés au cash**

Le montant de cashflow intégré au cash correspond à la somme des cashflows présents dans :math:`pfarisCashPerfInputCf`

Ainsi :

.. math::
    MtCf^{Perf}(t) = \sum{pfarisCashPerfInputCf.MtCf}

**Calcul de la valeur de marché et de la valeur comptable**

Ayant calculé :math:`MtCf` et :math:`MtPfi`, on peut calculer la valeur de marché après performance comme :

.. math::
    MtVm^{ApPerf}(t) = MtVm^{AvPerf}(t) + MtPfi^{Perf}(t) + MtCf^{Perf}(t)

.. math::
    MtVc^{ApPerf}(t) = MtVm^{ApPerf}(t)

Stratégie d'investissement
--------------------------

Préparation des données
^^^^^^^^^^^^^^^^^^^^^^^

Dans l'objectif d'appliquer la stratégie d'investissement, est nécessaire de calculer :

* les valeurs de marché par canton
* les valeurs de marché par classe d'actif
* les assiettes de calcul utilisées pour le calcul des achats ventes à réaliser

.. math::
    MtVmAvCanton_{Canton}(t) = \sum_{Canton}{MtVm^{AvPerf}_{ActifsUnitaires}(t)}

.. math::
    MtVmAvCdClasseActif_{CdClasseActif}(t) = \sum_{CdClasseActif}{MtVm^{AvPerf}_{ActifsUnitaires}(t)}

.. math::
    MtVmAvAssAchatVente_{CdClasseActif IndGestion}(t) = \sum_{CdClasseActif IndGestion}{MtVm^{AvPerf}_{ActifsUnitaires IndGestion}(t)}

Ce dernier montant doit être corrigé de sorte que les actifs indiciels pour lesquels IndGestion = 0 ne soient pas intégrés dans les assiettes de calculs.

.. math::
    MtVmAvAssAchatVente_{CdClasseActif, IndGestion=0}(t) = 0.0

Est finalement nécessaire de calculer les montants de valeur de marché cible à atteindre.

.. math::
    MtVmCibleCdClasseActif_{CdClasseActif}(t) = MtVmAvCanton_{Canton}(t) * HypTxAllocCible_{CdClasseActif}

Algorithme
^^^^^^^^^^

L'objectif est in fine de calculer, pour chaque CdClasseActif et chaque IndGestion les montant suivants :

* :math:`MtVmCible` : Le montant de valeur de marché cible à la maille CdClasseActif IndGestion, initialisé à 0. A noter que ce montant diffère de MtVmCibleCdClasseActif qui est par classe d'actif !
* :math:`MtAchatOblig` : le montant d'achat d'obligations à réaliser (ne concerne que les classes d'actifs relatives aux titre obligataires), initialisé à 0.0
* :math:`FacteurAchatVente` : le facteur d'achat vente, initialisé à 1.0

Est à noter qu'il convient de distinguer les cas suivants :

* La valeur de marché du canton est supérieure à zéro. Dans ce cas, on applique un algorithme assez classique.
* La valeur de marché du canton est inférieure à zéro. Dans ce cas, tous les actifs sont vendus et la projection est finalisée avec uniquement du cash.

**Cas où la valeur de marché du canton est négative**

Dans ce cas :

* :math:`MtAchatOblig` est conservé à 0 pour ne pas acheter d'obligations
* :math:`MtVmCible` est conservé à 0
* :math:`FacteurAchatVente` est défini à 0 dans tous les cas, sauf pour le cash.

Ceci permet de vendre tous les actifs unitaires et de continuer avec uniquement du cash.

**Cas où la valeur de marché du canton est positive**

Dans ce cas, on va traiter les couples CdClasseActif IndGestion de ma manière suivante.

.. math::
    FacteurAchatVente_{CdClasseActif \neq OBLIGATION} = \frac{MtVmCibleCdClasseActif_{CdClasseActif}}{mtVmAvCdClasseActif_{CdClasseActif}}


**Output de la stratégie d'investissement**

On dispose en output de l'algorithme d'une table :df:`StratInvInputOutput` contenant :math:`FacteurAchatVente` et :math:`MtAchatOblig` par classe d'actif / indice de gestion.

Impacts sur les portefeuilles d'actifs unitaires
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Impacts de FacteurAchatVente sur les actifs unitaires**

Les formules suivantes sont appliquées si :math:`FacteurAchatVente_{CdClasseActif} \leq 1`

.. math::
    MtVm_{ActifUnitaire}^{ApStratInv}(t) = MtVm_{ActifUnitaire}^{AvStratInv}(t) * FacteurAchatVente_{CdClasseActif}

.. math::
    MtVc_{ActifUnitaire}^{ApStratInv}(t) = MtVc_{ActifUnitaire}^{AvStratInv}(t) * FacteurAchatVente_{CdClasseActif}

.. math::
    MtPfi_{ActifUnitaire}^{StratInv}(t) = (MtVm_{ActifUnitaire}^{AvStratInv}(t) - MtVc_{ActifUnitaire}^{AvStratInv}(t)) * (1.0 - FacteurAchatVente_{CdClasseActif})

.. math::
    MtCf_{ActifUnitaire}^{StratInv}(t) = MtVm_{ActifUnitaire}^{AvStratInv}(t) - MtVm_{ActifUnitaire}^{ApStratInv}(t)


Les formules suivantes sont appliquées si :math:`FacteurAchatVente_{CdClasseActif} > 1`


.. math::
    MtVm_{ActifUnitaire}^{ApStratInv}(t) = MtVm_{ActifUnitaire}^{AvStratInv}(t) * FacteurAchatVente_{CdClasseActif}

.. math::
    MtVc_{ActifUnitaire}^{ApStratInv}(t) = MtVc_{ActifUnitaire}^{AvStratInv}(t) + MtVm_{ActifUnitaire}^{ApStratInv}(t) - MtVm_{ActifUnitaire}^{AvStratInv}(t)

.. math::
    MtPfi_{ActifUnitaire}^{StratInv}(t) = 0.0

.. math::
    MtCf_{ActifUnitaire}^{StratInv}(t) = MtVm_{ActifUnitaire}^{AvStratInv}(t) - MtVm_{ActifUnitaire}^{ApStratInv}(t)


**Achats de titres obligataires**

L'achat d'obligations se fait conformément aux caractéristiques présente dans la table :df:`HypStratInvInput`

A noter qu'à l'achat :
* la valeur de marché et la valeur comptable sont initialisées à :math:`MtAchatOblig`
* le nominal est d'abord initialisé à 1 euro avant de la risque neutraliser afin de recalculer le nominal idoine

Impacts sur la réserve de capitalisation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

La réalisation de PMVL sur les titres obligataires impacte un delta de réserve de capitalisation.

Ainsi :

.. math::
    MtReserveCapi_{Canton}^{ApStratInv}(t) = MtReserveCapi_{Canton}^{AvStratInv}(t) + \sum_{Canton}{MtPfi^{StratInv}_{Obligations}(t)}

Stratégie ALM
-------------

On dispose en output de la stratégie ALM de la table de données :df:`StratAlmOutput`, contenant notamment MtPmvr, le montant de plus ou moins values à réaliser.

Impacts sur les actifs unitaires
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Seules les PMVL des actifs indiciels sont utilisées dans le cadre de la stratégie ALM.

Pour ces actifs :

.. math::
    MtVm^{ApAlm}(t) = MtVm^{AvAlm}(t)

.. math::
    MtCf^{Alm}(t) = 0.0

.. math::
    MtVc^{ApAlm}(t) = MtVc^{AvAlm}(t) + \frac{MtPmvr_{ActifsIndiciels}}{MtPmvl_{ActifsIndiciels}} * (MtVm^{AvAlm} - MtVc^{AvAlm})

.. math::
    MtPfi^{Alm}(t) = MtVc^{ApAlm}(t) - MtVc^{AvAlm}(t)




Les cibles à atteindre par classe d'actif sont définies dans une table d'hypothèses nommée ACAP.
