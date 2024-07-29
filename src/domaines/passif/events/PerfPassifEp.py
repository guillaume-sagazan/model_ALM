

from typing import Tuple
from polars import DataFrame

from domaines.passif.ops.MpActifCashInputCfPerfPassifBuild import mpActifCashInputCfPerfPassifBuild
from domaines.passif.ops.MpPassifEpProjCopy import mpPassifEpProjCopy
from domaines.passif.ops.MpPassifEpProjPerfBuild import mpPassifEpProjPerfBuild
from metadata.dd.DdProjection import ModeleAlmEvenement


def perfPassifEp( mpPassifEpProj : DataFrame, mpPassifEpProjHypsPrstT : DataFrame, mpPassifEpProjHypsIcFgxT : DataFrame, period : int) -> Tuple[DataFrame, DataFrame] :
    mpPassifEpProj = mpPassifEpProjCopy(mpPassifEpProj = mpPassifEpProj, period= period, evenement=ModeleAlmEvenement.Perf)

    mpPassifEpProjPerf = mpPassifEpProjPerfBuild(mpPassifEpProj = mpPassifEpProj,
                                                 mpPassifEpProjHypsPrstT = mpPassifEpProjHypsPrstT,
                                                 mpPassifEpProjHypsIcFgxT = mpPassifEpProjHypsIcFgxT) #extension du passifepproj,
    
    mpActifCashInputCfPerfPassif = mpActifCashInputCfPerfPassifBuild(mpPassifEpProjPerf = mpPassifEpProjPerf) 
    
    return mpPassifEpProjPerf, mpActifCashInputCfPerfPassif #,None #On rajoutera une gestion ALM 