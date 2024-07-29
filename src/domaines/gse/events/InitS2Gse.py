import logging
from typing import Tuple
import polars as pl
from polars import DataFrame


from metadata.dd.DdGse import VarGse
from metadata.dd.DdProjection import VarProj
from metadata.dd.DdS2 import CdChocS2, VarS2


def initS2Gse(dfCdChocS2 : DataFrame, hypS2Chocs : DataFrame, gseCtRefObligPzc:DataFrame, gseOutputInflationInput : DataFrame) -> Tuple[DataFrame, DataFrame]:
    
    logging.info("Initialisation : ChocS2 : Gse : Definition de gseCtRefObligPzcRN et gseCtRefCashPerfFuiteEco, application des chocs sur l'inflation")
    
    gseCtRefObligPzcCentral = gseCtRefObligPzc.filter(pl.col(VarS2.cdChocS2Gse) == CdChocS2.central)#.drop(VarS2.cdChocS2Gse)

    gseOutputInflationInitS2 = dfCdChocS2.join(
        hypS2Chocs,
        how='left',
        on = VarS2.cdChocS2                    
    ).select([VarS2.cdChocS2Gse, 
        VarS2.cdChocS2PassifIcFgx, 
        VarS2.txChocExpenseInflation]
    ).join(
        gseOutputInflationInput,
        on=VarS2.cdChocS2Gse,
        how='left'
    ).with_columns(
        pl.when(pl.col(VarS2.cdChocS2PassifIcFgx) == CdChocS2.expense)
        .then(pl.col(VarGse.txInflation) + pl.col(VarS2.txChocExpenseInflation))
        .otherwise(pl.col(VarGse.txInflation))
        .alias(VarGse.facteurInflationCum)
    ).with_columns((1.0 + pl.col(VarGse.txInflation)
                    ).alias(VarGse.facteurInflationCum)
    ).with_columns(pl.col(VarGse.facteurInflationCum).cum_prod().over([VarS2.cdChocS2PassifIcFgx,VarProj.scenario]).alias(VarGse.facteurInflationCum))
    
    return gseCtRefObligPzcCentral, gseOutputInflationInitS2

