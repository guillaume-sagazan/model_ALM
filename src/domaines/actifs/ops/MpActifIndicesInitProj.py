from polars import DataFrame
import polars as pl
from domaines.actifs.expr.ActifsExpr import calcPmvl
from domaines.s2.expr.S2Expr import calcMtVmIndicesInitS2
from metadata.dd.DdActif import VarActif
from metadata.dd.DdAlm import VarAlm
from metadata.dd.DdProjection import ModeleAlmEvenement, VarProj
from metadata.dd.DdS2 import VarS2
from metadata.dfmd.DfMdActif import dfMdActif


def mpActifIndicesInitProjBuild ( mpActifIndicesInitS2 : DataFrame, scEcoList : list[int]) -> DataFrame :
    mpActifIndicesProj = mpActifIndicesInitS2.with_columns([
        pl.lit(scEcoList).alias(VarProj.scenario),
        pl.lit(0).alias(VarProj.period),
        pl.lit(ModeleAlmEvenement.Init).cast(pl.Categorical).alias(VarProj.evenement),
        pl.lit(0.0).alias(VarActif.mtVmAv),
        pl.lit(0.0).alias(VarActif.mtVcAv),
        pl.lit(0.0).alias(VarActif.mtPfi),
        pl.lit(0.0).alias(VarActif.mtCf),
        pl.lit(0.0).alias(VarAlm.mtFuiteEco),
        pl.lit(0.0).alias(VarAlm.mtFuiteVc)      
    ]).explode(VarProj.scenario) \
    .with_columns(pl.col(VarProj.scenario).cast(pl.Int32))
 
    return mpActifIndicesProj[dfMdActif.mdMpActifIndicesProj.allColumns]

