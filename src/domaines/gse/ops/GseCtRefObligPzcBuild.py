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

def gseCtRefObligPzcBuild(gseCtRef : DataFrame, dfCdChocS2 : DataFrame,
                                             projHorizon : int, gseObligMaturiteMax : int) -> Tuple[DataFrame,DataFrame] :
    gseCtRefTmp = dfCdChocS2.select(VarS2.cdChocS2Gse).unique() \
        .join(
            gseCtRef.select(
                [VarS2.cdChocS2Gse,VarGse.tzc,VarActif.maturite]
            ).filter(pl.col(VarActif.maturite) <= projHorizon + gseObligMaturiteMax),
            how="left",
            on=VarS2.cdChocS2Gse
        ).sort(
            [VarS2.cdChocS2Gse,VarActif.maturite]
        ).with_columns(
            ((1+pl.col(VarGse.tzc))**(-pl.col(VarActif.maturite))).alias(IntraPeriod.END)
        ).drop(
            VarGse.tzc
        ).with_columns(
            pl.col(IntraPeriod.END).shift(1).over(VarS2.cdChocS2Gse).fill_null(1.0).alias(IntraPeriod.BEG)
        ).with_columns(
            (pl.col(IntraPeriod.BEG)*(pl.col(IntraPeriod.END)/pl.col(IntraPeriod.BEG))**0.5).alias(IntraPeriod.MID)
        )
    
    gseCtRefObligPzc = gseCtRefTmp.melt(
            id_vars=[VarS2.cdChocS2Gse,VarActif.maturite],
            value_vars=[IntraPeriod.BEG,IntraPeriod.MID,IntraPeriod.END],
            value_name=VarGse.pzc,
            variable_name=VarProj.intraperiod
        )
    
    gseCtRefCashPerf = gseCtRefTmp.rename(
            {VarActif.maturite : VarProj.period}
        ).filter(
            pl.col(VarProj.period) <= projHorizon
        ).with_columns(
            (pl.col(IntraPeriod.BEG)/pl.col(IntraPeriod.END)).alias(IntraPeriod.BEG)
        ).with_columns(
            (pl.col(IntraPeriod.MID)/pl.col(IntraPeriod.END)).alias(IntraPeriod.MID)
        ).with_columns(
            (pl.lit(1.0)).alias(IntraPeriod.END)
        ).melt(
            id_vars=[VarS2.cdChocS2Gse,VarProj.period],
            value_vars=[IntraPeriod.BEG,IntraPeriod.MID,IntraPeriod.END],
            value_name=VarGse.facteurPerfTot,
            variable_name=VarProj.intraperiod
        )
    
    return gseCtRefObligPzc.select(dfMdGse.mdGseCtRefObligPzc.allColumns), gseCtRefCashPerf.select(dfMdGse.mdGseCtRefCashPerf.allColumns)