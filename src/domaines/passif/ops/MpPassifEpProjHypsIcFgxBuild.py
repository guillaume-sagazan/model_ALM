import polars as pl
from polars import DataFrame
from metadata.dd.DdActif import CdClasseActif, VarActif
from metadata.dd.DdGse import VarGse
from metadata.dd.DdPassifEp import VarPassif
from metadata.dd.DdProjection import VarProj
from metadata.dfmd.DfMdGse import dfMdGse
from metadata.dfmd.DfMdPassifEp import dfMdPassifEp

def mpPassifEpProjHypsIcFgxBuild(projHorizonList : list[int], mpPassifEpProj : DataFrame,
                                hypPassifEpFgx : DataFrame,
                                gseOutputIndicesPerfT : DataFrame,
                                gseOutputInflationInitS2T : DataFrame) -> DataFrame :

    mpPassifEpProjHypsIcFgx = mpPassifEpProj.with_columns(
        pl.lit(projHorizonList).alias(VarProj.period)
    ).explode(VarProj.period
    ).with_columns(pl.col(VarProj.period).cast(pl.Int32)
    ).join(
        hypPassifEpFgx, 
        how = "left", 
        on= dfMdPassifEp.mdHypPassifEpFgx.pks
    ).with_columns(
        pl.lit(CdClasseActif.ACTION).alias(VarActif.cdClasseActif)
    ).join(
        gseOutputIndicesPerfT.select([*dfMdGse.mdGseOutputIndicesPerf.pks,VarGse.facteurPerfTot]), 
        how = "left",
        on= dfMdGse.mdGseOutputIndicesPerf.pks  
    ).rename(
        {VarGse.facteurPerfTot : VarGse.facteurPerfTot+"_action"} # WARNING : On n'utilise pas la fonction suffixe ici car elle ne rajoute pas en suffixe si la colonne n'existe pas déjà
    ).with_columns(
        pl.lit(CdClasseActif.IMMOBILIER).alias(VarActif.cdClasseActif)
    ).join(
        gseOutputIndicesPerfT.select([*dfMdGse.mdGseOutputIndicesPerf.pks,VarGse.facteurPerfTot]), 
        how = "left",
        on= dfMdGse.mdGseOutputIndicesPerf.pks
    ).rename(
        {VarGse.facteurPerfTot : VarGse.facteurPerfTot+"_immo"} 
    ).with_columns(
        (
            (pl.col(VarActif.txActionT1)+pl.col(VarActif.txActionT2)+pl.col(VarActif.txActionStrat)) * pl.col(VarGse.facteurPerfTot+"_action")
            + (VarActif.txImmobilier) * pl.col(VarGse.facteurPerfTot+"_immo")
        ).alias(VarPassif.txIcUc)
    ).with_columns([
        pl.col(VarPassif.tmg).alias(VarPassif.txIcEu),
        pl.col(VarPassif.tmgBrt).alias(VarPassif.txIcEuBrt),
    ]
    ).with_columns([
        (((pl.col(VarPassif.txIcEu)+1)**0.5)-1).alias(VarPassif.txIcEuDemiPeriode),
        (((pl.col(VarPassif.txIcUc)+1)**0.5)-1).alias(VarPassif.txIcUcDemiPeriode),
        (((pl.col(VarPassif.txIcEuBrt)+1)**0.5)-1).alias(VarPassif.txIcEuBrtDemiPeriode),
    ]).join(
        gseOutputInflationInitS2T,
        how = "left",
        on = dfMdGse.mdGseOutputInflationInitS2.pks 
    ).select(dfMdPassifEp.mdMpPassifEpProjHypsIcFgx.allColumns)

    return mpPassifEpProjHypsIcFgx
