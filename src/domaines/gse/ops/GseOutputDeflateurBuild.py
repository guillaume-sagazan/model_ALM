import logging
from typing import Tuple
import polars as pl
from polars import DataFrame

from domaines.gse.expr.GseExpr import calcCashPerf, calcPzc
from metadata.dd.DdActif import CdClasseActif, VarActif
from metadata.dd.DdGse import VarGse
from metadata.dd.DdProjection import IntraPeriod, VarProj
from metadata.dd.DdS2 import VarS2
from metadata.dfmd.DfMdGse import dfMdGse

TX_INFLATION_DEFAULT_VALUE = 0.01
TX_DIVIDENDES_DEFAULT_VALUE = 0.00

def gseOutputDeflateurBuild(gseOutputObligPzc:DataFrame) -> DataFrame:

    """Méthode en charge du dataframe contenant les déflateurs
    :param gseOutputObligPzc: Prix zéro coupon utilisés pour la valorisation des obligations
    :type gseOutputObligPzc: DataFrame
    :return: Dataframe[GseOutputDeflateur]
    """

    gseOutputDeflateur = gseOutputObligPzc.filter(pl.col(VarActif.maturite) == 1) \
                .drop(VarActif.maturite) \
                .rename({VarGse.pzc : VarGse.deflateur}) \
                .with_columns(
                    pl.col(VarGse.deflateur).shift(1)
                        .over([c for c in dfMdGse.mdGseOutputDeflateur.pks if c != VarProj.period])
                        .fill_null(1.0).alias(VarGse.deflateur))
                
    
    return gseOutputDeflateur
