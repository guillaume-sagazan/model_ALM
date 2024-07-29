from datetime import datetime
from typing import Tuple

from polars import DataFrame

from domaines.passif.ops.MpPassifEpInitProj import mpPassifEpInitProjBuild
from domaines.passif.ops.MpPassifEpProjHypsIcFgxBuild import mpPassifEpProjHypsIcFgxBuild
from domaines.passif.ops.MpPassifEpProjHypsPrstBuild import mpPassifEpProjHypsPrstBuild 



def initProjPassifEp(mpPassifEpInitS2 : DataFrame,  scEcoList : list[int], projHorizonList : list[int], hypPassifEpFgx : DataFrame,gseOutputInflationInitS2 : DataFrame , hypPassifEpPrstRt : DataFrame,hypMortGen : DataFrame,hypMort : DataFrame, gseOutputIndicesPerfT : DataFrame) -> Tuple[DataFrame, DataFrame, DataFrame] :
    mpPassifEpProj = mpPassifEpInitProjBuild(mpPassifEpInit = mpPassifEpInitS2, scEcoList=scEcoList)
    mpPassifEpProjHypsPrst = mpPassifEpProjHypsPrstBuild(projHorizonList=projHorizonList, mpPassifEpProj=mpPassifEpProj, hypPassifEpPrstRt =hypPassifEpPrstRt, hypMortGen=hypMortGen, hypMort=hypMort)
    mpPassifEpProjIcFgx = mpPassifEpProjHypsIcFgxBuild(projHorizonList=projHorizonList, mpPassifEpProj=mpPassifEpProj, hypPassifEpFgx = hypPassifEpFgx, gseOutputIndicesPerfT=gseOutputIndicesPerfT, gseOutputInflationInitS2T=gseOutputInflationInitS2)
    return mpPassifEpProj,mpPassifEpProjHypsPrst, mpPassifEpProjIcFgx
    