import polars as pl
from polars import DataFrame

from metadata.dd.DdPassifEp import VarPassif
from metadata.dfmd.DfMdPassifEp import dfMdPassifEp


def prdAdPassifBuild(mpPassifEpProj : DataFrame) -> DataFrame:
    """Méthode en charge de la construction d'un dataframe au format "PrdAdPassif" à partir d'un dataframe au format "projPassifEpMp".
    :param projPassifEpMp: Dataframe au format "projPassifEpMp"
    :type projPassifEpMp: DataFrame
    :return: Dataframe au format "PrdAdPassif"
    """
    mdPrdAdPassif = dfMdPassifEp.mdPrdAdPassifEp
    prdAdPassif = mpPassifEpProj.select([c for c in mdPrdAdPassif.allColumns if c in mpPassifEpProj.columns]).group_by(mdPrdAdPassif.pks).sum()

    return prdAdPassif
