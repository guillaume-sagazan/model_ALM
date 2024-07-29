
import polars as pl

from dataclasses import dataclass
from enum import auto

from utils.VarCatalog import VarCatalog, DataTypeDesc
from utils.StrEnumExt import StrEnumLower

class VarFgx(StrEnumLower):

    txFgxPrstEu = auto()
    txFgxPlctEu = auto()
    txFgxPmEu = auto()

    txFgxPrstUc = auto()
    txFgxPlctUc = auto()
    txFgxPmUc = auto()
    
    mtFgxTotEu = auto()
    mtFgxPrstEu = auto()
    mtFgxPmEu = auto()
    mtFgxPlctEu = auto()

    mtFgxTotUc = auto()
    mtFgxPrstUc = auto()
    mtFgxPmUc = auto()
    mtFgxPlctUc = auto()


@dataclass(kw_only=True)
class DdFgx(VarCatalog):
    def __post_init__(self):
        self.ddElements = {}
        self.ddElements.update({

            VarFgx.txFgxPrstEu : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Taux de frais généraux sur les prestations"
            ),
            VarFgx.txFgxPlctEu : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Taux de frais généraux sur les placements"
            ),
            VarFgx.txFgxPmEu : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Taux de frais généraux sur les PM"
            ),

            VarFgx.mtFgxTotEu : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Montant de frais généraux totaux"                
            ),
            VarFgx.mtFgxPrstEu : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Montant de frais généraux sur prestations"
            ),
            VarFgx.mtFgxPmEu : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Montant de frais généraux sur PM"
            ),
            VarFgx.mtFgxPlctEu : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Montant de frais généraux de placement",
            ),

            

            VarFgx.txFgxPrstUc : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Taux de frais généraux sur les prestations",
            ),
            VarFgx.txFgxPlctUc : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Taux de frais généraux sur les placements",
            ),
            VarFgx.txFgxPmUc : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Taux de frais généraux sur les PM",
            ),

            VarFgx.mtFgxTotUc : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Montant de frais généraux totaux",
                
            ),
            VarFgx.mtFgxPrstUc : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Montant de frais généraux sur prestations",
            ),
            VarFgx.mtFgxPmUc : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Montant de frais généraux sur PM",
            ),
            VarFgx.mtFgxPlctUc : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Montant de frais généraux de placement",
            ),

        })

ddFgx = DdFgx()