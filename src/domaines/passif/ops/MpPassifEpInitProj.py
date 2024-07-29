from polars import DataFrame
import polars as pl
from domaines.actifs.expr.ActifsExpr import calcPmvl
from domaines.s2.expr.S2Expr import calcMtVmIndicesInitS2
from metadata.dd.DdActif import VarActif
from metadata.dd.DdAlm import VarAlm
from metadata.dd.DdPassifEp import VarPassif
from metadata.dd.DdProjection import ModeleAlmEvenement, VarProj
from metadata.dfmd.DfMdPassifEp import dfMdPassifEp


def mpPassifEpInitProjBuild ( mpPassifEpInit : DataFrame, scEcoList : list[int]) -> DataFrame :
    mpPassifEpInitProj = mpPassifEpInit.with_columns([
        pl.lit(scEcoList).alias(VarProj.scenario),
        pl.lit(0).alias(VarProj.period),
        pl.lit(ModeleAlmEvenement.Init).cast(pl.Categorical).alias(VarProj.evenement),
        pl.lit(0.0).alias(VarPassif.mtPmUcAv), ### J'ai enlevé tous les Av
        pl.lit(0.0).alias(VarPassif.mtPmEuAv),
        pl.lit(0.0).alias(VarPassif.nbCntAv),
    ]).explode(VarProj.scenario) \
    .with_columns(pl.col(VarProj.scenario).cast(pl.Int32))
 
    return mpPassifEpInitProj[dfMdPassifEp.mdMpPassifEpProj.allColumns]

