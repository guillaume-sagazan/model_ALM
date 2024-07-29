import polars as pl
from typing import Tuple
from polars import DataFrame

from domaines.actif.pipelines.ProjActif import projActif2projActifCashPerfInputCf, projActifCopy
from domaines.s2.expr.S2Expr import rsCdChocS2CdClasseActifAction, rsCdChocS2CdClasseActifImmo
from domaines.actif.expr.ActifsExpr import calcFuiteEco, calcFuiteVcActifPerf, calcPmvl
from metadata.dd.DdActif import CdClasseActif, VarActif
from metadata.dd.DdAlm import VarAlm
from metadata.dd.DdCommun import VarCommun
from metadata.dd.DdGse import VarGse
from metadata.dd.DdProjection import ModeleAlmEvenement, IntraPeriod, VarProj
from metadata.dd.DdS2 import CdChocS2, VarS2
from metadata.dfmd.DfMdActif import dfMdActif
from metadata.dfmd.DfMdAlmCr import DfMdAlm

def projActifIndicesBuild(scEcoList: list[int], mpActifIndices: DataFrame) -> DataFrame:

    """Méthode construisant le DataFrame projActifIndices à partir de mpActifindices, du choc S2 à jouer et du scenario économique
    Les chocs S2 impactant les actifs indiciels sont appliqués par cette méthode.
    
    :param chocS2: Choc Solvabilité 2
    :type chocS2: str
    :param mpActifIndices:
    :type mpActifIndices:  DataFrame
    :param hypS2Chocs: Paramètres des chocs à appliquer
    :type hypS2Chocs: DataFrame
    
    :returns: DataFrame au format "ProjActif" pour les actifs indiciels. Chocs S2 appliqués.
    
    """

    projActifIndices = mpActifIndices.select([*dfMdActif.mdMpActifIndicesInitS2.pks, VarActif.mtVc, VarActif.mtVm])

    projActifIndices = projActifIndices.with_columns([
        pl.lit(-1).alias(VarActif.nbPeriodTerme),
        pl.lit(scEcoList).alias(VarProj.scenario),
        pl.lit(0).alias(VarProj.period),
        pl.lit(ModeleAlmEvenement.Init).cast(pl.Categorical).alias(VarProj.evenement),
        pl.lit(0.0).alias(VarActif.mtVmAv),
        pl.lit(0.0).alias(VarActif.mtVcAv),
        pl.lit(0.0).alias(VarActif.mtPfi),
        pl.lit(0.0).alias(VarActif.mtCf),
        pl.lit(0.0).alias(VarActif.mtPdd),
        pl.lit(0.0).alias(VarAlm.mtFuiteEco),
        pl.lit(0.0).alias(VarAlm.mtFuiteVc)      
    ]).with_columns(
        calcPmvl().alias(VarActif.mtPmvl)
    ).explode(VarProj.scenario) \
    .with_columns(pl.col(VarProj.scenario).cast(pl.Int32))

    return projActifIndices[dfMdActif.mdProjActif.allColumns]


