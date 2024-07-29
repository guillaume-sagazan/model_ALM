Variables économiques
=====================

Cette partie de la documentation vise à préciser les méthodes de calcul des différentes variables économiques utilisées au cours de la projection, depuis les inputs disponibles en entrée du modèle.

Paramètres dont les variables économiques dépendent
---------------------------------------------------

Les variables économiques sont susceptibles de varier en fonction de

* **chocS2Gse ['CENTRAL','RATES_UP','RATES_DOWN'] :** Le choc S2 susceptible d'impacter les variables économiques associé au choc S2 en cours
* **chocS2PassifHypIcFgx ['CENTRAL','RATES_UP','RATES_DOWN', 'EXPENSE'] :** Le choc S2 susceptible d'impacter l'inflation
* **CdClasseActif ['OBLIGATION', 'ACTION','IMMOBILIER'] :** Le type d'actif indiciel
* **scenario :** l'identifiant du scenario
* **period :** le pas de temps de projection
* **mat :** la maturité (pour les courbes des taux)
* **intraperiod ['Beg','Mid','End'] :** le moment dans la période (début, milieu, fin) où le prix est calculé. Certaines variables économiques sont susceptibles de dépendre du moment dans la période.

Notations relatives aux courbes des taux
----------------------------------------

Courbes des taux, taux zéro coupons, prix zéro coupons
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Soit une courbe des taux CT quelconque définie par une liste de taux zéro coupon ou une liste de prix zéro coupons en fonction des maturités.

On notera :

* :math:`CT = \{pzc(mat)\}` : cette courbe des taux
* :math:`tzc(CT, mat)` : Le taux zéro coupon de la courbe CT à la maturité mat
* :math:`pzc(CT, mat)` : Le prix zéro coupon de la courbe CT à la maturité mat

On a la relation suivante entre tzc et pzc :

:math:`pzc(CT, mat) = \frac{1}{(1+tzc(CT, mat))^{mat}}`

A noter qu'on peut faire dépendre :math:`pzc` du paramètre 'intraperiod' comme suit :

:math:`pzc(CT,mat,'End') = pzc(CT, mat)`

:math:`pzc(CT,mat,'Beg') = pzc(CT, mat-1)`

:math:`pzc(CT,mat,'Mid') = pzc(CT, mat-1) * \sqrt{\frac{pzc(CT, mat)}{pzc(CT, mat-1)}}`

Types de courbes des taux manipulées
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

De manière générale, le modèle fonctionne à partir d'une courbe des taux initiale sans risque et éventuellement d'un jeu de scenarios contenant des courbes des taux par scenario et par pas de temps.

On notera :

* :math:`CT(chocS2Gse, référence, 0)` : la courbe des taux de référence
* :math:`CT(chocS2Gse, scenario, t)` : les courbes des taux utilisées pour la valorisation des obligations

.. note::

    La courbe des taux de référence et les variables directement inférées d'elle sont utilisées pour :

    * la risque neutralisation des obligations
    * la mesure de la fuite économique
    * éventuellement la génération des variables économiques en déterministe risque neutre dans le cas où projCfg.gseCrnAutoBuild = True

Calcul des prix zéro coupons forward
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
On rappelle que  :

* :math:`Offset` : représente le délai avant que le contrat forward ne commence, un Offset = 0 signifie que le contrat commence immédiatement, Offset = 1 signifie que le contrat commence dans un an.
* :math:`Mat` : représente la maturité du contrat forward. Si Mat = 1 et Offset = 0, alors le contrat a une maturité d'un an. Si Mat = 1 et Offset = 1, le contrat commence dans un an et a une maturité d'un an à partir de ce moment là soit deux ans à partir d'aujourd'hui

Finalement, pour les variables Offset >= 0 et Mat >= 0, on définit un prix forward comme :

.. math::
    pzcFwd(CT, Offset, Mat) = \frac{pzc(CT, Offset + Mat)}{pzc(CT, Offset)}

Données en entrée du modèle
---------------------------

Cas où gseScCrnAutoBuild = 'True'
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Dans ce cas, l'objectif est que les variables économiques soient toutes inférées de la courbe des taux initiale (à l'exception de l'inflation)

Les inputs suivants sont donc nécessaires :

* Le fichier :df:`GseCtRef` qui donne la courbe des taux de référence
* Le fichier :df:`GseOutputInflation` qui donne l'inflation

Cas où gseScCrnAutoBuild = "False"
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Dans ce cas, les variables économiques sont fournies en input.

