from polars import DataFrame
import polars as pl
from domaines.s2.expr.S2Expr import calcMtVmIndicesInitS2
from metadata.dd.DdActif import VarActif
from metadata.dd.DdAlm import VarAlm
from metadata.dd.DdPassifEp import VarPassif
from metadata.dd.DdProjection import ModeleAlmEvenement, VarProj
from metadata.dd.DdS2 import VarS2
from metadata.dfmd.DfMdPassifEp import dfMdPassifEp

def mpPassifEpProjCopy (period : int, evenement : ModeleAlmEvenement,mpPassifEpProj : DataFrame ) -> DataFrame : # TODO : à relire vite fait
    mpPassifEpProj = mpPassifEpProj.with_columns([
        pl.lit(period).alias(VarProj.period),
        pl.lit(evenement).cast(pl.Categorical).alias(VarProj.evenement),
        pl.col(VarPassif.mtPmEu).alias(VarPassif.mtPmEuAv),
        pl.col(VarPassif.mtPmUc).alias(VarPassif.mtPmUcAv),  
        pl.col(VarPassif.nbCnt).alias(VarPassif.nbCntAv)
    ]).select(dfMdPassifEp.mdMpPassifEpProj.allColumns)
    
    return mpPassifEpProj
