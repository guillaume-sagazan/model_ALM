import polars as pl
from polars import DataFrame

from metadata.dd.DdActif import VarActif

def calcPzc(colTzc : str, colMaturite : str = VarActif.maturite) -> pl.Expr:
    return (1.0 + pl.col(colTzc)) ** -pl.col(colMaturite)

def calcCashPerf(colPzc : str, colPzcBeg : str) -> pl.Expr:
    return pl.col(colPzcBeg) / pl.col(colPzc)

def calcPzcBegMid(df : DataFrame, colPzc : str) -> DataFrame:
    pass