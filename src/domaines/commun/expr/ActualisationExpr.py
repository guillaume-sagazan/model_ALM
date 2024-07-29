import polars as pl
from polars import DataFrame

from metadata.dd.DdActif import VarActif
from metadata.dd.DdProjection import VarProj

def calcDp(colMtCf : str, colPzc : str) -> pl.Expr:
    return pl.col(colMtCf) * pl.col(colPzc)

def calcDfDp(
        dfMtCf : DataFrame,
        colMtCf : str,
        dfPzc : DataFrame,
        mappingColPzcVa : dict[str, str],
        by : list[str],
        on : list[str] = [VarActif.maturite, VarProj.intraperiod],
        colMaturite : str = VarActif.maturite,
        colIntraperiod : str = VarProj.intraperiod) -> DataFrame :

    """
    Cette fonction permet d'actualiser les flux présents dans un premier dataframe dans un second dataframe

    :param dfMtCf: Dataframe contenant la liste des cashflows futurs
    :type dfMtCf: DataFrame

    :param colMtCf: Colonne contenant les montants de cashflows
    :type colMtCf: str

    :param dfPzc: Dataframe contenant les prix à appliquer
    :type dfPzc: DataFrame

    :param mappingColPzcVa: Mapping entre les colonnes PZC et les colonnes qui comprendront les valeurs actualisées
    :type mappingColPzcVa: dict[str, str]

    :param by: Liste des colonnes utilisées pour agréger les résultats
    :type by: list[str]

    :param on: Liste des colonnes sur lesquelles les colonnes PZC et Cf seront fusionnées (par défaut [VarActif.maturite, VarProj.intraperiod])
    :type on: list[str]

    :param colMaturite: Colonne maturité (par défaut VarActif.maturite)
    :type colMaturite: str

    :param colIntraperiod: Colonne intraperiod (par défaut VarProj.intraperiod)
    :type colIntraperiod: str

    :return: Dataframe contenant les valeurs actualisées selon les axes définis dans le paramètre by
    :rtype: DataFrame
    """

    #A noter que udp_df et cf_df sont sensés disposer des index maturite_col et intraperiod_col
    maturiteColInDfPzc: bool = colMaturite in dfPzc.columns
    intraperiodColInDfPzc: bool = colIntraperiod in dfPzc.columns
    if not intraperiodColInDfPzc :
        raise(Exception(f"Colonne {colIntraperiod} non trouvée dans l'index de dfPzc"))
    if not maturiteColInDfPzc:
        raise (Exception(f"Colonne {colMaturite} non trouvée dans l'index de dfPzc"))

    maturiteColInDfCf: bool = colMaturite in dfMtCf.columns
    intraperiodColInDfCf: bool = colIntraperiod in dfMtCf.columns
    if not intraperiodColInDfCf :
        raise(Exception(f"Colonne {colIntraperiod} non trouvée dans l'index de dfCf"))
    if not maturiteColInDfCf:
        raise (Exception(f"Colonne {colMaturite} non trouvée dans l'index de dfCf"))

    #Si udp_df <> cf_df alors on construit le merge des deux sur [DdRef.maturite, DdRef.intraperiod]
    if id(dfPzc) != id(dfMtCf):
        result : DataFrame = dfMtCf.join(dfPzc, how='left', on=on)
    else:
        result = dfMtCf
    
    calcExpr = [(pl.col(colMtCf) * pl.col(colPzc)).alias(colDp) for colPzc, colDp in mappingColPzcVa.items()]
    aggExpr = [pl.col(colDp).sum().alias(colDp) for colDp in mappingColPzcVa.values()]
    
    result = result.with_columns(
        calcExpr
    ).group_by(by).agg(aggExpr)

    return result



