import polars as pl
from dataclasses import dataclass
from enum import auto

from utils.VarCatalog import VarCatalog, DataTypeDesc
from utils.StrEnumExt import StrEnumCaps, StrEnumLower


class VarStratInv(StrEnumLower):

    txAllocCible = auto()
    txObligAchatCpn = auto()
    nbObligAchatMaturite = auto()
    txFraisPlct = auto()

    mtVmAvCanton = auto()
    mtVmAvCdClasseActif = auto()
    mtVmAvAssAchatVente = auto()

    mtVmCibleCdClasseActif = auto()

    mtAchatOblig = auto()
    facteurAchatVente = auto()


@dataclass(kw_only=True)
class DdStratInv(VarCatalog):
    def __post_init__(self):
        self.ddElements = {}
        self.ddElements.update({
            
            VarStratInv.txAllocCible : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Taux d'allocation cible",
            ),
            VarStratInv.txObligAchatCpn : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Taux de coupon des obligations à acheter",
            ),
            VarStratInv.nbObligAchatMaturite : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Maturité des obligations à acheter",
            ),
            VarStratInv.txFraisPlct : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Taux de frais de placement",
            ),

            VarStratInv.mtVmAvCanton : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Valeur de marché avant stratégie d'investissement pour le canton considéré",
            ),
            VarStratInv.mtVmAvCdClasseActif : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Valeur de marché avant stratégie d'investissement pour la classe d'actif considérée",
            ),
            VarStratInv.mtVmAvAssAchatVente : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Assiette utilisée pour les achats ventes à réaliser",
            ),

            VarStratInv.mtVmCibleCdClasseActif : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Valeur de marché cible",
            ),

            VarStratInv.mtAchatOblig : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Montant d'obligations à acheter (output de la stratégie d'investissement)",
            ),
            VarStratInv.facteurAchatVente : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Facteur d'achat vente (output de la stratégie d'investissement)",
            ),
        })

ddStratInv = DdStratInv()