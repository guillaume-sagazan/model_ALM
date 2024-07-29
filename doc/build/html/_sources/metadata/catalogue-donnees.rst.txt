Catalogue des données
=====================

Projection
----------

.. raw:: html

   <a id="cd_trajectoire"></a>

   <a id="dt_trajectoire"></a>

   <a id="dt_trajectoire_annee"></a>

   <a id="scenario"></a>

   <a id="period"></a>

   <a id="proj_annee"></a>

   <a id="evenement"></a>

   <a id="intraperiod"></a>

   <a id="proj_date_debut"></a>

.. list-table::
   :widths: 20 10 30
   :header-rows: 1
   :class: table-custom

   * - Variable
     - Type
     - Description
   * -  cd_trajectoire
     - String
     - Trajectoire

   * -  dt_trajectoire
     - Date
     - Trajectoire

   * -  dt_trajectoire_annee
     - Int32
     - Trajectoire Année

   * -  scenario
     - Int32
     - Identifiant du scenario

   * -  period
     - Int32
     - Identifiant du pas de temps

   * -  proj_annee
     - Int32
     - Année de projection

   * -  evenement
     - Categorical
     - Année de projection

   * -  intraperiod
     - String
     - Pour un cash flow donné, tombe t il en début, milieu

   * -  proj_date_debut
     - Date
     - Date de début de la projection


Données communes
----------------

.. raw:: html

   <a id="cd_table"></a>

   <a id="cd_societe"></a>

   <a id="cd_canton"></a>

   <a id="facteur"></a>

   <a id="dt_date_terme"></a>

   <a id="dt_date_terme_annee"></a>

   <a id="erreur"></a>

   <a id="type_erreur"></a>

   <a id="type_erreur_action"></a>

.. list-table::
   :widths: 20 10 30
   :header-rows: 1
   :class: table-custom

   * - Variable
     - Type
     - Description
   * -  cd_table
     - String
     - Nom de la table d'hypothèse

   * -  cd_societe
     - String
     - Code société

   * -  cd_canton
     - String
     - Code Canton

   * -  facteur
     - Float64
     - Facteur

   * -  dt_date_terme
     - Date
     - Date de terme

   * -  dt_date_terme_annee
     - Int64
     - Année associée à la date de terme

   * -  erreur
     - String
     - Description de l'erreur

   * -  type_erreur
     - String
     - Type d'erreur

   * -  type_erreur_action
     - String
     - Type d'action réalisée compte tenu de l'erreur


Variables économiques (GSE)
---------------------------

.. raw:: html

   <a id="cd_ct_ref"></a>

   <a id="facteur_perf_tot"></a>

   <a id="facteur_perf_net"></a>

   <a id="deflateur"></a>

   <a id="tx_dividendes"></a>

   <a id="pzc"></a>

   <a id="tzc"></a>

   <a id="tx_inflation"></a>

   <a id="facteur_inflation_cum"></a>

   <a id="tx_perf_tot"></a>

.. list-table::
   :widths: 20 10 30
   :header-rows: 1
   :class: table-custom

   * - Variable
     - Type
     - Description
   * -  cd_ct_ref
     - String
     - Facteur de performance total

   * -  facteur_perf_tot
     - Float64
     - Facteur d'inflation cummulé

   * -  facteur_perf_net
     - Float64
     - Facteur de performance net

   * -  deflateur
     - Float64
     - Deflateur

   * -  tx_dividendes
     - Float64
     - Taux de dividendes

   * -  pzc
     - Float64
     - Prix zéro coupon

   * -  tzc
     - Float64
     - Taux dans le cadre du scenario CENTRAL

   * -  tx_inflation
     - Float64
     - Taux d'inflation

   * -  facteur_inflation_cum
     - Float64
     - Facteur d'inflation cummulée

   * -  tx_perf_tot
     - Float64
     - Taux de performance total


Actif
-----

