
import polars as pl

from dataclasses import dataclass
from enum import auto, StrEnum


from utils.VarCatalog import VarCatalog, DataTypeDesc
from utils.StrEnumExt import StrEnumCaps, StrEnumIso, StrEnumLower

class CdClasseActif(StrEnumIso):
    """Enumération décrivant les différents types de classes d'actifs
    :param action: Type d'actif "Action"
    :param immobilier: Type d'actif "Immobilier"
    :param obligation: Type d'actif "Obligation"
    :param monetaire: Type d'actif "Monétaire"
    """
    ACTION = auto()
    IMMOBILIER = auto()
    OBLIGATION = auto()
    MONETAIRE = auto()

class VarActif(StrEnumLower):
    """
    Dictionnaire de données relatif à la modélisation des actifs
    """
    cdClasseActif = auto()
    cdClasseActifDetail = auto()
    cdIsin = auto()
    cdCqs = auto()
    maturite = auto()

    mtNominal = auto()
    txCpn = auto()
    txRemboursement = auto()
    nbDuration = auto()

    mtVmAv = auto()
    mtVm = auto()
    mtVcAv = auto()
    mtVc = auto()
    mtPmvl = auto()
    mtPmvr = auto()
    mtPfi = auto()
    mtCf = auto()

    txActionT1 = auto()
    txActionT2 = auto()
    txActionStrat = auto()
    txImmobilier = auto()

    mtPddAv = auto()
    mtPdd = auto()
    mtPreAv = auto()
    mtPre = auto()

    mtVmRn = auto()
    txVmRn = auto()

    txTra = auto()
    txTraMin = auto()
    txTraMax = auto()

    mtVcTra = auto()
    mtVcTraMin = auto()
    mtVcTraMax = auto()

    mtVcTraError = auto()
    nbPeriodTerme = auto()

@dataclass(kw_only=True)
class DdActif(VarCatalog):
    def __post_init__(self):
        
        self.ddElements = {}
        self.ddElements.update({

            VarActif.maturite : DataTypeDesc(
                data_type=pl.Int32, 
                description=f"Maturité en années d'un cashflow futur"
                ),

            VarActif.cdClasseActif : DataTypeDesc(
                data_type=pl.Utf8,  
                description=f"Classe d'actif"
                ),

            VarActif.cdClasseActifDetail : DataTypeDesc(
                data_type=pl.Utf8,  
                description=f"Classe d'actif détaillée",
            ),

            VarActif.cdCqs : DataTypeDesc(
                data_type=pl.Int32, 
                description=f"Credit Default Step de l'actif",
                
            ),

            VarActif.cdIsin : DataTypeDesc(
                data_type=pl.Utf8,  
                description=f"Identifiant du MP actif agrégé",
                
            ),

            VarActif.nbPeriodTerme : DataTypeDesc(
                data_type=pl.Int32, 
                description=f"Itération à laquelle l'actif considéré arrive à terme",
                
            ),
            VarActif.mtNominal : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Montant du nominal d'une obligation",
            ),
            VarActif.txCpn : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Taux de coupon d'une obligation",
            ),
            VarActif.txRemboursement : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Taux de remboursement d'une obligation",
            ),

            VarActif.nbDuration : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Duration de l'actif",
            ),

            VarActif.mtVmAv : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Valeur de marché (avant évènement)",
                
            ),
            VarActif.mtVm : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Valeur de marché",
                
            ),
            VarActif.mtVcAv : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Valeur comptable (avant évènement)",
                
            ),
            VarActif.mtVc : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Valeur comptable",
                
            ),
           
            VarActif.mtPmvl : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Plus ou moins values latentes disponibles",
                
            ),
            VarActif.mtPmvr : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Plus ou moins values latentes générés lors de l'évènement",
                
            ),
            VarActif.mtPfi : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Produits financier généré par l'évènement",
                
            ),
            VarActif.mtCf : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Cashflow",
                
            ),

            VarActif.txActionT1 : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Part de l'actif unitaire à choquer sous S2 avec le choc Action de Type 1",
                
            ),
            VarActif.txActionT2 : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Part de l'actif unitaire à choquer sous S2 avec le choc Action de Type 2",
                
            ),
            VarActif.txActionStrat : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Part de l'actif unitaire à choquer sous S2 avec le choc Action Stratégique",
                
            ),

            VarActif.txImmobilier : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Part de l'actif unitaire à choquer sous S2 avec le choc immobilier",
            ),

            VarActif.mtPddAv : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Provision pour dépréciation durable (avant évènement)",
                
            ),
            VarActif.mtPdd : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Provision pour dépréciation durable",
                
            ),
            VarActif.mtPreAv : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Provision pour risque d'éligibilité (avant évènement)",
                
            ),
            VarActif.mtPre : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Provision pour risque d'éligibilité",
                
            ),

            VarActif.mtVmRn : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Valeur de marché post risque neutralisation",
                
            ),
            VarActif.txVmRn : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Facteur à appliquer pour risque neutraliser une obligation",
                
            ),

            VarActif.txTra : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Dernier TRA  considéré pour équilibrer la valeur comptable",
                
            ),
            VarActif.txTraMin : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"TRA min considéré pour équilibrer la valeur comptable",
                
            ),
            VarActif.txTraMax : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"TRA max considéré pour équilibrer la valeur comptable",
                
            ),

            VarActif.mtVcTra : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Valeur comptable calculée avec le dernier TRA considéré",
                
            ),
            VarActif.mtVcTraMin : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Valeur comptable calculée avec le TRA min",
                
            ),
            VarActif.mtVcTraMax : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Valeur comptable calculée avec le TRA max",
                
            ),

            VarActif.mtVcTraError : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Erreur constatée sur le calcul de la valeur comptable avec le dernier TRA considéré",
            ),
            VarActif.nbPeriodTerme : DataTypeDesc(
                data_type=pl.Int32, 
                description=f"Montant de cashflow", # TODO : Pas la bonne description
            ),

        })

ddActif = DdActif()