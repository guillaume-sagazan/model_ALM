import polars as pl
from polars import DataFrame

from metadata.dd.DdPassifEp import VarPassif
from metadata.dd.DdProjection import VarProj
from metadata.dfmd.DfMdPassifEp import dfMdPassifEp


def mpPassifEpProjHypsPrstBuild(projHorizonList : list[int], mpPassifEpProj : DataFrame, hypPassifEpPrstRt : DataFrame, hypMortGen : DataFrame, hypMort : DataFrame) -> DataFrame :
    
    mpPassifEpProjHypsPrst = mpPassifEpProj.with_columns(
        pl.lit(projHorizonList).alias(VarProj.period)
    ).explode(VarProj.period
    ).with_columns(pl.col(VarProj.period).cast(pl.Int32)
    ).with_columns(
        (pl.col(VarPassif.nbAsseAgeMois)+pl.col(VarProj.period)*12).alias(VarPassif.nbAsseAgeMois),
        (pl.col(VarPassif.nbCntAncienneteMois)+pl.col(VarProj.period)*12).alias(VarPassif.nbCntAncienneteMois),
        (pl.col(VarPassif.nbAsseAgeAnnee)+pl.col(VarProj.period)).alias(VarPassif.nbAsseAgeAnnee),
        (pl.col(VarPassif.nbCntAncienneteAnnee)+pl.col(VarProj.period)).alias(VarPassif.nbCntAncienneteAnnee)
    ).join(
        hypPassifEpPrstRt, 
        how = "left", 
        left_on= [VarPassif.nbCntAncienneteAnnee, VarPassif.cdPrstRtCat],
        right_on= dfMdPassifEp.mdHypPassifEpPrstRt.pks
    ).join(
        hypMort, 
        how = "left", 
        left_on = [VarPassif.cdHypMortExp,VarPassif.cdAsseSexe,VarPassif.nbAsseAgeAnnee],
        right_on= dfMdPassifEp.mdHypMort.pksWithCdTable,
    ).join(
        hypMortGen, 
        how = "left",
        left_on = [VarPassif.cdHypMortExp,VarPassif.generation,VarPassif.cdAsseSexe,VarPassif.nbAsseAgeAnnee],
        right_on= dfMdPassifEp.mdHypMortGen.pksWithCdTable,
        suffix="_gen"
    ).with_columns(
        (pl.col(VarPassif.qx).fill_null(pl.col(VarPassif.qx + "_gen"))) #Modification du when pour simplifier
        .alias(VarPassif.txPrstDcAsseExp)
    ).select(dfMdPassifEp.mdMpPassifEpProjHypsPrst.allColumns)


    # TODO : Gestion d'erreurs si il reste des null

    return mpPassifEpProjHypsPrst