.. raw:: html

   <a id="maturite"></a>

   <a id="cd_classe_actif"></a>

   <a id="cd_classe_actif_detail"></a>

   <a id="cd_cqs"></a>

   <a id="cd_isin"></a>

   <a id="nb_period_terme"></a>

   <a id="mt_nominal"></a>

   <a id="tx_cpn"></a>

   <a id="tx_remboursement"></a>

   <a id="nb_duration"></a>

   <a id="mt_vm_av"></a>

   <a id="mt_vm"></a>

   <a id="mt_vc_av"></a>

   <a id="mt_vc"></a>

   <a id="mt_pmvl"></a>

   <a id="mt_pmvr"></a>

   <a id="mt_pfi"></a>

   <a id="mt_cf"></a>

   <a id="tx_action_t1"></a>

   <a id="tx_action_t2"></a>

   <a id="tx_action_strat"></a>

   <a id="tx_immobilier"></a>

   <a id="mt_pdd_av"></a>

   <a id="mt_pdd"></a>

   <a id="mt_pre_av"></a>

   <a id="mt_pre"></a>

   <a id="mt_vm_rn"></a>

   <a id="tx_vm_rn"></a>

   <a id="tx_tra"></a>

   <a id="tx_tra_min"></a>

   <a id="tx_tra_max"></a>

   <a id="mt_vc_tra"></a>

   <a id="mt_vc_tra_min"></a>

   <a id="mt_vc_tra_max"></a>

   <a id="mt_vc_tra_error"></a>

.. list-table::
   :widths: 20 10 30
   :header-rows: 1
   :class: table-custom

   * - Variable
     - Type
     - Description
   * -  maturite
     - Int32
     - Maturité en années d'un cashflow futur

   * -  cd_classe_actif
     - String
     - Classe d'actif

   * -  cd_classe_actif_detail
     - String
     - Classe d'actif détaillée

   * -  cd_cqs
     - Int32
     - Credit Default Step de l'actif

   * -  cd_isin
     - String
     - Identifiant du MP actif agrégé

   * -  nb_period_terme
     - Int32
     - Montant de cashflow

   * -  mt_nominal
     - Float64
     - Montant du nominal d'une obligation

   * -  tx_cpn
     - Float64
     - Taux de coupon d'une obligation

   * -  tx_remboursement
     - Float64
     - Taux de remboursement d'une obligation

   * -  nb_duration
     - Float64
     - Duration de l'actif

   * -  mt_vm_av
     - Float64
     - Valeur de marché (avant évènement)

   * -  mt_vm
     - Float64
     - Valeur de marché

   * -  mt_vc_av
     - Float64
     - Valeur comptable (avant évènement)

   * -  mt_vc
     - Float64
     - Valeur comptable

   * -  mt_pmvl
     - Float64
     - Plus ou moins values latentes disponibles

   * -  mt_pmvr
     - Float64
     - Plus ou moins values latentes générés lors de l'évènement

   * -  mt_pfi
     - Float64
     - Produits financier généré par l'évènement

   * -  mt_cf
     - Float64
     - Cashflow

   * -  tx_action_t1
     - Float64
     - Part de l'actif unitaire à choquer sous S2 avec le choc Action de Type 1

   * -  tx_action_t2
     - Float64
     - Part de l'actif unitaire à choquer sous S2 avec le choc Action de Type 2

   * -  tx_action_strat
     - Float64
     - Part de l'actif unitaire à choquer sous S2 avec le choc Action Stratégique

   * -  tx_immobilier
     - Float64
     - Part de l'actif unitaire à choquer sous S2 avec le choc immobilier

   * -  mt_pdd_av
     - Float64
     - Provision pour dépréciation durable (avant évènement)

   * -  mt_pdd
     - Float64
     - Provision pour dépréciation durable

   * -  mt_pre_av
     - Float64
     - Provision pour risque d'éligibilité (avant évènement)

   * -  mt_pre
     - Float64
     - Provision pour risque d'éligibilité

   * -  mt_vm_rn
     - Float64
     - Valeur de marché post risque neutralisation

   * -  tx_vm_rn
     - Float64
     - Facteur à appliquer pour risque neutraliser une obligation

   * -  tx_tra
     - Float64
     - Dernier TRA  considéré pour équilibrer la valeur comptable

   * -  tx_tra_min
     - Float64
     - TRA min considéré pour équilibrer la valeur comptable

   * -  tx_tra_max
     - Float64
     - TRA max considéré pour équilibrer la valeur comptable

   * -  mt_vc_tra
     - Float64
     - Valeur comptable calculée avec le dernier TRA considéré

   * -  mt_vc_tra_min
     - Float64
     - Valeur comptable calculée avec le TRA min

   * -  mt_vc_tra_max
     - Float64
     - Valeur comptable calculée avec le TRA max

   * -  mt_vc_tra_error
     - Float64
     - Erreur constatée sur le calcul de la valeur comptable avec le dernier TRA considéré


Passif
------