Les inputs suivants sont donc nécessaires :

* Le fichier :df:`GseCtRef` qui donne la courbe des taux de référence
* Le fichier :df:`GseOutputInflation` qui donne l'inflation
* Le fichier :df:`GseOutputIndices` qui donne les taux de performance des actifs indiciels et les courbes des taux par scenario et itération
* Le fichier :df:`GseOutputObligTzc` qui donne les taux de performance des actifs indiciels et les courbes des taux par scenario et itération


Données nécessaires au fonctionnement du modèle
-----------------------------------------------

Que ce soit en déterministe ou en stochastique, est attendu que les données suivantes soient calculées à l'initialisation du modèle.

GseCtRefObligPzc
^^^^^^^^^^^^^^^^

:df:`GseCtRefObligPzc` contient les prix zéro coupons :math:`pzc(CT(chocS2Gse, référence, 0), mat, intraperiod)`

* **chocS2Gse ['CENTRAL','RATES_UP','RATES_DOWN'] :** Le choc S2 susceptible d'impacter les variables économiques associé au choc S2 en cours
* **mat :** la maturité des obligations zéro coupon
* **intraperiod ['Beg','Mid','End'] :** le moment dans la période (début, milieu, fin) où le prix est calculé.

GseCtRefCashPerf
^^^^^^^^^^^^^^^^

:df:`GseCtRefCashPerf` contient le facteur de performance à appliquer au cash sur la base de la courbe des taux de référence.

Cette variable dépend de l'intraperiod car il est anticipé que des cash flows pourraient tomber en début, milieu ou fin de période.

Cette table contient une colonne :math:`facteurPerfTot` nommée dans les spécifications :math:`facteurPerfCashSsRisque(chocS2Gse, t, intraperiod)`, qui se calcule ainsi :


* **pour le début de période :** :math:`facteurPerfCashSsRisque(chocS2Gse,t,'Beg') = \frac{1}{pzcFwd(CT(chocS2Gse, référence, 0),t-1,1))}` 
* **pour le milieu de période :** :math:`facteurPerfCashSsRisque(chocS2Gse,t,'Mid') = \sqrt{facteurPerfCashSsRisque(chocS2Gse,t,'Beg')}`
* **pour la fin de période :**  :math:`facteurPerfCashSsRisque(chocS2Gse,t,'End') = 1` 

GseOutputObligPzc
^^^^^^^^^^^^^^^^^

:df:`GseOutputObligPzc` contient les prix zéro coupons :math:`pzc(CT(chocS2Gse, scenario, t), mat, intraperiod)`

Dans le cas où Cas gseScCrnAutoBuild = 'False', les prix sont construits à partir des **taux zéro coupons** présents dans le fichier :df:`GseOutputObligTzc`

Dans le cas où Cas gseScCrnAutoBuild = 'True', les prix sont construits à partir des **prix forward** issus de la courbe des taux de référence.

GseOutputDeflateur
^^^^^^^^^^^^^^^^^^

:df:`GseOutputDeflateur` contient les déflateurs utilisés pour l'actualisation des flux.

:math:`deflateur(chocS2Gse, scenario, t, intraperiod) = pzc(CT(chocS2Gse, scenario, t), 1, intraperiod)`

* **chocS2Gse ['CENTRAL','RATES_UP','RATES_DOWN'] :** Le choc S2 susceptible d'impacter les variables économiques associé au choc S2 en cours
* **scenario :** l'identifiant du scenario
* **t :** le temps ou la période où le déflateur est calculé 
* **intraperiod ['Beg','Mid','End'] :** le moment dans la période (début, milieu, fin) où le prix est calculé.
  
GseOutputCashPerf
^^^^^^^^^^^^^^^^^

:df:`GseOutputCashPerf` contient :math:`facteurPerfCash(chocS2Gse, scenario, t, intraperiod)` : Le facteur de performance à appliquer au cash.

De même que pour facteurPerfCashSsRisque :

* **pour le début de période :** :math:`facteurPerfCash(chocS2Gse, scenario, t, Beg) = \frac{1}{pzcFwd(CT(chocS2Gse, scenario, t-1), 0, 1))}`
* **pour le milieu de période :**:math:`facteurPerfCash(chocS2Gse, scenario, t, Mid) = \sqrt{facteurPerfCashSsRisque(chocS2Gse, scenario, t, Beg)}`
* **pour la fin de période :** :math:`facteurPerfCash(chocS2Gse, scenario, t, End) = 1` 

