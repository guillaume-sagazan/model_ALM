from polars import DataFrame
import polars as pl

from domaines.s2.expr.S2Expr import calcMtVmIndicesInitS2
from metadata.dd.DdPassifEp import VarPassif
from metadata.dd.DdS2 import VarS2
from metadata.dfmd.DfMdPassifEp import dfMdPassifEp



def mpPassifEpInitS2Build(mpPassifEpInitGbl : DataFrame ,dfCdChocS2 : DataFrame, hypS2Chocs : DataFrame) -> DataFrame :
    mpPassifEpInitS2 = dfCdChocS2.join(
        mpPassifEpInitGbl,how='cross'
    ).join(
        hypS2Chocs.select([VarS2.cdChocS2,VarS2.txChocProperty,VarS2.txChocEquityT1,VarS2.txChocEquityT2,VarS2.txChocEquityStrat]), how = 'left', on = VarS2.cdChocS2
    ).with_columns(
        calcMtVmIndicesInitS2(colMtVm=VarPassif.mtPmUc,alias = VarPassif.mtPmUc)
    ).select(dfMdPassifEp.mdMpPassifEpInitS2.allColumns)
    return mpPassifEpInitS2