.. raw:: html

   <a id="cd_fampdt"></a>

   <a id="cd_cnt"></a>

   <a id="dt_cnt_effet"></a>

   <a id="dt_cnt_terme"></a>

   <a id="nb_cnt_av"></a>

   <a id="nb_cnt"></a>

   <a id="cd_prst_rt_cat"></a>

   <a id="cd_capitalisation"></a>

   <a id="cd_cnt_support_type"></a>

   <a id="cd_hyp_mort_exp"></a>

   <a id="cd_hyp_mort_prov"></a>

   <a id="sexe"></a>

   <a id="age"></a>

   <a id="cd_asse_sexe"></a>

   <a id="dt_asse_naiss"></a>

   <a id="nb_asse_age_annee"></a>

   <a id="nb_asse_age_mois"></a>

   <a id="tx_prst_rt"></a>

   <a id="tx_prst_chgt"></a>

   <a id="tx_prst_dc_asse_exp"></a>

   <a id="taf"></a>

   <a id="tfgse"></a>

   <a id="tfgse_uc"></a>

   <a id="tmg"></a>

   <a id="tmg_type"></a>

   <a id="tmg_brt"></a>

   <a id="tx_ic_eu"></a>

   <a id="tx_ic_uc"></a>

   <a id="tx_ic_eu_brt"></a>

   <a id="tx_ic_eu_demi_periode"></a>

   <a id="tx_ic_uc_demi_periode"></a>

   <a id="tx_ic_eu_brt_demi_periode"></a>

   <a id="facteur_actu_tx_tech"></a>

   <a id="cd_hrg_eu"></a>

   <a id="mt_pm_eu_av"></a>

   <a id="mt_pm_eu"></a>

   <a id="mt_prst_tot_eu_brt"></a>

   <a id="mt_prst_tot_eu_net"></a>

   <a id="mt_prst_tot_eu_chgt"></a>

   <a id="mt_prst_dc_eu_brt"></a>

   <a id="mt_prst_dc_eu_net"></a>

   <a id="mt_prst_dc_eu_chgt"></a>

   <a id="mt_prst_rt_eu_brt"></a>

   <a id="mt_prst_rt_eu_net"></a>

   <a id="mt_prst_rt_eu_chgt"></a>

   <a id="cd_hrg_uc"></a>

   <a id="mt_pm_uc_av"></a>

   <a id="mt_pm_uc"></a>

   <a id="mt_prst_tot_uc_brt"></a>

   <a id="mt_prst_tot_uc_net"></a>

   <a id="mt_prst_tot_uc_chgt"></a>

   <a id="mt_prst_dc_uc_brt"></a>

   <a id="mt_prst_dc_uc_net"></a>

   <a id="mt_prst_dc_uc_chgt"></a>

   <a id="mt_prst_rt_uc_brt"></a>

   <a id="mt_prst_rt_uc_net"></a>

   <a id="mt_prst_rt_uc_chgt"></a>

   <a id="mt_ic_eu_rest"></a>

   <a id="mt_ic_uc_rest"></a>

   <a id="mt_ic_eu_sort"></a>

   <a id="mt_ic_uc_sort"></a>

   <a id="mt_fgse_uc"></a>

   <a id="mt_fgse_eu"></a>

   <a id="mt_pb_ass"></a>

   <a id="mt_pb_brt"></a>

   <a id="mt_pb_brt_cg"></a>

   <a id="mt_pb_net"></a>

   <a id="mt_csg"></a>

   <a id="nb_cnt_anciennete_annee"></a>

   <a id="nb_cnt_anciennete_mois"></a>

   <a id="generation"></a>

   <a id="qx"></a>

