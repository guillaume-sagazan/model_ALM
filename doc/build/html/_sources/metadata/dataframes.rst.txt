Format des dataframes
=====================

Variables économiques (GSE)
---------------------------

.. raw:: html

   <a id="GseCtRefInput"></a>

GseCtRefInput
^^^^^^^^^^^^^

.. list-table::
   :widths: 3 25 10 40
   :header-rows: 1
   :class: table-custom

   * - Pk
     - Variable
     - Type
     - Description
   * - :octicon:`key`
     - cd_trajectoire
     - String
     - Trajectoire
   * - :octicon:`key`
     - dt_trajectoire
     - Date
     - Trajectoire
   * - :octicon:`key`
     - cd_ct_ref
     - String
     - Facteur de performance total
   * - :octicon:`key`
     - maturite
     - Int32
     - Maturité en années d'un cashflow futur
   * - :octicon:`key`
     - cd_choc_s2_gse
     - Categorical
     - Choc Solvabilité 2 applicable aux variables économiques
   * - 
     - tzc
     - Float64
     - Taux dans le cadre du scenario CENTRAL
.. raw:: html

   <a id="GseCtRefObligPzc"></a>

GseCtRefObligPzc
^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 3 25 10 40
   :header-rows: 1
   :class: table-custom

   * - Pk
     - Variable
     - Type
     - Description
   * - :octicon:`key`
     - cd_choc_s2_gse
     - Categorical
     - Choc Solvabilité 2 applicable aux variables économiques
   * - :octicon:`key`
     - maturite
     - Int32
     - Maturité en années d'un cashflow futur
   * - :octicon:`key`
     - intraperiod
     - String
     - Pour un cash flow donné, tombe t il en début, milieu
   * - 
     - pzc
     - Float64
     - Prix zéro coupon
.. raw:: html

   <a id="GseCtRefCashPerf"></a>

GseCtRefCashPerf
^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 3 25 10 40
   :header-rows: 1
   :class: table-custom

   * - Pk
     - Variable
     - Type
     - Description
   * - :octicon:`key`
     - cd_choc_s2_gse
     - Categorical
     - Choc Solvabilité 2 applicable aux variables économiques
   * - :octicon:`key`
     - period
     - Int32
     - Identifiant du pas de temps
   * - :octicon:`key`
     - intraperiod
     - String
     - Pour un cash flow donné, tombe t il en début, milieu
   * - 
     - facteur_perf_tot
     - Float64
     - Facteur d'inflation cummulé
.. raw:: html

   <a id="GseOutputObligInput"></a>

GseOutputObligInput
^^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 3 25 10 40
   :header-rows: 1
   :class: table-custom

   * - Pk
     - Variable
     - Type
     - Description
   * - :octicon:`key`
     - cd_trajectoire
     - String
     - Trajectoire
   * - :octicon:`key`
     - dt_trajectoire
     - Date
     - Trajectoire
   * - :octicon:`key`
     - scenario
     - Int32
     - Identifiant du scenario
   * - :octicon:`key`
     - cd_classe_actif
     - String
     - Classe d'actif
   * - :octicon:`key`
     - cd_choc_s2_gse
     - Categorical
     - Choc Solvabilité 2 applicable aux variables économiques
   * - :octicon:`key`
     - maturite
     - Int32
     - Maturité en années d'un cashflow futur
   * - :octicon:`key`
     - period
     - Int32
     - Identifiant du pas de temps
   * - 
     - tzc
     - Float64
     - Taux dans le cadre du scenario CENTRAL
.. raw:: html

   <a id="GseOutputIndicesInput"></a>

GseOutputIndicesInput
^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 3 25 10 40
   :header-rows: 1
   :class: table-custom

   * - Pk
     - Variable
     - Type
     - Description
   * - :octicon:`key`
     - cd_trajectoire
     - String
     - Trajectoire
   * - :octicon:`key`
     - dt_trajectoire
     - Date
     - Trajectoire
   * - :octicon:`key`
     - scenario
     - Int32
     - Identifiant du scenario
   * - :octicon:`key`
     - cd_choc_s2_gse
     - Categorical
     - Choc Solvabilité 2 applicable aux variables économiques
   * - :octicon:`key`
     - cd_classe_actif
     - String
     - Classe d'actif
   * - :octicon:`key`
     - period
     - Int32
     - Identifiant du pas de temps
   * - 
     - tx_perf_tot
     - Float64
     - Taux de performance total
   * - 
     - tx_dividendes
     - Float64
     - Taux de dividendes
.. raw:: html

   <a id="GseOutputObligPzc"></a>

GseOutputObligPzc
^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 3 25 10 40
   :header-rows: 1
   :class: table-custom

   * - Pk
     - Variable
     - Type
     - Description
   * - :octicon:`key`
     - cd_choc_s2_gse
     - Categorical
     - Choc Solvabilité 2 applicable aux variables économiques
   * - :octicon:`key`
     - scenario
     - Int32
     - Identifiant du scenario
   * - :octicon:`key`
     - period
     - Int32
     - Identifiant du pas de temps
   * - :octicon:`key`
     - maturite
     - Int32
     - Maturité en années d'un cashflow futur
   * - :octicon:`key`
     - intraperiod
     - String
     - Pour un cash flow donné, tombe t il en début, milieu
   * - 
     - pzc
     - Float64
     - Prix zéro coupon
.. raw:: html

   <a id="GseOutputIndicesPerf"></a>

GseOutputIndicesPerf
^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 3 25 10 40
   :header-rows: 1
   :class: table-custom

   * - Pk
     - Variable
     - Type
     - Description
   * - :octicon:`key`
     - cd_choc_s2_gse
     - Categorical
     - Choc Solvabilité 2 applicable aux variables économiques
   * - :octicon:`key`
     - scenario
     - Int32
     - Identifiant du scenario
   * - :octicon:`key`
     - period
     - Int32
     - Identifiant du pas de temps
   * - :octicon:`key`
     - cd_classe_actif
     - String
     - Classe d'actif
   * - 
     - facteur_perf_tot
     - Float64
     - Facteur d'inflation cummulé
   * - 
     - facteur_perf_net
     - Float64
     - Facteur de performance net
   * - 
     - tx_dividendes
     - Float64
     - Taux de dividendes
.. raw:: html

   <a id="GseOutputCashPerf"></a>

GseOutputCashPerf
^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 3 25 10 40
   :header-rows: 1
   :class: table-custom

   * - Pk
     - Variable
     - Type
     - Description
   * - :octicon:`key`
     - cd_choc_s2_gse
     - Categorical
     - Choc Solvabilité 2 applicable aux variables économiques
   * - :octicon:`key`
     - scenario
     - Int32
     - Identifiant du scenario
   * - :octicon:`key`
     - period
     - Int32
     - Identifiant du pas de temps
   * - :octicon:`key`
     - intraperiod
     - String
     - Pour un cash flow donné, tombe t il en début, milieu
   * - 
     - facteur_perf_tot
     - Float64
     - Facteur d'inflation cummulé
.. raw:: html

   <a id="GseOutputDeflateur"></a>

GseOutputDeflateur
^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 3 25 10 40
   :header-rows: 1
   :class: table-custom

   * - Pk
     - Variable
     - Type
     - Description
   * - :octicon:`key`
     - cd_choc_s2_gse
     - Categorical
     - Choc Solvabilité 2 applicable aux variables économiques
   * - :octicon:`key`
     - scenario
     - Int32
     - Identifiant du scenario
   * - :octicon:`key`
     - period
     - Int32
     - Identifiant du pas de temps
   * - :octicon:`key`
     - intraperiod
     - String
     - Pour un cash flow donné, tombe t il en début, milieu
   * - 
     - deflateur
     - Float64
     - Deflateur
.. raw:: html

   <a id="GseOutputInflationInput"></a>

GseOutputInflationInput
^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 3 25 10 40
   :header-rows: 1
   :class: table-custom

   * - Pk
     - Variable
     - Type
     - Description
   * - :octicon:`key`
     - cd_trajectoire
     - String
     - Trajectoire
   * - :octicon:`key`
     - dt_trajectoire
     - Date
     - Trajectoire
   * - :octicon:`key`
     - scenario
     - Int32
     - Identifiant du scenario
   * - :octicon:`key`
     - period
     - Int32
     - Identifiant du pas de temps
   * - :octicon:`key`
     - maturite
     - Int32
     - Maturité en années d'un cashflow futur
   * - :octicon:`key`
     - cd_choc_s2_gse
     - Categorical
     - Choc Solvabilité 2 applicable aux variables économiques
   * - 
     - tx_inflation
     - Float64
     - Taux d'inflation
.. raw:: html

   <a id="GseOutputInflationInitS2"></a>

GseOutputInflationInitS2
^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 3 25 10 40
   :header-rows: 1
   :class: table-custom

   * - Pk
     - Variable
     - Type
     - Description
   * - :octicon:`key`
     - cd_choc_s2_passif_ic_fgx
     - Categorical
     - Choc Solvabilité 2 applicable à la table PassifHypsIcFgx
   * - :octicon:`key`
     - scenario
     - Int32
     - Identifiant du scenario
   * - :octicon:`key`
     - period
     - Int32
     - Identifiant du pas de temps
   * - 
     - tx_inflation
     - Float64
     - Taux d'inflation
   * - 
     - facteur_inflation_cum
     - Float64
     - Facteur d'inflation cummulée



Actif
-----

.. raw:: html

   <a id="MpActifIndices"></a>

MpActifIndices
^^^^^^^^^^^^^^

