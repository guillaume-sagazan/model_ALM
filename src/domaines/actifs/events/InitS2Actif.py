from typing import Tuple

from polars import DataFrame

from domaines.actifs.ops.MpActifIndicesInitS2 import mpActifIndicesInitS2Build 

def initS2Actif(mpActifIndicesInitGbl : DataFrame, dfCdChocS2 : DataFrame, hypS2Chocs : DataFrame) -> Tuple[DataFrame] :
    return mpActifIndicesInitS2Build(mpActifIndicesInitGbl=mpActifIndicesInitGbl,dfCdChocS2=dfCdChocS2,hypS2Chocs=hypS2Chocs)
    