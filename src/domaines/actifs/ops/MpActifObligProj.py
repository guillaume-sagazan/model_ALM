from typing import Tuple
import polars as pl
import numpy as np
from polars import DataFrame


from domaines.actif.pipelines.ProjActif import projActif2projActifCashPerfInputCf, projActifCopy
from domaines.commun.expr.ActualisationExpr import calcDfDp, calcDp
from metadata.dd.DdS2 import VarS2
from metadata.dd.DdActif import VarActif
from metadata.dd.DdAlm import VarAlm
from domaines.actif.expr.ActifsExpr import calcFuiteEco, calcFuiteVcActifPerf, calcPmvl
from metadata.dd.DdGse import VarGse
from metadata.dd.DdCommun import VarCommun
from metadata.dd.DdProjection import ModeleAlmEvenement, IntraPeriod, VarProj
from metadata.dfmd.DfMdActif import dfMdActif
from metadata.dfmd.DfMdProj import dfMdProj
from metadata.dfmd.DfMdS2 import dfMdS2
from utils.pl import checkDfUniqueColsConsistency

def projActifObligBuild(period : int, evenement : ModeleAlmEvenement, 
                        mpActifOblig:DataFrame, projActifObligCf:DataFrame, 
                        gseOutputObligPzcT:DataFrame, scEcoList : list[int]=None) -> DataFrame:

    """Méthode construisant le DataFrame projActifOblig à partir de mpActifOblig, du choc S2, du scenario économique et de l'évènement
    :param chocS2: Choc Solvabilité 2
    :param period: Itération
    :param evenement: Evenement
    :param mpActifOblig: Portefeuille d'obligations
    :param projActifObligCf: Chroniques de cashflows associés au portefeuille d'obligations
    :param gseOutputObligPzcT: Prix zéro coupons
    :return: DataFrame projActifOblig au format ProjActif
    """

    csMpActifOblig = [*dfMdActif.mdProjActifObligMp.pks, VarActif.mtVc, VarActif.mtVm, VarActif.nbPeriodTerme]
    if VarProj.scenario not in mpActifOblig.columns:
        csMpActifOblig.remove(VarProj.scenario)
    if VarProj.period not in mpActifOblig.columns:
        csMpActifOblig.remove(VarProj.period)

    projActifOblig = mpActifOblig.select(csMpActifOblig
    ).with_columns([
        pl.lit(period).alias(VarProj.period),
        pl.lit(evenement).cast(pl.Categorical).alias(VarProj.evenement),
        pl.lit(0.0).alias(VarActif.mtVmAv),
        pl.lit(0.0).alias(VarActif.mtVcAv),
        pl.lit(0.0).alias(VarActif.mtPfi),
        pl.lit(0.0).alias(VarActif.mtCf),
        pl.lit(0.0).alias(VarActif.mtPdd),
        pl.lit(0.0).alias(VarAlm.mtFuiteEco),
        pl.lit(0.0).alias(VarAlm.mtFuiteVc)
    ]).with_columns(
        calcPmvl().alias(VarActif.mtPmvl)
    )
    
    if scEcoList is not None and VarProj.scenario not in projActifOblig.columns:
        projActifOblig = projActifOblig.with_columns(
            pl.lit(scEcoList).alias(VarProj.scenario),
        ).explode(VarProj.scenario) \
        .with_columns(pl.col(VarProj.scenario).cast(pl.Int32).alias(VarProj.scenario))

    #Recalcul des VM avec les courbes des taux
    projActifOblig.drop(VarActif.mtVm)
    projActifObligVm = calcDfDp(
        dfMtCf=projActifObligCf,
        colMtCf=VarActif.mtCf,
        dfPzc=gseOutputObligPzcT,
        on=[VarS2.cdChocS2Gse, VarProj.scenario, VarActif.maturite, VarProj.intraperiod],
        mappingColPzcVa={VarGse.pzc: VarActif.mtVm},
        by=[VarS2.cdChocS2Gse, VarProj.scenario, *dfMdActif.mdPksActifUnitaire]
    )
    projActifOblig = projActifOblig.join(
        projActifObligVm,
        how='left',
        on=[VarS2.cdChocS2Gse, VarProj.scenario, *dfMdActif.mdPksActifUnitaire]
    )
        
    return projActifOblig.select(dfMdActif.mdProjActif.allColumns)


