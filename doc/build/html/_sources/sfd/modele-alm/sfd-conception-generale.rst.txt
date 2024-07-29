Conception générale
===================

Introduction
------------

Cette partie de la documentation décrit la conception générale du modèle ALM.

L'objectif est de suivre le schéma ci dessous, qui décrit de manière synthétique le fonctionnement du modèle ALM.

.. image:: ../../../rss/img/ModeleAlmSequencementEvenements.png
  :alt: Séquencement des évènements au sein du modèle ALM

Les fonctions décrites ci-dessous sont appelées dans cet ordre par l':ref:`orchestrateur <modules/orchestrateur:orchestrateur>` des calculs

Initialisation du traitement
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

L'initialisation du traitement est effectué en différentes sous étapes.

**Chargement des données** 

Chargement pur et simple des inputs du modèle

**Validation de la qualité des données** 

Les actions suivantes sont réalisées à cette étape :

* Ajout de champs calculés simples 
* Tests de cohérence entre les différentes tables et tests unitaires par table
* Ecriture en sortie de rapports d'erreurs

**Initialisation des chocs Solvabilité 2** 

Les actions suivantes sont réalisées à cette étape :

* Intégration de la notion de choc Solvabilité 2 (axe nommé **cdChocS2**) pour les tables pertinentes.
* Risque neutralisation des actifs obligataires
* Calcul des TRA des actifs obligataires
* Application des chocs S2 s'appliquent en t=0 et sur les différentes tables d'hypothèses

**Initialisation de la projection**

L'objectif de cette étape est de préparer les dataframes relatifs à l'état de la société post initialisation pour réutilisation dans la boucle relative au passage du temps.
Sont donc ajoutés à ce stade les notions de scenario, de période et d'évènement.

Projection
^^^^^^^^^^

S'en suit une unique boucle sur l'horizon de projection défini en paramètre et dans laquelle sont appliqués successivement :

* la performance : passage du temps sans aucune "management action"
* la stratégie d'investissement : modélisation des actions du management en termes de gestion des actifs au sein de chaque canton
* la stratégie ALM et l'établissement du compte de résultat

Fin du traitement
^^^^^^^^^^^^^^^^^

La projection terminée, peuvent être calculés les différents indicateurs S2 Ifrs17.
Les outputs du modèle souhaités sont par ailleurs écrits à cette étape.

Détails des opérations réalisées
--------------------------------

Chargement des données
^^^^^^^^^^^^^^^^^^^^^^

Les tables chargées durant cette étape peuvent être splitées en plusieurs mais aucunes données ne sont ni calculées ni retraitées à ce stade.

.. dropdown:: **loadFsGse :** Fonction permettant de charger la courbe des taux de référence ainsi que les différents outputs du GSE(Générateur de Scénarios Economiques)
   :icon: quote
   :animate: fade-in-slide-down

   Outputs :

   * :ref:`gseCtRefInput <metadata/dataframes:gsectrefinput>`
   * :ref:`gseOutputIndicesInput <metadata/dataframes:gseOutputIndicesInput>`
   * :ref:`gseOutputObligInput <metadata/dataframes:gseoutputobliginput>`
   * :ref:`gseOutputInflationInput <metadata/dataframes:gseoutputinflationinput>`

.. dropdown:: **loadFsActif :** Fonction permettant de charger les inputs associés à l'actif
   :icon: quote
   :animate: fade-in-slide-down

   Outputs : 

   .. * :ref:`mpActifOblig` 

   * :ref:`mpActifIndices <metadata/dataframes:mpactifindices>`
   * :ref:`hypStratInvTxAllocCible <metadata/dataframes:hypstratinvtxalloccible>`
   * :ref:`hypStratInvObligAchat <metadata/dataframes:hypstratinvobligachat>`
   * :ref:`hypStratInvFraisPlct <metadata/dataframes:hypstratinvtxfraisplct>`

.. dropdown:: **loadPassif :** Fonction permettant de charger les inputs associés aux passifs d'assurance 
   :icon: quote
   :animate: fade-in-slide-down

   Outputs : 

   * :ref:`mpPassifEp <metadata/dataframes:mppassifep>`
   * :ref:`hypPassifEpFgx <metadata/dataframes:hyppassifepfgx>`
   * :ref:`hypPassifEpPrstRt <metadata/dataframes:hyppassifepprstrt>`
   * :ref:`hypMortGen <metadata/dataframes:hypmortgen>`
   * :ref:`hypMort <metadata/dataframes:hypmort>`