.. list-table::
   :widths: 3 25 10 40
   :header-rows: 1
   :class: table-custom

   * - Pk
     - Variable
     - Type
     - Description
   * - :octicon:`key`
     - cd_trajectoire
     - String
     - Trajectoire
   * - :octicon:`key`
     - dt_trajectoire
     - Date
     - Trajectoire
   * - :octicon:`key`
     - cd_societe
     - String
     - Code société
   * - :octicon:`key`
     - cd_canton
     - String
     - Code Canton
   * - :octicon:`key`
     - cd_classe_actif
     - String
     - Classe d'actif
   * - :octicon:`key`
     - cd_classe_actif_detail
     - String
     - Classe d'actif détaillée
   * - :octicon:`key`
     - cd_isin
     - String
     - Identifiant du MP actif agrégé
   * - 
     - mt_vm
     - Float64
     - Valeur de marché
   * - 
     - mt_vc
     - Float64
     - Valeur comptable
   * - 
     - tx_action_t1
     - Float64
     - Part de l'actif unitaire à choquer sous S2 avec le choc Action de Type 1
   * - 
     - tx_action_t2
     - Float64
     - Part de l'actif unitaire à choquer sous S2 avec le choc Action de Type 2
   * - 
     - tx_action_strat
     - Float64
     - Part de l'actif unitaire à choquer sous S2 avec le choc Action Stratégique
   * - 
     - mt_pdd
     - Float64
     - Provision pour dépréciation durable
.. raw:: html

   <a id="MpActifIndicesInitGbl"></a>

MpActifIndicesInitGbl
^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 3 25 10 40
   :header-rows: 1
   :class: table-custom

   * - Pk
     - Variable
     - Type
     - Description
   * - :octicon:`key`
     - cd_trajectoire
     - String
     - Trajectoire
   * - :octicon:`key`
     - dt_trajectoire
     - Date
     - Trajectoire
   * - :octicon:`key`
     - cd_societe
     - String
     - Code société
   * - :octicon:`key`
     - cd_canton
     - String
     - Code Canton
   * - :octicon:`key`
     - cd_classe_actif
     - String
     - Classe d'actif
   * - :octicon:`key`
     - cd_classe_actif_detail
     - String
     - Classe d'actif détaillée
   * - :octicon:`key`
     - cd_isin
     - String
     - Identifiant du MP actif agrégé
   * - 
     - mt_vm
     - Float64
     - Valeur de marché
   * - 
     - mt_vc
     - Float64
     - Valeur comptable
   * - 
     - tx_action_t1
     - Float64
     - Part de l'actif unitaire à choquer sous S2 avec le choc Action de Type 1
   * - 
     - tx_action_t2
     - Float64
     - Part de l'actif unitaire à choquer sous S2 avec le choc Action de Type 2
   * - 
     - tx_action_strat
     - Float64
     - Part de l'actif unitaire à choquer sous S2 avec le choc Action Stratégique
   * - 
     - mt_pdd
     - Float64
     - Provision pour dépréciation durable
   * - 
     - mt_pmvl
     - Float64
     - Plus ou moins values latentes disponibles
.. raw:: html

   <a id="MpActifIndicesInitS2"></a>

MpActifIndicesInitS2
^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 3 25 10 40
   :header-rows: 1
   :class: table-custom

   * - Pk
     - Variable
     - Type
     - Description
   * - :octicon:`key`
     - cd_choc_s2
     - Categorical
     - Choc Solvabilité 2
   * - :octicon:`key`
     - cd_choc_s2_gse
     - Categorical
     - Choc Solvabilité 2 applicable aux variables économiques
   * - :octicon:`key`
     - cd_trajectoire
     - String
     - Trajectoire
   * - :octicon:`key`
     - dt_trajectoire
     - Date
     - Trajectoire
   * - :octicon:`key`
     - cd_societe
     - String
     - Code société
   * - :octicon:`key`
     - cd_canton
     - String
     - Code Canton
   * - :octicon:`key`
     - cd_classe_actif
     - String
     - Classe d'actif
   * - :octicon:`key`
     - cd_classe_actif_detail
     - String
     - Classe d'actif détaillée
   * - :octicon:`key`
     - cd_isin
     - String
     - Identifiant du MP actif agrégé
   * - 
     - mt_vm
     - Float64
     - Valeur de marché
   * - 
     - mt_vc
     - Float64
     - Valeur comptable
   * - 
     - tx_action_t1
     - Float64
     - Part de l'actif unitaire à choquer sous S2 avec le choc Action de Type 1
   * - 
     - tx_action_t2
     - Float64
     - Part de l'actif unitaire à choquer sous S2 avec le choc Action de Type 2
   * - 
     - tx_action_strat
     - Float64
     - Part de l'actif unitaire à choquer sous S2 avec le choc Action Stratégique
   * - 
     - mt_pdd
     - Float64
     - Provision pour dépréciation durable
.. raw:: html

   <a id="MpActifIndicesProj"></a>

MpActifIndicesProj
^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 3 25 10 40
   :header-rows: 1
   :class: table-custom

   * - Pk
     - Variable
     - Type
     - Description
   * - :octicon:`key`
     - scenario
     - Int32
     - Identifiant du scenario
   * - :octicon:`key`
     - period
     - Int32
     - Identifiant du pas de temps
   * - :octicon:`key`
     - evenement
     - Categorical
     - Année de projection
   * - :octicon:`key`
     - cd_choc_s2
     - Categorical
     - Choc Solvabilité 2
   * - :octicon:`key`
     - cd_choc_s2_gse
     - Categorical
     - Choc Solvabilité 2 applicable aux variables économiques
   * - :octicon:`key`
     - cd_trajectoire
     - String
     - Trajectoire
   * - :octicon:`key`
     - dt_trajectoire
     - Date
     - Trajectoire
   * - :octicon:`key`
     - cd_societe
     - String
     - Code société
   * - :octicon:`key`
     - cd_canton
     - String
     - Code Canton
   * - :octicon:`key`
     - cd_classe_actif
     - String
     - Classe d'actif
   * - :octicon:`key`
     - cd_classe_actif_detail
     - String
     - Classe d'actif détaillée
   * - :octicon:`key`
     - cd_isin
     - String
     - Identifiant du MP actif agrégé
   * - 
     - mt_vm
     - Float64
     - Valeur de marché
   * - 
     - mt_vc
     - Float64
     - Valeur comptable
   * - 
     - tx_action_t1
     - Float64
     - Part de l'actif unitaire à choquer sous S2 avec le choc Action de Type 1
   * - 
     - tx_action_t2
     - Float64
     - Part de l'actif unitaire à choquer sous S2 avec le choc Action de Type 2
   * - 
     - tx_action_strat
     - Float64
     - Part de l'actif unitaire à choquer sous S2 avec le choc Action Stratégique
   * - 
     - mt_pdd
     - Float64
     - Provision pour dépréciation durable
   * - 
     - mt_vm_av
     - Float64
     - Valeur de marché (avant évènement)
   * - 
     - mt_vc_av
     - Float64
     - Valeur comptable (avant évènement)
   * - 
     - mt_pfi
     - Float64
     - Produits financier généré par l'évènement
   * - 
     - mt_cf
     - Float64
     - Cashflow
   * - 
     - mt_fuite_eco
     - Float64
     - Montant de la fuite économique
   * - 
     - mt_fuite_vc
     - Float64
     - Montant de fuite de valeur comptable
.. raw:: html

   <a id="StratInvInputOutput"></a>

StratInvInputOutput
^^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 3 25 10 40
   :header-rows: 1
   :class: table-custom

   * - Pk
     - Variable
     - Type
     - Description
   * - :octicon:`key`
     - cd_choc_s2
     - Categorical
     - Choc Solvabilité 2
   * - :octicon:`key`
     - cd_choc_s2_gse
     - Categorical
     - Choc Solvabilité 2 applicable aux variables économiques
   * - :octicon:`key`
     - scenario
     - Int32
     - Identifiant du scenario
   * - :octicon:`key`
     - period
     - Int32
     - Identifiant du pas de temps
   * - :octicon:`key`
     - cd_societe
     - String
     - Code société
   * - :octicon:`key`
     - cd_canton
     - String
     - Code Canton
   * - :octicon:`key`
     - cd_classe_actif
     - String
     - Classe d'actif
   * - 
     - mt_vm_av
     - Float64
     - Valeur de marché (avant évènement)
   * - 
     - mt_vm_av_canton
     - Float64
     - Valeur de marché avant stratégie d'investissement pour le canton considéré
   * - 
     - tx_alloc_cible
     - Float64
     - Taux d'allocation cible
   * - 
     - mt_vm_av_cd_classe_actif
     - Float64
     - Valeur de marché avant stratégie d'investissement pour la classe d'actif considérée
   * - 
     - mt_vm_cible_cd_classe_actif
     - Float64
     - Valeur de marché cible
   * - 
     - mt_achat_oblig
     - Float64
     - Montant d'obligations à acheter (output de la stratégie d'investissement)
   * - 
     - facteur_achat_vente
     - Float64
     - Facteur d'achat vente (output de la stratégie d'investissement)
.. raw:: html

   <a id="HypStratInvInput"></a>

HypStratInvInput
^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 3 25 10 40
   :header-rows: 1
   :class: table-custom

   * - Pk
     - Variable
     - Type
     - Description
   * - :octicon:`key`
     - cd_societe
     - String
     - Code société
   * - :octicon:`key`
     - cd_canton
     - String
     - Code Canton
   * - :octicon:`key`
     - cd_classe_actif
     - String
     - Classe d'actif
   * - 
     - tx_alloc_cible
     - Float64
     - Taux d'allocation cible
   * - 
     - tx_oblig_achat_cpn
     - Float64
     - Taux de coupon des obligations à acheter
   * - 
     - nb_oblig_achat_maturite
     - Float64
     - Maturité des obligations à acheter
   * - 
     - tx_frais_plct
     - Float64
     - Taux de frais de placement
.. raw:: html

   <a id="HypStratInvTxAllocCible"></a>

HypStratInvTxAllocCible
^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 3 25 10 40
   :header-rows: 1
   :class: table-custom

   * - Pk
     - Variable
     - Type
     - Description
   * - :octicon:`key`
     - cd_societe
     - String
     - Code société
   * - :octicon:`key`
     - cd_canton
     - String
     - Code Canton
   * - :octicon:`key`
     - cd_classe_actif
     - String
     - Classe d'actif
   * - 
     - tx_alloc_cible
     - Float64
     - Taux d'allocation cible
