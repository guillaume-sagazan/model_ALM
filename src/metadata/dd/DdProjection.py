import polars as pl


from dataclasses import dataclass
from enum import StrEnum, auto



from utils.VarCatalog import VarCatalog, DataTypeDesc
from utils.StrEnumExt import StrEnumCaps, StrEnumLower


class ModeleAlmEvenement(StrEnum):
    """
    Evènements au sein du modèle ALM
    :param Init: Initialisation
    :param Perf: Performance
    :param StratInv: Stratégie d'investissement
    :param AlmCr: Stratégie ALM et compte de résultat
    """
    Init = '0.Init'
    Perf = '1.Perf'
    StratInv = '2.StratInv'
    AlmCr = '3.AlmCr'


class IntraPeriod(StrEnum):
    """Enumération permettant de qualifier si un cashflow tombe en début milieu ou fin de période

    :param BEG: Début de période
    :param MID: Milieu de période
    :param END: Fin de période
    """
    BEG = 'Beg'
    MID = 'Mid'
    END = 'End'

class PerfCash(StrEnum):
    """Enumération permettant de qualifier si un cashflow tombe en début milieu ou fin de période
    On essaye de calculer la performance
    :param BEG: Début de période
    :param MID: Milieu de période
    :param END: Fin de période
    """
    BEG = 'Beg'
    MID = 'Mid'
    END = 'End'

class ModeProjection(StrEnum):
    """Enumeration décrivant les options possibles quant au mode de projection
    :param ACTIF_SEUL: Seuls l'actif du bilan est projeté
    :param PASSIF_SEUL: Seuls l'actif du bilan est projeté
    :param ALM: L'actif et le passif du bilan sont projetés simultanément
    """
    ACTIF_SEUL = 'ACTIF_SEUL'
    PASSIF_SEUL = 'PASSIF_SEUL'
    ALM = 'ALM'


class VarProj(StrEnumLower):
    
    cdTrajectoire = auto()	
    dtTrajectoire = auto()
    dtTrajectoireAnnee = auto()
    scenario = auto()
    period = auto()
    projAnnee = auto()
    evenement = auto()
    intraperiod = auto()
    projDateDebut = auto()


@dataclass(kw_only=True)
class DdProj(VarCatalog):
    def __post_init__(self):
        self.ddElements = {}
        self.ddElements.update({
            VarProj.cdTrajectoire : DataTypeDesc(
                data_type=pl.Utf8,  
                description=f"Trajectoire",
            ),
            VarProj.dtTrajectoire : DataTypeDesc(
                data_type=pl.Date,  
                description=f"Trajectoire",
            ),

            VarProj.dtTrajectoireAnnee : DataTypeDesc(
                data_type=pl.Int32,  
                description=f"Trajectoire Année",
            ),

            VarProj.scenario : DataTypeDesc(
                data_type=pl.Int32, 
                description=f"Identifiant du scenario",
            ),
            VarProj.period : DataTypeDesc(
                data_type=pl.Int32, 
                description=f"Identifiant du pas de temps",
                
            ),
            VarProj.projAnnee : DataTypeDesc(
                data_type=pl.Int32, 
                description=f"Année de projection",
            ),
            VarProj.evenement : DataTypeDesc(
                data_type=pl.Categorical,
                description=f"Année de projection",
            ),
            VarProj.intraperiod : DataTypeDesc(
                data_type=pl.Utf8, 
                description=f"Pour un cash flow donné, tombe t il en début, milieu",
            ),
            VarProj.projDateDebut : DataTypeDesc(
                data_type=pl.Date, 
                description=f"Date de début de la projection",
            ),
        })

ddProj = DdProj()