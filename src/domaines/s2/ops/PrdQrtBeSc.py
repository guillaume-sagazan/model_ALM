import polars as pl
from polars import DataFrame

from metadata.dd.DdS2 import VarS2
from metadata.dfmd.DfMdS2 import dfMdS2

def prdQrtBeScBuild(prdQrtBeBrtScPeriodTypeFlux : DataFrame) -> DataFrame:
    """Méthode en charge d'agréger les BE à la maille requise et de calculer la duration modifiée
    :param rcarsScCf: Liste des cashflows actualisés
    :type rcarsScCf: DataFrame
    :return: DataFrame rcarsSc
    :rtype: DataFrame
    """

    if prdQrtBeBrtScPeriodTypeFlux is None:
        return None

    prdQrtBeSc = prdQrtBeBrtScPeriodTypeFlux.group_by(dfMdS2.mdPrdQrtBeSc.pks).sum() \
        .with_columns([
            pl.col(VarS2.mtDurationMod) / pl.col(VarS2.mtBeBrt).alias(VarS2.mtDurationMod)
        ])
    
    return prdQrtBeSc