.. raw:: html

   <a id="HypStratInvObligAchat"></a>

HypStratInvObligAchat
^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 3 25 10 40
   :header-rows: 1
   :class: table-custom

   * - Pk
     - Variable
     - Type
     - Description
   * - :octicon:`key`
     - cd_societe
     - String
     - Code société
   * - :octicon:`key`
     - cd_canton
     - String
     - Code Canton
   * - :octicon:`key`
     - cd_classe_actif
     - String
     - Classe d'actif
   * - 
     - tx_oblig_achat_cpn
     - Float64
     - Taux de coupon des obligations à acheter
   * - 
     - nb_oblig_achat_maturite
     - Float64
     - Maturité des obligations à acheter
.. raw:: html

   <a id="HypStratInvTxFraisPlct"></a>

HypStratInvTxFraisPlct
^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 3 25 10 40
   :header-rows: 1
   :class: table-custom

   * - Pk
     - Variable
     - Type
     - Description
   * - :octicon:`key`
     - cd_societe
     - String
     - Code société
   * - :octicon:`key`
     - cd_canton
     - String
     - Code Canton
   * - :octicon:`key`
     - cd_classe_actif
     - String
     - Classe d'actif
   * - 
     - tx_frais_plct
     - Float64
     - Taux de frais de placement
.. raw:: html

   <a id="MpActifCashInputCf"></a>

MpActifCashInputCf
^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 3 25 10 40
   :header-rows: 1
   :class: table-custom

   * - Pk
     - Variable
     - Type
     - Description
   * - :octicon:`key`
     - cd_choc_s2
     - Categorical
     - Choc Solvabilité 2
   * - :octicon:`key`
     - cd_choc_s2_gse
     - Categorical
     - Choc Solvabilité 2 applicable aux variables économiques
   * - :octicon:`key`
     - scenario
     - Int32
     - Identifiant du scenario
   * - :octicon:`key`
     - period
     - Int32
     - Identifiant du pas de temps
   * - :octicon:`key`
     - intraperiod
     - String
     - Pour un cash flow donné, tombe t il en début, milieu
   * - :octicon:`key`
     - cd_societe
     - String
     - Code société
   * - :octicon:`key`
     - cd_canton
     - String
     - Code Canton
   * - :octicon:`key`
     - cd_type_flux
     - Categorical
     - Type de flux
   * - 
     - mt_cf
     - Float64
     - Cashflow
.. raw:: html

   <a id="PrdAdActif"></a>

PrdAdActif
^^^^^^^^^^

.. list-table::
   :widths: 3 25 10 40
   :header-rows: 1
   :class: table-custom

   * - Pk
     - Variable
     - Type
     - Description
   * - :octicon:`key`
     - cd_choc_s2
     - Categorical
     - Choc Solvabilité 2
   * - :octicon:`key`
     - scenario
     - Int32
     - Identifiant du scenario
   * - :octicon:`key`
     - period
     - Int32
     - Identifiant du pas de temps
   * - :octicon:`key`
     - evenement
     - Categorical
     - Année de projection
   * - :octicon:`key`
     - cd_societe
     - String
     - Code société
   * - :octicon:`key`
     - cd_canton
     - String
     - Code Canton
   * - :octicon:`key`
     - cd_classe_actif
     - String
     - Classe d'actif
   * - 
     - mt_vm_av
     - Float64
     - Valeur de marché (avant évènement)
   * - 
     - mt_vm
     - Float64
     - Valeur de marché
   * - 
     - mt_vc_av
     - Float64
     - Valeur comptable (avant évènement)
   * - 
     - mt_vc
     - Float64
     - Valeur comptable
   * - 
     - mt_pmvl
     - Float64
     - Plus ou moins values latentes disponibles
   * - 
     - mt_pfi
     - Float64
     - Produits financier généré par l'évènement
   * - 
     - mt_cf
     - Float64
     - Cashflow
   * - 
     - mt_pdd
     - Float64
     - Provision pour dépréciation durable
   * - 
     - mt_fuite_eco
     - Float64
     - Montant de la fuite économique
   * - 
     - mt_fuite_vc
     - Float64
     - Montant de fuite de valeur comptable



Passif
------

.. raw:: html

   <a id="HypPassifEpFgx"></a>

HypPassifEpFgx
^^^^^^^^^^^^^^

.. list-table::
   :widths: 3 25 10 40
   :header-rows: 1
   :class: table-custom

   * - Pk
     - Variable
     - Type
     - Description
   * - :octicon:`key`
     - cd_societe
     - String
     - Code société
   * - :octicon:`key`
     - cd_fampdt
     - Categorical
     - Code Famille de produit
   * - 
     - tx_fgx_pm_eu
     - Float64
     - Taux de frais généraux sur les PM
   * - 
     - tx_fgx_prst_eu
     - Float64
     - Taux de frais généraux sur les prestations
   * - 
     - tx_fgx_plct_eu
     - Float64
     - Taux de frais généraux sur les placements
   * - 
     - tx_fgx_pm_uc
     - Float64
     - Taux de frais généraux sur les PM
   * - 
     - tx_fgx_prst_uc
     - Float64
     - Taux de frais généraux sur les prestations
   * - 
     - tx_fgx_plct_uc
     - Float64
     - Taux de frais généraux sur les placements
.. raw:: html

   <a id="HypPassifEpPrstRt"></a>

HypPassifEpPrstRt
^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 3 25 10 40
   :header-rows: 1
   :class: table-custom

   * - Pk
     - Variable
     - Type
     - Description
   * - :octicon:`key`
     - nb_cnt_anciennete_annee
     - Int32
     - Ancienneté du contrat en année
   * - :octicon:`key`
     - cd_prst_rt_cat
     - Int16
     - Catégorie de prestation rachat
   * - 
     - tx_prst_rt
     - Float64
     - Taux de prestation de rachat total
.. raw:: html

   <a id="HypMort"></a>

HypMort
^^^^^^^

.. list-table::
   :widths: 3 25 10 40
   :header-rows: 1
   :class: table-custom

   * - Pk
     - Variable
     - Type
     - Description
   * - :octicon:`key`
     - sexe
     - String
     - Sexe
   * - :octicon:`key`
     - age
     - Int32
     - Age en années
   * - 
     - qx
     - Float64
     - Taux de mortalité
.. raw:: html

   <a id="HypMortGen"></a>

HypMortGen
^^^^^^^^^^

.. list-table::
   :widths: 3 25 10 40
   :header-rows: 1
   :class: table-custom

   * - Pk
     - Variable
     - Type
     - Description
   * - :octicon:`key`
     - generation
     - Int32
     - Année de naissance d'une génération donnée
   * - :octicon:`key`
     - sexe
     - String
     - Sexe
   * - :octicon:`key`
     - age
     - Int32
     - Age en années
   * - 
     - qx
     - Float64
     - Taux de mortalité
.. raw:: html

   <a id="MpPassifEp"></a>

MpPassifEp
^^^^^^^^^^

.. list-table::
   :widths: 3 25 10 40
   :header-rows: 1
   :class: table-custom

   * - Pk
     - Variable
     - Type
     - Description
   * - :octicon:`key`
     - cd_trajectoire
     - String
     - Trajectoire
   * - :octicon:`key`
     - dt_trajectoire
     - Date
     - Trajectoire
   * - :octicon:`key`
     - cd_societe
     - String
     - Code société
   * - :octicon:`key`
     - cd_canton
     - String
     - Code Canton
   * - :octicon:`key`
     - cd_prtf_ifrs17
     - Categorical
     - Code Portefeuille Ifrs17
   * - :octicon:`key`
     - cd_fampdt
     - Categorical
     - Code Famille de produit
   * - :octicon:`key`
     - cd_cnt
     - Int32
     - Identifiant d'un contrat
   * - 
     - nb_cnt
     - Float64
     - Nombre de contrats
   * - 
     - cd_asse_sexe
     - String
     - Sexe de l'assuré
   * - 
     - dt_asse_naiss
     - Date
     - Date de naissance de l'assuré
   * - 
     - dt_cnt_effet
     - Date
     - Date d'effet du contrat
   * - 
     - mt_pm_eu
     - Float64
     - Montant de la PM
   * - 
     - cd_hrg_eu
     - Int32
     - HRG associé au support euro
   * - 
     - mt_pm_uc
     - Float64
     - Montant de la PM
   * - 
     - cd_hrg_uc
     - Int32
     - HRG associé au support uc
   * - 
     - cd_prst_rt_cat
     - Int16
     - Catégorie de prestation rachat
   * - 
     - cd_capitalisation
     - Enum(categories=['capi', 'ncapi'])
     - Contrat de capitalisation
   * - 
     - tmg
     - Float64
     - Taux minimum garanti
   * - 
     - tmg_type
     - Enum(categories=['net', 'brut'])
     - Taux minimum garanti
   * - 
     - taf
     - Float64
     - Taux d'affectation des produits financiers
   * - 
     - tfgse
     - Float64
     - Taux de frais de gestion sur encours euro
   * - 
     - tfgse_uc
     - Float64
     - Taux de frais de gestion sur encours UC
   * - 
     - cd_hyp_mort_exp
     - String
     - Table de mortalite d'expérience à appliquer
   * - 
     - cd_hyp_mort_prov
     - String
     - Table de mortalite utilisée pour le provisionnement
   * - 
     - tx_prst_chgt
     - Float64
     - Taux de chargement sur les prestations
   * - 
     - tx_action_t1
     - Float64
     - Part de l'actif unitaire à choquer sous S2 avec le choc Action de Type 1
   * - 
     - tx_action_t2
     - Float64
     - Part de l'actif unitaire à choquer sous S2 avec le choc Action de Type 2
   * - 
     - tx_action_strat
     - Float64
     - Part de l'actif unitaire à choquer sous S2 avec le choc Action Stratégique
   * - 
     - tx_immobilier
     - Float64
     - Part de l'actif unitaire à choquer sous S2 avec le choc immobilier
