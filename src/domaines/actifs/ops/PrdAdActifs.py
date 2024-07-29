import polars as pl
from polars import DataFrame

from metadata.dfmd.DfMdActif import dfMdActif

def prdAdActifBuild(mpActifProj : DataFrame) -> DataFrame:
    """Méthode permettant de construire le dataframe PrdAd à partir d'un dataframe projActif
    Ceci est réalisé en agrégeant les éléments projetés des actifs unitaires à la maille PrdAd.
    :param projActif: Etat courant des éléments projetés pour les actifs unitaires
    :type projActif: DataFrame
    :return: dataframe au format PrdAd
    """
    return mpActifProj.select(
        [c for c in dfMdActif.mdPrdAdActif.allColumns if c in mpActifProj.columns]
    ).group_by(
        dfMdActif.mdPrdAdActif.pks
    ).sum()
        