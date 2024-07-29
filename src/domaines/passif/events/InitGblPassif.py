from datetime import date, datetime
from typing import Tuple

from polars import DataFrame

from domaines.passif.ops.MpPassifEpInitGblBuild import mpPassifEpInitGblBuild
from metadata.dd.DdProjection import VarProj 

def initGblPassif(mpPassifEp : DataFrame, projDateDebut : date) -> DataFrame :
    # TODO : Intégrer MpPassifEpErreurs
    return mpPassifEpInitGblBuild(mpPassifEp = mpPassifEp, projDateDebut=projDateDebut)
    