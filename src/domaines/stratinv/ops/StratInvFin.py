import logging
from typing import Tuple

import polars as pl
from polars import DataFrame, LazyFrame

from domaines.actif.pipelines.PrdAdActifs import prdAdActifBuild
from metadata.dd.DdProjection import ModeleAlmEvenement
from utils.ProjResults import ProjResultRctProjActif, ProjResultPrdAd


def stratInvFin(
        period:int,
        projActifObligCf:DataFrame, projActifOblig:DataFrame, projActifIndices:DataFrame, projActifCash:DataFrame,
        stratInvInputOutput : DataFrame,
        projResultRctProjActif:ProjResultRctProjActif,
        projResultPrdAd:ProjResultPrdAd
        ) -> Tuple[DataFrame, DataFrame]:

    logging.info(f'StratInv ({period}) : Fin')
    projActifStratInvT = pl.concat([projActifOblig, projActifIndices, projActifCash])
    projResultRctProjActif.appendOutputRctProjProjActif(projActifStratInvT)

    prdAdActifStratInvT = prdAdActifBuild(projActifStratInvT)
    projResultPrdAd.appendOutputPrdAdActif(prdAdActifStratInvT)

    projResultRctProjActif.appendOutputRctProjActifObligCf(projActifObligCf=projActifObligCf,
                                                 period=period, evenement=ModeleAlmEvenement.StratInv)

    return projActifStratInvT, prdAdActifStratInvT


def fnProjStratInvFinBH(
        period: int,
        projActifObligCf: DataFrame, projActifOblig: DataFrame, projActifIndices: DataFrame, projActifCash: DataFrame,
        projResultRctProjActif: ProjResultRctProjActif,
        projResultPrdAd: ProjResultPrdAd) -> Tuple[DataFrame, DataFrame]:

    return None, None
