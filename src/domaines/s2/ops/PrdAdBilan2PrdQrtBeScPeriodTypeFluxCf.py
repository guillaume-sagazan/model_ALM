import polars as pl
from polars import DataFrame

from metadata.dd.DdActif import VarActif
from metadata.dd.DdAlm import VarAlm
from metadata.dd.DdPassifEp import VarPassif
from metadata.dd.DdProjection import IntraPeriod, VarProj
from metadata.dd.DdS2 import VarS2
from metadata.dfmd.DfMdAlmCr import dfMdAlmCr
from metadata.dfmd.DfMdS2 import dfMdS2
from metadata.dfmd.DfMdActif import dfMdActif


def prdAdBilan2PrdQrtBeScPeriodTypeFluxCf(prdAdBilan : DataFrame) -> DataFrame:
    """Méthode en charge d'ajouter la PPB fin de projection aux cashflows entrant dans le BE
    :param prdAdBilan: DataFrame contenant la PPB
    :type prdAdBilan: DataFrame
    :return: DataFrame au format CashInputCf
    :rtype: DataFrame
    """
    pks = [pk for pk in dfMdAlmCr.mdPrdAdBilan.pks if pk in dfMdActif.mdProjActifCashInputCf.pks]
    prdQrtBeScPeriodTypeFluxCf = prdAdBilan.select([*dfMdAlmCr.mdPrdAdBilan.pks, VarAlm.mtPpe]) \
            .group_by(pks).sum() \
            .melt(
                id_vars=pks,
                value_vars=[VarAlm.mtPpe],
                variable_name=VarS2.cdTypeFlux,
                value_name=VarActif.mtCf
            ).with_columns([
                pl.lit('TBD').alias(VarPassif.cdFampdt),
                pl.lit(IntraPeriod.END).alias(VarProj.intraperiod)
            ])

    return prdQrtBeScPeriodTypeFluxCf.select(dfMdS2.mdPrdQrtBeScPeriodTypeFluxCf.allColumns)