def projActifIndicesPerf(period: int,
                      projActifIndices: DataFrame,
                      gseOutputIndicesPerfT: DataFrame,
                      gseCtRefCashPerfT: DataFrame) -> Tuple[DataFrame, DataFrame]:

    """Méthode appliquant l'évènement "performance" sur une DataFrame projActifIndices

    L'application de la performance sur le cash implique :
    * de faire une copie du dataframe d'entrée
    * renseigner dans cette copie le scenario, l'itération et l'évènement (Perf)
    * d'appliquer le taux de performance du cash sur la base du DataFrame gseOutputIndicesPerfT
    * de calculer la fuite économique comme la différence entre l'augmentation de VM sur la base du taux de performance du cash appliqué et du taux de performance du cash attendu dans le cadre du scenario CRN

    :param period: période
    :type period: int
    :param projActifIndices: DataFrame projActifIndices en entrée
    :type projActifIndices: DataFrame
    :param gseOutputIndicesPerfT: Taux de performance du cash à appliquer pour le scenario et l'itération
    :param gseCtRefCashPerfT: Taux de performance attendu dans le cadre du scenario CRN
    :return: DataFrame projActifIndices mis à jour

    """

    mdProjActif = dfMdActif.mdProjActif

    newProjActifIndices = projActifCopy(projActifIndices, period=period, evenement=ModeleAlmEvenement.Perf)

    newProjActifIndices = newProjActifIndices.join(
        gseOutputIndicesPerfT,
        how='left',
        on=[VarS2.cdChocS2Gse, VarActif.cdClasseActif, VarProj.period],
    ).with_columns(
        pl.lit(IntraPeriod.BEG).alias(VarProj.intraperiod)
    ).join(gseCtRefCashPerfT,
        how='left',
        on=[VarS2.cdChocS2Gse, VarProj.period, VarProj.intraperiod],
        suffix='_ct_ref'
    ).with_columns([
        (pl.col(VarGse.facteurPerfNet) * pl.col(VarActif.mtVmAv)).alias(VarActif.mtVm),
        (pl.col(VarActif.mtVmAv) * pl.col(VarGse.txDividendes)).alias(VarActif.mtPfi),
        (pl.col(VarActif.mtVmAv) * pl.col(VarGse.txDividendes)).alias(VarActif.mtCf),
        pl.lit(0.0).alias(VarActif.mtPdd)
    ]).with_columns([
        calcPmvl().alias(VarActif.mtPmvl),
        calcFuiteEco().alias(VarAlm.mtFuiteEco),
        calcFuiteVcActifPerf().alias(VarAlm.mtFuiteVc)
    ])
    
    projActifCashPerfInputCf = projActif2projActifCashPerfInputCf(newProjActifIndices)

    return newProjActifIndices.select(mdProjActif.allColumns), projActifCashPerfInputCf

def almCrProjActifIndices(period: int,
                       projActif: DataFrame,
                       almCrInputActif: DataFrame,
                       almCrAlmOutput: DataFrame
                       ) -> DataFrame:

    """Méthode appliquant l'évènement "AlmCr" sur un DataFrame projActifIndices
    
    L'application de l'évènement "AlmCr" sur les actifs indiciels implique :
    
    * de faire une copie du dataframe d'entrée
    * renseigner dans cette copie le scenario, l'itération et l'évènement (Perf)
    * de réaliser les plus ou moins values latentes décidées dans le cadre de la stratégie ALM

    :param period: Itération
    :type period: int
    :param projActif: DataFrame projActif à partir duquel travailler
    :param projActif: DataFrame
    :param almCrInputActif: Input de la stratégie ALM, dans lequel on trouve notamment les plus ou moins values latentes avant l'évènement AlmCr
    :type almCrInputActif: DataFrame
    :param almCrAlmOutput: Output de la stratégie ALM, dans lequel on trouve notamment les plus ou moins values à réaliser
    :type almCrAlmOutput: DataFrame
    
    :returns: projActifIndices mis à jour
    """
    mdStratAlmInputActif = dfMdAlmCr.mdAlmCrInputActif
    projActifStratAlm = \
        projActifCopy(projActif, period, ModeleAlmEvenement.AlmCr) \
        .with_columns(
            pl.col(VarActif.mtPmvl).sum().over(set(dfMdAlmCr.mdAlmCrAlmOutput.pks) - {VarAlm.stratAlmCas}).alias(VarActif.mtPmvl)
        ).join(almCrAlmOutput.select(set(dfMdAlmCr.mdAlmCrAlmOutput.pks) - {VarAlm.stratAlmCas} | {VarActif.mtPmvr}),
              how='left',
              on=set(dfMdAlmCr.mdAlmCrAlmOutput.pks) - {VarAlm.stratAlmCas}
        ).with_columns([
            (  
                pl.col(VarActif.mtVcAv)
                + pl.col(VarActif.mtPmvr) / pl.col(VarActif.mtPmvl)
                * pl.col(VarActif.mtVmAv) - pl.col(VarActif.mtVcAv)
            ).alias(VarActif.mtVc),
            (
                pl.col(VarActif.mtVc) - pl.col(VarActif.mtVcAv)
            ).alias(VarActif.mtPfi)
        ]).drop(VarActif.mtPmvl) \
        .with_columns(calcPmvl().alias(VarActif.mtPmvl)) \
        .select(dfMdActif.mdProjActif.allColumns)

    return projActifStratAlm
