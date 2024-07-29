from polars import DataFrame

from domaines.s2.expr.S2Expr import calcMtVmIndicesInitS2
from metadata.dd.DdS2 import VarS2


def mpActifIndicesInitS2Build (dfCdChocS2 : DataFrame, mpActifIndicesInitGbl : DataFrame, hypS2Chocs : DataFrame) -> DataFrame :
    mpActifIndicesInitS2 = dfCdChocS2.select(
        [VarS2.cdChocS2,VarS2.cdChocS2Gse]
    ).join(
        mpActifIndicesInitGbl,how='cross'
    ).join(
        hypS2Chocs.select([VarS2.cdChocS2,VarS2.txChocProperty,VarS2.txChocEquityT1,VarS2.txChocEquityT2,VarS2.txChocEquityStrat]), how = 'left', on = VarS2.cdChocS2
    ).with_columns(
        calcMtVmIndicesInitS2()
    )

    return mpActifIndicesInitS2
