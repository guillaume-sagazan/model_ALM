Modélisation des passifs
========================

Choix de modélisation des différents produits
---------------------------------------------

Epargne individuelle multisupport
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Pour AAVI, l'évolution des différents agrégats suit la logique générale du modèle.

Calculs réalisés à l'initialisation du modèle
---------------------------------------------

Précalcul associés à la diffusion technique des PM
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A l'initialisation du modèle sont calculés :

* Les taux de rachat en fonction de t éventuellement choqués en fonction du choc S2
* Les nombres de contrats en vigueur à chaque t
* Les taux de décès des assurés / bénéficiaires en fonction de t , éventuellement choqués en fonction du choc S2
* Les nombres d'assurés / nombres de bénéficiaires à prendre en compte d'une part dans les calculs de PM unitaires et ceux diffusés compte tenu des taux de décès à appliquer compte tenu du choc S2
* Les nombres d'arrérage, utilisés pour calculer les prestations de rente
* Les montants de PM unitaires utilisés pour le calcul de PM pour FONLIB en fonction de t

L'ensemble de ces éléments dépendent du choc S2 mais pas du scenario économique.

On stocke l'ensemble de ces résultats dans un dataframe nommé :df:`mpPassifEpProjHypsPrst`

Précalcul des taux de frais généraux inflatés et taux d'intérêts crédités
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Certaines données associés à la diffusion des contrats supports dépendent en plus du scenario économique.

C'est le cas par exemple des taux de frais généraux à appliquer qui sont impactés par l'inflation, ou encore des taux d'intérêts crédités qui pour les supports uc dépendent des taux de performance des actifs indiciels.

On stocke l'ensemble de ces données dans un dataframe nommé :df:`mpPassifEpProjHypsIcFgx`

Application des chocs S2 sur les PM UC
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Les chocs S2 ACTION, IMMO sont appliqués sur les PM UC en fonction de la classe d'actif de l'UC en question.

Ainsi, si on est dans le cas chocS2 = "ACTION" ou "BEG_ACTION" et pour un support UC associé CdClasseActif = "ACTION" :

