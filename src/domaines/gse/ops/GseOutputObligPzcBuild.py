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


def gseOutputObligPzcBuild(
        gseOutputObligInput : DataFrame,
        dfCdChocS2 : DataFrame,
        scEcoList : list[int],
        projHorizon : int,
        gseObligMaturiteMax : int) -> Tuple[DataFrame, DataFrame]:

    """Méthode en charge de la construction des prix zéro coupon
    :param gseOutputObligInput: Dataframe Igse
    :type gseOutputObligInput: DataFrame
    :param dfCdChocS2: Ensemble des choc S2 issus de la configuration de la projection
    :type dfCdChocS2: DataFrame
    :param scEcoList: Liste des scenarios économiques
    :type scEcoList: list[int]
    :param projHorizon: Horizon de projection
    :type projHorizon: int
    :param gseObligMaturiteMax: Maturités maximum à prendre en compte dans le cadre de la valorisation des obligations
    :type gseObligMaturiteMax: int
    :return: Dataframe[GseOutputObligPzc]
    """

    gseOutputObligPzc = dfCdChocS2.select(VarS2.cdChocS2Gse).unique() \
                            .join(gseOutputObligInput, on=VarS2.cdChocS2Gse, how='left') \
                            .select((pl.col(VarProj.scenario).is_in(scEcoList))
                                & (pl.col(VarProj.period) <= projHorizon)) \
                            .with_columns(calcPzc(VarGse.tzc, VarActif.maturite).alias(IntraPeriod.END)) \
                            .with_columns(pl.col(IntraPeriod.END).shift(1).over(VarS2.cdChocS2Gse).fill_null(0).alias(IntraPeriod.BEG)) \
                            .with_columns((pl.col(IntraPeriod.BEG) * (pl.col(IntraPeriod.END) / pl.col(IntraPeriod.MID)) ** 0.5).alias(IntraPeriod.MID)) \
                            .melt(
                                id_vars=[col for col in gseOutputObligPzc.columns if col not in [IntraPeriod.BEG, IntraPeriod.MID, IntraPeriod.END]], 
                                variable_name=VarProj.intraperiod, 
                                value_vars=[IntraPeriod.BEG, IntraPeriod.MID, IntraPeriod.END], 
                                value_name=VarGse.pzc)

    return gseOutputObligPzc
