import polars as pl

from metadata.dd.DdActif import VarActif
from metadata.dd.DdAlm import VarAlm
from metadata.dd.DdFgx import VarFgx
from metadata.dd.DdPassifEp import VarPassif

def calcMtPfiAssr(alias:str=None) -> pl.Expr:
    
    expr = (
                pl.col(VarAlm.mtPfiInit) + pl.col(VarActif.mtPmvr) 
            ) * (1.0 - pl.col(VarAlm.txPfiAsseRepartPc))
            
    if not alias is None:
        expr = expr.alias(alias)    
    
    return expr

def calcMtPfiAsse(alias:str=None) -> pl.Expr:
    
    expr = (
                pl.col(VarAlm.mtPfiInit) + pl.col(VarActif.mtPmvr) 
            ) * pl.col(VarAlm.txPfiAsseRepartPc)
            
    if not alias is None:
        expr = expr.alias(alias)    
    
    return expr

def calcMtPfiAssePb(alias:str=None) -> pl.Expr:
    
    expr = pl.col(VarAlm.mtPfiAsse) - pl.col(VarPassif.mtFgseEu) - pl.col(VarFgx.mtFgxPlct) 
            
    if not alias is None:
        expr = expr.alias(alias)    
    
    return expr

def calcMtPfiBesoinTxCible(colMtPfiAssePb:str=VarAlm.mtPfiAssePb, alias:str=None) -> pl.Expr:
    expr = (pl.col(VarActif.mtPfi + "_" + VarAlm.txCible) - pl.col(colMtPfiAssePb) )
    
    if not alias is None:
        expr = expr.alias(alias)    
    
    return expr

def calcMtPbBrtBesoinTxCible(colMtPbBrt:str=VarPassif.mtPbBrt, alias:str=None) -> pl.Expr:
    expr = (pl.col(colMtPbBrt) 
        - pl.col(VarPassif.mtPbBrt + "_" + VarAlm.txCible)
        - pl.col(VarAlm.mtPpeReprise)
        + pl.col(VarAlm.mtPpeDotation)
    )
    
    if not alias is None:
        expr = expr.alias(alias)    
    
    return expr