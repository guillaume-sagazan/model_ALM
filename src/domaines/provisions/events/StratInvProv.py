import logging
from typing import Tuple

from polars import DataFrame, LazyFrame


from dao.writers.ResultsWriter import ResultsWriter
from domaines.actif.pipelines.StratInv import projProvOtherStratInv, projProvPpeStratInv
from metadata.dd.DdProjection import ModeleAlmEvenement
from utils.ProjResults import ProjResultRctProjProv, ProjResultPrdAd


def stratInvProv(period:int, projProvOther:DataFrame, projProvPpe:DataFrame, projActifOblig:DataFrame,
                       projResultPrdAd: ProjResultPrdAd
                       ) -> Tuple[DataFrame, DataFrame]:

    logging.info(f'StratInv ({period}) : Provisions')
    projProvOther = projProvOtherStratInv(period=period, projProvOther=projProvOther, projActifOblig=projActifOblig)
    projResultPrdAd.appendOutputPrdAdProjProvOther(projProvOther)

    projProvPpe = projProvPpeStratInv(period=period, projProvPpe=projProvPpe)
    projResultPrdAd.appendOutputPrdAdProjProvPpe(projProvPpe)
    return projProvOther, projProvPpe

def fnProjStratInvProvBH(period:int, projProvOther:DataFrame, projProvPpe:DataFrame,
                       projResultPrdAd: ProjResultPrdAd) -> Tuple[DataFrame, DataFrame]:
    return None, None