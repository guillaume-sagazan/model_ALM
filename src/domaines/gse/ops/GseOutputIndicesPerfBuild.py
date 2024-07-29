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

def gseOutputIndicesPerfBuild(
        gseOutputIndicesInput : DataFrame,
        dfCdChocS2 : DataFrame,
        scEcoList : list[int],
        projHorizon : int) -> DataFrame:

    """Méthode en charge de la construction du dataframe gseOutputIndicesPerf
    :param gseOutputIndicesInput:
    :type gseOutputIndicesInput:
    :param dfCdChocS2: Ensemble des choc S2 issus de la configuration de la projection
    :type dfCdChocS2: DataFrame
    :param scEcoList: liste des scenarios économiques
    :type scEcoList: list[int]
    :param projHorizon: Horizon de projection
    :type projHorizon: int
    :return: Dataframe[GseOutputIndicesPerf]
    """

    gseOutputIndicesPerf = dfCdChocS2.select(VarS2.cdChocS2Gse).unique() \
                            .join(gseOutputIndicesInput, on=VarS2.cdChocS2Gse, how='left') \
                            .filter((pl.col(VarProj.scenario).is_in(scEcoList)) & (pl.col(VarProj.period) <= projHorizon)) \
                            .with_columns((1. + VarGse.txPerfTot).alias(VarGse.facteurPerfTot)) \
                            .with_columns((VarGse.facteurPerfTot - VarGse.txDividendes).alias(VarGse.facteurPerfNet)) \
                            .drop(VarGse.txPerfTot)
                                                
    
    return gseOutputIndicesPerf