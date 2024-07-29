import polars as pl
def calcAgeMois(colDateRef : str , colDate : str, alias : str) -> pl.Expr :
    return  (pl.col(colDate).dt.year()*12 + pl.col(colDate).dt.month() 
             -pl.col(colDateRef).dt.year()*12 - pl.col(colDateRef).dt.month()
             ).alias(alias)