.. raw:: html

   <a id="MpPassifEpInitGbl"></a>

MpPassifEpInitGbl
^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 3 25 10 40
   :header-rows: 1
   :class: table-custom

   * - Pk
     - Variable
     - Type
     - Description
   * - :octicon:`key`
     - cd_trajectoire
     - String
     - Trajectoire
   * - :octicon:`key`
     - dt_trajectoire
     - Date
     - Trajectoire
   * - :octicon:`key`
     - cd_societe
     - String
     - Code société
   * - :octicon:`key`
     - cd_canton
     - String
     - Code Canton
   * - :octicon:`key`
     - cd_prtf_ifrs17
     - Categorical
     - Code Portefeuille Ifrs17
   * - :octicon:`key`
     - cd_fampdt
     - Categorical
     - Code Famille de produit
   * - :octicon:`key`
     - cd_cnt
     - Int32
     - Identifiant d'un contrat
   * - 
     - nb_cnt
     - Float64
     - Nombre de contrats
   * - 
     - cd_asse_sexe
     - String
     - Sexe de l'assuré
   * - 
     - dt_asse_naiss
     - Date
     - Date de naissance de l'assuré
   * - 
     - dt_cnt_effet
     - Date
     - Date d'effet du contrat
   * - 
     - mt_pm_eu
     - Float64
     - Montant de la PM
   * - 
     - cd_hrg_eu
     - Int32
     - HRG associé au support euro
   * - 
     - mt_pm_uc
     - Float64
     - Montant de la PM
   * - 
     - cd_hrg_uc
     - Int32
     - HRG associé au support uc
   * - 
     - cd_prst_rt_cat
     - Int16
     - Catégorie de prestation rachat
   * - 
     - cd_capitalisation
     - Enum(categories=['capi', 'ncapi'])
     - Contrat de capitalisation
   * - 
     - tmg
     - Float64
     - Taux minimum garanti
   * - 
     - tmg_type
     - Enum(categories=['net', 'brut'])
     - Taux minimum garanti
   * - 
     - taf
     - Float64
     - Taux d'affectation des produits financiers
   * - 
     - tfgse
     - Float64
     - Taux de frais de gestion sur encours euro
   * - 
     - tfgse_uc
     - Float64
     - Taux de frais de gestion sur encours UC
   * - 
     - cd_hyp_mort_exp
     - String
     - Table de mortalite d'expérience à appliquer
   * - 
     - cd_hyp_mort_prov
     - String
     - Table de mortalite utilisée pour le provisionnement
   * - 
     - tx_prst_chgt
     - Float64
     - Taux de chargement sur les prestations
   * - 
     - tx_action_t1
     - Float64
     - Part de l'actif unitaire à choquer sous S2 avec le choc Action de Type 1
   * - 
     - tx_action_t2
     - Float64
     - Part de l'actif unitaire à choquer sous S2 avec le choc Action de Type 2
   * - 
     - tx_action_strat
     - Float64
     - Part de l'actif unitaire à choquer sous S2 avec le choc Action Stratégique
   * - 
     - tx_immobilier
     - Float64
     - Part de l'actif unitaire à choquer sous S2 avec le choc immobilier
   * - 
     - nb_asse_age_annee
     - Int32
     - Age de l'assuré en années
   * - 
     - nb_asse_age_mois
     - Int32
     - Age de l'assuré en années
   * - 
     - nb_cnt_anciennete_annee
     - Int32
     - Ancienneté du contrat en année
   * - 
     - nb_cnt_anciennete_mois
     - Int32
     - Ancienneté du contrat en mois
   * - 
     - tmg_brt
     - Float64
     - Taux minimum garanti, brut de taf et tfgse
   * - 
     - generation
     - Int32
     - Année de naissance d'une génération donnée
.. raw:: html

   <a id="MpPassifEpInitS2"></a>

MpPassifEpInitS2
^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 3 25 10 40
   :header-rows: 1
   :class: table-custom

   * - Pk
     - Variable
     - Type
     - Description
   * - :octicon:`key`
     - cd_choc_s2
     - Categorical
     - Choc Solvabilité 2
   * - :octicon:`key`
     - cd_choc_s2_gse
     - Categorical
     - Choc Solvabilité 2 applicable aux variables économiques
   * - :octicon:`key`
     - cd_choc_s2_passif_prst
     - Categorical
     - Choc Solvabilité 2 applicable aux hypothèses de prestations
   * - :octicon:`key`
     - cd_choc_s2_passif_ic_fgx
     - Categorical
     - Choc Solvabilité 2 applicable à la table PassifHypsIcFgx
   * - :octicon:`key`
     - cd_trajectoire
     - String
     - Trajectoire
   * - :octicon:`key`
     - dt_trajectoire
     - Date
     - Trajectoire
   * - :octicon:`key`
     - cd_societe
     - String
     - Code société
   * - :octicon:`key`
     - cd_canton
     - String
     - Code Canton
   * - :octicon:`key`
     - cd_prtf_ifrs17
     - Categorical
     - Code Portefeuille Ifrs17
   * - :octicon:`key`
     - cd_fampdt
     - Categorical
     - Code Famille de produit
   * - :octicon:`key`
     - cd_cnt
     - Int32
     - Identifiant d'un contrat
   * - 
     - nb_cnt
     - Float64
     - Nombre de contrats
   * - 
     - cd_asse_sexe
     - String
     - Sexe de l'assuré
   * - 
     - dt_asse_naiss
     - Date
     - Date de naissance de l'assuré
   * - 
     - dt_cnt_effet
     - Date
     - Date d'effet du contrat
   * - 
     - mt_pm_eu
     - Float64
     - Montant de la PM
   * - 
     - cd_hrg_eu
     - Int32
     - HRG associé au support euro
   * - 
     - mt_pm_uc
     - Float64
     - Montant de la PM
   * - 
     - cd_hrg_uc
     - Int32
     - HRG associé au support uc
   * - 
     - cd_prst_rt_cat
     - Int16
     - Catégorie de prestation rachat
   * - 
     - cd_capitalisation
     - Enum(categories=['capi', 'ncapi'])
     - Contrat de capitalisation
   * - 
     - tmg
     - Float64
     - Taux minimum garanti
   * - 
     - tmg_type
     - Enum(categories=['net', 'brut'])
     - Taux minimum garanti
   * - 
     - taf
     - Float64
     - Taux d'affectation des produits financiers
   * - 
     - tfgse
     - Float64
     - Taux de frais de gestion sur encours euro
   * - 
     - tfgse_uc
     - Float64
     - Taux de frais de gestion sur encours UC
   * - 
     - cd_hyp_mort_exp
     - String
     - Table de mortalite d'expérience à appliquer
   * - 
     - cd_hyp_mort_prov
     - String
     - Table de mortalite utilisée pour le provisionnement
   * - 
     - tx_prst_chgt
     - Float64
     - Taux de chargement sur les prestations
   * - 
     - tx_action_t1
     - Float64
     - Part de l'actif unitaire à choquer sous S2 avec le choc Action de Type 1
   * - 
     - tx_action_t2
     - Float64
     - Part de l'actif unitaire à choquer sous S2 avec le choc Action de Type 2
   * - 
     - tx_action_strat
     - Float64
     - Part de l'actif unitaire à choquer sous S2 avec le choc Action Stratégique
   * - 
     - tx_immobilier
     - Float64
     - Part de l'actif unitaire à choquer sous S2 avec le choc immobilier
   * - 
     - nb_asse_age_annee
     - Int32
     - Age de l'assuré en années
   * - 
     - nb_asse_age_mois
     - Int32
     - Age de l'assuré en années
   * - 
     - nb_cnt_anciennete_annee
     - Int32
     - Ancienneté du contrat en année
   * - 
     - nb_cnt_anciennete_mois
     - Int32
     - Ancienneté du contrat en mois
   * - 
     - tmg_brt
     - Float64
     - Taux minimum garanti, brut de taf et tfgse
   * - 
     - generation
     - Int32
     - Année de naissance d'une génération donnée
.. raw:: html

   <a id="MpPassifEpErreurs"></a>

