Modèle ALM - Tests de cohérence
===============================

Dans le cadre du modèle ALM, est attendu qu'un certains nombres de tests soient respectés.

Ceux peuvent être structurés par évènement, concerner l'actif ou le passif et être relatifs au choix à l'évolution de la valeur comptable ou à l'évolution de la valeur de marché.

Evènement Performance
---------------------

**Passif - Evolution de la VC**

Pour les contrats d'épargne, est attendu qu'il soit possible d'expliquer la PM après performance à partir de la PM avant performance et des différents élements impactant celle ci.

:math:`MtPm_{ContratSupport}^{Ap Perf}(t) = MtPm_{ContratSupport}^{Av Perf}(t) - MtPrstTotBrt_{ContratSupport}^{Perf}(t) + MtIc_{ContratSupport}^{Perf}(t)`

:math:`MtPm_{ContratSupport}^{Ap Perf}(t) = MtPm_{ContratSupport}^{Av Perf}(t) - MtPrstTotBrt_{ContratSupport}^{Perf}(t) + MtIc_{ContratSupport}^{Perf}(t)`


**Actif - Evolution de la VC**

Pour les actifs unitaires, il doit être possible, actif par actif d'expliquer l'évolution de la VC à partir des cash flows générés et des produits financiers générés.

:math:`MtVc_{ActifUnitaire}^{Ap Perf}(t) = MtVc_{ActifUnitaire}^{Av Perf}(t) + MtPfi_{ActifUnitaire}^{Perf}(t) - MtCf_{ActifUnitaire}^{Perf}(t)`

**Actif - Evolution de la VM**

Pour les actifs unitaires, la valeur de marché évolue en fonction scenarios économiques.

Les calculs de Best Estimate étant réalisés en univers Risque Neutre, il est cependant possible de mesurer un test de fuite économique.

Ce test consiste à vérifier si la performance des actifs est bien cohérente avec la courbe des taux sans risque initiale.

Soit le prix zéro coupon associé à la courbe des taux initiale :  :math:`pzc_{TxSsRisque}(mat)=\frac{1}{(1+TxSsRisque(mat))^{mat}}`

On peut donc définir le taux de performance des actifs attendu comme le taux forward 1 an pour chaque période.

:math:`FactPerfActif_{TxSsRisque}(t)=\frac{Pzc_{TxSsRisque}(t-1)}{Pzc_{TxSsRisque}(t)}`

Est donc attendu qu'en moyenne, la valeur de marché des actifs unitaires augmente de ce facteur.
Dans le cas spécifique d'un traitement déterministe, est attendu que l'augmentation de valeur de marché de l'ensemble des actifs suive exactement ce facteur.

On définit ainsi, pour chaque actif unitaire :