GseOutputIndicesPerf
^^^^^^^^^^^^^^^^^^^^

:df:`GseOutputIndicesPerf` contient :math:`facteurPerfTot`, le facteur à appliquer aux valeurs de marché des actifs indiciels, nommé dans la suite des spécifications :math:`facteurPerfTotIndice(typeIndice, chocS2Gse, t)`

Dans le cas où Cas gseScCrnAutoBuild = 'False', ces facteurs sont repris du fichier :df:`GseOutputIndicesPerf`

:math:`facteurPerfTotIndice(typeIndice, chocS2Gse, scenario, t) = 1 + TxPerfTotIndice(typeIndice, ChocS2Gse, scenario, t)`

Dans le cas où Cas gseScCrnAutoBuild = 'True', les prix sont construits à partir des prix forward issus de la courbe des taux de référence.

GseOutputInflation
^^^^^^^^^^^^^^^^^^

:df:`GseOutputInflation` contenant :math:`facteurInflationCum(chocS2PassifHypsIcFgx, scenario, t)` le facteur d'inflation cumulé

.. math::
    facteurInflationCum(chocS2PassifHypsIcFgx, scenario, t)
    \\ =
    \left\{\begin{array}{l}
    facteurInflationCum(chocS2PassifHypsIcFgx, scenario, t-1)
    \\ * ( 1. + txInflation(chocS2PassifHypsIcFgx, scenario, t) )
    \end{array}\right.

Où txInflation peut être trouvé dans :df:`GseOutputInflation`

On considère les variables suivantes : 

* :math:`tzc(CT(chocS2Gse, référence, 0), mat)` : Le taux zéro coupon issu de la courbe des taux de référence
* :math:`pzc(CT(chocS2Gse, référence, 0), mat)` : Le prix zéro coupon associé au taux issu de la courbe des taux de référence
* :math:`facteurPerfCashSsRisque(chocS2Gse, t, intraperiod)` : Le facteur de performance à appliquer au cash. Prenant en compte que certains cashflows pourraient tomber en début milieu ou fin de période, est nécessaire que ce facteur soit défini en fonction du paramètre intraperiod.

:math:`facteurPerfCashSsRisque(chocS2Gse, t, intraperiod)` se calcule ainsi :

* :math:`facteurPerfCashSsRisque(chocS2Gse, t, 'End') = 1`
* :math:`facteurPerfCashSsRisque(chocS2Gse, t, 'Beg') = \frac{1}{pzcFwd(CT(chocS2Gse, référence, 0), t-1, 1))}`
* :math:`facteurPerfCashSsRisque(chocS2Gse, t, 'Mid') = \sqrt{facteurPerfCashSsRisque(chocS2Gse, t, "Beg")}`

**Variables associées aux actifs indiciels**

L'évolution des valeurs de marché des actifs indiciels et la détermination éventuelle

* :math:`txPerfTotIndice(typeIndice, chocS2Gse, t)` : Le taux de performance pour l'indice "typeIndice", le choc S2 "chocS2Gse" et l'itération "t"
* :math:`facteurPerfTotIndice(typeIndice, chocS2Gse, t) = 1 + TxPerfTotIndice(typeIndice, ChocS2Gse, t)`
* :math:`txDividendeIndice(typeIndice, chocS2Gse, t)` : Le taux de dividende pour l'indice considéré
* :math:`txPerfNetIndice(typeIndice, chocS2Gse, t)` : Le taux de performance pour l'indice considéré, net de dividendes
* :math:`facteurPerfNetIndice(typeIndice, chocS2Gse, t) = 1 + TxPerfNetIndice(typeIndice, chocS2Gse, t)` : Le facteur de performance net de dividendes

**Variables associées au cash**

:math:`facteurPerfCash(chocS2Gse, t, intraperiod)` : Le facteur de performance à appliquer au cash.

De même que pour facteurPerfCashSsRisque :

* :math:`facteurPerfCash(chocS2Gse, t, 'End') = 1`
* :math:`facteurPerfCash(chocS2Gse, t, 'Beg') = \frac{1}{pzcFwd(CT_{Valorisation}^{chocS2Gse, t-1}, 0, 1))}`
* :math:`facteurPerfCash(chocS2Gse, t, 'Mid') = \sqrt{facteurPerfCashSsRisque(chocS2Gse, t, 'Beg')}`


Cas gseScCrnAutoBuild = "True"


Dans ce cas, l'objectif est de créer les




