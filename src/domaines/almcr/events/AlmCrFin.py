from typing import Tuple
import polars as pl
from polars import DataFrame, LazyFrame

from config import ErrConfig
from dao.writers.ResultsWriter import ResultsWriter
from domaines.actif.pipelines.PrdAdActifs import prdAdActifBuild
from domaines.provisions.pipelines.PrdAdBilan import prdAdBilanCalc
from metadata.dd.DdAlm import VarAlm
from metadata.dd.DdCommun import VarCommun, TypeErreur, TypeErreurAction
from outputs.ProjResult import ProjResultRctProjActif, ProjResultPrdAd


def almCrFin(projActifOblig:DataFrame, 
             projActifIndices:DataFrame, 
             projActifCash:DataFrame,
             projPassifEpMp:DataFrame,
             projProvOther:DataFrame, 
             projProvPpe:DataFrame,
             equilibreBilanErrorMax:float,
             projResultRctProjActif: ProjResultRctProjActif,
             projResultPrdAd: ProjResultPrdAd,
            ) -> Tuple[DataFrame, DataFrame, DataFrame, DataFrame]:

    projActifAlmCrT = pl.concat([projActifOblig, projActifIndices, projActifCash])
    projResultRctProjActif.appendOutputRctProjProjActif(projActifAlmCrT)

    # Constitution du prdAdActifAlmCr
    prdAdActifAlmCrT = prdAdActifBuild(projActifAlmCrT)
    projResultPrdAd.appendOutputPrdAdActif(prdAdActifAlmCrT)

    # Construction du bilan
    prdAdBilanT = prdAdBilanCalc(projActifOblig=projActifOblig, 
                                 projActifCash=projActifCash,
                                 projActifIndices=projActifIndices,
                                 projPassifEpMp=projPassifEpMp,
                                 projProvOther=projProvOther, 
                                 projProvPpe=projProvPpe)

    projResultPrdAd.appendOutputPrdAdBilan(prdAdBilanT)

    erreursPrdAdBilanT = prdAdBilanT.filter(
        pl.col(VarAlm.mtFuiteVc).abs() > equilibreBilanErrorMax
    ).with_columns([
        pl.lit('Fuite Valeur Comptable > equilibreBilanErrorMax').alias(VarCommun.erreur),
        pl.lit(TypeErreur.Erreur).alias(VarCommun.typeErreur),
        pl.lit(TypeErreurAction.NePasUtiliserLesResultats).alias(VarCommun.typeErreurAction)
    ])
    
    projResultPrdAd.appendOutputErreursProjPrdAdBilan(erreursPrdAdBilanT)

    return projActifAlmCrT, prdAdActifAlmCrT, prdAdBilanT, erreursPrdAdBilanT

def almCrFinBH(projActifOblig:DataFrame, 
               projActifIndices:DataFrame, 
               projActifCash:DataFrame,
               projPassifEpMp:DataFrame,
               projProvOther:DataFrame, 
               projProvPpe:DataFrame,
               errCfg:ErrConfig,
               projResultRctProjActif: ProjResultRctProjActif,
               projResultPrdAd: ProjResultPrdAd,
               ) -> Tuple[DataFrame,DataFrame,DataFrame,DataFrame]:
    
    return None,None,None,None
    