.. list-table::
   :widths: 20 10 30
   :header-rows: 1
   :class: table-custom

   * - Variable
     - Type
     - Description
   * -  cd_fampdt
     - Categorical
     - Code Famille de produit

   * -  cd_cnt
     - Int32
     - Identifiant d'un contrat

   * -  dt_cnt_effet
     - Date
     - Date d'effet du contrat

   * -  dt_cnt_terme
     - Date
     - Date de terme du contrat

   * -  nb_cnt_av
     - Float64
     - Nombre de contrats (avant évènement)

   * -  nb_cnt
     - Float64
     - Nombre de contrats

   * -  cd_prst_rt_cat
     - Int16
     - Catégorie de prestation rachat

   * -  cd_capitalisation
     - Enum(categories=['capi', 'ncapi'])
     - Contrat de capitalisation

   * -  cd_cnt_support_type
     - Enum(categories=['EU', 'UC'])
     - Type de support du contrat

   * -  cd_hyp_mort_exp
     - String
     - Table de mortalite d'expérience à appliquer

   * -  cd_hyp_mort_prov
     - String
     - Table de mortalite utilisée pour le provisionnement

   * -  sexe
     - String
     - Sexe

   * -  age
     - Int32
     - Age en années

   * -  cd_asse_sexe
     - String
     - Sexe de l'assuré

   * -  dt_asse_naiss
     - Date
     - Date de naissance de l'assuré

   * -  nb_asse_age_annee
     - Int32
     - Age de l'assuré en années

   * -  nb_asse_age_mois
     - Int32
     - Age de l'assuré en années

   * -  tx_prst_rt
     - Float64
     - Taux de prestation de rachat total

   * -  tx_prst_chgt
     - Float64
     - Taux de chargement sur les prestations

   * -  tx_prst_dc_asse_exp
     - Float64
     - Taux de prestation décès appliqué dans la diffusion du nombre d'assuré

   * -  taf
     - Float64
     - Taux d'affectation des produits financiers

   * -  tfgse
     - Float64
     - Taux de frais de gestion sur encours euro

   * -  tfgse_uc
     - Float64
     - Taux de frais de gestion sur encours UC

   * -  tmg
     - Float64
     - Taux minimum garanti

   * -  tmg_type
     - Enum(categories=['net', 'brut'])
     - Taux minimum garanti

   * -  tmg_brt
     - Float64
     - Taux minimum garanti, brut de taf et tfgse

   * -  tx_ic_eu
     - Float64
     - Taux d'intérêts crédités Euro

   * -  tx_ic_uc
     - Float64
     - Taux d'intérêts crédités UC

   * -  tx_ic_eu_brt
     - Float64
     - Taux d'intérêts crédités Euro brut de taf et tfgse

   * -  tx_ic_eu_demi_periode
     - Float64
     - Taux d'intérêts crédités Euro

   * -  tx_ic_uc_demi_periode
     - Float64
     - Taux d'intérêts crédités UC

   * -  tx_ic_eu_brt_demi_periode
     - Float64
     - Taux d'intérêts crédités Euro brut de taf et tfgse

   * -  facteur_actu_tx_tech
     - Float64
     - Facteur d'actualisation au taux technique

   * -  cd_hrg_eu
     - Int32
     - HRG associé au support euro

   * -  mt_pm_eu_av
     - Float64
     - Montant de la PM (avant évènement)

   * -  mt_pm_eu
     - Float64
     - Montant de la PM

   * -  mt_prst_tot_eu_brt
     - Float64
     - Montant de prestations totales, brutes de chargements

   * -  mt_prst_tot_eu_net
     - Float64
     - Montant de prestations totales, nettes de chargements

   * -  mt_prst_tot_eu_chgt
     - Float64
     - Montant de chargements sur l'ensemble des prestations

   * -  mt_prst_dc_eu_brt
     - Float64
     - Montant de prestations décès, brutes de chargements

   * -  mt_prst_dc_eu_net
     - Float64
     - Montant de prestations décès, nettes de chargements

   * -  mt_prst_dc_eu_chgt
     - Float64
     - Montant de chargements sur les prestations décès

   * -  mt_prst_rt_eu_brt
     - Float64
     - Montant de prestations rachat, brutes de chargements

   * -  mt_prst_rt_eu_net
     - Float64
     - Montant de prestations rachat, nettes de chargements

   * -  mt_prst_rt_eu_chgt
     - Float64
     - Montant de chargements sur les prestations rachats

   * -  cd_hrg_uc
     - Int32
     - HRG associé au support uc

   * -  mt_pm_uc_av
     - Float64
     - Montant de la PM (avant évènement)

   * -  mt_pm_uc
     - Float64
     - Montant de la PM

   * -  mt_prst_tot_uc_brt
     - Float64
     - Montant de prestations totales, brutes de chargements

   * -  mt_prst_tot_uc_net
     - Float64
     - Montant de prestations totales, nettes de chargements

   * -  mt_prst_tot_uc_chgt
     - Float64
     - Montant de chargements sur l'ensemble des prestations

   * -  mt_prst_dc_uc_brt
     - Float64
     - Montant de prestations décès, brutes de chargements

   * -  mt_prst_dc_uc_net
     - Float64
     - Montant de prestations décès, nettes de chargements

   * -  mt_prst_dc_uc_chgt
     - Float64
     - Montant de chargements sur les prestations décès

   * -  mt_prst_rt_uc_brt
     - Float64
     - Montant de prestations rachat, brutes de chargements

   * -  mt_prst_rt_uc_net
     - Float64
     - Montant de prestations rachat, nettes de chargements

   * -  mt_prst_rt_uc_chgt
     - Float64
     - Montant de chargements sur les prestations rachats

   * -  mt_ic_eu_rest
     - Float64
     - Montant d'intérêts crédités des contrats Euro encore en cours à la fin de l'année

   * -  mt_ic_uc_rest
     - Float64
     - Montant d'intérêts crédités des contrats UC encore en cours à la fin de l'année

   * -  mt_ic_eu_sort
     - Float64
     - Montant d'intérêts crédités des contrats Euro sortis en cours d'année

   * -  mt_ic_uc_sort
     - Float64
     - Montant d'intérêts crédités des contrats UC sortis en cours d'année

   * -  mt_fgse_uc
     - Float64
     - Montant de frais de gestion sur encours

   * -  mt_fgse_eu
     - Float64
     - Montant de la marge financière assuré issue des TFGSE

   * -  mt_pb_ass
     - Float64
     - Assiette utilisée pour le calcul de la PB

   * -  mt_pb_brt
     - Float64
     - Montant de PB brut de CSG

   * -  mt_pb_brt_cg
     - Float64
     - Montant de PB brut post application des TAF et TFGSE

   * -  mt_pb_net
     - Float64
     - Montant de PB net de CSG

   * -  mt_csg
     - Float64
     - Montant de CSG

   * -  nb_cnt_anciennete_annee
     - Int32
     - Ancienneté du contrat en année

   * -  nb_cnt_anciennete_mois
     - Int32
     - Ancienneté du contrat en mois

   * -  generation
     - Int32
     - Année de naissance d'une génération donnée

   * -  qx
     - Float64
     - Taux de mortalité


