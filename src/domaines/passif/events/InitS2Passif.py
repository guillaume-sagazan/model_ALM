from typing import Tuple

from polars import DataFrame



from domaines.passif.ops.MpPassifEpInitS2Build import mpPassifEpInitS2Build



def initS2PassifEp(mpPassifEpInitGbl : DataFrame, hypS2Chocs : DataFrame, dfCdChocS2 : DataFrame) -> DataFrame :
    return mpPassifEpInitS2Build(mpPassifEpInitGbl=mpPassifEpInitGbl,hypS2Chocs=hypS2Chocs,dfCdChocS2=dfCdChocS2)
    