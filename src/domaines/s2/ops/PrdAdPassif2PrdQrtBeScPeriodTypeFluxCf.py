import polars as pl
from polars import DataFrame
from metadata.dd.DdActif import VarActif
from metadata.dd.DdPassifEp import VarPassif
from metadata.dd.DdProjection import IntraPeriod, VarProj
from metadata.dd.DdS2 import VarS2
from metadata.dfmd.DfMdPassifEp import dfMdPassifEp
from metadata.dfmd.DfMdActif import dfMdActif
from metadata.dfmd.DfMdS2 import dfMdS2

def prdAdPassif2PrdQrtBeScPeriodTypeFluxCf(prdAdPassif : DataFrame) -> DataFrame:
    """Méthode en charge d'ajouter les PM fin de projection aux cashflows entrant dans le BE

    :param prdAdPassif: DataFrame contenant les PM
    :type prdAdPassif: DataFrame
    :return: DataFrame au format CashInputCf
    :rtype: DataFrame
    """
    pks = [pk for pk in dfMdPassifEp.mdPrdAdPassifEp.pks if pk in dfMdActif.mdProjActifCashInputCf.pks]
    
    prdQrtBeBrtCf = prdAdPassif.select([*dfMdPassifEp.mdPrdAdPassifEp.pks, VarPassif.mtPmEu, VarPassif.mtPmUc
                                        ]) \
            .group_by(pks).sum() \
            .melt(id_vars=pks,
                value_vars=[VarPassif.mtPm],
                variable_name=VarS2.cdTypeFlux,
                value_name=VarActif.mtCf
            ).with_columns([
                pl.lit(IntraPeriod.END).alias(VarProj.intraperiod)
            ])

    return prdQrtBeBrtCf.select(dfMdS2.mdPrdQrtBeScPeriodTypeFluxCf.allColumns)