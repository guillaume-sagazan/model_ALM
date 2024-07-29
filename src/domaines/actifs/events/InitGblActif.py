from typing import Tuple

from polars import DataFrame 
from domaines.actifs.ops.MpActifIndicesInitGblBuild import mpActifIndicesInitGblBuild 


def initGblActif(mpActifIndices : DataFrame) -> Tuple[DataFrame] :
    
    return mpActifIndicesInitGblBuild(mpActifIndices)
    