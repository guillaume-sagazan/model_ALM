
import logging
import polars as pl

from dataclasses import dataclass
from enum import auto, StrEnum

from metadata.dd.DdActif import VarActif
from metadata.dd.DdCommun import VarCommun
from metadata.dd.DdFgx import VarFgx
from utils.VarCatalog import VarCatalog, DataTypeDesc
from utils.StrEnumExt import StrEnumCaps, StrEnumIso, StrEnumLower


class CdCapitalisation(StrEnumIso):
    capi = auto()
    ncapi = auto()

class TmgType(StrEnumIso):
    net = auto()
    brut = auto()

class CdCntSupportType(StrEnumIso):
    EU = auto()
    UC = auto()

class VarPassif(StrEnumLower):

    #Elements associés au contrat
    cdFampdt = auto()
    cdPrstRtCat = auto()

    cdCnt = auto()
    cdCntSupportType = auto()

    cdHypMortExp = auto()
    cdHypMortProv = auto()
    
    cdCapitalisation = auto()

    dtCntEffet = auto()
    dtCntTerme = auto()

    nbCntAv = auto()
    nbCnt = auto()

    nbCntAncienneteAnnee = auto()
    nbCntAncienneteMois = auto()
    
    generation = auto()
    sexe = auto()
    age = auto()
    qx = auto()

    dtAsseNaiss = auto()
    nbAsseAgeAnnee = auto()
    nbAsseAgeMois = auto()

    cdAsseSexe = auto()

    # Taux
    txPrstRt = auto()
    txPrstChgt = auto()
    txPrstDcAsseExp = auto()

    taf = auto()
    tfgse = auto()
    tfgseUc = auto()
    tmg = auto()
    tmgType = auto()
    tmgBrt = auto()
    txIcEu = auto()
    txIcEuBrt = auto()
    txIcUc = auto()

    txIcEuDemiPeriode = auto()
    txIcUcDemiPeriode = auto()
    txIcEuBrtDemiPeriode = auto()
    
    facteurActuTxTech = auto()

    #Montants
    cdHrgEu = auto()
    mtPmEuAv = auto()
    mtPmEu = auto()

    cdHrgUc = auto()
    mtPmUcAv = auto()
    mtPmUc = auto()

    mtPrstTotEuBrt = auto()
    mtPrstTotEuNet = auto()
    mtPrstTotEuChgt = auto()
    mtPrstDcEuBrt = auto()
    mtPrstDcEuNet = auto()
    mtPrstDcEuChgt = auto()
    mtPrstRtEuBrt = auto()
    mtPrstRtEuNet = auto()
    mtPrstRtEuChgt = auto()

    mtPrstTotUcBrt = auto()
    mtPrstTotUcNet = auto()
    mtPrstTotUcChgt = auto()
    mtPrstDcUcBrt = auto()
    mtPrstDcUcNet = auto()
    mtPrstDcUcChgt = auto()
    mtPrstRtUcBrt = auto()
    mtPrstRtUcNet = auto()
    mtPrstRtUcChgt = auto()

    mtIcEuRest = auto()
    mtIcEuSort = auto()
    mtIcUcRest = auto()
    mtIcUcSort = auto()
    mtFgseUc = auto()
    mtFgseEu = auto()

    mtPbAss = auto()
    mtPbBrt = auto()
    mtPbBrtCg = auto()
    mtPbNet = auto()
    mtCsg = auto()

