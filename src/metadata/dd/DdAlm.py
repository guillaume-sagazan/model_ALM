
import polars as pl

from dataclasses import dataclass
from enum import auto, StrEnum

import polars as pl

from utils.VarCatalog import VarCatalog, DataTypeDesc
from utils.StrEnumExt import StrEnumCaps, StrEnumLower

class CdMethodeTxServi(StrEnum):
    """Méthodes possibles quant au calcul du Taux Servi
    :param NET: Les calculs sont réalisés nets de TAF et TFGSE
    :param BRT: Les calculs sont réalisés bruts de TAF et TFGSE
    """
    NET = 'NET'
    BRT = 'BRT'


class CdMethodeInitEquilibreBilan(StrEnum):
    """Méthodes possibles quant à l'équilibrage du bilan en t=0
    :param CASH: Le cash est utilisé en t=0 pour équilibrer le bilan
    :param FONDS_PROPRES: Les fonds propres sont utilisés en t = 0 pour équilibrer le bilan
    """
    CASH = 'CASH'
    FONDS_PROPRES = 'FONDS_PROPRES'

class StratAlmCas(StrEnum):
    """Cas possibles dans le cadre de la stratégie ALM

    :param TX_SERVI_CIBLE: Taux servi cible
    :param TX_SERVI_CIBLE_DIV2: Taux servi cible divisé par 2
    :param TMG: seuls les TMG sont servis
    :param BEG: Cas spécifique dans le cas d'un calcul de BEG
    :param PASSIF_NUL: Cas passif nul
    :param UC: Cas unités de comptes, utilisé post stratégie ALM pour les supports euro pour disposer du compte de résultat pour les unités de compte

    """
    TX_CIBLE = auto()
    TX_CIBLE_DIV2 = auto()
    TMG = auto()
    UC = auto()
    PASSIF_NUL = auto()

class VarAlm(StrEnumLower):
    """
    Enumération contenant les variables ALM
    """
    stratAlmCas = auto()
    stratAlmCasPriorite = auto()
    stratAlmCasPrioriteMin = auto()

    nbPpeGeneration = auto()
    nbPpeGenerationMax = auto()
    txPbMinReglSoldeFin = auto()
    txPbMinReglSoldeTech = auto()
    cdMethodeTxCible = auto()
    txCibleFixe = auto()
    txCible = auto()
    txIs = auto()
    idScenarioPb = auto()

    txServiBrt = auto()
    txServiNet = auto()
    txTmg = auto()
    pentePbBrt = auto()
    pentePfi = auto()

    mtPbBrtMinRegl = auto()
    mtIcRestCumSum = auto()
    mtIcRestCanton = auto()

    mtPmvrMax = auto()

    mtPpeAv = auto()
    mtPpe = auto()
    mtPbAssCanton = auto()

    mtReserveCapiAv = auto()
    mtReserveCapi = auto()

    mtCapitauxPropresAv = auto()
    mtCapitauxPropres = auto()

    cdMethodePfiCleRepart = auto()
    cdTypeCanton = auto()

    mtCashInit = auto()

    mtPfiInit = auto()
    mtPfiBesoinTxCible = auto()
    mtPbBrtBesoinTxCible = auto()

    mtPpeDelta = auto()
    mtPpeRestante = auto()
    mtPpeReprise = auto()
    mtPpeDispo = auto()
    mtPpeDotation = auto()
    mtPpeCumSum = auto()

    txPfiAsseRepartPc = auto()
    mtPfiAsse = auto()
    mtPfiAssePb = auto()
    mtPfiAssr = auto()

    mtResBrt = auto()
    mtResBrtAsse = auto()
    mtResIs = auto()
    mtResNet = auto()
    
    mtFuiteEco = auto()
    mtFuiteVc = auto()
    mtFuiteVcEu = auto()
    mtFuiteVcUc = auto()
    mtFuiteVcTmp = auto()

    mtProv = auto()

class CdMethodePfiCleRepart(StrEnum):
    """
    Enumération décrivant les possibilités quant au calcul de la clé de répartition des produits financiers entre
    """
    CleRepart_100PC_ASSURE = '100PC_ASSURE'


class TypeCanton(StrEnum):
    """
    Enumération décrivant les types de cantons

    :param FONDS_PROPRES: Dans ce cas, le canton correspond au fonds propres de la société
    :param ASSURE: Dans ce cas, le canton est un canton en représentation de contrats d'assurance

    """
    FONDS_PROPRES = auto()
    FONDS_GENERAL = auto()
    ASSURE = auto()


