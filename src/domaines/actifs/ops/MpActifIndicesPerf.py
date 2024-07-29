from polars import DataFrame
import polars as pl
from domaines.actifs.expr.ActifsExpr import calcFuiteEco, calcFuiteVcActifPerf, calcPmvl
from domaines.actifs.ops.MpActifProjCopy import mpActifProjCopy
from domaines.s2.expr.S2Expr import calcMtVmIndicesInitS2
from metadata.dd.DdActif import VarActif
from metadata.dd.DdAlm import VarAlm
from metadata.dd.DdGse import VarGse
from metadata.dd.DdProjection import IntraPeriod, ModeleAlmEvenement, VarProj
from metadata.dd.DdS2 import VarS2
from metadata.dfmd.DfMdActif import dfMdActif 
from metadata.dfmd.DfMdGse import dfMdGse


def mpActifIndicesPerf (period : int, mpActifIndicesProj : DataFrame, gseCtRefCashPerfT : DataFrame, gseOutputIndicesPerfT : DataFrame) -> DataFrame :
    mpActifIndicesProj = mpActifProjCopy(
        period=period,
        evenement=ModeleAlmEvenement.Perf,
        mpActifProj=mpActifIndicesProj
    ).join(
        gseOutputIndicesPerfT, 
        how = 'left',
        on = set(dfMdActif.mdMpActifIndicesProj.pks) & set(dfMdGse.mdGseOutputIndicesPerf.pks)
    ).with_columns(
        pl.lit(IntraPeriod.BEG).alias(VarProj.intraperiod)
    ).join(
        gseCtRefCashPerfT,
        how = 'left',
        on = set([*dfMdActif.mdMpActifIndicesProj.pks, VarProj.intraperiod]) & set(dfMdGse.mdGseCtRefCashPerf.pks),
        suffix = '_ct_ref'
    ).with_columns([
        (pl.col(VarActif.mtVmAv) * pl.col(VarGse.facteurPerfNet)).alias(VarActif.mtVm),
        (pl.col(VarActif.mtVmAv) * pl.col(VarGse.txDividendes)).alias(VarActif.mtPfi),
        (pl.col(VarActif.mtVmAv) * pl.col(VarGse.txDividendes)).alias(VarActif.mtCf),
        pl.lit(0.0).alias(VarActif.mtPdd)
    ]).with_columns([
        calcPmvl().alias(VarActif.mtPmvl),
        calcFuiteEco().alias(VarAlm.mtFuiteEco),
        calcFuiteVcActifPerf().alias(VarAlm.mtFuiteVc)
    ])
    return mpActifIndicesProj.select(dfMdActif.mdMpActifIndicesProj.allColumns)