def projActifObligCfBuild(mpActifOblig: DataFrame, period:int, dfCdChocS2:DataFrame = None, scEcoList:list[int]=None):

    """Méthode permettant de construire la chronique de cash flows à partir des obligations en portefeuille
    :param mpActifOblig: Obligations en portefeuille
    :type mpActifOblig: DataFrame
    :returns: DataFrame projActifObligCf contenant les chroniques de cashflows associées aux obligations en portefeuille
    """

    csMpActifOblig = [*dfMdActif.mdMpActifObligInitS2.pks,
                VarCommun.dtDateTermeAnnee, VarActif.mtNominal, VarActif.txRemboursement, VarActif.txCpn, VarActif.nbPeriodTerme]
    csResult = [c for c in dfMdActif.mdProjActifObligCf.allColumns if c != VarProj.scenario]
    
    if VarProj.scenario in mpActifOblig.columns:
        csMpActifOblig.append(VarProj.scenario)
        csResult.append(VarProj.scenario)

    projActifObligCf = mpActifOblig.select(csMpActifOblig) \
        .with_columns(pl.lit(period).cast(pl.Int32).alias(VarProj.period)) \
        .with_columns(pl.lit(IntraPeriod.END).alias(VarProj.intraperiod)) \
        .with_columns(pl.lit(1).alias('maturite_min')) \
        .with_columns((pl.col(VarActif.nbPeriodTerme) + 1).alias('maturite_max')) \
        .with_columns(pl.int_ranges('maturite_min', 'maturite_max').alias(VarActif.maturite)) \
        .explode(VarActif.maturite) \
        .with_columns([
            pl.lit(0.0).alias(VarActif.mtCf),
            pl.col(VarActif.maturite).cast(pl.Int32).alias(VarActif.maturite)
        ]) \
        .with_columns(
            pl.when(pl.col(VarActif.maturite) < pl.col(VarActif.nbPeriodTerme))
        .then(pl.col(VarActif.mtNominal) * pl.col(VarActif.txCpn))
        .when(pl.col(VarActif.maturite) == pl.col(VarActif.nbPeriodTerme))
        .then(pl.col(VarActif.mtNominal) * (pl.col(VarActif.txRemboursement) + pl.col(VarActif.txCpn)))
        .otherwise(0.0)
        .alias(VarActif.mtCf)
        )
    
    if VarS2.cdChocS2 not in projActifObligCf.columns and dfCdChocS2 is not None:
        projActifObligCf = projActifObligCf.join(dfCdChocS2.select([VarS2.cdChocS2, VarS2.cdChocS2Gse]), how='cross')
    
    if VarProj.scenario not in projActifObligCf.columns and scEcoList is not None:
        projActifObligCf.with_columns(pl.lit(scEcoList).alias(VarProj.scenario)) \
            .explode(VarProj.scenario) \
            .with_columns(pl.col(VarProj.scenario).cast(pl.Int32))

    return projActifObligCf.select(csResult)