.. .. dropdown:: **loadAlm :** Fonction permettant de charger les inputs associés à l'ALM
..    :icon: quote
..    :animate: fade-in-slide-down

..    Outputs :

..    * :ref:`mpProvOther`
..    * :ref:`mpProvPpe`
..    * :ref:`HypStratAlmTxServi`
..    * :ref:`HypStratAlmCr`

.. dropdown:: **loadHypS2 :** Fonction permettant de charger les inputs associés à Solvabilité2 
   :icon: quote
   :animate: fade-in-slide-down

   Outputs : 
   
   * :ref:`hypS2Chocs <metadata/dataframes:hyps2chocs>`
   * :ref:`hypS2ChocsSpread <metadata/dataframes:hyps2chocsspread>`

.. .. dropdown:: **loadGseOutputInflation :** Fonction permettant de charger les inputs associés à l'inflation en sortie du GSE
..    :icon: quote
..    :animate: fade-in-slide-down

..    Outputs : 

..    * :ref:`GseOutputInflation`

.. .. dropdown:: **loadGseOutput :** Fonction permettant de charger les courbes des taux et performances des actifs indiciels
..    :icon: quote
..    :animate: fade-in-slide-down

..    Outputs : 

..    * :ref:`GseOutputObligTzc`
..    * :ref:`GseOutputIndicesPerf`

Qualité des données et champs calculés
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Cette étape calculatoire permet de réaliser des vérifications sur les données chargées table par table. Ces tests sont de deux types :

* la vérification de contraintes sur chaque table unitaires
* des tests de cohérence entre les différentes tables

Des champs additionnels inférés des différents inputs sont par ailleurs ajoutés aux différentes tables.

.. dropdown:: **initGblGse :** Fonction en change de calculer l'ensemble des variables économiques pertinentes pour la projection à partir des inputs duisponibles en input du modèle
   :icon: quote
   :animate: fade-in-slide-down

   NB : Cette fonction prend en compte le paramètre gseCrnAutoBuild si activé

   Inputs : 

   * :ref:`dfCdChocS2 <metadata/dataframes:dfcdchocs2>`
   * gseObligMaturiteMax : int
   * gseScEcoList : list[int]
   * gseScUnivers : ScUnivers
   * gseScCrnAutoBuild : bool
   * projHorizon : int
   * :ref:`gseCtRefInput <metadata/dataframes:gsectrefinput>`
   * :ref:`gseOutputIndicesInput <metadata/dataframes:gseoutputindicesinput>`
   * :ref:`gseOutputInflationInput <metadata/dataframes:gseoutputinflationinput>`
   * :ref:`gseOutputObligInput <metadata/dataframes:gseoutputobliginput>` 

   Outputs : 

   * :ref:`gseCtRefObligPzc <metadata/dataframes:gsectrefobligpzc>`
   * :ref:`gseCtRefCashPerf <metadata/dataframes:gsectrefcashperf>`
   * :ref:`gseOutputObligPzc <metadata/dataframes:gseoutputobligpzc>`
   * :ref:`gseOutputIndicesPerf <metadata/dataframes:gseoutputindicesperf>`
   * :ref:`gseOutputCashPerf <metadata/dataframes:gseoutputcashperf>`
   * :ref:`gseOutputDeflateur <metadata/dataframes:gseoutputdeflateur>`

.. dropdown:: **initS2Gse :** Definition de différents input et application des chocs sur l'inflation
   :icon: quote
   :animate: fade-in-slide-down

   Inputs : 

   * :ref:`dfCdChocS2 <metadata/dataframes:dfcdchocs2>`
   * :ref:`hypS2Chocs <metadata/dataframes:hyps2chocs>`
   * :ref:`gseCtRefObligPzc <metadata/dataframes:gsectrefobligpzc>`
   * :ref:`gseOutputInflationInput <metadata/dataframes:gseoutputinflationinput>`

   Outputs : 

   * :ref:`gseCtRefObligPzcCentral <metadata/dataframes:gsectrefobligpzc>`
   * :ref:`gseOutputInflationInitS2 <metadata/dataframes:gseoutputinflationinits2>`

