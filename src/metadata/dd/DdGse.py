
import polars as pl

from dataclasses import dataclass
from enum import auto, StrEnum


from utils.VarCatalog import VarCatalog, DataTypeDesc
from utils.StrEnumExt import StrEnumCaps, StrEnumLower

class ScUnivers(StrEnum):
    """Enumeration décrivant les options possibles quant à l'univers de projection

    :param RN: Risque neutre
    :param RW: Monde Reel

    """
    RN = 'RN'
    RW = 'RW'

class VarGse(StrEnumLower):
    cdCtRef = auto()
    facteurPerfTot = auto()
    facteurPerfNet = auto()
    deflateur = auto()
    txPerfTot = auto()
    txDividendes = auto()
    pzc = auto()
    tzc = auto()
    txInflation = auto()
    facteurInflationCum = auto()


@dataclass(kw_only=True)
class DdGse(VarCatalog):
    def __post_init__(self):
        self.ddElements = {}
        self.ddElements.update({
            
            VarGse.cdCtRef : DataTypeDesc(
                data_type=pl.Utf8, 
                description=f"Facteur de performance total",
            ),
            
            VarGse.facteurPerfTot : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Facteur de performance total",
            ),

            VarGse.facteurPerfNet : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Facteur de performance net",
            ),
            VarGse.deflateur : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Deflateur",
            ),
            VarGse.txDividendes : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Taux de dividendes",
            ),
            VarGse.pzc : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Prix zéro coupon",
            ),
            VarGse.tzc : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Taux dans le cadre du scenario CENTRAL",
            ),
            
            VarGse.txInflation : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Taux d'inflation",
            ),
            VarGse.facteurInflationCum : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Facteur d'inflation cummulée",
            ),

            VarGse.txPerfTot  : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Taux de performance total",
            ),

            VarGse.facteurPerfTot : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Facteur d'inflation cummulé",
            ),
        })

ddGse = DdGse()




