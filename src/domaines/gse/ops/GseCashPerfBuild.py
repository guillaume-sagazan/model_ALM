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

def gseOutputCashPerfBuild(gseOutputObligPzc : DataFrame, projHorizon : int) -> DataFrame: #TODO : Ajouter un horizon à cette fonction
    """Méthode en charge du calcul des taux de performance du cash
    :param gseObligPzc: Prix zéro coupon
    :type gseObligPzc: DataFrame
    :param projHorizon: Horizon de projection en années
    :type projHorizon: int
    :return: Dataframe[GseCashPerf]
    """
    
    gseCashPerf = gseOutputObligPzc
    
    if VarProj.period in gseCashPerf.columns and VarActif.maturite in gseCashPerf.columns:
        gseCashPerf = gseCashPerf.filter(
            pl.col(VarActif.maturite) == 1
        ).drop(VarActif.maturite)

    elif VarProj.period not in gseCashPerf.columns and VarActif.maturite in gseCashPerf.columns:
        gseCashPerf = gseCashPerf.rename({VarActif.maturite : VarProj.period})

    gseCashPerfEnd = gseCashPerf.filter(pl.col(VarProj.intraperiod) == IntraPeriod.END).drop(VarProj.intraperiod).rename({VarGse.pzc : "pzcEnd"})

    gseCashPerf = gseCashPerf.join(
        gseCashPerfEnd,
        how='left',
        on=set(gseCashPerf.columns) & set(gseCashPerfEnd.columns)    
    ).with_columns([
        (1 + pl.col(VarProj.period)).alias(VarProj.period),
        (pl.col(VarGse.pzc) / pl.col("pzcEnd")).alias(VarGse.facteurPerfTot)
    ]).filter(pl.col(VarProj.period) <= projHorizon
              )
    
    return gseCashPerf.select(dfMdGse.mdGseOutputCashPerf.allColumns)