.. dropdown:: **initGblPassif :** Fonction en charge de calculer des champs additionnels pour mpPassifEp de valider la qualité des données pour les données de passif
   :icon: quote
   :animate: fade-in-slide-down

   Inputs : 
   
   * :ref:`mpPassifEp <metadata/dataframes:mppassifep>`
   * projDateDebut : date
  
   Outputs : 
   
   * :ref:`mpPassifEpInitGbl <metadata/dataframes:mppassifepinitgbl>`


.. dropdown:: **initGblActif :** Fonction en charge d'ajouter certains champs calculés pour les actifs unitaires et de valider la qualité des données d'actifs en entrée 
   :icon: quote
   :animate: fade-in-slide-down

   Inputs :

   * :ref:`mpActifIndices <metadata/dataframes:mpactifindices>`
  
   Outputs : 
   
   * :ref:`mpActifIndicesInitGbl <metadata/dataframes:mpactifindicesinitgbl>` 
   * :ref:`mpActifIndicesErreurs <metadata/dataframes:mpactifindicesinitgbl>` 

Application des chocs Solvabilité 2
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Cette étape calculatoire ajoute l'axe analytique cdChocS2 aux inputs chargés pertinents et applique les chocs S2 s'appliquant en t=0

.. dropdown:: **initS2PassifEp :** Ajout de l'axe cdChocS2 + application des chocs S2 en t=0 sur les PM UC
   :icon: quote
   :animate: fade-in-slide-down

   Inputs : 
   
   * :ref:`dfCdChocS2 <metadata/dataframes:dfcdchocs2>`
   * :ref:`mpPassifEpInitGbl <metadata/dataframes:mppassifepinitgbl>`
   * :ref:`hypS2Chocs <metadata/dataframes:hyps2chocs>`

   Outputs : 
   
   * :ref:`mpPassifEpInitS2 <metadata/dataframes:mpPassifEpInitS2>`

.. dropdown:: **initS2Actif :** Ajout de l'axe cdChocS2 + Chroniques de cashflows futurs des obligations + Risque neutralisation + Calcul des TRA + Application des chocs spread  
   :icon: quote
   :animate: fade-in-slide-down

   Inputs : 
   
   * :ref:`hypS2Chocs <metadata/dataframes:hyps2chocs>`
   * :ref:`dfCdChocS2 <metadata/dataframes:dfcdchocs2>`
   * :ref:`mpActifIndicesInitGbl <metadata/dataframes:mpactifindicesinitgbl>`

   Outputs : 

   * :ref:`mpActifIndicesInitS2 <metadata/dataframes:mpActifIndicesInitS2>`

Initialisation Projection
^^^^^^^^^^^^^^^^^^^^^^^^^

.. dropdown:: **initProjActif :** Initialisation de l'état de la société Actif yc axes scenario & period
   :icon: quote
   :animate: fade-in-slide-down

   Inputs : 
   
   * scEcoList : list[int]
   * :ref:`mpActifIndicesInitS2 <metadata/dataframes:mpActifIndicesInitS2>`

   Outputs : 
   
   * :ref:`mpActifIndicesProj <metadata/dataframes:mpActifIndicesProj>`

.. dropdown:: **initProjPassifEp :** Fonction en charge de calculer les taux de mortalité, rachat, IC, Frais Généraux à appliquer pour chaque cdChocS2 paramétré, contrat, period. 
   :icon: quote
   :animate: fade-in-slide-down

   Inputs : 

   * scEcoList : list[int]
   * projHorizonList : list[int]
   * :ref:`mpPassifEpInitS2 <metadata/dataframes:mpPassifEpInitS2>` 
   * :ref:`hypPassifEpFgx <metadata/dataframes:hyppassifepfgx>`
   * :ref:`gseOutputInflationInitS2 <metadata/dataframes:gseoutputinflationinits2>`
   * :ref:`hypPassifEpPrstRt <metadata/dataframes:hyppassifepprstrt>`
   * :ref:`hypMortGen <metadata/dataframes:hypmortgen>`
   * :ref:`hypMort <metadata/dataframes:hypmort>` 
   * :ref:`gseOutputIndicesPerfT <metadata/dataframes:gseoutputindicesperf>`

   Outputs : 
   
   * :ref:`mpPassifEpProj <metadata/dataframes:mpPassifEpProj>`
   * :ref:`mpPassifEpProjHypsPrst <metadata/dataframes:mpPassifEpProjHypsPrst>`
   * :ref:`mpPassifEpProjHypsIcFgx <metadata/dataframes:mpPassifEpProjHypsIcFgx>`

