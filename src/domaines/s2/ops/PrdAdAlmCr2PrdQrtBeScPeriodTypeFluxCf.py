import polars as pl
from polars import DataFrame

from metadata.dd.DdActif import VarActif
from metadata.dd.DdFgx import VarFgx
from metadata.dd.DdPassifEp import VarPassif
from metadata.dd.DdProjection import IntraPeriod, VarProj
from metadata.dd.DdS2 import VarS2
from metadata.dfmd.DfMdAlmCr import dfMdAlmCr
from metadata.dfmd.DfMdS2 import dfMdS2
from metadata.dfmd.DfMdActif import dfMdActif

def prdAdCr2PrdQrtBeScPeriodTypeFluxCf(prdAdCr : DataFrame) -> DataFrame:
    """Méthode en charge d'ajouter les frais de placement aux cashflows entrant dans le BE

    :param prdAdCr: DataFrame contenant les frais de placement de l'année
    :type prdAdCr: DataFrame
    :return: DataFrame au format CashInputCf
    :rtype: DataFrame
    """
    pks = [pk for pk in dfMdAlmCr.mdPrdAdAlmCr.pks if pk in dfMdActif.mdProjActifCashInputCf.pks]

    prdQrtBeBrtCf = prdAdCr.select([*dfMdAlmCr.mdPrdAdAlmCr.pks, VarFgx.mtFgxPlct]) \
            .group_by(pks).sum() \
            .melt(id_vars=pks,
                value_vars=[VarFgx.mtFgxPlct],
                variable_name=VarS2.cdTypeFlux,
                value_name=VarActif.mtCf
            ).with_columns([
                pl.lit('TBD').alias(VarPassif.cdFampdt),
                pl.col(VarS2.cdTypeFlux).cast(pl.Categorical).alias(VarS2.cdTypeFlux),
                pl.lit(IntraPeriod.END).alias(VarProj.intraperiod)
            ])

    return prdQrtBeBrtCf.select(dfMdS2.mdPrdQrtBeScPeriodTypeFluxCf.allColumns)