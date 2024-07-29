import polars as pl
from polars import DataFrame

from metadata.dd.DdActif import VarActif
from metadata.dd.DdCommun import VarCommun
from metadata.dd.DdS2 import VarS2
from metadata.dfmd.DfMdActif import dfMdActif
from metadata.dfmd.DfMdS2 import dfMdS2
from metadata.dfmd.DfMdS2 import mappingCfBe

def cashInputCfAsse2PrdQrtBeScPeriodTypeFluxCf(cfsBeS2 : DataFrame) -> DataFrame:

    """Méthode en charge de transcrire la liste des cash flows assurés en liste de cashflows à intégrer au Best Estimate

    :param cfsBeS2: Liste des cashflows alimentant le BE
    :type cfsBeS2: DataFrame
    :return: Liste des cashflows alimentant le BE
    :rtype: DataFrame
    """
    prdQrtBeScPeriodTypeFluxCf = cfsBeS2.group_by(dfMdActif.mdProjActifCashInputCf.pks).sum() \
        .join(
            mappingCfBe,
            how='inner',
            on=VarS2.cdTypeFlux
        ).with_columns(
            (pl.col(VarActif.mtCf) * pl.col(VarCommun.facteur)).alias(VarActif.mtCf)
        )

    return prdQrtBeScPeriodTypeFluxCf.select(dfMdS2.mdPrdQrtBeScPeriodTypeFluxCf.allColumns)