Projection : Performance
^^^^^^^^^^^^^^^^^^^^^^^^

L'évènement performance consiste à simuler le passage du temps sans aucune "management action".

En résulte au passif :

* Le calcul des prestations versées aux assurés
* Le calcul des chargements associés
* Le calcul des frais généraux dépendant d'assiettes de PM et de prestations

Une fois ces éléments calculés, il est possible de calculer le résultat technique.

En résulte à l'actif :

* la mise à jour des valeurs de marché des actifs (sur la base de la nouvelle courbe des taux pour les actifs obligataires ou en prenant en compte les taux de performance pour les actifs indiciels)
* la mise à jour des valeurs comptables des différents actifs
* la mesure de la fuite économique

Plus spécifiquement pour le cash de chaque canton, la mise à jour de la valeur de marché prend en compte :

* le taux de performance du cash
* le fait que des prestations ont été versées au passif, ce qui impacte le cash
* le fait que les actifs unitaires ont eux-mêmes généré des cashflows alimentant le cash

La valeur comptable du cash mise à jour correspond par ailleurs à sa valeur de marché.

Pour tous les actifs, il convient par ailleurs de calculer les produits financiers générés par la performance afin d'alimenter in fine la stratégie ALM avec cet input.

.. dropdown:: **perfPassif :** Fonction en charge d'appliquer la performance sur les MPs
   :icon: quote
   :animate: fade-in-slide-down

   Inputs : 
   
   * period : int
   * :ref:`mpPassifEpProj <metadata/dataframes:mpPassifEpProj>`
   * :ref:`mpPassifEpProjHypsPrstT <metadata/dataframes:mpPassifEpProjHypsPrst>`
   * :ref:`mpPassifEpProjHypsIcFgxT <metadata/dataframes:mpPassifEpProjHypsIcFgx>`

   Outputs : 
   
   * :ref:`mpPassifEpProjPerf <metadata/dataframes:mpPassifEpProjPerf>`
   * :ref:`mpActifCashInputCfPerfPassif <metadata/dataframes:mpactifcashinputcf>`

.. dropdown:: **perfActif :** Fonction en charge d'appliquer la performance sur les actifs unitaires
   :icon: quote
   :animate: fade-in-slide-down

   Inputs : 

   * period : int
   * :ref:`mpActifIndicesProj <metadata/dataframes:mpActifIndicesProj>`
   * :ref:`gseCtRefCashPerfT <metadata/dataframes:gsectrefcashperf>`
   * :ref:`gseOutputIndicesPerfT <metadata/dataframes:gseoutputindicesperf>`

   Outputs : 

   * :ref:`mpActifIndicesProj <metadata/dataframes:mpActifIndicesProj>`

Projection : Stratégie d'investissement
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

La stratégie d'investissement vise à modéliser les actions du management en termes de gestion des actifs au sein de chaque canton.

En résulte que :

* la stratégie d'investissement se fait à valeur de marché constante
* les achats ventes des actifs unitaires impliquent cependant une évolution de la valeur comptable de chaque canton, correspondant à des produits financiers qui ont eux aussi vocation à alimenter la stratégie ALM de fin d'année.

.. dropdown:: **stratInv :** Application de l'algorithme de stratégie d'investissement
   :icon: quote
   :animate: fade-in-slide-down

   Inputs : 

   * period : int
   * :ref:`dfCdChocS2Sc <metadata/dataframes:dfcdchocs2sc>`
   * :ref:`hypStratInvTxAllocCible <metadata/dataframes:hypstratinvtxalloccible>`
   * :ref:`mpActifIndicesProj <metadata/dataframes:mpActifIndicesProj>`

   Outputs : 
   
   * :ref:`stratInvInputOutput <metadata/dataframes:stratinvinputoutput>`
   * :ref:`mpActifIndicesProj <metadata/dataframes:mpActifIndicesProj>`

