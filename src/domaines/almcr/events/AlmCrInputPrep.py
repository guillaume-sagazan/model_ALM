from typing import Tuple
import polars as pl
from polars import DataFrame, LazyFrame

from domaines.almcr.pipelines.AlmCrAlgoUtils import buildAlmCrInputActif, buildAlmCrInputTxServiCible
from metadata.dd.DdAlm import VarAlm
from metadata.dfmd.DfMdAlmCr import DfMdAlm
from outputs.ProjResult import ProjResultRctProjAlmCr


def almCrInputs(period:int,
                    projActifPerfT:DataFrame, projActifStratInvT:DataFrame,
                    projProvOther:DataFrame, projProvPpe:DataFrame,
                    hypStratAlmCr:DataFrame, hypStratAlmTxServi:DataFrame,
                    hypStratInvTxFraisPlct : DataFrame,
                    gseOutputObligPzcT:DataFrame,
                    projResultRctProjAlmCr: ProjResultRctProjAlmCr
                    ) -> Tuple[DataFrame, DataFrame, DataFrame]:

    almCrInputActif = buildAlmCrInputActif(projActifPerfT=projActifPerfT,
                                                 projActifStratInvT=projActifStratInvT,
                                                 projProvOther=projProvOther,
                                                 hypStratInvTxFraisPlct=hypStratInvTxFraisPlct,
                                                 hypStratAlmCr=hypStratAlmCr
                                                 )

    almCrInputTxServiCible = buildAlmCrInputTxServiCible(
        almCrInputActif=almCrInputActif, 
        hypStratAlmTxServi=hypStratAlmTxServi, 
        gseOutputObligPzcT=gseOutputObligPzcT
    )

    almCrInputPpe = projProvPpe.with_columns([
        pl.when(pl.col(VarAlm.nbPpeGeneration) == pl.col(VarAlm.nbPpeGenerationMax))
        .then(pl.col(VarAlm.mtPpe))
        .otherwise(pl.lit(0.0))
        .alias(VarAlm.mtPpeReprise),
        pl.when(pl.col(VarAlm.nbPpeGeneration) != pl.col(VarAlm.nbPpeGenerationMax))
        .then(pl.col(VarAlm.mtPpe))
        .otherwise(pl.lit(0.0))
        .alias(VarAlm.mtPpeDispo),
    ]).select([*dfMdAlmCr.mdAlmCrInputActif.pks, VarAlm.mtPpeDispo, VarAlm.mtPpeReprise]).group_by(dfMdAlmCr.mdAlmCrInputActif.pks).sum()

    prdAdCrSoldeTechPks = [*dfMdAlmCr.mdPrdAdAlmCr.pks]
    prdAdCrSoldeTechPks.remove(VarAlm.stratAlmCas)

    projResultRctProjAlmCr.appendOutputRctProjStratAlmInputActif(almCrInputActif=almCrInputActif)
    projResultRctProjAlmCr.appendOutputRctProjStratAlmInputTxServiCible(
        almCrInputTxServiCible=almCrInputTxServiCible
    )

    return almCrInputActif, almCrInputPpe, almCrInputTxServiCible

def almCrInputsBH(period:int,
                    projActifPerfT:DataFrame, projActifStratInvT:DataFrame,
                    projProvOther:DataFrame, projProvPpe:DataFrame,
                    hypStratAlmCr:DataFrame, hypStratAlmTxServi:DataFrame,
                    hypStratInvTxFraisPlct : DataFrame,
                    gseOutputObligPzcT:DataFrame,
                    projResultRctProjAlmCr: ProjResultRctProjAlmCr
                    ) -> Tuple[DataFrame, DataFrame, DataFrame]:

    return None, None, None
