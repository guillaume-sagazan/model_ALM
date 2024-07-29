
from datetime import date
from typing import Tuple
from polars import DataFrame
import polars as pl

from domaines.passif.expr.PassifExpr import calcAgeMois
from metadata.dd.DdPassifEp import VarPassif
from metadata.dd.DdProjection import VarProj
from metadata.dfmd.DfMdPassifEp import dfMdPassifEp


def mpPassifEpInitGblBuild(mpPassifEp : DataFrame, projDateDebut : date ) ->  DataFrame :
    mpPassifEpInitGbl = mpPassifEp.with_columns(
            pl.lit(projDateDebut).alias(VarProj.projDateDebut)
    ).with_columns(
            calcAgeMois(colDate=VarProj.projDateDebut,
                        colDateRef=VarPassif.dtAsseNaiss,
                        alias=VarPassif.nbAsseAgeMois)
    ).with_columns(
            (pl.col(VarPassif.nbAsseAgeMois)//12
        ).alias(VarPassif.nbAsseAgeAnnee) 
    ).with_columns(
            calcAgeMois(colDate=VarProj.projDateDebut,
                        colDateRef=VarPassif.dtCntEffet,
                        alias=VarPassif.nbCntAncienneteMois)
    ).with_columns(
            (pl.col(VarPassif.nbCntAncienneteMois)//12
        ).alias(VarPassif.nbCntAncienneteAnnee) 
    ).with_columns(
            ((pl.col(VarPassif.tmg)+pl.col(VarPassif.tfgse))/pl.col(VarPassif.taf)).alias(VarPassif.tmgBrt)
    ).with_columns(
        pl.col(VarPassif.dtAsseNaiss).dt.year().alias(VarPassif.generation)
    )


    # TODO : Améliorer la gestion d'erreur pour report l'erreur à l'utilisateur

    return mpPassifEpInitGbl