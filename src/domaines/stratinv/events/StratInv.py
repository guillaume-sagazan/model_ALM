

import logging
from typing import Tuple
from domaines.actifs.ops.MpActifProjStratInv import mpActifProjStratInvApplyFacteurAchatVente
from domaines.stratinv.ops.StratInvAlgo import stratInvInputOutputBuild
from polars import DataFrame
from metadata.dfmd.DfMdActif import dfMdActif

def stratInv(period:int, dfCdChocS2Sc:DataFrame,  mpActifIndicesProj:DataFrame, hypStratInvTxAllocCible:DataFrame) -> Tuple[DataFrame,DataFrame]:

    logging.info(f'StratInv ({period}) : Algo')
    stratInvInputOutput = stratInvInputOutputBuild(period = period,
                                                   dfCdChocS2Sc=dfCdChocS2Sc,
                                                   hypStratInvTxAllocCible=hypStratInvTxAllocCible,
                                                   mpActifIndicesProj=mpActifIndicesProj)
    
    mpActifIndicesProj = mpActifProjStratInvApplyFacteurAchatVente(
        mpActifProj=mpActifIndicesProj,
        stratInvInputOutput=stratInvInputOutput,
        period=period
    ).select(
        dfMdActif.mdMpActifIndicesProj.allColumns
    )

    return stratInvInputOutput,mpActifIndicesProj