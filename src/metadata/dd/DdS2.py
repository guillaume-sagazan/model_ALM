import polars as pl

from dataclasses import dataclass
from enum import auto



from metadata.dd.DdGse import VarGse

from utils.VarCatalog import VarCatalog, DataTypeDesc
from utils.StrEnumExt import StrEnumCaps, StrEnumLower

class CdChocS2(StrEnumCaps):

    central = auto()
    
    lapseDown = auto()
    lapseUp = auto()
    lapseMass = auto()
    
    mortality = auto()
    longevity = auto()
    mortalityCat = auto()
    expense = auto()
    ratesUp = auto()
    ratesDown = auto()
    property = auto()
    equity = auto()
    spread = auto()

class VarS2(StrEnumLower):
    cdChocS2 = auto()
    cdChocS2Gse = auto()
    cdChocS2PassifPrst = auto()
    cdChocS2PassifIcFgx = auto()

    cdTypeTaux = auto()
    cdTypeFlux = auto()
    cdTypeProvMvBeNav = auto()

    txChocMort = auto()
    txChocExpense = auto()
    txChocExpenseInflation = auto()
    txChocMortCat = auto()
    txChocLapse = auto()
    txChocLapseMass = auto()
    
    txChocEquityT1 = auto()
    txChocEquityT2 = auto()
    txChocProperty = auto()
    txChocLongevity = auto()
    txChocRevision = auto()
    txChocInval = auto()
    txChocEquityStrat = auto()
    txChocSpreadStress = auto()
    txChocSpreadA = auto()
    txChocSpreadB = auto()
    nbDurationMin = auto()
    nbDurationMax = auto()
    facteurChocSpreadMtVm = auto()

    mtBeBrt = auto()
    mtBeNet = auto()
    mtBeReass = auto()
    mtBeReassAjst = auto()
    mtDurationMod = auto()


@dataclass(kw_only=True)
class DdS2(VarCatalog):
    def __post_init__(self):
        self.ddElements = {}
        self.ddElements.update({
            
            VarS2.cdChocS2 : DataTypeDesc(
                data_type=pl.Categorical,
                description=f"Choc Solvabilité 2",
            ),
            VarS2.cdChocS2Gse : DataTypeDesc(
                data_type=pl.Categorical,
                description=f"Choc Solvabilité 2 applicable aux variables économiques",
            ),
            VarS2.cdChocS2PassifPrst : DataTypeDesc(
                data_type=pl.Categorical,
                description=f"Choc Solvabilité 2 applicable aux hypothèses de prestations",
            ),
            VarS2.cdChocS2PassifIcFgx : DataTypeDesc(
                data_type=pl.Categorical,
                description=f"Choc Solvabilité 2 applicable à la table PassifHypsIcFgx",
            ),

            VarS2.cdTypeFlux : DataTypeDesc(
                data_type=pl.Categorical,
                description=f"Type de flux",
            ),
            VarS2.cdTypeProvMvBeNav : DataTypeDesc(
                data_type=pl.Categorical,description=f"Type de provision"
            ),
            VarS2.txChocMort : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Choc Solvabilité 2 associé à la mortalité",
            ),
            VarS2.txChocExpense : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Choc Solvabilité 2 associé aux frais généraux",
            ),
            VarS2.txChocExpenseInflation : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Choc Solvabilité 2 associé à l'inflation des frais généraux",
            ),
            VarS2.txChocMortCat : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Choc Solvabilité 2 mortalité catastrophe",
            ),
            VarS2.txChocLapse : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Choc Solvabilité 2 rachat",
            ),
            VarS2.txChocLapseMass : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Choc Solvabilité 2 rachat masse",
            ),
            VarS2.cdTypeTaux : DataTypeDesc(
                data_type=pl.Utf8,  
                description=f"Type de taux dans la table hypS2Chocs",
            ),
            VarS2.txChocEquityT1 : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Choc Solvabilité 2 action de type 1",
            ),
            VarS2.txChocEquityT2 : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Choc Solvabilité 2 action de type 2",
            ),
            VarS2.txChocProperty : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Choc Solvabilité 2 immobilier",
            ),
            VarS2.txChocLongevity : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Choc Solvabilité 2 longévité",
            ),
            VarS2.txChocRevision : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Choc Solvabilité 2 révision",
                
            ),
            VarS2.txChocInval : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Choc Solvabilité 2 invalidité",
            ),
            VarS2.txChocEquityStrat : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Choc Solvabilité 2 action stratégique",
            ),
            VarS2.txChocSpreadStress : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Choc Solvabilité 2 spread stress",
            ),
            VarS2.txChocSpreadA : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Choc Solvabilité 2 spread A",
            ),
            VarS2.txChocSpreadB : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Choc Solvabilité 2 spread B",
            ),
            VarS2.nbDurationMin : DataTypeDesc(
                data_type=pl.Int32, 
                description=f"Borne minimum de duration pour l'application du choc spread",
            ),
            VarS2.nbDurationMax : DataTypeDesc(
                data_type=pl.Int32,  
                description=f"Borne maximum de duration pour l'application du choc spread",
            ),
            VarS2.facteurChocSpreadMtVm : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Facteur de choc spread sur le montant de valeur de marché",
            ),
            VarS2.mtBeBrt : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Best Estimate bruts de réassurance",
            ),
            VarS2.mtBeNet : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Best Estimate net de réassurance",
            ),
            VarS2.mtBeReass : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Best Estimate cédé",
            ),
            VarS2.mtBeReassAjst : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Ajustement pour défaut",
            ),
            VarS2.mtDurationMod : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Duration modifiée",
            ),

        })

ddS2 = DdS2()