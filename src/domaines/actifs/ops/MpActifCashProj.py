import polars as pl
from polars import DataFrame


from metadata.dd.DdActif import CdClasseActif, VarActif
from metadata.dd.DdAlm import VarAlm

from metadata.dd.DdGse import VarGse
from metadata.dd.DdPassifEp import VarPassif
from metadata.dd.DdCommun import VarCommun
from metadata.dd.DdProjection import ModeleAlmEvenement, IntraPeriod, VarProj
from domaines.actifs.expr.ActifsExpr import calcFuiteEco, calcFuiteVcActifPerf, calcPmvl
from metadata.dd.DdS2 import VarS2
from metadata.dfmd.DfMdGse import DfMdGse
from metadata.dfmd.DfMdActif import dfMdActif


def projActifCashBuild(scEcoList : list[int], mpActifCash:DataFrame) -> DataFrame:

    """Méthode construisant le DataFrame projActifCash à partir de actifCash, du choc S2 à jouer et du scenario économique
    :param chocS2: Choc Solvabilité 2
    :type chocS2: str
    :param actifCash: Caractériques du cash en input du modèle par canton
    :type actifCash: DataFrame
    :returns: DataFrame projActifCash au format attendu
    :rtype: DataFrame
    """

    projActifCash = mpActifCash.select([*dfMdActif.mdMpActifCashInitS2.pks, VarActif.mtVc, VarActif.mtVm]) \
        .with_columns([
            pl.lit(0).alias(VarActif.nbPeriodTerme),
            pl.lit(scEcoList).alias(VarProj.scenario),
            pl.lit(0).alias(VarProj.period),
            pl.lit(ModeleAlmEvenement.Init).cast(pl.Categorical).alias(VarProj.evenement),
            calcPmvl().alias(VarActif.mtPmvl),
            pl.lit(0.0).alias(VarActif.mtVmAv),
            pl.lit(0.0).alias(VarActif.mtVcAv),
            pl.lit(0.0).alias(VarActif.mtPfi),
            pl.lit(0.0).alias(VarActif.mtCf),
            pl.lit(0.0).alias(VarActif.mtPdd),
            pl.lit(0.0).alias(VarAlm.mtFuiteEco),
            pl.lit(0.0).alias(VarAlm.mtFuiteVc)
        ]).explode(VarProj.scenario) \
        .with_columns(pl.col(VarProj.scenario).cast(pl.Int32).alias(VarProj.scenario))

    return projActifCash.select(dfMdActif.mdProjActif.allColumns)

