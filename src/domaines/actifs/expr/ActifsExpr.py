import polars as pl
from polars import DataFrame

from domaines.gse.expr.GseExpr import calcPzc
from domaines.commun.expr.NumericExpr import calcErrorRelative
from metadata.dd.DdActif import CdClasseActif, VarActif
from metadata.dd.DdAlm import VarAlm
from metadata.dd.DdGse import VarGse
from metadata.dfmd.DfMdActif import dfMdActif

mappingTraPzc = {'tra_1': 'pzc_1', 'tra_2': 'pzc_2', 'tra_3': 'pzc_3'}
mappingPzcMtVc = {'pzc_1': 'mt_vc_1', 'pzc_2': 'mt_vc_2', 'pzc_3': 'mt_vc_3'}
mappingMtVcMtVcError = {'mt_vc_1': 'mt_vc_1_error', 'mt_vc_2': 'mt_vc_2_error', 'mt_vc_3': 'mt_vc_3_error'}

calcPzcExpr : pl.Expr = [calcPzc(colTzc=colTzc).alias(colPzc) for colTzc, colPzc in mappingTraPzc.items()]
calcMtVcCfExpr  : pl.Expr= [(pl.col(colPzc) * pl.col(VarActif.mtCf)).sum().over(dfMdActif.mdPksActifUnitaire).alias(colMtVc) for colPzc, colMtVc in mappingPzcMtVc.items()]
calcMtVcErrorExpr : pl.Expr = [calcErrorRelative(VarActif.mtVc, colMtVc).alias(colMtVcError) for colMtVc, colMtVcError in mappingMtVcMtVcError.items()]

def calcFuiteEco(colMtFuiteEco : str = VarAlm.mtFuiteEco, colMtVmFin : str = VarActif.mtVm, colMtCf : str = VarActif.mtCf, colMtVmDebut : str = VarActif.mtVmAv, colFacteurPerfTot : str = VarGse.facteurPerfTot + '_ct_ref') -> pl.Expr:
    """Cette fonction permet de calculer la fuite économique pour un dataframe donné
    :param colMtFuiteEco: nom de la colonne qui contiendra la fuite économique
    :param colMtVmFin: nom de la colonne qui contient la valeur de marché de fin de période
    :param colMtCf: nom de la colonne qui contient la valeur du cashflow
    :param colMtVmDebut: nom de la colonne qui contient la valeur du cashflow
    :param colFacteurPerfTot: nom de la colonne qui contient la performance totale attendue
    """
    return pl.col(colMtVmFin) + pl.col(colMtCf) - pl.col(colMtVmDebut) * pl.col(colFacteurPerfTot)

def calcFuiteVcActifPerf(colMtVcDebut : str = VarActif.mtVcAv, colMtVcFin : str = VarActif.mtVc, colMtCf : str = VarActif.mtCf, colMtPfi : str = VarActif.mtPfi) -> pl.Expr:
    """
    Cette fonction permet de calculer la fuite de valeur comptable
    :param colMtFuiteVc: nom de la colonne qui contiendra la fuite économique
    :param colMtVcDebut: nom de la colonne qui contient le montant de valeur comptable de début
    :param colMtVcFin: nom de la colonne qui contient le montant de valeur comptable de fin
    :param colMtCf: nom de la colonne qui contient le montant de cashflow
    :param colMtPfi: nom de la colonne qui contient le montant de produits financiers
    """
    return pl.col(colMtVcFin) - pl.col(colMtVcDebut) - pl.col(colMtPfi) + pl.col(colMtCf)


def calcPmvl(colMtVm : str = VarActif.mtVm, colMtVc : str = VarActif.mtVc) -> pl.Expr:
    """
    Calcule la plus-value ou la moins-value latente d'un actif en soustrayant le montant de vente du montant de valorisation.

    :param colMtVm: Le nom de la colonne contenant le montant de valorisation de l'actif (par défaut: VarActif.mtVm)
    :type colMtVm: str
    :param colMtVc: Le nom de la colonne contenant le montant de vente de l'actif (par défaut: VarActif.mtVc)
    :type colMtVc: str
    :return: La plus-value ou la moins-value latente de l'actif
    :rtype: Series
    """
    return pl.col(colMtVm) - pl.col(colMtVc)




def rsMpActifIndicesTxActionSommeNEq1 () -> pl.Expr :
    return ( pl.col(VarActif.cdClasseActif) == CdClasseActif.ACTION ) & ( pl.col(VarActif.txActionStrat)+pl.col(VarActif.txActionT1)+pl.col(VarActif.txActionT2) != 1.0 )
