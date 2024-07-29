import logging
from typing import Tuple
from polars import DataFrame
import polars as pl
from domaines.gse.ops.GseCashPerfBuild import gseOutputCashPerfBuild
from domaines.gse.ops.GseCtRefObligPzcBuild import gseCtRefObligPzcBuild
from domaines.gse.ops.GseOutputBuildCrn import gseOutputBuildCrn
from domaines.gse.ops.GseOutputDeflateurBuild import gseOutputDeflateurBuild
from domaines.gse.ops.GseOutputIndicesPerfBuild import gseOutputIndicesPerfBuild
from domaines.gse.ops.GseOutputObligPzcBuild import gseOutputObligPzcBuild
from metadata.dd.DdActif import VarActif
from metadata.dd.DdGse import ScUnivers, VarGse
from metadata.dd.DdProjection import IntraPeriod, PerfCash, VarProj
from metadata.dd.DdS2 import VarS2


def initGblGse(gseCtRef : DataFrame,
                  dfCdChocS2 : DataFrame,
                  projHorizon : int,
                  gseObligMaturiteMax : int,
                  gseScUnivers : ScUnivers,
                  gseScEcoList : list[int],
                  gseScCrnAutoBuild : bool,
                  gseOutputObligInput : DataFrame,
                  gseOutputIndicesInput : DataFrame,
                  gseOutputInflationInput : DataFrame,
                     ) -> Tuple[
                         DataFrame, # gseCtRefObligPzc
                         DataFrame, # gseCtRefCashPerf
                         DataFrame, # gseOutputObligPzc
                         DataFrame, # df3
                         DataFrame, # df4
                         DataFrame  # df5
                ]:
    
    """
    
    """

    logging.info("Initialisation : Global : GSE : Construction des variables économiques")
    gseCtRefObligPzc, gseCtRefCashPerf = gseCtRefObligPzcBuild(gseCtRef = gseCtRef, dfCdChocS2 = dfCdChocS2,
                                             projHorizon = projHorizon, gseObligMaturiteMax = gseObligMaturiteMax)

    logging.info("Initialisation : Global : Gse : Construction des variables économiques issues de IGSE")
    if not (gseScUnivers == ScUnivers.RN and gseScEcoList == [1] and gseScCrnAutoBuild):
        gseOutputObligPzc = gseOutputObligPzcBuild(gseOutputObligInput, dfCdChocS2, gseScEcoList,
                                            projHorizon, gseObligMaturiteMax)
        gseOutputIndicesPerf = gseOutputIndicesPerfBuild(gseOutputIndicesInput, dfCdChocS2, gseScEcoList,
                                                  projHorizon)
        gseOutputCashPerf = gseOutputCashPerfBuild(gseOutputObligPzc, projHorizon)
    else:
        gseOutputObligPzc, gseOutputIndicesPerf, gseOutputCashPerf = gseOutputBuildCrn(gseCtRefObligPzc,projHorizon,
                                                                            gseObligMaturiteMax)
           
    gseOutputDeflateur = gseOutputDeflateurBuild(gseOutputObligPzc)

    return gseCtRefObligPzc,gseCtRefCashPerf,gseOutputObligPzc,gseOutputIndicesPerf,gseOutputCashPerf,gseOutputDeflateur