Frais généraux
--------------

.. raw:: html

   <a id="tx_fgx_prst_eu"></a>

   <a id="tx_fgx_plct_eu"></a>

   <a id="tx_fgx_pm_eu"></a>

   <a id="mt_fgx_tot_eu"></a>

   <a id="mt_fgx_prst_eu"></a>

   <a id="mt_fgx_pm_eu"></a>

   <a id="mt_fgx_plct_eu"></a>

   <a id="tx_fgx_prst_uc"></a>

   <a id="tx_fgx_plct_uc"></a>

   <a id="tx_fgx_pm_uc"></a>

   <a id="mt_fgx_tot_uc"></a>

   <a id="mt_fgx_prst_uc"></a>

   <a id="mt_fgx_pm_uc"></a>

   <a id="mt_fgx_plct_uc"></a>

.. list-table::
   :widths: 20 10 30
   :header-rows: 1
   :class: table-custom

   * - Variable
     - Type
     - Description
   * -  tx_fgx_prst_eu
     - Float64
     - Taux de frais généraux sur les prestations

   * -  tx_fgx_plct_eu
     - Float64
     - Taux de frais généraux sur les placements

   * -  tx_fgx_pm_eu
     - Float64
     - Taux de frais généraux sur les PM

   * -  mt_fgx_tot_eu
     - Float64
     - Montant de frais généraux totaux

   * -  mt_fgx_prst_eu
     - Float64
     - Montant de frais généraux sur prestations

   * -  mt_fgx_pm_eu
     - Float64
     - Montant de frais généraux sur PM

   * -  mt_fgx_plct_eu
     - Float64
     - Montant de frais généraux de placement

   * -  tx_fgx_prst_uc
     - Float64
     - Taux de frais généraux sur les prestations

   * -  tx_fgx_plct_uc
     - Float64
     - Taux de frais généraux sur les placements

   * -  tx_fgx_pm_uc
     - Float64
     - Taux de frais généraux sur les PM

   * -  mt_fgx_tot_uc
     - Float64
     - Montant de frais généraux totaux

   * -  mt_fgx_prst_uc
     - Float64
     - Montant de frais généraux sur prestations

   * -  mt_fgx_pm_uc
     - Float64
     - Montant de frais généraux sur PM

   * -  mt_fgx_plct_uc
     - Float64
     - Montant de frais généraux de placement


ALM
---

