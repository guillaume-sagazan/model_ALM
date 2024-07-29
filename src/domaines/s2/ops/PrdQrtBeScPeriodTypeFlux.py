import polars as pl
from polars import DataFrame

from domaines.commun.expr.ActualisationExpr import calcDp
from metadata.dd.DdActif import VarActif
from metadata.dd.DdGse import VarGse
from metadata.dd.DdProjection import VarProj
from metadata.dd.DdS2 import VarS2
from metadata.dfmd.DfMdS2 import dfMdS2


def prdQrtBeScPeriodTypeFluxBuild(
        dfCdChocS2: DataFrame, 
        prdQrtBeScPeriodTypeFluxCf: DataFrame, 
        gseOutputDeflateur: DataFrame) -> DataFrame:
    
    """Méthode en charge d'actualiser les flux dans le cadre des calculs de BE
    :param rcarsScCf: Cashflows à actualiser
    :type rcarsScCf: DataFrame
    :param gseOutputDeflateur: Déflateurs
    :type gseOutputDeflateur: DataFrame
    :return: Flux actualisés
    :rtype: DataFrame
    """

    if prdQrtBeScPeriodTypeFluxCf is None:
        return None

    prdQrtBeBrtScPeriodTypeFlux = prdQrtBeScPeriodTypeFluxCf.join(
        dfCdChocS2.select([VarS2.cdChocS2, VarS2.cdChocS2Gse]),
        how='left',
        on=VarS2.cdChocS2
    ).join(
        gseOutputDeflateur,
        on=[VarS2.cdChocS2Gse, VarProj.scenario, VarProj.period, VarProj.intraperiod]
    ).with_columns([
        calcDp(VarActif.mtCf, VarGse.deflateur).alias(VarS2.mtBeBrt),
        pl.lit(0.0).cast(pl.Float64).alias(VarS2.mtBeReass),
        pl.lit(0.0).cast(pl.Float64).alias(VarS2.mtBeReassAjst),
    ]).with_columns([
        pl.col(VarS2.mtBeBrt) - pl.col(VarS2.mtBeReass) + pl.col(VarS2.mtBeReassAjst).alias(VarS2.mtBeNet),
        (pl.col(VarProj.period) * pl.col(VarS2.mtBeBrt)).alias(VarS2.mtDurationMod)
    ]).group_by(dfMdS2.mdPrdQrtBeScPeriodTypeFlux.pks).sum()

    return prdQrtBeBrtScPeriodTypeFlux
