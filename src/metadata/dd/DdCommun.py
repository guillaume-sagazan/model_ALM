
import polars as pl


from dataclasses import dataclass
from enum import auto, StrEnum

from metadata.dd.DdActif import CdClasseActif
from metadata.dd.DdProjection import ModeleAlmEvenement, IntraPeriod
from metadata.dd.DdS2 import CdChocS2

from utils.VarCatalog import VarCatalog, DataTypeDesc
from utils.StrEnumExt import StrEnumCaps, StrEnumIso, StrEnumLower


class TypeErreur(StrEnumIso):
    """Type d'erreur

    :param Information: Pour information
    :param Attention: Point d'attention
    :param Erreur: Erreur

    """
    Information = auto()
    Attention = auto()
    Erreur = auto()


class TypeErreurAction(StrEnumIso):
    """Action réalisée à la détection de l'erreur

    :param AucuneAction: Aucune action
    :param NonPrisEnCompte: Exclusion du cas détecté pour la suite de la projection
    :param NePasUtiliserLesResultats: Dans ce cas, l'erreur détectée implique que les résultats en sortie sont faux et ne doivent pas être utilisés.

    """
    AucuneAction = auto()
    NonPrisEnCompte = auto()
    NePasUtiliserLesResultats = auto()

class VarCommun(StrEnumLower):

    cdTable = auto()
    cdSociete = auto()
    cdCanton = auto()
    facteur = auto()
    
    dtDateTerme = auto()
    dtDateTermeAnnee = auto()
    erreur = auto()
    typeErreur = auto()
    typeErreurAction = auto()


@dataclass(kw_only=True)
class DdCommun(VarCatalog):
    def __post_init__(self):
        
        self.ddElements = {}
        self.ddElements.update({
            VarCommun.cdTable : DataTypeDesc(
                data_type=pl.Utf8,
                description=f"Nom de la table d'hypothèse",
            ),
            VarCommun.cdSociete : DataTypeDesc(
                data_type=pl.Utf8,  
                description=f"Code société",
            ),
            VarCommun.cdCanton : DataTypeDesc(
                data_type=pl.Utf8,  
                description=f"Code Canton",  
            ),
            VarCommun.facteur : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Facteur",
            ),
            VarCommun.dtDateTerme : DataTypeDesc(
                    data_type=pl.Date, 
                description=f"Date de terme",
                
            ),
            VarCommun.dtDateTermeAnnee : DataTypeDesc(
                data_type=pl.Int64, 
                description=f"Année associée à la date de terme",
                
            ),
            VarCommun.erreur : DataTypeDesc(
                data_type=pl.Utf8,  
                description=f"Description de l'erreur",
                
            ),
            VarCommun.typeErreur : DataTypeDesc(
                data_type=pl.Utf8, 
                description=f"Type d'erreur"
            ),
            VarCommun.typeErreurAction : DataTypeDesc(
                data_type=pl.Utf8, 
                description=f"Type d'action réalisée compte tenu de l'erreur"
            ),
        })

ddCommun = DdCommun()