@dataclass(kw_only=True)
class DdPassifEp(VarCatalog):
    def __post_init__(self):
        self.ddElements = {}
        self.ddElements.update({
            
            VarPassif.cdFampdt : DataTypeDesc(
                data_type=pl.Categorical,  
                description=f"Code Famille de produit",
            ),

            VarPassif.cdCnt : DataTypeDesc(
                data_type=pl.Int32,  
                description=f"Identifiant d'un contrat",
                
            ),
            
            VarPassif.dtCntEffet : DataTypeDesc(
                data_type=pl.Date, 
                description=f"Date d'effet du contrat",
            ),

            VarPassif.dtCntTerme : DataTypeDesc(
                data_type=pl.Date, 
                description=f"Date de terme du contrat",
            ),
            
            VarPassif.nbCntAv : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Nombre de contrats (avant évènement)",
            ),
            VarPassif.nbCnt : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Nombre de contrats",
            ),

            VarPassif.cdPrstRtCat : DataTypeDesc(
                data_type=pl.Int16,
                description=f"Catégorie de prestation rachat"
            ),

            VarPassif.cdCapitalisation : DataTypeDesc(
                data_type=pl.Enum([val.value for val in list(CdCapitalisation)]),  
                description=f"Contrat de capitalisation",
                valeursPossibles=[val.value for val in list(CdCapitalisation)]
            ),

            VarPassif.cdCntSupportType : DataTypeDesc(
                data_type=pl.Enum([val.value for val in list(CdCntSupportType)]),  
                description=f"Type de support du contrat",
                valeursPossibles=[val.value for val in list(CdCntSupportType)]
            ),

            VarPassif.cdHypMortExp : DataTypeDesc(
                data_type=pl.Utf8,  
                description=f"Table de mortalite d'expérience à appliquer",
            ),

            VarPassif.cdHypMortProv : DataTypeDesc(
                data_type=pl.Utf8,  
                description=f"Table de mortalite utilisée pour le provisionnement",
            ),
            VarPassif.sexe : DataTypeDesc(
                data_type=pl.Utf8,  
                description=f"Sexe"
            ),

            VarPassif.age : DataTypeDesc(
                data_type=pl.Int32, 
                description=f"Age en années"
            ),

            VarPassif.cdAsseSexe : DataTypeDesc(
                data_type=pl.Utf8,  
                description=f"Sexe de l'assuré"
            ),


            VarPassif.dtAsseNaiss : DataTypeDesc(
                data_type=pl.Date, 
                description=f"Date de naissance de l'assuré",
            ),
            
            VarPassif.nbAsseAgeAnnee : DataTypeDesc(
                data_type=pl.Int32, 
                description=f"Age de l'assuré en années",
            ),

            VarPassif.nbAsseAgeMois : DataTypeDesc(
                data_type=pl.Int32, 
                description=f"Age de l'assuré en années",
                
            ),

            # Taux
            VarPassif.txPrstRt : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Taux de prestation de rachat total",
                
            ),
            VarPassif.txPrstChgt : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Taux de chargement sur les prestations",
                
            ),
            VarPassif.txPrstDcAsseExp : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Taux de prestation décès appliqué dans la diffusion du nombre d'assuré",
                
            ),

            VarPassif.taf : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Taux d'affectation des produits financiers",
                
            ),
            VarPassif.tfgse : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Taux de frais de gestion sur encours euro",
            ),

            VarPassif.tfgseUc : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Taux de frais de gestion sur encours UC",
            ),

            VarPassif.tmg : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Taux minimum garanti",
            ),
            
            VarPassif.tmgType : DataTypeDesc(
                data_type=pl.Enum([var.value for var in list(TmgType)]), 
                description=f"Taux minimum garanti",
                valeursPossibles=[var.value for var in list(TmgType)]
            ),

            VarPassif.tmgBrt : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Taux minimum garanti, brut de taf et tfgse",
                
            ),
            VarPassif.txIcEu : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Taux d'intérêts crédités Euro",
                
            ),
            VarPassif.txIcUc : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Taux d'intérêts crédités UC",
                
            ),
            VarPassif.txIcEuBrt : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Taux d'intérêts crédités Euro brut de taf et tfgse",
                
            ),
            VarPassif.txIcEuDemiPeriode : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Taux d'intérêts crédités Euro",
                
            ),
            VarPassif.txIcUcDemiPeriode : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Taux d'intérêts crédités UC",
                
            ),
            VarPassif.txIcEuBrtDemiPeriode : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Taux d'intérêts crédités Euro brut de taf et tfgse",
                
            ),

            VarPassif.facteurActuTxTech : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Facteur d'actualisation au taux technique",
                
            ),

            # Montants
            VarPassif.cdHrgEu : DataTypeDesc(
                data_type=pl.Int32,
                description=f"HRG associé au support euro",
            ),

            VarPassif.mtPmEuAv : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Montant de la PM (avant évènement)",
                
            ),
            VarPassif.mtPmEu : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Montant de la PM",
            ),

            VarPassif.mtPrstTotEuBrt : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Montant de prestations totales, brutes de chargements",
                
            ),
            VarPassif.mtPrstTotEuNet : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Montant de prestations totales, nettes de chargements",
                
            ),
            VarPassif.mtPrstTotEuChgt : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Montant de chargements sur l'ensemble des prestations",
            ),
          
            VarPassif.mtPrstDcEuBrt : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Montant de prestations décès, brutes de chargements",
            ),
            VarPassif.mtPrstDcEuNet : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Montant de prestations décès, nettes de chargements",
            ),
            VarPassif.mtPrstDcEuChgt : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Montant de chargements sur les prestations décès",
            ),
            VarPassif.mtPrstRtEuBrt : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Montant de prestations rachat, brutes de chargements",
            ),
            VarPassif.mtPrstRtEuNet : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Montant de prestations rachat, nettes de chargements",
            ),
            VarPassif.mtPrstRtEuChgt : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Montant de chargements sur les prestations rachats",
            ),


            VarPassif.cdHrgUc : DataTypeDesc(
                data_type=pl.Int32,
                description=f"HRG associé au support uc",
            ),

            VarPassif.mtPmUcAv : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Montant de la PM (avant évènement)",
                
            ),
            VarPassif.mtPmUc : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Montant de la PM",
            ),

            VarPassif.mtPrstTotUcBrt : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Montant de prestations totales, brutes de chargements",
                
            ),
            VarPassif.mtPrstTotUcNet : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Montant de prestations totales, nettes de chargements",
                
            ),
            VarPassif.mtPrstTotUcChgt : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Montant de chargements sur l'ensemble des prestations",
            ),
          
            VarPassif.mtPrstDcUcBrt : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Montant de prestations décès, brutes de chargements",
            ),
            VarPassif.mtPrstDcUcNet : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Montant de prestations décès, nettes de chargements",
            ),
            VarPassif.mtPrstDcUcChgt : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Montant de chargements sur les prestations décès",
            ),
            VarPassif.mtPrstRtUcBrt : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Montant de prestations rachat, brutes de chargements",
            ),
            VarPassif.mtPrstRtUcNet : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Montant de prestations rachat, nettes de chargements",
            ),
            VarPassif.mtPrstRtUcChgt : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Montant de chargements sur les prestations rachats",
            ),
            

            VarPassif.mtIcEuRest : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Montant d'intérêts crédités des contrats Euro encore en cours à la fin de l'année",
                
            ),
            

            VarPassif.mtIcUcRest : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Montant d'intérêts crédités des contrats UC encore en cours à la fin de l'année",
                
            ),
            VarPassif.mtIcEuSort : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Montant d'intérêts crédités des contrats Euro sortis en cours d'année",
                
            )
            ,
            VarPassif.mtIcUcSort : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Montant d'intérêts crédités des contrats UC sortis en cours d'année",
                
            ),
            VarPassif.mtFgseUc : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Montant de frais de gestion sur encours",
                
            ),
            VarPassif.mtFgseEu : DataTypeDesc(
                data_type=pl.Float64,  
                description=f"Montant de la marge financière assuré issue des TFGSE",
            ),

            VarPassif.mtPbAss : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Assiette utilisée pour le calcul de la PB",
                
            ),
            VarPassif.mtPbBrt : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Montant de PB brut de CSG",
                
            ),
            VarPassif.mtPbBrtCg : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Montant de PB brut post application des TAF et TFGSE",
                
            ),
            VarPassif.mtPbNet : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Montant de PB net de CSG",
                
            ),
            VarPassif.mtCsg : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Montant de CSG",
            ),
            
            VarPassif.nbCntAncienneteAnnee : DataTypeDesc(
                data_type=pl.Int32, 
                description=f"Ancienneté du contrat en année",
            ),
            VarPassif.nbCntAncienneteMois : DataTypeDesc(
                data_type=pl.Int32, 
                description=f"Ancienneté du contrat en mois",
            ),

            VarPassif.generation : DataTypeDesc(
                data_type=pl.Int32, 
                description=f"Année de naissance d'une génération donnée",
                
            ),
            VarPassif.qx : DataTypeDesc(
                data_type=pl.Float64, 
                description=f"Taux de mortalité",
            ),
        })
        varlistwarning = self.checkVarListNotRegistered([var.value for var in VarPassif])
        if len(varlistwarning) > 0 :
            logging.warning(f"Les varaibles suivantes ne sont pas présentes dans ddPassifEp : {varlistwarning}")

ddPassifEp = DdPassifEp()