MpPassifEpErreurs
^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 3 25 10 40
   :header-rows: 1
   :class: table-custom

   * - Pk
     - Variable
     - Type
     - Description
   * - :octicon:`key`
     - type_erreur
     - String
     - Type d'erreur
   * - :octicon:`key`
     - erreur
     - String
     - Description de l'erreur
   * - :octicon:`key`
     - type_erreur_action
     - String
     - Type d'action réalisée compte tenu de l'erreur
   * - :octicon:`key`
     - cd_trajectoire
     - String
     - Trajectoire
   * - :octicon:`key`
     - dt_trajectoire
     - Date
     - Trajectoire
   * - :octicon:`key`
     - cd_societe
     - String
     - Code société
   * - :octicon:`key`
     - cd_canton
     - String
     - Code Canton
   * - :octicon:`key`
     - cd_prtf_ifrs17
     - Categorical
     - Code Portefeuille Ifrs17
   * - :octicon:`key`
     - cd_fampdt
     - Categorical
     - Code Famille de produit
   * - :octicon:`key`
     - cd_cnt
     - Int32
     - Identifiant d'un contrat
   * - 
     - nb_cnt
     - Float64
     - Nombre de contrats
   * - 
     - cd_asse_sexe
     - String
     - Sexe de l'assuré
   * - 
     - dt_asse_naiss
     - Date
     - Date de naissance de l'assuré
   * - 
     - dt_cnt_effet
     - Date
     - Date d'effet du contrat
   * - 
     - mt_pm_eu
     - Float64
     - Montant de la PM
   * - 
     - cd_hrg_eu
     - Int32
     - HRG associé au support euro
   * - 
     - mt_pm_uc
     - Float64
     - Montant de la PM
   * - 
     - cd_hrg_uc
     - Int32
     - HRG associé au support uc
   * - 
     - cd_prst_rt_cat
     - Int16
     - Catégorie de prestation rachat
   * - 
     - cd_capitalisation
     - Enum(categories=['capi', 'ncapi'])
     - Contrat de capitalisation
   * - 
     - tmg
     - Float64
     - Taux minimum garanti
   * - 
     - tmg_type
     - Enum(categories=['net', 'brut'])
     - Taux minimum garanti
   * - 
     - taf
     - Float64
     - Taux d'affectation des produits financiers
   * - 
     - tfgse
     - Float64
     - Taux de frais de gestion sur encours euro
   * - 
     - tfgse_uc
     - Float64
     - Taux de frais de gestion sur encours UC
   * - 
     - cd_hyp_mort_exp
     - String
     - Table de mortalite d'expérience à appliquer
   * - 
     - cd_hyp_mort_prov
     - String
     - Table de mortalite utilisée pour le provisionnement
   * - 
     - tx_prst_chgt
     - Float64
     - Taux de chargement sur les prestations
   * - 
     - tx_action_t1
     - Float64
     - Part de l'actif unitaire à choquer sous S2 avec le choc Action de Type 1
   * - 
     - tx_action_t2
     - Float64
     - Part de l'actif unitaire à choquer sous S2 avec le choc Action de Type 2
   * - 
     - tx_action_strat
     - Float64
     - Part de l'actif unitaire à choquer sous S2 avec le choc Action Stratégique
   * - 
     - tx_immobilier
     - Float64
     - Part de l'actif unitaire à choquer sous S2 avec le choc immobilier
   * - 
     - nb_asse_age_annee
     - Int32
     - Age de l'assuré en années
   * - 
     - nb_asse_age_mois
     - Int32
     - Age de l'assuré en années
   * - 
     - nb_cnt_anciennete_annee
     - Int32
     - Ancienneté du contrat en année
   * - 
     - nb_cnt_anciennete_mois
     - Int32
     - Ancienneté du contrat en mois
   * - 
     - tmg_brt
     - Float64
     - Taux minimum garanti, brut de taf et tfgse
   * - 
     - generation
     - Int32
     - Année de naissance d'une génération donnée
.. raw:: html

   <a id="MpPassifEpProj"></a>

MpPassifEpProj
^^^^^^^^^^^^^^

.. list-table::
   :widths: 3 25 10 40
   :header-rows: 1
   :class: table-custom

   * - Pk
     - Variable
     - Type
     - Description
   * - :octicon:`key`
     - cd_choc_s2
     - Categorical
     - Choc Solvabilité 2
   * - :octicon:`key`
     - cd_choc_s2_gse
     - Categorical
     - Choc Solvabilité 2 applicable aux variables économiques
   * - :octicon:`key`
     - cd_choc_s2_passif_prst
     - Categorical
     - Choc Solvabilité 2 applicable aux hypothèses de prestations
   * - :octicon:`key`
     - cd_choc_s2_passif_ic_fgx
     - Categorical
     - Choc Solvabilité 2 applicable à la table PassifHypsIcFgx
   * - :octicon:`key`
     - scenario
     - Int32
     - Identifiant du scenario
   * - :octicon:`key`
     - period
     - Int32
     - Identifiant du pas de temps
   * - :octicon:`key`
     - evenement
     - Categorical
     - Année de projection
   * - :octicon:`key`
     - cd_societe
     - String
     - Code société
   * - :octicon:`key`
     - cd_canton
     - String
     - Code Canton
   * - :octicon:`key`
     - cd_prtf_ifrs17
     - Categorical
     - Code Portefeuille Ifrs17
   * - :octicon:`key`
     - cd_fampdt
     - Categorical
     - Code Famille de produit
   * - :octicon:`key`
     - cd_cnt
     - Int32
     - Identifiant d'un contrat
   * - 
     - nb_cnt
     - Float64
     - Nombre de contrats
   * - 
     - cd_asse_sexe
     - String
     - Sexe de l'assuré
   * - 
     - dt_asse_naiss
     - Date
     - Date de naissance de l'assuré
   * - 
     - dt_cnt_effet
     - Date
     - Date d'effet du contrat
   * - 
     - mt_pm_eu
     - Float64
     - Montant de la PM
   * - 
     - cd_hrg_eu
     - Int32
     - HRG associé au support euro
   * - 
     - mt_pm_uc
     - Float64
     - Montant de la PM
   * - 
     - cd_hrg_uc
     - Int32
     - HRG associé au support uc
   * - 
     - cd_prst_rt_cat
     - Int16
     - Catégorie de prestation rachat
   * - 
     - cd_capitalisation
     - Enum(categories=['capi', 'ncapi'])
     - Contrat de capitalisation
   * - 
     - tmg
     - Float64
     - Taux minimum garanti
   * - 
     - tmg_type
     - Enum(categories=['net', 'brut'])
     - Taux minimum garanti
   * - 
     - taf
     - Float64
     - Taux d'affectation des produits financiers
   * - 
     - tfgse
     - Float64
     - Taux de frais de gestion sur encours euro
   * - 
     - tfgse_uc
     - Float64
     - Taux de frais de gestion sur encours UC
   * - 
     - cd_hyp_mort_exp
     - String
     - Table de mortalite d'expérience à appliquer
   * - 
     - cd_hyp_mort_prov
     - String
     - Table de mortalite utilisée pour le provisionnement
   * - 
     - tx_prst_chgt
     - Float64
     - Taux de chargement sur les prestations
   * - 
     - tx_action_t1
     - Float64
     - Part de l'actif unitaire à choquer sous S2 avec le choc Action de Type 1
   * - 
     - tx_action_t2
     - Float64
     - Part de l'actif unitaire à choquer sous S2 avec le choc Action de Type 2
   * - 
     - tx_action_strat
     - Float64
     - Part de l'actif unitaire à choquer sous S2 avec le choc Action Stratégique
   * - 
     - tx_immobilier
     - Float64
     - Part de l'actif unitaire à choquer sous S2 avec le choc immobilier
   * - 
     - nb_asse_age_annee
     - Int32
     - Age de l'assuré en années
   * - 
     - nb_asse_age_mois
     - Int32
     - Age de l'assuré en années
   * - 
     - nb_cnt_anciennete_annee
     - Int32
     - Ancienneté du contrat en année
   * - 
     - nb_cnt_anciennete_mois
     - Int32
     - Ancienneté du contrat en mois
   * - 
     - tmg_brt
     - Float64
     - Taux minimum garanti, brut de taf et tfgse
   * - 
     - generation
     - Int32
     - Année de naissance d'une génération donnée
   * - 
     - mt_pm_eu_av
     - Float64
     - Montant de la PM (avant évènement)
   * - 
     - mt_pm_uc_av
     - Float64
     - Montant de la PM (avant évènement)
   * - 
     - nb_cnt_av
     - Float64
     - Nombre de contrats (avant évènement)
.. raw:: html

   <a id="MpPassifEpProjHypsPrst"></a>

MpPassifEpProjHypsPrst
^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 3 25 10 40
   :header-rows: 1
   :class: table-custom

   * - Pk
     - Variable
     - Type
     - Description
   * - :octicon:`key`
     - cd_choc_s2_passif_prst
     - Categorical
     - Choc Solvabilité 2 applicable aux hypothèses de prestations
   * - :octicon:`key`
     - period
     - Int32
     - Identifiant du pas de temps
   * - :octicon:`key`
     - cd_societe
     - String
     - Code société
   * - :octicon:`key`
     - cd_canton
     - String
     - Code Canton
   * - :octicon:`key`
     - cd_prtf_ifrs17
     - Categorical
     - Code Portefeuille Ifrs17
   * - :octicon:`key`
     - cd_fampdt
     - Categorical
     - Code Famille de produit
   * - :octicon:`key`
     - cd_cnt
     - Int32
     - Identifiant d'un contrat
   * - 
     - tx_prst_rt
     - Float64
     - Taux de prestation de rachat total
   * - 
     - tx_prst_dc_asse_exp
     - Float64
     - Taux de prestation décès appliqué dans la diffusion du nombre d'assuré
   * - 
     - tx_prst_chgt
     - Float64
     - Taux de chargement sur les prestations
.. raw:: html

   <a id="MpPassifEpProjHypsIcFgx"></a>

MpPassifEpProjHypsIcFgx
^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 3 25 10 40
   :header-rows: 1
   :class: table-custom

   * - Pk
     - Variable
     - Type
     - Description
   * - :octicon:`key`
     - cd_choc_s2_passif_ic_fgx
     - Categorical
     - Choc Solvabilité 2 applicable à la table PassifHypsIcFgx
   * - :octicon:`key`
     - scenario
     - Int32
     - Identifiant du scenario
   * - :octicon:`key`
     - period
     - Int32
     - Identifiant du pas de temps
   * - :octicon:`key`
     - cd_societe
     - String
     - Code société
   * - :octicon:`key`
     - cd_canton
     - String
     - Code Canton
   * - :octicon:`key`
     - cd_prtf_ifrs17
     - Categorical
     - Code Portefeuille Ifrs17
   * - :octicon:`key`
     - cd_fampdt
     - Categorical
     - Code Famille de produit
   * - :octicon:`key`
     - cd_cnt
     - Int32
     - Identifiant d'un contrat
   * - 
     - tx_fgx_prst_eu
     - Float64
     - Taux de frais généraux sur les prestations
   * - 
     - tx_fgx_pm_eu
     - Float64
     - Taux de frais généraux sur les PM
   * - 
     - tx_fgx_prst_uc
     - Float64
     - Taux de frais généraux sur les prestations
   * - 
     - tx_fgx_pm_uc
     - Float64
     - Taux de frais généraux sur les PM
   * - 
     - tx_ic_eu
     - Float64
     - Taux d'intérêts crédités Euro
   * - 
     - tx_ic_eu_brt
     - Float64
     - Taux d'intérêts crédités Euro brut de taf et tfgse
   * - 
     - tx_ic_uc
     - Float64
     - Taux d'intérêts crédités UC
   * - 
     - tx_ic_eu_demi_periode
     - Float64
     - Taux d'intérêts crédités Euro
   * - 
     - tx_ic_eu_brt_demi_periode
     - Float64
     - Taux d'intérêts crédités Euro brut de taf et tfgse
   * - 
     - tx_ic_uc_demi_periode
     - Float64
     - Taux d'intérêts crédités UC
   * - 
     - taf
     - Float64
     - Taux d'affectation des produits financiers
   * - 
     - tfgse
     - Float64
     - Taux de frais de gestion sur encours euro
   * - 
     - facteur_inflation_cum
     - Float64
     - Facteur d'inflation cummulée