.. raw:: html

   <a id="nb_ppe_generation"></a>

   <a id="nb_ppe_generation_max"></a>

   <a id="strat_alm_cas"></a>

   <a id="strat_alm_cas_priorite"></a>

   <a id="strat_alm_cas_priorite_min"></a>

   <a id="tx_pb_min_regl_solde_fin"></a>

   <a id="tx_pb_min_regl_solde_tech"></a>

   <a id="cd_methode_tx_cible"></a>

   <a id="tx_cible_fixe"></a>

   <a id="tx_is"></a>

   <a id="tx_servi_brt"></a>

   <a id="tx_servi_net"></a>

   <a id="tx_tmg"></a>

   <a id="pente_pb_brt"></a>

   <a id="pente_pfi"></a>

   <a id="mt_pb_brt_min_regl"></a>

   <a id="mt_ic_rest_cum_sum"></a>

   <a id="mt_ic_rest_canton"></a>

   <a id="mt_ppe_av"></a>

   <a id="mt_ppe"></a>

   <a id="mt_pb_ass_canton"></a>

   <a id="mt_reserve_capi_av"></a>

   <a id="mt_reserve_capi"></a>

   <a id="mt_capitaux_propres_av"></a>

   <a id="mt_capitaux_propres"></a>

   <a id="cd_methode_pfi_cle_repart"></a>

   <a id="cd_type_canton"></a>

   <a id="mt_cash_init"></a>

   <a id="mt_pfi_init"></a>

   <a id="mt_pfi_besoin_tx_cible"></a>

   <a id="mt_pb_brt_besoin_tx_cible"></a>

   <a id="mt_ppe_delta"></a>

   <a id="mt_ppe_restante"></a>

   <a id="mt_ppe_reprise"></a>

   <a id="mt_ppe_dispo"></a>

   <a id="mt_ppe_dotation"></a>

   <a id="mt_ppe_cum_sum"></a>

   <a id="tx_pfi_asse_repart_pc"></a>

   <a id="mt_pfi_asse"></a>

   <a id="mt_pfi_asse_pb"></a>

   <a id="mt_pfi_assr"></a>

   <a id="mt_res_brt"></a>

   <a id="mt_res_brt_asse"></a>

   <a id="mt_res_is"></a>

   <a id="mt_res_net"></a>

   <a id="mt_fuite_eco"></a>

   <a id="mt_fuite_vc"></a>

   <a id="mt_fuite_vc_tmp"></a>

   <a id="mt_fuite_vc_eu"></a>

   <a id="mt_fuite_vc_uc"></a>

   <a id="mt_prov"></a>

.. list-table::
   :widths: 20 10 30
   :header-rows: 1
   :class: table-custom

   * - Variable
     - Type
     - Description
   * -  nb_ppe_generation
     - Int64
     - Génération de PPE

   * -  nb_ppe_generation_max
     - Int64
     - Génération de PPE maximum

   * -  strat_alm_cas
     - String
     - Cas possibles pour la stratégie ALM (chaine de caractères)

   * -  strat_alm_cas_priorite
     - Int64
     - Priorité donnée aux cas possibles pour la stratégie ALM (entier)

   * -  strat_alm_cas_priorite_min
     - Int64
     - Priorité minimum associé aux cas possibles pour la stratégie ALM (entier)

   * -  tx_pb_min_regl_solde_fin
     - Float64
     - Taux minimum règlementaire associé au partage du résultat financier

   * -  tx_pb_min_regl_solde_tech
     - Float64
     - Taux minimum règlementaire associé au partage du résultat technique

   * -  cd_methode_tx_cible
     - String
     - Méthode associé au calcul du taux cible

   * -  tx_cible_fixe
     - Float64
     - Taux servi cible

   * -  tx_is
     - Float64
     - Taux d'impôts sur les société

   * -  tx_servi_brt
     - Float64
     - Taux servi brut

   * -  tx_servi_net
     - Float64
     - Taux servi net

   * -  tx_tmg
     - Float64
     - Taux minimum garanti

   * -  pente_pb_brt
     - Float64
     - Pente de la courbe MtPbBrt=f(txServiBrt)

   * -  pente_pfi
     - Float64
     - Pente de la courbe MtPfi=f(txServiBrt)

   * -  mt_pb_brt_min_regl
     - Float64
     - Montant de PB minimum règlementaire

   * -  mt_ic_rest_cum_sum
     - Float64
     - Montant d'intérêts crédités total

   * -  mt_ic_rest_canton
     - Float64
     - Montant d'intérêts crédités restants au niveau canton

   * -  mt_ppe_av
     - Float64
     - Montant de PPB (avant évènement)

   * -  mt_ppe
     - Float64
     - Montant de PPB

   * -  mt_pb_ass_canton
     - Float64
     - Assiette servant au calcul de la PB (au niveau canton)

   * -  mt_reserve_capi_av
     - Float64
     - Montant de réserve de capitalisation (avant évènement)

   * -  mt_reserve_capi
     - Float64
     - Montant de réserve de capitalisation

   * -  mt_capitaux_propres_av
     - Float64
     - Montant de capitaux propres (avant évènement)

   * -  mt_capitaux_propres
     - Float64
     - Montant de capitaux propres

   * -  cd_methode_pfi_cle_repart
     - String
     - Indice de Gestion

   * -  cd_type_canton
     - String
     - Indice de Gestion

   * -  mt_cash_init
     - Float64
     - Montant de cash initial

   * -  mt_pfi_init
     - Float64
     - Produits financiers initiaux disponibles en input de l'algorithme ALM

   * -  mt_pfi_besoin_tx_cible
     - Float64
     - Besoin en pfi pour servir le taux cible

   * -  mt_pb_brt_besoin_tx_cible
     - Float64
     - Besoin en pb pour servir le taux cible

   * -  mt_ppe_delta
     - Float64
     - Delta de PPB

   * -  mt_ppe_restante
     - Float64
     - Montant de PPB restante

   * -  mt_ppe_reprise
     - Float64
     - Montant de la reprise de PPB

   * -  mt_ppe_dispo
     - Float64
     - Montant de la reprise de PPB complémentaire

   * -  mt_ppe_dotation
     - Float64
     - Montant de la dotation à la PPB

   * -  mt_ppe_cum_sum
     - Float64
     - Somme des générations de PPB pour un canton donné

   * -  tx_pfi_asse_repart_pc
     - Float64
     - Part des produits financiers du canton qui a vocation à être réparti en marge financière et PB

   * -  mt_pfi_asse
     - Float64
     - Montant des produits financiers assurés

   * -  mt_pfi_asse_pb
     - Float64
     - Montant des produits financiers assurés en input du compte de PB

   * -  mt_pfi_assr
     - Float64
     - Montant de la marge financière assureur

   * -  mt_res_brt
     - Float64
     - Montant de résultat brut

   * -  mt_res_brt_asse
     - Float64
     - Montant de résultat brut issu du compte de PB

   * -  mt_res_is
     - Float64
     - Impots sur les sociétés

   * -  mt_res_net
     - Float64
     - Montant de résultat net

   * -  mt_fuite_eco
     - Float64
     - Montant de la fuite économique

   * -  mt_fuite_vc
     - Float64
     - Montant de fuite de valeur comptable

   * -  mt_fuite_vc_tmp
     - Float64
     - Montant de fuite de valeur comptable (variable temporaire)

   * -  mt_fuite_vc_eu
     - Float64
     - Montant de fuite de valeur comptable en Euro

   * -  mt_fuite_vc_uc
     - Float64
     - Montant de fuite de valeur comptable en Uc

   * -  mt_prov
     - Float64
     - Montant de provision


