from polars import DataFrame

from domaines.actifs.ops.MpActifIndicesPerf import mpActifIndicesPerf


def perfActif (period : int, mpActifIndicesProj : DataFrame, gseCtRefCashPerfT : DataFrame, gseOutputIndicesPerfT : DataFrame) -> DataFrame :
    mpActifIndicesProj = mpActifIndicesPerf(
        period=period,
        mpActifIndicesProj=mpActifIndicesProj,
        gseCtRefCashPerfT=gseCtRefCashPerfT,
        gseOutputIndicesPerfT=gseOutputIndicesPerfT,
    )
    
    return mpActifIndicesProj