.. raw:: html

   <a id="MpPassifEpProjPerf"></a>

MpPassifEpProjPerf
^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 3 25 10 40
   :header-rows: 1
   :class: table-custom

   * - Pk
     - Variable
     - Type
     - Description
   * - :octicon:`key`
     - cd_choc_s2
     - Categorical
     - Choc Solvabilité 2
   * - :octicon:`key`
     - cd_choc_s2_gse
     - Categorical
     - Choc Solvabilité 2 applicable aux variables économiques
   * - :octicon:`key`
     - cd_choc_s2_passif_prst
     - Categorical
     - Choc Solvabilité 2 applicable aux hypothèses de prestations
   * - :octicon:`key`
     - cd_choc_s2_passif_ic_fgx
     - Categorical
     - Choc Solvabilité 2 applicable à la table PassifHypsIcFgx
   * - :octicon:`key`
     - scenario
     - Int32
     - Identifiant du scenario
   * - :octicon:`key`
     - period
     - Int32
     - Identifiant du pas de temps
   * - :octicon:`key`
     - evenement
     - Categorical
     - Année de projection
   * - :octicon:`key`
     - cd_societe
     - String
     - Code société
   * - :octicon:`key`
     - cd_canton
     - String
     - Code Canton
   * - :octicon:`key`
     - cd_prtf_ifrs17
     - Categorical
     - Code Portefeuille Ifrs17
   * - :octicon:`key`
     - cd_fampdt
     - Categorical
     - Code Famille de produit
   * - :octicon:`key`
     - cd_cnt
     - Int32
     - Identifiant d'un contrat
   * - 
     - nb_cnt
     - Float64
     - Nombre de contrats
   * - 
     - cd_asse_sexe
     - String
     - Sexe de l'assuré
   * - 
     - dt_asse_naiss
     - Date
     - Date de naissance de l'assuré
   * - 
     - dt_cnt_effet
     - Date
     - Date d'effet du contrat
   * - 
     - mt_pm_eu
     - Float64
     - Montant de la PM
   * - 
     - cd_hrg_eu
     - Int32
     - HRG associé au support euro
   * - 
     - mt_pm_uc
     - Float64
     - Montant de la PM
   * - 
     - cd_hrg_uc
     - Int32
     - HRG associé au support uc
   * - 
     - cd_prst_rt_cat
     - Int16
     - Catégorie de prestation rachat
   * - 
     - cd_capitalisation
     - Enum(categories=['capi', 'ncapi'])
     - Contrat de capitalisation
   * - 
     - tmg
     - Float64
     - Taux minimum garanti
   * - 
     - tmg_type
     - Enum(categories=['net', 'brut'])
     - Taux minimum garanti
   * - 
     - taf
     - Float64
     - Taux d'affectation des produits financiers
   * - 
     - tfgse
     - Float64
     - Taux de frais de gestion sur encours euro
   * - 
     - tfgse_uc
     - Float64
     - Taux de frais de gestion sur encours UC
   * - 
     - cd_hyp_mort_exp
     - String
     - Table de mortalite d'expérience à appliquer
   * - 
     - cd_hyp_mort_prov
     - String
     - Table de mortalite utilisée pour le provisionnement
   * - 
     - tx_prst_chgt
     - Float64
     - Taux de chargement sur les prestations
   * - 
     - tx_action_t1
     - Float64
     - Part de l'actif unitaire à choquer sous S2 avec le choc Action de Type 1
   * - 
     - tx_action_t2
     - Float64
     - Part de l'actif unitaire à choquer sous S2 avec le choc Action de Type 2
   * - 
     - tx_action_strat
     - Float64
     - Part de l'actif unitaire à choquer sous S2 avec le choc Action Stratégique
   * - 
     - tx_immobilier
     - Float64
     - Part de l'actif unitaire à choquer sous S2 avec le choc immobilier
   * - 
     - nb_asse_age_annee
     - Int32
     - Age de l'assuré en années
   * - 
     - nb_asse_age_mois
     - Int32
     - Age de l'assuré en années
   * - 
     - nb_cnt_anciennete_annee
     - Int32
     - Ancienneté du contrat en année
   * - 
     - nb_cnt_anciennete_mois
     - Int32
     - Ancienneté du contrat en mois
   * - 
     - tmg_brt
     - Float64
     - Taux minimum garanti, brut de taf et tfgse
   * - 
     - generation
     - Int32
     - Année de naissance d'une génération donnée
   * - 
     - mt_pm_eu_av
     - Float64
     - Montant de la PM (avant évènement)
   * - 
     - mt_pm_uc_av
     - Float64
     - Montant de la PM (avant évènement)
   * - 
     - nb_cnt_av
     - Float64
     - Nombre de contrats (avant évènement)
   * - 
     - mt_prst_tot_eu_brt
     - Float64
     - Montant de prestations totales, brutes de chargements
   * - 
     - mt_prst_tot_eu_net
     - Float64
     - Montant de prestations totales, nettes de chargements
   * - 
     - mt_prst_tot_eu_chgt
     - Float64
     - Montant de chargements sur l'ensemble des prestations
   * - 
     - mt_prst_dc_eu_brt
     - Float64
     - Montant de prestations décès, brutes de chargements
   * - 
     - mt_prst_dc_eu_net
     - Float64
     - Montant de prestations décès, nettes de chargements
   * - 
     - mt_prst_dc_eu_chgt
     - Float64
     - Montant de chargements sur les prestations décès
   * - 
     - mt_prst_rt_eu_brt
     - Float64
     - Montant de prestations rachat, brutes de chargements
   * - 
     - mt_prst_rt_eu_net
     - Float64
     - Montant de prestations rachat, nettes de chargements
   * - 
     - mt_prst_rt_eu_chgt
     - Float64
     - Montant de chargements sur les prestations rachats
   * - 
     - mt_prst_tot_uc_brt
     - Float64
     - Montant de prestations totales, brutes de chargements
   * - 
     - mt_prst_tot_uc_net
     - Float64
     - Montant de prestations totales, nettes de chargements
   * - 
     - mt_prst_tot_uc_chgt
     - Float64
     - Montant de chargements sur l'ensemble des prestations
   * - 
     - mt_prst_dc_uc_brt
     - Float64
     - Montant de prestations décès, brutes de chargements
   * - 
     - mt_prst_dc_uc_net
     - Float64
     - Montant de prestations décès, nettes de chargements
   * - 
     - mt_prst_dc_uc_chgt
     - Float64
     - Montant de chargements sur les prestations décès
   * - 
     - mt_prst_rt_uc_brt
     - Float64
     - Montant de prestations rachat, brutes de chargements
   * - 
     - mt_prst_rt_uc_net
     - Float64
     - Montant de prestations rachat, nettes de chargements
   * - 
     - mt_prst_rt_uc_chgt
     - Float64
     - Montant de chargements sur les prestations rachats
   * - 
     - mt_ic_eu_rest
     - Float64
     - Montant d'intérêts crédités des contrats Euro encore en cours à la fin de l'année
   * - 
     - mt_ic_eu_sort
     - Float64
     - Montant d'intérêts crédités des contrats Euro sortis en cours d'année
   * - 
     - mt_ic_uc_rest
     - Float64
     - Montant d'intérêts crédités des contrats UC encore en cours à la fin de l'année
   * - 
     - mt_ic_uc_sort
     - Float64
     - Montant d'intérêts crédités des contrats UC sortis en cours d'année
   * - 
     - mt_fgse_uc
     - Float64
     - Montant de frais de gestion sur encours
   * - 
     - mt_fgse_eu
     - Float64
     - Montant de la marge financière assuré issue des TFGSE
   * - 
     - mt_fgx_prst_eu
     - Float64
     - Montant de frais généraux sur prestations
   * - 
     - mt_fgx_pm_eu
     - Float64
     - Montant de frais généraux sur PM
   * - 
     - mt_fgx_prst_uc
     - Float64
     - Montant de frais généraux sur prestations
   * - 
     - mt_fgx_pm_uc
     - Float64
     - Montant de frais généraux sur PM
.. raw:: html

   <a id="MpPassifEpProjAlmCr"></a>