def projActifObligPerf(period : int,
                    projActifOblig : DataFrame, projActifObligCf : DataFrame, projActifObligMp : DataFrame,
                    gseOutputObligPzcT : DataFrame,
                    gseCtRefCashPerfT : DataFrame) -> Tuple[DataFrame, DataFrame, DataFrame]:

    """Méthode en charge de l'application de la performance sur les actifs obligataires
    :param period: Itération
    :type period: int
    :param projActifOblig: Etat courant des éléments projetés pour les obligations au format projActif
    :param projActifObligCf: Etat courant des chroniques de cash flows du portefeuilles d'obligations
    :param mpActifOblig: Etat courant du portefeuilles d'obligations au format mpActif
    :param gseOutputObligPzcT: Prix zéro coupons servant à valoriser les obligations à t
    :param gseCtRefCashPerfT: Performance attendue des actifs dans le scenario Central Risque Neutre

    :return:
        * projActifOblig : Etat courant des éléments projetés mis à jour
        * projActifObligCf : Etat courant des chroniques de cash flows du portefeuilles d'obligations mis à jour
        * mpActifOblig: : Etat courant des chroniques de cash flows du portefeuilles d'obligations mis à jour
        * projActifObligCashPerfInputCf : dataframe contenant les cashflows à intégrer à l'actif

    Ceci est réalisé via les actions suivantes :

    * On commence par copier le précédent ProjActif
    * On va calculer les CF pour toutes les obligations à partir des
    * On met à jour projActifObligCf pour simuler la performance
    * En résulte que les indices de PFAD_Oblig & projActifObligCf peuvent ne plus être cohérents
    * du fait des obligations arrivées à maturité >> On va donc devoir distinguer les deux cas

        * Pour les obligations arrivées à maturité : VC = 0, VM= 0, PFI = Pfi calculés
        * Pour les obligations en cours : on suit les calculs classiques

    """

    checkDfUniqueColsConsistency('projActifObligCf vs mpActifOblig', projActifObligCf, projActifObligMp, keys=[c for c in dfMdActif.mdMpActifOblig.pks if c in dfMdActif.mdProjActifObligCf.pks])

    mdProjActif = dfMdActif.mdProjActif
    mdProjActifObligCf = dfMdActif.mdProjActifObligCf
    mdProjActifObligMp = dfMdActif.mdProjActifObligMp

    ###########################################################
    #Performance sur les obligations : les actions suivantes vont être réalisées
    # On commence par copier le précédent ProjActif
    # On va calculer les CF pour toutes les obligations à partir des
    # On met à jour projActifObligCf pour simuler la performance
    # En résulte que les indices de PFAD_Oblig & projActifObligCf peuvent ne plus être cohérents
    # du fait des obligations arrivées à maturité >> On va donc devoir distinguer les deux cas
    # - Pour les obligations arrivées à maturité : VC = 0, VM= 0, PFI = Pfi calculés
    # - Pout les obligations en cours : on suit les calculs classiques

    print(projActifOblig.shape[0])
    print(projActifObligMp.shape[0])
    print(projActifObligCf.shape[0])
    

    # Application de la performance sur projActifObligCf
    projActifObligMp = projActifObligMp.with_columns(
        pl.lit(period).alias(VarProj.period)
    ).filter(pl.col(VarProj.period) <= pl.col(VarActif.nbPeriodTerme))
    
    projActifObligCf = projActifObligCf.with_columns([
        pl.lit(period).alias(VarProj.period),
        (pl.col(VarActif.maturite) - 1).alias(VarActif.maturite)
    ])
    
    print(projActifOblig.shape[0])

    projActifObligCfT = projActifObligCf.filter(
        pl.col(VarActif.maturite) == 0
    ).drop([VarActif.maturite, VarProj.intraperiod])

    projActifObligCf = projActifObligCf.filter(
        pl.col(VarActif.maturite) > 0
    )

    # On commence par copier le précédent ProjActif
    newProjActifOblig = projActifCopy(
        projActifOblig, period=period, evenement=ModeleAlmEvenement.Perf                
    ).join(
        projActifObligMp,
        how='inner',
        on=mdProjActifObligMp.pks
    )
    
    print(projActifOblig.shape[0])
    print(projActifObligMp.shape[0])
    print(projActifObligCf.shape[0])

    newProjActifOblig = newProjActifOblig.drop(
        VarActif.mtCf
    ).join(
        projActifObligCfT,
        how='left',
        on=dfMdActif.mdPksCdChocS2ActifUnitaire
    ).with_columns(pl.col(VarActif.mtCf).fill_null(0.0).alias(VarActif.mtCf))

    print(projActifObligMp.shape[0])
    print(newProjActifOblig.shape[0])

    #Attention, certaines obligations étant précédemment arrivées à maturité doivent être éjectées du précédent ProjActif
    checkDfUniqueColsConsistency('projActifOblig vs projActifObligCf', newProjActifOblig, projActifObligCf, keys=[VarS2.cdChocS2, VarS2.cdChocS2Gse, *dfMdActif.mdPksActifUnitaire])
    checkDfUniqueColsConsistency('projActifOblig vs mpActifOblig', newProjActifOblig, projActifObligMp, keys=[VarS2.cdChocS2, VarS2.cdChocS2Gse, *dfMdActif.mdPksActifUnitaire])

    #Calcul des VM de fin de période : Calcul
    projActifObligVm = calcDfDp(
        dfMtCf=projActifObligCf,
        colMtCf=VarActif.mtCf,
        dfPzc=gseOutputObligPzcT,
        on=[VarS2.cdChocS2Gse, VarProj.scenario, VarActif.maturite, VarProj.intraperiod],
        mappingColPzcVa={VarGse.pzc: VarActif.mtVm},
        by=dfMdActif.mdPksProjActifCalcVm
    )

    # Calcul des VM de fin de période : Ajout de la colonne VM au ProjActif
    newProjActifOblig = newProjActifOblig.drop(VarActif.mtVm) \
        .join(projActifObligVm,
              how='left',
              on=dfMdActif.mdPksProjActifCalcVm
        ).with_columns(
            pl.col(VarActif.mtVm).fill_null(0.0)
        )
    
    print(newProjActifOblig.shape[0])
    print(projActifObligMp.shape[0])


    newProjActifOblig = newProjActifOblig.join(
            projActifObligMp.select([*mdProjActifObligMp.pks, VarActif.txTra]),
            how='left',
            on=mdProjActifObligMp.pks
        ).with_columns(
            (pl.col(VarActif.mtVcAv) * pl.col(VarActif.txTra)).alias(VarActif.mtPfi)
        ).with_columns(
            (pl.col(VarActif.mtVcAv) + pl.col(VarActif.mtPfi) - pl.col(VarActif.mtCf)).alias(VarActif.mtVc)
        ).with_columns([
            calcPmvl().alias(VarActif.mtPmvl),
            pl.lit(0.0).alias(VarActif.mtPdd),
            pl.lit(IntraPeriod.BEG).alias(VarProj.intraperiod)
        ])
    
    print(newProjActifOblig.shape[0])

    newProjActifOblig = newProjActifOblig.join(
            gseCtRefCashPerfT,
            how='left', 
            on=[VarProj.period, VarProj.intraperiod]
        ).with_columns([
            calcFuiteEco(colFacteurPerfTot=VarGse.facteurPerfTot).alias(VarAlm.mtFuiteEco),
            calcFuiteVcActifPerf().alias(VarAlm.mtFuiteVc)
        ]).select(mdProjActif.allColumns)

    print(newProjActifOblig.shape[0])
    print(projActifObligMp.shape[0])


    #On met temporairement INTRAPERIOD en colonne pour rappatrier le FACTEUR_PERF_TOT_GSEP
    projActifObligCashPerfInputCf = projActif2projActifCashPerfInputCf(newProjActifOblig)

    #A l'issue de ces calculs, on éjecte les lignes de PFAD_Oblig étant arrivées à maturité
    # projActifObligMp = projActifObligMp.filter(
    #     pl.col(period) <= pl.col(VarActif.nbPeriodTerme)
    # )

    return newProjActifOblig, projActifObligCf, projActifObligMp.select(mdProjActifObligMp.allColumns), projActifObligCashPerfInputCf

def almCrProjActifOblig(period: int,
                     projActif : DataFrame,
                     almCrAlmOutput : DataFrame
                     ) -> DataFrame:

    """Méthode en cahrge de l'application de l'évènement AlmCr sur le portefueille d'obligations

    :param period: Itération
    :type period: int
    :param projActif: Etat courant des éléments projetés pour les actifs
    :type projActif: DataFrame
    :param almCrAlmOutput: Outputs de la stratégie ALM
    :type almCrAlmOutput: DataFrame
    :return: projActif mis à jour

     Ceci est réalisé via les actions suivantes :
        * Simple copie de l'état des éléments projetés dans la mesure où il n'y a pas de réalisation de PMVL pour les obligations


    """

    projActifStratAlm = projActifCopy(projActif, period, ModeleAlmEvenement.AlmCr).with_columns(
        calcPmvl().alias(VarActif.mtPmvl)
    )

    return projActifStratAlm