import polars as pl

def calcErrorRelative(refColName : str, colName : str) -> pl.Expr:
    """Méthode en charge de calculer l'erreur relative entre une colonne de référence et
    :param refColName: Nom de la colonne contenant les valeurs de référence
    :type refColName: str
    :param colName: Nom de la colonne contenant les valeurs
    :type colName: str
    """
    return 2 * ( pl.col(colName) - pl.col(refColName) ) / ( pl.col(colName) + pl.col(refColName) )