Stratégie d'investissement
--------------------------

.. raw:: html

   <a id="tx_alloc_cible"></a>

   <a id="tx_oblig_achat_cpn"></a>

   <a id="nb_oblig_achat_maturite"></a>

   <a id="tx_frais_plct"></a>

   <a id="mt_vm_av_canton"></a>

   <a id="mt_vm_av_cd_classe_actif"></a>

   <a id="mt_vm_av_ass_achat_vente"></a>

   <a id="mt_vm_cible_cd_classe_actif"></a>

   <a id="mt_achat_oblig"></a>

   <a id="facteur_achat_vente"></a>

.. list-table::
   :widths: 20 10 30
   :header-rows: 1
   :class: table-custom

   * - Variable
     - Type
     - Description
   * -  tx_alloc_cible
     - Float64
     - Taux d'allocation cible

   * -  tx_oblig_achat_cpn
     - Float64
     - Taux de coupon des obligations à acheter

   * -  nb_oblig_achat_maturite
     - Float64
     - Maturité des obligations à acheter

   * -  tx_frais_plct
     - Float64
     - Taux de frais de placement

   * -  mt_vm_av_canton
     - Float64
     - Valeur de marché avant stratégie d'investissement pour le canton considéré

   * -  mt_vm_av_cd_classe_actif
     - Float64
     - Valeur de marché avant stratégie d'investissement pour la classe d'actif considérée

   * -  mt_vm_av_ass_achat_vente
     - Float64
     - Assiette utilisée pour les achats ventes à réaliser

   * -  mt_vm_cible_cd_classe_actif
     - Float64
     - Valeur de marché cible

   * -  mt_achat_oblig
     - Float64
     - Montant d'obligations à acheter (output de la stratégie d'investissement)

   * -  facteur_achat_vente
     - Float64
     - Facteur d'achat vente (output de la stratégie d'investissement)


Solvabilité 2
-------------

