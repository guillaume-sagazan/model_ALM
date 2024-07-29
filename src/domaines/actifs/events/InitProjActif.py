from datetime import datetime
from typing import Tuple

from polars import DataFrame #Je sais pas si c'est de polars ou de datetime cet import, il m'a proposé les deux

from domaines.actifs.ops.MpActifIndicesInitGblBuild import mpActifIndicesInitGblBuild
from domaines.actifs.ops.MpActifIndicesInitProj import mpActifIndicesInitProjBuild
from domaines.actifs.ops.MpActifIndicesInitS2 import mpActifIndicesInitS2Build 


def initProjActif(mpActifIndicesInitS2: DataFrame, scEcoList : list[int]) -> Tuple[DataFrame] :
    return mpActifIndicesInitProjBuild(mpActifIndicesInitS2 = mpActifIndicesInitS2, scEcoList=scEcoList)
    