.. math::
    mtPm_{UcChocS2Action} =
    \left\{\begin{array}{l} mtPm_{UcChocS2Action} *
                            \\ ( 1
                            \\ + txActionT1_{UcChocS2Action} * txChocActionT1
                            \\ + txActionT2_{UcChocS2Action} * txChocActionT2
                            \\ + txActionStrat_{UcChocS2Action} * txChocActionStrat
                            \\ )
    \end{array}\right.


Ainsi, si on est dans le cas chocS2 = "IMMO" ou "BEG_IMMO" et pour un support UC associé CdClasseActif = "IMMO" :

.. math::
    mtPm_{UcChocS2Immo} = mtPm_{UcChocS2Immo}  * (1 + txChocImmo)

Performance pour les contrats / supports
----------------------------------------

Inputs
^^^^^^

L'application de la performance sur les contrats supports nécessite de disposer :

* d'un dataframe d'origine au format :df:`mpPassifEpProj`, résultat de l'évènement précédent
* du dataframe :df:`mpPassifEpProjHypsPrstT` issu de l'initialisation du modèle
* du dataframe :df:`mpPassifEpProjHypsIcFgxT`  issu de l'initialisation du modèle

Outputs
^^^^^^^

Sont attendus en output de l'application de la performance :

* la mise à jour du dataframe :df:`mpPassifEpProjPerf`
* un dataframe mpActifCashInputCfPerfPassif au format :df:`mpActifCashInputCfPerfPassif` contenant les cashflows à intégrer au cash des cantons en représentation des passifs
.. * un dataframe au format :df:`StratAlmInputPassif` afin d'alimenter la stratégie ALM et les calculs de PB

Calculs réalisés : Initialisation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Soit une copie du dataframe :df:`mpPassifEpProjPerf` en input dans lequel :

* le pas de temps t et l'évènement ont été mis à jour
* les agrégats avant évènement sont définis à partir des agrégats après évènement

On peut faire la jointure de ce dataframe avec les dataframes :df:`mpPassifEpProjHypsPrstT` et :df:`mpPassifEpProjHypsIcFgxT` de sorte à disposer de l'ensemble des hypothèses à appliquer pour le pas de temps.

Le résultat de cette fusion est stockée temporairement dans le dataframe nommé mpPassifEpProjPerf.

.. **Calculs réalisés : **

Calculs réalisés : Gestion des rachats totaux
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
On va ici réaliser tous les calculs à mi-période (c'est un choix de modélisation)
Ainsi, nous avons du calculer le taux équivalent de demi période associé :
:math:`txIcDemiPeriode = \sqrt{1+txIc} - 1`

On actualise les PM (UC et EU) à mi période : 
:math:`mtPm = mtPmAv * (1+txIcDemiPeriode)`

On calcule le montant de rachats totaux, les chargements associés et on met à jour les PM en milieu de période.

:math:`mtPrstRtBrt = mtPmAv * txPrstRt`

:math:`mtPrstRtChgt = mtPrstRtBrt * txPrstChgt`

:math:`mtPrstRtNet = mtPrstRtBrt - mtPrstRtChgt`

On met à jour le montant de la PM puis on calcule les mêmes indicateurs pour les prestations décès.

:math:`mtPm = mtPm - mtPrstRtBrt`

:math:`mtPrstDcChgt = mtPrstDcBrt * txPrstChgt`

:math:`mtPrstDcNet = mtPrstRtBrt - mtPrstDcChgt`

On met désormais à jour le montant de la PM en retranchant la prestation décès.

:math:`mtPm = mtPm - mtPrstDcBrt`

On actualise les PM jusqu'à fin de période :

:math:`mtPm = mtPm * (1+txIcDemiPeriode)`

.. Pour les contrats FONLIB en phase de restitution, on met à jour le montant d'arrérage de l'éventuel facteur d'arrérage à appliquer et on calcule les prestations de rentes.

..     :math: mtPrstArrBrt_{FonlibRestit} =
..     \left\{\begin{array}{l} nbArr_{FonlibRestit}
..                             \\ * mtArrerage_{FonlibRestit}
..                             \\ * nbContrats_{FonlibRestit}
..     \end{array}\right.

.. :math:`mtPrstArrChgt_{FonlibRestit} = mtPrstArrBrt_{FonlibRestit} * txPrstChgt`

.. :math:`mtPrstArrNet_{FonlibRestit} = mtPrstArrBrt_{FonlibRestit} - mtPrstArrChgt_{FonlibRestit}`

Calculs des totaux
^^^^^^^^^^^^^^^^^^

Une fois ces premiers éléments calculés on peut calculer les totaux :

.. math::

    mtPrstTotBrt =
    \begin{cases} 
        mtPrstRtBrt \\
        + mtPrstDcBrt 
    \end{cases}

.. math::

    mtPrstTotNet =
    \begin{cases} 
        mtPrstRtNet \\
        + mtPrstDcNet 
    \end{cases}

.. math::

    mtPrstTotChgt =
    \begin{cases} 
        mtPrstRtChgt \\
        + mtPrstDcChgt 
    \end{cases}


Calcul des intérêts crédités, PM ap Perf et préparation des inputs de la stratégie ALM
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Les calculs de PB sont réalisés à l'aide d'une assiette de calcul de la PB nommée mtPbAss.
Est à noter que ce montant de PB correspond à un complément de rémunération en plus des intérêts crédités versés.

On définit :

* :math:`mtIcRest` les intérêts crédités versés aux contrats encore en cours en fin d'année
* :math:`mtIcSort` les intérêts crédités versés aux contrats sortis en cours d'année

:math:`mtIcRest = mtPm * txIcDemiPeriode`
:math:`mtIcSort = (mtPmAv * (1 + txIcDemiPeriode) - mtPm)*txIcDemiPeriode`

.. Compte tenu du fait que tous les rachats et décès interviennent dans le modèle en début d'année, :math:`ctarisMp.mtIcSort = 0`

.. Pour les contrats en phase de constitution, l'assiette de PB correspond aux PM après prestations :

.. * :math:`mtPbAss = mtPm`
.. * :math:`mtIcRest = mtPm * txIc`
.. * :math:`mtPm = mtPm + mtIcRest`

.. Dans le cas de de FONLIB, on définit :

.. * :math:`mtPm_{Fonlib} = \left\{\begin{array}{l} nbContrats_{Fonlib} \\ * mtArrerage_{Fonlib} \\ * mtPmUnit_{Fonlib} \end{array}\right.`
.. * :math:`txIc_{Fonlib} = txTech_{Fonlib}`
.. * :math:`mtIcRest_{Fonlib} = mtPm_{Fonlib} * txIc_{Fonlib}`
.. * :math:`mtPbAss_{Fonlib} = mtPm_{Fonlib}`

Calcul des frais généraux
^^^^^^^^^^^^^^^^^^^^^^^^^

Sur la base des éléments calculés jusqu'à présent, est possible de calculer les frais généraux sur PM et sur prestations.

:math:`mtFgxPm = txFgxPm * mtPm`

:math:`mtFgxPrst = txFgxPrst * mtPrstTotBrt`

Calcul des Frais de Gestion Sur Encours 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
On calcule le montant des frais de gestion sur encours des types de contrats.

:math:`mtFgse_{SupportUC} = mtPm_{SupportUC} * tfgse_{SupportUC}`

:math:`mtPm_{SupportUC} = mtPm_{SupportUC} - mtFgse_{SupportUC}`


Calcul des cashflows à intégrer au cash
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

On définit ctarisCashPerfInputCfAsse le dataframe au format :df:`ProjActifCashInputCf` contenant les flux suivants : [mtPrstRtNet, mtPrstDcNet, mtPrstArrNet, mtPrstRtChgt, mtPrstDcChgt, mtPrstArrChgt]

Ces flux sont indiqués comme tombant en début de période.

Construction des outputs attendus
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A ce stade, toutes les données sont présentes dans un unique dataframe ctarisMp.

On peut construire les outputs attendus dans :df:`mpPassifEpProjPerf`

.. Ainsi :

.. * ctarisFluxCnt = colonnes de ctarisMp présentes dans :df:`mpPassifEpProjPerf`
.. * ctarisFgx = colonnes de ctarisMp présentes dans :df:`ProjPassifEpPerfFgx`
.. * almCrInputPassif = colonnes de ctarisMp présentes dans :df:`StratAlmInputPassif` pour les supports euro
.. * ctarisCashPerfInputCfAsse construit tel que présenté ci-dessus
.. * ctarisMp = colonnes de ctarisMp présentes dans :df:`MpPassifEp`

.. Stratégie ALM pour les contrats / supports euro
.. -----------------------------------------------

.. Inputs
.. ^^^^^^

.. Pour rappel, la stratégie ALM a déterminé un taux servi au client et a généré en output de celle ci un dataframe :df:`StratAlmOutputPassif` contenant notamment la PB pour chaque support euro.

.. Ce montant de PB a été calculé comme :math:`mtPb = mtPbAss * TxServi - mtIcRest`

.. On a par ailleurs en input de cet évènement un dataframe :df:`MpPassifEp`

.. Outputs
.. ^^^^^^^

.. On attend en output le dataframe :df:`MpPassifEp` mis à jour

.. Calculs réalisés
.. ^^^^^^^^^^^^^^^^

.. Soit une copie du dataframe :df:`MpPassifEp` en input dans lequel :

.. * le pas de temps t et l'évènement ont été mis à jour
.. * les agrégats avant évènement sont définis à partir des agrégats après évènement

.. On peut faire la jointure de ce dataframe avec le dataframe :df:`StratAlmOutputPassif` précédemment mentionné.

.. Finalement on met à jour le montant de PM comme suit :

.. :math:`mtPm_{SupportEuro} = mtPmAv_{SupportEuro} + mtPb_{SupportEuro}`