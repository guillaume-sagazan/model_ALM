import polars as pl

from metadata.dd.DdActif import CdClasseActif, VarActif
from metadata.dd.DdGse import VarGse
from metadata.dd.DdProjection import VarProj
from metadata.dd.DdS2 import CdChocS2, VarS2

def rsCdChocS2PrstLapseMass() -> pl.Expr:
    return (pl.col(VarProj.period) == 1) & (pl.col(VarS2.cdChocS2PassifPrst) == CdChocS2.lapseMass)

def rsCdChocS2PrstLapseUpDown() -> pl.Expr:
    return (pl.col(VarS2.cdChocS2PassifPrst) == CdChocS2.lapseUp) | (pl.col(VarS2.cdChocS2PassifPrst) == CdChocS2.lapseDown)

def rsCdChocS2PrstMort() -> pl.Expr:
    return (pl.col(VarS2.cdChocS2PassifPrst) == CdChocS2.mortality)

def rsCdChocS2PrstMortCat() -> pl.Expr:
    return (pl.col(VarS2.cdChocS2PassifPrst) == CdChocS2.mortalityCat)

def rsCdChocS2PrstLong() -> pl.Expr:
    return (pl.col(VarS2.cdChocS2PassifPrst) == CdChocS2.longevity)

def rsCdChocS2Equity() -> pl.Expr:
    return pl.col(VarS2.cdChocS2) == CdChocS2.equity

def rsCdChocS2Property() -> pl.Expr:
    return pl.col(VarS2.cdChocS2) == CdChocS2.property

def rsCdChocS2Expense() -> pl.Expr:
    return pl.col(VarS2.cdChocS2) == CdChocS2.expense

def rsCdChocS2PassifIcFgxExpense() -> pl.Expr:
    return pl.col(VarS2.cdChocS2PassifIcFgx) == CdChocS2.expense

def rsCdChocS2CdClasseActifAction() -> pl.Expr:
    return (pl.col(VarS2.cdChocS2) == CdChocS2.equity) & \
                     (pl.col(VarActif.cdClasseActif) == CdClasseActif.ACTION)

def rsCdChocS2CdClasseActifImmo() -> pl.Expr:
    return (pl.col(VarS2.cdChocS2) == CdChocS2.property) & \
                (pl.col(VarActif.cdClasseActif) == CdClasseActif.IMMOBILIER)

def rsCdClasseActifDetailSecuPublic() -> pl.Expr:
    return (pl.col(VarActif.cdClasseActifDetail) == 'SECURISEEPUBLIC')

def rsCdClasseActifDetailOther() -> pl.Expr:
    return (~rsCdClasseActifDetailSecuPublic())

def rsCdClasseActifDetailSecuPublicDurationMin5() -> pl.Expr:
    return (rsCdClasseActifDetailSecuPublic()) & (pl.col(VarActif.nbDuration) >= 5)

def rsCdClasseActifDetailSecuPublicDurationMin0() -> pl.Expr:
    return (rsCdClasseActifDetailSecuPublic()) & (~rsCdClasseActifDetailSecuPublicDurationMin5())

def rsCdClasseActifDetailOtherDurationMin5() -> pl.Expr:
    return (rsCdClasseActifDetailOther()) & (pl.col(VarActif.nbDuration) >= 5) & (pl.col(VarActif.nbDuration) < 10)

def rsCdClasseActifDetailOtherDurationMin10() -> pl.Expr:
    return (rsCdClasseActifDetailOther()) & (pl.col(VarActif.nbDuration) >= 10) & (pl.col(VarActif.nbDuration) < 20)

def rsCdClasseActifDetailOtherDurationMin20() -> pl.Expr:
    return (rsCdClasseActifDetailOther()) & (pl.col(VarActif.nbDuration) >= 20)

def rsCdClasseActifDetailOtherDurationMin0() -> pl.Expr:
    return (rsCdClasseActifDetailOther()) & (~rsCdClasseActifDetailOtherDurationMin5()) & (~rsCdClasseActifDetailOtherDurationMin10()) & (~rsCdClasseActifDetailOtherDurationMin20())

def calcQxChocS2Mortality(colQx : str) -> pl.Expr:
    return pl.col(colQx) * (1.0 + pl.col(VarS2.txChocMort))

def calcQxChocS2MortalityCat(colQx : str) -> pl.Expr:
    return pl.col(colQx) * pl.col(VarS2.txChocMortCat)

def calcQxChocS2Longevity(colQx : str) -> pl.Expr:
    return pl.col(colQx) * (1.0 + pl.col(VarS2.txChocLongevity)) 

def calcTxPrstRtChocS2LapseUpDown(colTxPrstRt : str) -> pl.Expr:
    return pl.col(colTxPrstRt) * (1.0 + pl.col(VarS2.txChocLapse))

def calcMtVmChocEquity(colMtVm : str = VarActif.mtVm, alias : str = VarActif.mtVm) -> pl.Expr:
    expr = pl.col(colMtVm) * (
        1.
        + pl.col(VarS2.txChocEquityT1) * pl.col(VarActif.txActionT1)
        + pl.col(VarS2.txChocEquityT2) * pl.col(VarActif.txActionT2)
        + pl.col(VarS2.txChocEquityStrat) * pl.col(VarActif.txActionStrat)
        )
    
    if alias is not None:
        expr = expr.alias(alias)
    
    return expr 

def calcMtVmChocProperty(colMtVm : str = VarActif.mtVm, alias:str = VarActif.mtVm) -> pl.Expr:
    expr = pl.col(colMtVm) * (1. + pl.col(VarS2.txChocProperty))
    if alias is not None:
        expr = expr.alias(alias)
    return expr

def calcMtVmIndicesInitS2(colMtVm : str = VarActif.mtVm, alias : str = VarActif.mtVm) -> pl.Expr:
    expr = pl.when(rsCdChocS2Equity()) \
            .then(calcMtVmChocEquity(colMtVm=colMtVm, alias=None)) \
            .when(rsCdChocS2Property()) \
            .then(calcMtVmChocProperty(colMtVm=colMtVm, alias=None)) \
            .otherwise(pl.col(colMtVm))
    
    if alias is not None:
        expr = expr.alias(alias)

    return expr

def calcTxFgxChocExpense(colTxFgx : str, colTxChocExpense : str = VarS2.txChocExpense, colFacteurInflationCum : str = VarGse.facteurInflationCum):
    return pl.col(colTxFgx) * (1. + pl.col(colTxChocExpense)) * pl.col(colFacteurInflationCum)