MpPassifEpProjAlmCr
^^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 3 25 10 40
   :header-rows: 1
   :class: table-custom

   * - Pk
     - Variable
     - Type
     - Description
   * - :octicon:`key`
     - cd_choc_s2
     - Categorical
     - Choc Solvabilité 2
   * - :octicon:`key`
     - cd_choc_s2_gse
     - Categorical
     - Choc Solvabilité 2 applicable aux variables économiques
   * - :octicon:`key`
     - cd_choc_s2_passif_prst
     - Categorical
     - Choc Solvabilité 2 applicable aux hypothèses de prestations
   * - :octicon:`key`
     - cd_choc_s2_passif_ic_fgx
     - Categorical
     - Choc Solvabilité 2 applicable à la table PassifHypsIcFgx
   * - :octicon:`key`
     - scenario
     - Int32
     - Identifiant du scenario
   * - :octicon:`key`
     - period
     - Int32
     - Identifiant du pas de temps
   * - :octicon:`key`
     - evenement
     - Categorical
     - Année de projection
   * - :octicon:`key`
     - cd_societe
     - String
     - Code société
   * - :octicon:`key`
     - cd_canton
     - String
     - Code Canton
   * - :octicon:`key`
     - cd_prtf_ifrs17
     - Categorical
     - Code Portefeuille Ifrs17
   * - :octicon:`key`
     - cd_fampdt
     - Categorical
     - Code Famille de produit
   * - :octicon:`key`
     - cd_cnt
     - Int32
     - Identifiant d'un contrat
   * - 
     - nb_cnt
     - Float64
     - Nombre de contrats
   * - 
     - cd_asse_sexe
     - String
     - Sexe de l'assuré
   * - 
     - dt_asse_naiss
     - Date
     - Date de naissance de l'assuré
   * - 
     - dt_cnt_effet
     - Date
     - Date d'effet du contrat
   * - 
     - mt_pm_eu
     - Float64
     - Montant de la PM
   * - 
     - cd_hrg_eu
     - Int32
     - HRG associé au support euro
   * - 
     - mt_pm_uc
     - Float64
     - Montant de la PM
   * - 
     - cd_hrg_uc
     - Int32
     - HRG associé au support uc
   * - 
     - cd_prst_rt_cat
     - Int16
     - Catégorie de prestation rachat
   * - 
     - cd_capitalisation
     - Enum(categories=['capi', 'ncapi'])
     - Contrat de capitalisation
   * - 
     - tmg
     - Float64
     - Taux minimum garanti
   * - 
     - tmg_type
     - Enum(categories=['net', 'brut'])
     - Taux minimum garanti
   * - 
     - taf
     - Float64
     - Taux d'affectation des produits financiers
   * - 
     - tfgse
     - Float64
     - Taux de frais de gestion sur encours euro
   * - 
     - tfgse_uc
     - Float64
     - Taux de frais de gestion sur encours UC
   * - 
     - cd_hyp_mort_exp
     - String
     - Table de mortalite d'expérience à appliquer
   * - 
     - cd_hyp_mort_prov
     - String
     - Table de mortalite utilisée pour le provisionnement
   * - 
     - tx_prst_chgt
     - Float64
     - Taux de chargement sur les prestations
   * - 
     - tx_action_t1
     - Float64
     - Part de l'actif unitaire à choquer sous S2 avec le choc Action de Type 1
   * - 
     - tx_action_t2
     - Float64
     - Part de l'actif unitaire à choquer sous S2 avec le choc Action de Type 2
   * - 
     - tx_action_strat
     - Float64
     - Part de l'actif unitaire à choquer sous S2 avec le choc Action Stratégique
   * - 
     - tx_immobilier
     - Float64
     - Part de l'actif unitaire à choquer sous S2 avec le choc immobilier
   * - 
     - nb_asse_age_annee
     - Int32
     - Age de l'assuré en années
   * - 
     - nb_asse_age_mois
     - Int32
     - Age de l'assuré en années
   * - 
     - nb_cnt_anciennete_annee
     - Int32
     - Ancienneté du contrat en année
   * - 
     - nb_cnt_anciennete_mois
     - Int32
     - Ancienneté du contrat en mois
   * - 
     - tmg_brt
     - Float64
     - Taux minimum garanti, brut de taf et tfgse
   * - 
     - generation
     - Int32
     - Année de naissance d'une génération donnée
   * - 
     - mt_pm_eu_av
     - Float64
     - Montant de la PM (avant évènement)
   * - 
     - mt_pm_uc_av
     - Float64
     - Montant de la PM (avant évènement)
   * - 
     - nb_cnt_av
     - Float64
     - Nombre de contrats (avant évènement)
   * - 
     - mt_pb_brt
     - Float64
     - Montant de PB brut de CSG
   * - 
     - mt_pb_net
     - Float64
     - Montant de PB net de CSG
   * - 
     - mt_csg
     - Float64
     - Montant de CSG
.. raw:: html

   <a id="AlmCrAlmOutputPassif"></a>

AlmCrAlmOutputPassif
^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 3 25 10 40
   :header-rows: 1
   :class: table-custom

   * - Pk
     - Variable
     - Type
     - Description
   * - :octicon:`key`
     - cd_choc_s2
     - Categorical
     - Choc Solvabilité 2
   * - :octicon:`key`
     - scenario
     - Int32
     - Identifiant du scenario
   * - :octicon:`key`
     - period
     - Int32
     - Identifiant du pas de temps
   * - :octicon:`key`
     - cd_societe
     - String
     - Code société
   * - :octicon:`key`
     - cd_canton
     - String
     - Code Canton
   * - :octicon:`key`
     - cd_prtf_ifrs17
     - Categorical
     - Code Portefeuille Ifrs17
   * - :octicon:`key`
     - cd_fampdt
     - Categorical
     - Code Famille de produit
   * - :octicon:`key`
     - cd_cnt
     - Int32
     - Identifiant d'un contrat
   * - :octicon:`key`
     - strat_alm_cas
     - String
     - Cas possibles pour la stratégie ALM (chaine de caractères)
   * - 
     - tx_servi_brt
     - Float64
     - Taux servi brut
   * - 
     - tx_servi_net
     - Float64
     - Taux servi net
   * - 
     - mt_pb_ass
     - Float64
     - Assiette utilisée pour le calcul de la PB
   * - 
     - mt_pb_brt
     - Float64
     - Montant de PB brut de CSG
   * - 
     - mt_csg
     - Float64
     - Montant de CSG
   * - 
     - mt_pb_net
     - Float64
     - Montant de PB net de CSG
.. raw:: html

   <a id="PrdAdPassifEp"></a>

PrdAdPassifEp
^^^^^^^^^^^^^

.. list-table::
   :widths: 3 25 10 40
   :header-rows: 1
   :class: table-custom

   * - Pk
     - Variable
     - Type
     - Description
   * - :octicon:`key`
     - cd_choc_s2
     - Categorical
     - Choc Solvabilité 2
   * - :octicon:`key`
     - scenario
     - Int32
     - Identifiant du scenario
   * - :octicon:`key`
     - period
     - Int32
     - Identifiant du pas de temps
   * - :octicon:`key`
     - evenement
     - Categorical
     - Année de projection
   * - :octicon:`key`
     - cd_societe
     - String
     - Code société
   * - :octicon:`key`
     - cd_canton
     - String
     - Code Canton
   * - :octicon:`key`
     - cd_fampdt
     - Categorical
     - Code Famille de produit
   * - 
     - nb_cnt
     - Float64
     - Nombre de contrats
   * - 
     - cd_asse_sexe
     - String
     - Sexe de l'assuré
   * - 
     - dt_asse_naiss
     - Date
     - Date de naissance de l'assuré
   * - 
     - dt_cnt_effet
     - Date
     - Date d'effet du contrat
   * - 
     - mt_pm_eu
     - Float64
     - Montant de la PM
   * - 
     - cd_hrg_eu
     - Int32
     - HRG associé au support euro
   * - 
     - mt_pm_uc
     - Float64
     - Montant de la PM
   * - 
     - cd_hrg_uc
     - Int32
     - HRG associé au support uc
   * - 
     - cd_prst_rt_cat
     - Int16
     - Catégorie de prestation rachat
   * - 
     - cd_capitalisation
     - Enum(categories=['capi', 'ncapi'])
     - Contrat de capitalisation
   * - 
     - tmg
     - Float64
     - Taux minimum garanti
   * - 
     - tmg_type
     - Enum(categories=['net', 'brut'])
     - Taux minimum garanti
   * - 
     - taf
     - Float64
     - Taux d'affectation des produits financiers
   * - 
     - tfgse
     - Float64
     - Taux de frais de gestion sur encours euro
   * - 
     - tfgse_uc
     - Float64
     - Taux de frais de gestion sur encours UC
   * - 
     - cd_hyp_mort_exp
     - String
     - Table de mortalite d'expérience à appliquer
   * - 
     - cd_hyp_mort_prov
     - String
     - Table de mortalite utilisée pour le provisionnement
   * - 
     - tx_prst_chgt
     - Float64
     - Taux de chargement sur les prestations
   * - 
     - tx_action_t1
     - Float64
     - Part de l'actif unitaire à choquer sous S2 avec le choc Action de Type 1
   * - 
     - tx_action_t2
     - Float64
     - Part de l'actif unitaire à choquer sous S2 avec le choc Action de Type 2
   * - 
     - tx_action_strat
     - Float64
     - Part de l'actif unitaire à choquer sous S2 avec le choc Action Stratégique
   * - 
     - tx_immobilier
     - Float64
     - Part de l'actif unitaire à choquer sous S2 avec le choc immobilier
   * - 
     - nb_asse_age_annee
     - Int32
     - Age de l'assuré en années
   * - 
     - nb_asse_age_mois
     - Int32
     - Age de l'assuré en années
   * - 
     - nb_cnt_anciennete_annee
     - Int32
     - Ancienneté du contrat en année
   * - 
     - nb_cnt_anciennete_mois
     - Int32
     - Ancienneté du contrat en mois
   * - 
     - tmg_brt
     - Float64
     - Taux minimum garanti, brut de taf et tfgse
   * - 
     - generation
     - Int32
     - Année de naissance d'une génération donnée
   * - 
     - mt_pm_eu_av
     - Float64
     - Montant de la PM (avant évènement)
   * - 
     - mt_pm_uc_av
     - Float64
     - Montant de la PM (avant évènement)
   * - 
     - nb_cnt_av
     - Float64
     - Nombre de contrats (avant évènement)
   * - 
     - mt_prst_tot_eu_brt
     - Float64
     - Montant de prestations totales, brutes de chargements
   * - 
     - mt_prst_tot_eu_net
     - Float64
     - Montant de prestations totales, nettes de chargements
   * - 
     - mt_prst_tot_eu_chgt
     - Float64
     - Montant de chargements sur l'ensemble des prestations
   * - 
     - mt_prst_dc_eu_brt
     - Float64
     - Montant de prestations décès, brutes de chargements
   * - 
     - mt_prst_dc_eu_net
     - Float64
     - Montant de prestations décès, nettes de chargements
   * - 
     - mt_prst_dc_eu_chgt
     - Float64
     - Montant de chargements sur les prestations décès
   * - 
     - mt_prst_rt_eu_brt
     - Float64
     - Montant de prestations rachat, brutes de chargements
   * - 
     - mt_prst_rt_eu_net
     - Float64
     - Montant de prestations rachat, nettes de chargements
   * - 
     - mt_prst_rt_eu_chgt
     - Float64
     - Montant de chargements sur les prestations rachats
   * - 
     - mt_prst_tot_uc_brt
     - Float64
     - Montant de prestations totales, brutes de chargements
   * - 
     - mt_prst_tot_uc_net
     - Float64
     - Montant de prestations totales, nettes de chargements
   * - 
     - mt_prst_tot_uc_chgt
     - Float64
     - Montant de chargements sur l'ensemble des prestations
   * - 
     - mt_prst_dc_uc_brt
     - Float64
     - Montant de prestations décès, brutes de chargements
   * - 
     - mt_prst_dc_uc_net
     - Float64
     - Montant de prestations décès, nettes de chargements
   * - 
     - mt_prst_dc_uc_chgt
     - Float64
     - Montant de chargements sur les prestations décès
   * - 
     - mt_prst_rt_uc_brt
     - Float64
     - Montant de prestations rachat, brutes de chargements
   * - 
     - mt_prst_rt_uc_net
     - Float64
     - Montant de prestations rachat, nettes de chargements
   * - 
     - mt_prst_rt_uc_chgt
     - Float64
     - Montant de chargements sur les prestations rachats
   * - 
     - mt_ic_eu_rest
     - Float64
     - Montant d'intérêts crédités des contrats Euro encore en cours à la fin de l'année
   * - 
     - mt_ic_eu_sort
     - Float64
     - Montant d'intérêts crédités des contrats Euro sortis en cours d'année
   * - 
     - mt_ic_uc_rest
     - Float64
     - Montant d'intérêts crédités des contrats UC encore en cours à la fin de l'année
   * - 
     - mt_ic_uc_sort
     - Float64
     - Montant d'intérêts crédités des contrats UC sortis en cours d'année
   * - 
     - mt_fgse_uc
     - Float64
     - Montant de frais de gestion sur encours
   * - 
     - mt_fgse_eu
     - Float64
     - Montant de la marge financière assuré issue des TFGSE
   * - 
     - mt_fgx_prst_eu
     - Float64
     - Montant de frais généraux sur prestations
   * - 
     - mt_fgx_pm_eu
     - Float64
     - Montant de frais généraux sur PM
   * - 
     - mt_fgx_prst_uc
     - Float64
     - Montant de frais généraux sur prestations
   * - 
     - mt_fgx_pm_uc
     - Float64
     - Montant de frais généraux sur PM
   * - 
     - mt_pb_brt
     - Float64
     - Montant de PB brut de CSG
   * - 
     - mt_pb_net
     - Float64
     - Montant de PB net de CSG
   * - 
     - mt_csg
     - Float64
     - Montant de CSG



