from polars import DataFrame
import polars as pl
from domaines.s2.expr.S2Expr import calcMtVmIndicesInitS2
from metadata.dd.DdActif import VarActif
from metadata.dd.DdAlm import VarAlm
from metadata.dd.DdProjection import ModeleAlmEvenement, VarProj
from metadata.dd.DdS2 import VarS2


def mpActifProjCopy (period : int, evenement : ModeleAlmEvenement,mpActifProj : DataFrame, ) -> DataFrame :
    mpActifProj = mpActifProj.with_columns([
        pl.lit(period).alias(VarProj.period),
        pl.lit(evenement).cast(pl.Categorical).alias(VarProj.evenement),
        pl.col(VarActif.mtVm).alias(VarActif.mtVmAv),
        pl.col(VarActif.mtVc).alias(VarActif.mtVcAv),    
        pl.lit(0.0).alias(VarActif.mtPdd),
        pl.lit(0.0).alias(VarActif.mtPfi),
        pl.lit(0.0).alias(VarActif.mtCf),
        pl.lit(0.0).alias(VarActif.mtPmvl),
        pl.lit(0.0).alias(VarAlm.mtFuiteEco),
        pl.lit(0.0).alias(VarAlm.mtFuiteVc)
    ])
    return mpActifProj