class CdMethodeTxCible(StrEnum):
    """
    Enumération décrivant les options de calcul du taux cible à donner aux clients

    :param Fixe: Dans ce cas, le taux cible est fixe, issu de la table sppb
    :param TZC_X: Dans ce cas, le taux cible correspond à un taux zéro coupon (non utilisé)

    """
    Fixe = 'FIXE'
    TZC_X = 'TZC_X'

@dataclass(kw_only=True)
class DdAlm(VarCatalog):
    def __post_init__(self):
        self.ddElements = {}
        self.ddElements.update(
            {
                VarAlm.nbPpeGeneration : DataTypeDesc(
                    data_type=pl.Int64, 
                    description=f"Génération de PPE"
                ),
                VarAlm.nbPpeGenerationMax : DataTypeDesc(
                    data_type=pl.Int64, 
                    description=f"Génération de PPE maximum"
                ),
                VarAlm.stratAlmCas : DataTypeDesc(
                    data_type=pl.Utf8, 
                    description=f"Cas possibles pour la stratégie ALM (chaine de caractères)"
                    #valeursPossibles=[x for x in StratAlmCas]$
                ),
                VarAlm.stratAlmCasPriorite : DataTypeDesc(
                    data_type=pl.Int64, 
                    description=f"Priorité donnée aux cas possibles pour la stratégie ALM (entier)",
                ),
                VarAlm.stratAlmCasPrioriteMin : DataTypeDesc(
                    data_type=pl.Int64, 
                    description=f"Priorité minimum associé aux cas possibles pour la stratégie ALM (entier)",
                ),
            
                VarAlm.txPbMinReglSoldeFin : DataTypeDesc(
                    data_type=pl.Float64,  
                    description=f"Taux minimum règlementaire associé au partage du résultat financier"
                ),
                VarAlm.txPbMinReglSoldeTech : DataTypeDesc(
                    data_type=pl.Float64,  
                    description=f"Taux minimum règlementaire associé au partage du résultat technique"
                ),
                VarAlm.cdMethodeTxCible : DataTypeDesc(
                    data_type=pl.Utf8,  
                    description=f"Méthode associé au calcul du taux cible"
                ),
                VarAlm.txCibleFixe : DataTypeDesc(
                    data_type=pl.Float64,  
                    description=f"Taux servi cible"
                ),
                VarAlm.txIs : DataTypeDesc(
                    data_type=pl.Float64,  
                    description=f"Taux d'impôts sur les société"
                ),
                VarAlm.txServiBrt : DataTypeDesc(
                    data_type=pl.Float64,  
                    description=f"Taux servi brut",  
                ),
                VarAlm.txServiNet : DataTypeDesc(
                    data_type=pl.Float64,  
                    description=f"Taux servi net",
                ),
                VarAlm.txTmg : DataTypeDesc(
                    data_type=pl.Float64,  
                    description=f"Taux minimum garanti",
                ),
                VarAlm.pentePbBrt : DataTypeDesc(
                    data_type=pl.Float64,  
                    description=f"Pente de la courbe MtPbBrt=f(txServiBrt)",
                ),
                VarAlm.pentePfi : DataTypeDesc(
                    data_type=pl.Float64,  
                    description=f"Pente de la courbe MtPfi=f(txServiBrt)",
                ),
                VarAlm.txTmg : DataTypeDesc(
                    data_type=pl.Float64,  
                    description=f"Taux minimum garanti",
                ),
                VarAlm.mtPbBrtMinRegl : DataTypeDesc(
                    data_type=pl.Float64,  
                    description=f"Montant de PB minimum règlementaire"  
                ),
                VarAlm.mtIcRestCumSum : DataTypeDesc(
                    data_type=pl.Float64,  
                    description=f"Montant d'intérêts crédités total"
                ),
                VarAlm.mtIcRestCanton : DataTypeDesc(
                    data_type=pl.Float64,  
                    description=f"Montant d'intérêts crédités restants au niveau canton"
                ),
                VarAlm.mtPpeAv : DataTypeDesc(
                    data_type=pl.Float64,  
                    description=f"Montant de PPB (avant évènement)"
                ),
                VarAlm.mtPpe : DataTypeDesc(
                    data_type=pl.Float64,  
                    description=f"Montant de PPB"
                ),
                VarAlm.mtPbAssCanton : DataTypeDesc(
                    data_type=pl.Float64,  
                    description=f"Assiette servant au calcul de la PB (au niveau canton)",
                ),
                VarAlm.mtReserveCapiAv : DataTypeDesc(
                    data_type=pl.Float64,  
                    description=f"Montant de réserve de capitalisation (avant évènement)",
                ),
                VarAlm.mtReserveCapi : DataTypeDesc(
                    data_type=pl.Float64,  
                    description=f"Montant de réserve de capitalisation",
                ),
                VarAlm.mtCapitauxPropresAv : DataTypeDesc(
                    data_type=pl.Float64,  
                    description=f"Montant de capitaux propres (avant évènement)",
                ),
                VarAlm.mtCapitauxPropres : DataTypeDesc(
                    data_type=pl.Float64,  
                    description=f"Montant de capitaux propres",
                ),
                VarAlm.cdMethodePfiCleRepart : DataTypeDesc(
                    data_type=pl.Utf8, 
                    description=f"Indice de Gestion"
                ),
                VarAlm.cdTypeCanton : DataTypeDesc(
                    data_type=pl.Utf8, 
                    description=f"Indice de Gestion"
                ),
                VarAlm.mtCashInit : DataTypeDesc(
                    data_type=pl.Float64,  
                    description=f"Montant de cash initial",
                ),
                VarAlm.mtPfiInit : DataTypeDesc(
                    data_type=pl.Float64,  
                    description=f"Produits financiers initiaux disponibles en input de l'algorithme ALM",
                ),
                VarAlm.mtPfiBesoinTxCible : DataTypeDesc(
                    data_type=pl.Float64,  
                    description=f"Besoin en pfi pour servir le taux cible",
                ),
                VarAlm.mtPbBrtBesoinTxCible : DataTypeDesc(
                    data_type=pl.Float64,  
                    description=f"Besoin en pb pour servir le taux cible",
                ),
                VarAlm.mtPpeDelta : DataTypeDesc(
                    data_type=pl.Float64,  
                    description=f"Delta de PPB",
                ),
                VarAlm.mtPpeRestante : DataTypeDesc(
                    data_type=pl.Float64,  
                    description=f"Montant de PPB restante",
                ),
                VarAlm.mtPpeReprise : DataTypeDesc(
                    data_type=pl.Float64,  
                    description=f"Montant de la reprise de PPB",
                ),
                VarAlm.mtPpeDispo : DataTypeDesc(
                    data_type=pl.Float64,  
                    description=f"Montant de la reprise de PPB complémentaire",
                ),
                VarAlm.mtPpeDotation : DataTypeDesc(
                    data_type=pl.Float64,  
                    description=f"Montant de la dotation à la PPB",
                ),
                VarAlm.mtPpeCumSum : DataTypeDesc(
                    data_type=pl.Float64,  
                    description=f"Somme des générations de PPB pour un canton donné",
                ),
            
                VarAlm.txPfiAsseRepartPc : DataTypeDesc(
                    data_type=pl.Float64,  
                    description=f"Part des produits financiers du canton qui a vocation à être réparti en marge financière et PB"
                ),
                VarAlm.mtPfiAsse : DataTypeDesc(
                    data_type=pl.Float64,  
                    description=f"Montant des produits financiers assurés",
                ),
                VarAlm.mtPfiAssePb : DataTypeDesc(
                    data_type=pl.Float64,  
                    description=f"Montant des produits financiers assurés en input du compte de PB",
                ),
                VarAlm.mtPfiAssr : DataTypeDesc(
                    data_type=pl.Float64,  
                    description=f"Montant de la marge financière assureur",
                ),
                
                VarAlm.mtResBrt : DataTypeDesc(
                    data_type=pl.Float64,  
                    description=f"Montant de résultat brut",
                ),
                VarAlm.mtResBrtAsse : DataTypeDesc(
                    data_type=pl.Float64,  
                    description=f"Montant de résultat brut issu du compte de PB",
                ),
                VarAlm.mtResIs : DataTypeDesc(
                    data_type=pl.Float64,  
                    description=f"Impots sur les sociétés",
                ),
                VarAlm.mtResNet : DataTypeDesc(
                    data_type=pl.Float64,  
                    description=f"Montant de résultat net",
                ),
                VarAlm.mtFuiteEco : DataTypeDesc (
                    data_type=pl.Float64,  
                    description=f"Montant de la fuite économique",
                ),
                VarAlm.mtFuiteVc : DataTypeDesc (
                    data_type=pl.Float64,  
                    description=f"Montant de fuite de valeur comptable",
                ),
                VarAlm.mtFuiteVcTmp : DataTypeDesc (
                    data_type=pl.Float64,  
                    description=f"Montant de fuite de valeur comptable (variable temporaire)",
                ),
                VarAlm.mtFuiteVcEu : DataTypeDesc (
                    data_type=pl.Float64,  
                    description=f"Montant de fuite de valeur comptable en Euro",
                ),
                VarAlm.mtFuiteVcUc : DataTypeDesc (
                    data_type=pl.Float64,  
                    description=f"Montant de fuite de valeur comptable en Uc",
                ),
                VarAlm.mtProv : DataTypeDesc (
                    data_type=pl.Float64,  
                    description=f"Montant de provision",
                )
            }
        )

ddAlm = DdAlm()