def projActifCashPerf(period : int, projActifCash : DataFrame, projActifCashPerfInputCf : DataFrame, gseOutputCashPerfT : DataFrame, gseCtRefCashPerfT : DataFrame) -> DataFrame:

    """Méthode appliquant l'évènement "performance" sur un DataFrame projActifCash
    :param period: Itération
    :param projActifCash: DataFrame projActifCash en entrée
    :param projActifCashPerfInputCf: Cashflows en provenance de l'actif et du passif à intégrer au cash
    :param gseOutputCashPerfT: Taux de performance du cash à appliquer pour le scenario et l'itération
    :param gseCtRefCashPerfT: Taux de performane du cash attendu sur la base du scenario CRN
    :returns: DataFrame projActifCash mis à jour

    L'application de la performance sur le cash est réalisée via les actions suivantes :
        * de faire une copie du dataframe d'entrée
        * renseigner dans cette copie le scenario, l'itération et l'évènement (Perf)
        * d'intégrer les cashflows en provenance de l'actif et du passif
        * d'appliquer le taux de performance du cash sur la base du DataFrame gseOutputCashPerfT
        * de calculer la fuite économique comme la différence entre l'augmentation de VM sur la base du taux de performance du cash appliqué et du taux de performance du cash attendu dans le cadre du scenario CRN

    """

    mdProjActif = dfMdActif.mdProjActif
    mdGseOutputCashPerf = dfMdGse.mdGseOutputCashPerf
    mdGseCtRefCashPerf = dfMdGse.mdGseCtRefCashPerf

    projActifCashStock = projActifCopy(projActifCash, period=period, evenement=ModeleAlmEvenement.Perf)
    projActifCashStock = projActifCashStock.with_columns(
        pl.lit(IntraPeriod.BEG).alias(VarProj.intraperiod)
    ).join(gseOutputCashPerfT,
        how='left',
        on=mdGseOutputCashPerf.pks
    ).join(
        gseCtRefCashPerfT,
        how='left',
        on=mdGseCtRefCashPerf.pks,
        suffix='_ct_ref'
    ).with_columns([
        (pl.col(VarActif.mtVmAv) * pl.col(VarGse.facteurPerfTot)).alias(VarActif.mtVm),
        (pl.col(VarActif.mtVm) - pl.col(VarActif.mtVmAv)).alias(VarActif.mtPfi),
        calcFuiteEco().alias(VarAlm.mtFuiteEco)
    ]).with_columns([
        pl.col(VarActif.mtVm).alias(VarActif.mtVc),
    ]).with_columns(
        calcFuiteVcActifPerf().alias(VarAlm.mtFuiteVc)
    ).select(mdProjActif.allColumns)

    #Pour les différents cashflows, on calcule les pfis / vm fin / fuite eco issus des cash flows qui tombent
    projActifCashCf = projActifCashPerfInputCf.join(
        gseOutputCashPerfT,
        how='left',
        on=mdGseOutputCashPerf.pks
    ).join(
        gseCtRefCashPerfT,
        how='left',
        on=mdGseCtRefCashPerf.pks,
        suffix='_ct_ref'
    ).with_columns([
        pl.lit(ModeleAlmEvenement.Perf).cast(pl.Categorical).alias(VarProj.evenement),
        pl.lit(CdClasseActif.MONETAIRE).alias(VarActif.cdClasseActif),
        pl.lit(CdClasseActif.MONETAIRE).alias(VarActif.cdClasseActifDetail),
        pl.lit(CdClasseActif.MONETAIRE).alias(VarActif.cdIsin),
        pl.lit(0.0).alias(VarActif.mtVcAv),
        pl.lit(0.0).alias(VarActif.mtVmAv),
        pl.lit(-1).cast(pl.Int32).alias(VarActif.nbPeriodTerme),
        pl.lit(0.0).alias(VarActif.mtPdd),
        (pl.col(VarActif.mtCf) * pl.col(VarGse.facteurPerfTot)).alias(VarActif.mtVm)
    ]).with_columns(
        (pl.col(VarActif.mtVm) - pl.col(VarActif.mtCf)).alias(VarActif.mtPfi)
    ).with_columns([
        (pl.col(VarActif.mtVm) - pl.col(VarActif.mtCf) * pl.col(VarGse.facteurPerfTot + '_ct_ref')).alias(VarAlm.mtFuiteEco),
        (pl.col(VarActif.mtVm)).alias(VarActif.mtVc),
        pl.lit(0.0).alias(VarActif.mtPmvl),
        (pl.col(VarActif.mtVm) - pl.col(VarActif.mtCf) - pl.col(VarActif.mtPfi)).alias(VarAlm.mtFuiteVc),
    ]).select(mdProjActif.allColumns)
    

    projActifCash = pl.concat([projActifCashStock, projActifCashCf]) \
        .group_by(mdProjActif.pks).sum()

    return projActifCash

def almCrProjActifCash(period: int,
                    projActif : DataFrame,
                    prdAdCr : DataFrame,
                    mpProvOther : DataFrame,
                    ) -> DataFrame:

    """Méthode appliquant l'évènement "AlmCr" sur un DataFrame projActifCash
    :param period: Itération
    :type period: int
    :param projActif: DataFrame projActifCash à partir duquel on travaille
    :type projActif: DataFrame
    :param prdAdCr: Compte de résultat à partir dans lequel on trouve les éléments qui impactent le cash
    :type prdAdCr: DataFrame
    :param mpProvOther: On trouve notamment dans ce DataFrame le type du canton
    :type mpProvOther: DataFrame

    :returns: DataFrame[projActifCash] mis à jour

    L'application de l'évènement "AlmCr" sur le cash implique :

    * de faire une copie du dataframe d'entrée
    * renseigner dans cette copie le scenario, l'itération et l'évènement (AlmCr)
    * retrancher du cash le résultat brut du canton
    * retrancher du cash les frais de placement

    """

    projActifCashAlmCr = projActifCopy(projActif, period, ModeleAlmEvenement.AlmCr)
    projActifCashAlmCr = projActifCashAlmCr.join(prdAdCr, 
                                         how='left', 
                                         on=set(projActifCashAlmCr.columns) & set(prdAdCr.columns)
    ).join(mpProvOther,
        how='left', 
        on=set(projActifCashAlmCr.columns) & set(mpProvOther.columns)
    ).with_columns([
        (
            pl.col(VarActif.mtVm)
            - pl.col(VarAlm.mtPfiAssr)
            - pl.col(VarAlm.mtResBrtAsse)
            - pl.col(VarFgx.mtFgxPlct)
        ).alias(VarActif.mtVm),
        (
            pl.col(VarActif.mtVc)
            - pl.col(VarAlm.mtPfiAssr)
            - pl.col(VarAlm.mtResBrtAsse)
            - pl.col(VarFgx.mtFgxPlct)
        ).alias(VarActif.mtVc),
        (
            - pl.col(VarAlm.mtPfiAssr)
            - pl.col(VarAlm.mtResBrtAsse)
            - pl.col(VarFgx.mtFgxPlct)
        ).alias(VarActif.mtCf)
    ]).with_columns(
        calcPmvl().alias(VarActif.mtPmvl)
    )

    return projActifCashAlmCr.select(dfMdActif.mdProjActif.allColumns)