.. raw:: html

   <a id="cd_choc_s2"></a>

   <a id="cd_choc_s2_gse"></a>

   <a id="cd_choc_s2_passif_prst"></a>

   <a id="cd_choc_s2_passif_ic_fgx"></a>

   <a id="cd_type_flux"></a>

   <a id="cd_type_prov_mv_be_nav"></a>

   <a id="tx_choc_mort"></a>

   <a id="tx_choc_expense"></a>

   <a id="tx_choc_expense_inflation"></a>

   <a id="tx_choc_mort_cat"></a>

   <a id="tx_choc_lapse"></a>

   <a id="tx_choc_lapse_mass"></a>

   <a id="cd_type_taux"></a>

   <a id="tx_choc_equity_t1"></a>

   <a id="tx_choc_equity_t2"></a>

   <a id="tx_choc_property"></a>

   <a id="tx_choc_longevity"></a>

   <a id="tx_choc_revision"></a>

   <a id="tx_choc_inval"></a>

   <a id="tx_choc_equity_strat"></a>

   <a id="tx_choc_spread_stress"></a>

   <a id="tx_choc_spread_a"></a>

   <a id="tx_choc_spread_b"></a>

   <a id="nb_duration_min"></a>

   <a id="nb_duration_max"></a>

   <a id="facteur_choc_spread_mt_vm"></a>

   <a id="mt_be_brt"></a>

   <a id="mt_be_net"></a>

   <a id="mt_be_reass"></a>

   <a id="mt_be_reass_ajst"></a>

   <a id="mt_duration_mod"></a>

.. list-table::
   :widths: 20 10 30
   :header-rows: 1
   :class: table-custom

   * - Variable
     - Type
     - Description
   * -  cd_choc_s2
     - Categorical
     - Choc Solvabilité 2

   * -  cd_choc_s2_gse
     - Categorical
     - Choc Solvabilité 2 applicable aux variables économiques

   * -  cd_choc_s2_passif_prst
     - Categorical
     - Choc Solvabilité 2 applicable aux hypothèses de prestations

   * -  cd_choc_s2_passif_ic_fgx
     - Categorical
     - Choc Solvabilité 2 applicable à la table PassifHypsIcFgx

   * -  cd_type_flux
     - Categorical
     - Type de flux

   * -  cd_type_prov_mv_be_nav
     - Categorical
     - Type de provision

   * -  tx_choc_mort
     - Float64
     - Choc Solvabilité 2 associé à la mortalité

   * -  tx_choc_expense
     - Float64
     - Choc Solvabilité 2 associé aux frais généraux

   * -  tx_choc_expense_inflation
     - Float64
     - Choc Solvabilité 2 associé à l'inflation des frais généraux

   * -  tx_choc_mort_cat
     - Float64
     - Choc Solvabilité 2 mortalité catastrophe

   * -  tx_choc_lapse
     - Float64
     - Choc Solvabilité 2 rachat

   * -  tx_choc_lapse_mass
     - Float64
     - Choc Solvabilité 2 rachat masse

   * -  cd_type_taux
     - String
     - Type de taux dans la table hypS2Chocs

   * -  tx_choc_equity_t1
     - Float64
     - Choc Solvabilité 2 action de type 1

   * -  tx_choc_equity_t2
     - Float64
     - Choc Solvabilité 2 action de type 2

   * -  tx_choc_property
     - Float64
     - Choc Solvabilité 2 immobilier

   * -  tx_choc_longevity
     - Float64
     - Choc Solvabilité 2 longévité

   * -  tx_choc_revision
     - Float64
     - Choc Solvabilité 2 révision

   * -  tx_choc_inval
     - Float64
     - Choc Solvabilité 2 invalidité

   * -  tx_choc_equity_strat
     - Float64
     - Choc Solvabilité 2 action stratégique

   * -  tx_choc_spread_stress
     - Float64
     - Choc Solvabilité 2 spread stress

   * -  tx_choc_spread_a
     - Float64
     - Choc Solvabilité 2 spread A

   * -  tx_choc_spread_b
     - Float64
     - Choc Solvabilité 2 spread B

   * -  nb_duration_min
     - Int32
     - Borne minimum de duration pour l'application du choc spread

   * -  nb_duration_max
     - Int32
     - Borne maximum de duration pour l'application du choc spread

   * -  facteur_choc_spread_mt_vm
     - Float64
     - Facteur de choc spread sur le montant de valeur de marché

   * -  mt_be_brt
     - Float64
     - Best Estimate bruts de réassurance

   * -  mt_be_net
     - Float64
     - Best Estimate net de réassurance

   * -  mt_be_reass
     - Float64
     - Best Estimate cédé

   * -  mt_be_reass_ajst
     - Float64
     - Ajustement pour défaut

   * -  mt_duration_mod
     - Float64
     - Duration modifiée

