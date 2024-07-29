
from typing import Tuple
from polars import DataFrame
import polars as pl
from domaines.actifs.expr.ActifsExpr import calcPmvl, rsMpActifIndicesTxActionSommeNEq1
from metadata.dd.DdActif import VarActif


def mpActifIndicesInitGblBuild(mpActifIndicesInput : DataFrame ) ->  Tuple[DataFrame,DataFrame] :
    mpActifIndicesInitGbl = mpActifIndicesInput.with_columns([
        calcPmvl().alias(VarActif.mtPmvl)
    ]
    )
    mpActifIndicesErreurs = mpActifIndicesInitGbl.filter(rsMpActifIndicesTxActionSommeNEq1())
    mpActifIndicesInitGbl = mpActifIndicesInitGbl.filter(~rsMpActifIndicesTxActionSommeNEq1())
    
    # TODO : Améliorer la gestion d'erreur pour report l'erreur à l'utilisateur

    return mpActifIndicesInitGbl,mpActifIndicesErreurs