Alm
---


Solvablité 2
------------

.. raw:: html

   <a id="DfCdChocS2"></a>

DfCdChocS2
^^^^^^^^^^

.. list-table::
   :widths: 3 25 10 40
   :header-rows: 1
   :class: table-custom

   * - Pk
     - Variable
     - Type
     - Description
   * - :octicon:`key`
     - cd_choc_s2
     - Categorical
     - Choc Solvabilité 2
   * - 
     - cd_choc_s2_gse
     - Categorical
     - Choc Solvabilité 2 applicable aux variables économiques
   * - 
     - cd_choc_s2_passif_prst
     - Categorical
     - Choc Solvabilité 2 applicable aux hypothèses de prestations
   * - 
     - cd_choc_s2_passif_ic_fgx
     - Categorical
     - Choc Solvabilité 2 applicable à la table PassifHypsIcFgx
.. raw:: html

   <a id="DfCdChocS2Sc"></a>

DfCdChocS2Sc
^^^^^^^^^^^^

.. list-table::
   :widths: 3 25 10 40
   :header-rows: 1
   :class: table-custom

   * - Pk
     - Variable
     - Type
     - Description
   * - :octicon:`key`
     - cd_choc_s2
     - Categorical
     - Choc Solvabilité 2
   * - :octicon:`key`
     - scenario
     - Int32
     - Identifiant du scenario
   * - 
     - cd_choc_s2_gse
     - Categorical
     - Choc Solvabilité 2 applicable aux variables économiques
   * - 
     - cd_choc_s2_passif_prst
     - Categorical
     - Choc Solvabilité 2 applicable aux hypothèses de prestations
   * - 
     - cd_choc_s2_passif_ic_fgx
     - Categorical
     - Choc Solvabilité 2 applicable à la table PassifHypsIcFgx
.. raw:: html

   <a id="HypS2Chocs"></a>

HypS2Chocs
^^^^^^^^^^

.. list-table::
   :widths: 3 25 10 40
   :header-rows: 1
   :class: table-custom

   * - Pk
     - Variable
     - Type
     - Description
   * - :octicon:`key`
     - cd_choc_s2
     - Categorical
     - Choc Solvabilité 2
   * - 
     - tx_choc_mort
     - Float64
     - Choc Solvabilité 2 associé à la mortalité
   * - 
     - tx_choc_longevity
     - Float64
     - Choc Solvabilité 2 longévité
   * - 
     - tx_choc_expense
     - Float64
     - Choc Solvabilité 2 associé aux frais généraux
   * - 
     - tx_choc_expense_inflation
     - Float64
     - Choc Solvabilité 2 associé à l'inflation des frais généraux
   * - 
     - tx_choc_mort_cat
     - Float64
     - Choc Solvabilité 2 mortalité catastrophe
   * - 
     - tx_choc_lapse
     - Float64
     - Choc Solvabilité 2 rachat
   * - 
     - tx_choc_lapse_mass
     - Float64
     - Choc Solvabilité 2 rachat masse
   * - 
     - tx_choc_equity_t1
     - Float64
     - Choc Solvabilité 2 action de type 1
   * - 
     - tx_choc_equity_t2
     - Float64
     - Choc Solvabilité 2 action de type 2
   * - 
     - tx_choc_equity_strat
     - Float64
     - Choc Solvabilité 2 action stratégique
   * - 
     - tx_choc_property
     - Float64
     - Choc Solvabilité 2 immobilier
   * - 
     - tx_choc_revision
     - Float64
     - Choc Solvabilité 2 révision
   * - 
     - tx_choc_inval
     - Float64
     - Choc Solvabilité 2 invalidité
.. raw:: html

   <a id="HypS2ChocsInit"></a>

HypS2ChocsInit
^^^^^^^^^^^^^^

.. list-table::
   :widths: 3 25 10 40
   :header-rows: 1
   :class: table-custom

   * - Pk
     - Variable
     - Type
     - Description
   * - :octicon:`key`
     - cd_choc_s2
     - Categorical
     - Choc Solvabilité 2
   * - 
     - cd_choc_s2_gse
     - Categorical
     - Choc Solvabilité 2 applicable aux variables économiques
   * - 
     - cd_choc_s2_passif_ic_fgx
     - Categorical
     - Choc Solvabilité 2 applicable à la table PassifHypsIcFgx
   * - 
     - cd_choc_s2_passif_prst
     - Categorical
     - Choc Solvabilité 2 applicable aux hypothèses de prestations
   * - 
     - tx_choc_mort
     - Float64
     - Choc Solvabilité 2 associé à la mortalité
   * - 
     - tx_choc_longevity
     - Float64
     - Choc Solvabilité 2 longévité
   * - 
     - tx_choc_expense
     - Float64
     - Choc Solvabilité 2 associé aux frais généraux
   * - 
     - tx_choc_expense_inflation
     - Float64
     - Choc Solvabilité 2 associé à l'inflation des frais généraux
   * - 
     - tx_choc_mort_cat
     - Float64
     - Choc Solvabilité 2 mortalité catastrophe
   * - 
     - tx_choc_lapse
     - Float64
     - Choc Solvabilité 2 rachat
   * - 
     - tx_choc_lapse_mass
     - Float64
     - Choc Solvabilité 2 rachat masse
   * - 
     - tx_choc_equity_t1
     - Float64
     - Choc Solvabilité 2 action de type 1
   * - 
     - tx_choc_equity_t2
     - Float64
     - Choc Solvabilité 2 action de type 2
   * - 
     - tx_choc_equity_strat
     - Float64
     - Choc Solvabilité 2 action stratégique
   * - 
     - tx_choc_property
     - Float64
     - Choc Solvabilité 2 immobilier
   * - 
     - tx_choc_revision
     - Float64
     - Choc Solvabilité 2 révision
   * - 
     - tx_choc_inval
     - Float64
     - Choc Solvabilité 2 invalidité
.. raw:: html

   <a id="HypS2ChocsSpread"></a>

HypS2ChocsSpread
^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 3 25 10 40
   :header-rows: 1
   :class: table-custom

   * - Pk
     - Variable
     - Type
     - Description
   * - :octicon:`key`
     - cd_classe_actif_detail
     - String
     - Classe d'actif détaillée
   * - :octicon:`key`
     - nb_duration_min
     - Int32
     - Borne minimum de duration pour l'application du choc spread
   * - :octicon:`key`
     - nb_duration_max
     - Int32
     - Borne maximum de duration pour l'application du choc spread
   * - :octicon:`key`
     - cd_cqs
     - Int32
     - Credit Default Step de l'actif
   * - 
     - tx_choc_spread_a
     - Float64
     - Choc Solvabilité 2 spread A
   * - 
     - tx_choc_spread_b
     - Float64
     - Choc Solvabilité 2 spread B


