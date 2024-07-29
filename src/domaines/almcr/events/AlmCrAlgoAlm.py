import logging
from typing import Tuple

import polars as pl
from polars import DataFrame, LazyFrame


from domaines.almcr.pipelines.AlmCrAlgoOutput import buildStratAlmOutput
from domaines.almcr.pipelines.AlmCrAlgoUtils import almCrAlmOutputPassifFromTxServiBrt
from domaines.s2.pipelines.ModeleAlmPrdQrt import prdAdCr2PrdQrtBeScPeriodTypeFluxCf
from dao.writers.ResultsWriter import ResultsWriter
from metadata.dd.DdAlm import VarAlm
from metadata.dd.DdCommun import VarCommun
from metadata.dd.DdProjection import ModeleAlmEvenement, VarProj
from metadata.dfmd.DfMdAlmCr import DfMdAlm
from outputs.ProjResult import ProjResultRctProjAlmCr, ProjResultPrdAd, ProjResultPrdQrt


def almCrAlgoAlm(almCrInputPassif:DataFrame,
                    almCrInputActif:DataFrame,
                    almCrInputPpe:DataFrame,
                    almCrInputTxServiCible:DataFrame,
                    prdAdPassifPerf:DataFrame,
                    projResultRctProjAlmCr: ProjResultRctProjAlmCr,
                    projResultPrdAd: ProjResultPrdAd,
                    projResultPrdQrt: ProjResultPrdQrt
                    ) -> Tuple[DataFrame, DataFrame]: 

    almCrAlmOutputAll = buildStratAlmOutput(
        almCrInputPassif=almCrInputPassif,
        almCrInputActif=almCrInputActif,
        almCrInputPpe=almCrInputPpe,
        almCrInputTxServiCible=almCrInputTxServiCible,
        prdAdPassifPerf=prdAdPassifPerf.filter(pl.col(VarCommun.cdCanton) != 'UC'),
    )

    projResultRctProjAlmCr.appendOutputRctAlmCrAlmOutput(almCrAlmOutputAll)

    # Sélection du strat alm cas optimal
    almCrAlmOutput = almCrAlmOutputAll.filter(
        pl.col(VarAlm.mtResBrt) > 0
    ).with_columns(
        pl.col(VarAlm.stratAlmCasPriorite).max().over(set(dfMdAlmCr.mdAlmCrAlmOutput.allColumns) - {VarAlm.stratAlmCas}).alias(VarAlm.stratAlmCasPriorite + '_max')
    ).filter(
        pl.col(VarAlm.stratAlmCasPriorite) == pl.col(VarAlm.stratAlmCasPriorite + '_max')
    )

    prdAdAlmCr = almCrAlmOutput.select(
        set(dfMdAlmCr.mdPrdAdAlmCr.allColumns) & set(dfMdAlmCr.mdAlmCrAlmOutput.allColumns)
    ).with_columns(
        pl.lit(ModeleAlmEvenement.AlmCr).cast(pl.Categorical).alias(VarProj.evenement),
    )
    
    projResultPrdAd.appendOutputPrdAlmCrAlmOutput(almCrAlmOutput)
    projResultPrdAd.appendOutputPrdAdAlmCr(prdAdAlmCr)
    projResultPrdQrt.appendOutputPrdQrtBeCf(prdAdCr2PrdQrtBeScPeriodTypeFluxCf(prdAdAlmCr))

    return almCrAlmOutput, prdAdAlmCr

def almCrAlgoAlmBH(almCrInputPassif:DataFrame,
                        almCrInputActif:DataFrame,
                        almCrInputTxServiBrt:DataFrame,
                        prdAdCrMrgTech:DataFrame,
                        projResultRctProjAlmCr: ProjResultRctProjAlmCr,
                        projResultPrdAd: ProjResultPrdAd,) -> Tuple[DataFrame, DataFrame]:
    return None, None, None, None, None, None