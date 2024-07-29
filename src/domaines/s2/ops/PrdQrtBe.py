from polars import DataFrame

from metadata.dfmd.DfMdS2 import dfMdS2

def prdQrtBeBuild(prdQrtBeSc : DataFrame) -> DataFrame:
    """Méthode en charge de faire la moyenne des Best Estimate par scenario
    :param rcarsSc: Best Estimate par scenarios
    :type rcarsSc: DataFrame
    :return: Best Estimate
    :rtype: DataFrame
    """

    if prdQrtBeSc is None:
        return None

    prdQrtBe = prdQrtBeSc.group_by(dfMdS2.mdPrdQrtBe.pks).mean()
    return prdQrtBe

