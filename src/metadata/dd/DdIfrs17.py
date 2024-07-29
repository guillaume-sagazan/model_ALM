import polars as pl


from dataclasses import dataclass
from enum import StrEnum, auto
from utils.VarCatalog import VarCatalog, DataTypeDesc
from utils.StrEnumExt import StrEnumCaps, StrEnumLower

class VarIfrs17(StrEnumLower):
    
    cdPrtfIfrs17 = auto()	
    cdCohorte = auto()
    cdProfitabilite = auto()
    

@dataclass(kw_only=True)
class DdIfrs17(VarCatalog):
    def __post_init__(self):
        self.ddElements = {}
        self.ddElements.update({
            VarIfrs17.cdPrtfIfrs17 : DataTypeDesc(
                data_type=pl.Categorical,  
                description=f"Code Portefeuille Ifrs17",
            ),
            VarIfrs17.cdCohorte : DataTypeDesc(
                data_type=pl.Int32,  
                description=f"Cohorte Ifrs17",
            ),
            VarIfrs17.cdProfitabilite : DataTypeDesc(
                data_type=pl.Int16,  
                description=f"Profitabilite Ifrs17",
            ),
        })

ddIfrs17 = DdIfrs17()