Projection : Stratégie ALM & Compte de résultat
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

De manière générale, la stratégie ALM constate l'augmentation de valeur comptable à l'actif d'une part et au passif d'autre part, constate les marges de manoeuvre, et permet de rééquilibrer le bilan en déterminant :

* La PB versée aux contrats d'assurances (sachant que des IC ont déjà été versés et sont un input)
* La marge financière associée aux contrats
* La dotation reprise de PPE
* La réalisation de PMVL à l'actif (marge de manoeuvre d'augmentation / réduction de la valeur comptable à l'actif)

Pour ce faire, la stratégie ALM dispose en input :

* Du stock de PPE
* D'un taux cible de participation aux bénéfices (par canton) en input du modèle
* Des éléments nécessaires pour calculer la PB en fonction du taux de PB (assiettes de calcul de la PB notamment)
* Des produits financiers générés à l'actif pendant l'année (issus de la performance et de la stratégie d'investissement)
* Du stock de pmvl disponibles à l'actif (sachant que les pmvl obligataires sont exclues)
* Du résultat technique de l'année

Les outputs de la stratégie ALM sont les suivants :

* Le taux de PB
* Le montant de pmvl à réaliser à l'actif
* La dotation / reprise de PPE
* Les résultats financiers et techniques de l'année

Ces éléments calculés, il est possible de calculer le résultat brut comme la somme du résultat technique et du résultat financier.

Une fois le résultat brut calculé, celui-ci est extrait du cash du canton pour équilibrer le bilan.

Il est éventuellement possible de calculer l'impôt sur les sociétés et le résultat net mais cela n'a pas d'impact sur la projection. Le taux d'IS en entrée du modèle est donc nul.

.. .. dropdown:: **almCrInputsPrep :** Initialisation des inputs de la stratégie ALM
..    :icon: quote
..    :animate: fade-in-slide-down

..    Inputs : 
   
..    * period : int
..    * projActifPerfT : :ref:`ProjActif` 
..    * projActifStratInvT : :ref:`ProjActif`
..    * projProvOther : :ref:`ProjProvOther`
..    * projProvPpe : :ref:`ProjProvPpe`
..    * almCrInputPassif : :ref:`StratAlmInputPassif`
..    * hypStratAlmCr : :ref:`HypStratAlmCr`
..    * hypStratAlmTxServi : :ref:`HypStratAlmTxServi`
..    * hypStratInvTxFraisPlct : :ref:`HypStratInvTxFraisPlct`
..    * prdAdPassifPerf : :ref:`PrdAdPassif`
..    * prdAdActifStratInv : :ref:`PrdAdActif`
..    * gseOutputObligPzcT : :ref:`GseOutputObligPzc`
..    * projResultRctProjAlmCr : ProjResultRctProjAlmCr

..    Outputs : 
   
..    * almCrInputActif : :ref:`StratAlmInputActif` 
..    * almCrInputTxServiCible : :ref:`StratAlmInputTxServiCible`
..    * prdAdCrSoldeTech : :ref:`PrdAdAlmCr`

.. .. dropdown:: **almCrAlmAlgo :** Calcul des outputs de l'algorithme ALM à partir des inputs de celui ci 
..    :icon: quote
..    :animate: fade-in-slide-down

..    Inputs : 
   
..    * almCrInputPassif : :ref:`StratAlmInputPassif`
..    * almCrInputActif : :ref:`StratAlmInputActif`
..    * almCrInputTxServiCible : :ref:`StratAlmInputTxServiCible`
..    * prdAdPassif : :ref:`PrdAdPassif`
..    * prdAdCrMrgTech : :ref:`PrdAdAlmCr`
..    * hypStratAlmCr : :ref:`HypStratAlmCr`
..    * projProvPpe : :ref:`ProjProvPpe`
..    * projProvOther : :ref:`ProjProvOther`
..    * projResultRctProjAlmCr : ProjResultRctProjAlmCr,
..    * projResultPrdAd : ProjResultPrdAd,
..    * projResultPrdQrt : ProjResultPrdQrt,
..    * prdAdCrUc : :ref:`PrdAdAlmCr`

..    Outputs : 
   
..    * almCrAlmOutputAll : :ref:`StratAlmOutput`
..    * almCrAlmOutputPassifAll : :ref:`StratAlmOutputPassif`
..    * prdAdCrTAll : :ref:`PrdAdAlmCr`

.. .. dropdown:: **almCrPassif :** Application des outputs de la stratégie ALM sur les contrats d'assurance
..    :icon: quote
..    :animate: fade-in-slide-down

..    Inputs : 
   
..    * period : int 
..    * projPassifEpMp : :ref:`ProjPassifEpMp`
..    * almCrAlmOutputPassif : :ref:`StratAlmOutputPassif`
..    * projResultRctProjPassif: ProjResultRctProjPassif
..    * projResultPrdAd: ProjResultPrdAd

..    Outputs : 
   
..    * projPassifEpMp : :ref:`ProjPassifEpMp`
..    * projPassifEpAlmCr : :ref:`ProjPassifEpAlmCr` 
..    * prdAdPassifAlmCr : :ref:`PrdAdPassif`

.. .. dropdown:: **almCrActif :** Application des outputs de la stratégie ALM sur les contrats d'assurance
..    :icon: quote
..    :animate: fade-in-slide-down

..    Inputs : 
   
..    * period : int
..    * projActifOblig : :ref:`ProjActif`
..    * projActifIndices : :ref:`ProjActif`
..    * projActifCash : :ref:`ProjActif`
..    * prdAdCrT : :ref:`PrdAdAlmCr`
..    * almCrInputActif : :ref:`StratAlmInputActif`
..    * mpProvOther : :ref:`mpProvOther`
..    * almCrAlmOutput : :ref:`StratAlmOutput`

..    Outputs : 
   
..    * projActifOblig : :ref:`ProjActif`
..    * projActifIndices : :ref:`ProjActif` 
..    * projActifCash : :ref:`ProjActif`

.. .. dropdown:: **almCrProv :** Application des outputs de la stratégie ALM sur les provisions
..    :icon: quote
..    :animate: fade-in-slide-down
   
..    Inputs : 
  
..    * period : int
..    * projProvOther : :ref:`ProjProvOther`
..    * projProvPpe : :ref:`ProjProvPpe`
..    * almCrAlmOutput : :ref:`StratAlmOutput` 
..    * prdAdCrT : :ref:`PrdAdAlmCr`
..    * projResultPrdAd : ProjResultPrdAd,

..    Outputs : 
   
..    * projProvPpe : :ref:`ProjProvPpe`
..    * projProvOther : :ref:`ProjProvOther`

.. .. dropdown:: **almCrFin :** Alimentation des outputs de la projection post stratégie ALM
..    :icon: quote
..    :animate: fade-in-slide-down

..    Inputs : 
   
..    * projActifOblig : :ref:`ProjActif` 
..    * projActifIndices: :ref:`ProjActif`
..    * projActifCash : :ref:`ProjActif`
..    * projPassifEpMp : :ref:`ProjPassifEpMp`
..    * projProvOther : :ref:`ProjProvOther`
..    * projProvPpe : :ref:`ProjProvPpe`
..    * errCfg : ErrConfig
..    * projResultRctProjActif : ProjResultRctProjActif
..    * projResultPrdAd : ProjResultPrdAd

..    Outputs : 
   
..    * projActifAlmCrT : :ref:`ProjActif`
..    * prdAdActifAlmCrT : :ref:`PrdAdActif`
..    * prdAdBilanT : :ref:`PrdAdBilan`
..    * erreursPrdAdBilanT : :ref:`PrdAdBilanErreurs`

Fin de traitement
^^^^^^^^^^^^^^^^^

.. dropdown:: **projFin :** Fonction en charge des traitements de fin de projection + calculs d'indicateurs
   :icon: quote
   :animate: fade-in-slide-down

   Inputs : 
   
   * period : int 
   * projHorizon : int 
   * prdAdPassifEp : :ref:`PrdAdPassifEp <metadata/dataframes:prdadpassifep>` 
   * prdAdBilan : :ref:`PrdAdBilan`
   * projResultPrdQrt : ProjResultPrdQrt

   Outputs : 
   
   None