.. math::

    MtFuiteEco_{ActifUnitaire}^{Perf}(t) =
    \left\{\begin{array}{l}
    MtVm_{ActifUnitaire}^{Ap Perf}(t) + MtCf_{ActifUnitaire}^{Perf}(t)
    \\ - MtVm_{ActifUnitaire}^{Ap Perf}(t) * FactPerfActif_{TxSsRisque}(t)
    \end{array}\right.


Evènement Stratégie d'investissement
------------------------------------

**Actif - Evolution de la VC**

La stratégie d'investissement impliquant des achats ventes, la valeur comptable du canton est impactée.

Cette évolution de la valeur comptable doit cependant être expliquée par les produits financiers générés par les ventes d'actifs.

Ainsi, doit donc pouvoir être vérifié que :
:math:`MtVc_{Canton}^{Ap StratInv}(t) = MtVc_{Canton}^{Ap StratInv}(t) + MtPfi_{Canton}^{StratInv}(t)`

**Actif - Evolution de la VM**

Est attendu que la stratégie d'investissement se fasse à valeur de marché constante au niveau de chaque canton.

Doit donc pouvoir être vérifié que :
:math:`MtVm_{Canton}^{Ap Perf}(t) = MtVm_{Canton}^{Av Perf}(t)`

**Actif - Cohérence de la VM avec l'allocation cible**

La stratégie d'investissement vise à équilibrer les différentes classes d'actif les unes par rapport aux autres selon une variable :math:`TxAllocCible_{Canton/CdClasseActif}`

Doit donc pouvoir être vérifié pour chaque canton et chaque classe d'actif que :

:math:`MtVm_{Canton/CdClasseActif}^{Ap StratInv}(t) = MtVm_{Canton}^{Ap StratInv}(t) * TxAllocCible_{Canton/CdClasseActif}`


Evènement Stratégie ALM & Compte de résultat
--------------------------------------------

**Cohérence du compte de résultat**

Les variables suivantes sont attendues en output de la stratégie ALM :

* :math:`MtIc` : Les intérêts crédités de l'année (input de la stratégie ALM)
* :math:`MtPbBrt` : La PB complémentaire versée aux contrats
* :math:`MtPfiAsse` : Les produits financiers de l'année (yc réalisation des PMVL ordonnées dans le cadre de la stratégie ALM)
* :math:`MtFgxPlct` : Frais généraux associés aux placement, à prendre en compte dans le cadre de l'algorithme ALM
* :math:`MtPmvr` : Le complément de produits financiers à réaliser dans le cadre de la stratégie ALM
* :math:`MtPpbReprise` : La reprise de PPE
* :math:`MtPpbDotation` : La reprise de PPE
* :math:`MtResBrtTech` : Le résultat technique
* :math:`MtResBrtFiAssr` : Correspond aux produits financiers issu des capitaux propres (nuls dans le cadre du modèle ALM implémenté)
* :math:`MtResBrtFiAsse` : Le résultat financier, décomposé comme suit :
* :math:`MtResBrtFiAsseTfgse` : La part du résultat financier issu des TFGSE
* :math:`MtResBrtFiAsseVarVcMoy` : La part du résultat financier basée sur la valeur comptable moyenne de l'année
* :math:`MtResBrtFiAsseVarPfi` : La part du résultat financier basée sur les produits financiers de l'année
* :math:`MtResBrtFiAsseBeg` : Le montant de résultat financier complémentaire spécifique dans le cas d'un calcul de BEG
* :math:`MtResBrtFiAsseReliquat` : Le reliquat de marge (Montant négatif ou nul)

En output de la stratégie ALM, les égalités suivantes seront respectées :

.. math::

    MtResBrtFiAsse = \left\{\begin{array}{l}
    MtResBrtFiAsseTfgse
    \\ + MtResBrtFiAsseVarVcMoy
    \\ + MtResBrtFiAsseVarPfi
    \\ + MtResBrtFiAsseBeg
    \\ + MtResBrtFiAsseReliquat
    \end{array}\right.

.. math::

    \left\{\begin{array}{l} MtPfiAsse
                            \\ - MtFgxPlct
                            \\ - MtResReportPertes
                            \\ - MtPpbDotation
                            \\ + MtPpbReprise
    \end{array}\right.
    = \left\{\begin{array}{l} MtIcSort
                            \\ + MtIcRest
                            \\ + MtPbBrt
                            \\ + MtResBrtFiAssr
                            \\ + MtResBrtFiAsse
    \end{array}\right.

**Equilibre Bilan**

L'équilibre bilan doit être respecté post Stratégie ALM & Compte de résultat.

Ainsi, doit pouvoir être vérifié l'égalité suivante :

.. math::

    \left\{\begin{array}{l}
    MtPm
    \\ + MtPpb
    \\ + MtPre
    \\ + MtPdd
    \\ + MtReserveCapi
    \\ + MtCapPropres
    \end{array}\right. = \left\{\begin{array}{l} MtVc_{Actif}
    \\ + MtResReportPertes
    \end{array}\right.



