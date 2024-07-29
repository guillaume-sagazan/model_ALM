from polars import DataFrame
import polars as pl
from metadata.dd.DdAlm import VarAlm
from metadata.dd.DdFgx import VarFgx
from metadata.dd.DdPassifEp import VarPassif
from metadata.dfmd.DfMdPassifEp import dfMdPassifEp

def mpPassifEpProjPerfBuild(mpPassifEpProj : DataFrame,mpPassifEpProjHypsPrstT : DataFrame,mpPassifEpProjHypsIcFgxT : DataFrame) -> DataFrame :
    mpPassifEpProjPerf = mpPassifEpProj.join(
        mpPassifEpProjHypsPrstT,
        how = 'left',
        on = dfMdPassifEp.mdMpPassifEpProjHypsPrst.pks
    ).join(
        mpPassifEpProjHypsIcFgxT,
        how='left',
        on=dfMdPassifEp.mdMpPassifEpProjHypsIcFgx.pks
    ).with_columns([ #Actualisation des Pm à mi période
        (pl.col(VarPassif.mtPmEuAv)*( 1.0 + pl.col(VarPassif.txIcEuDemiPeriode) )).alias(VarPassif.mtPmEu),
        (pl.col(VarPassif.mtPmUcAv)*( 1.0 + pl.col(VarPassif.txIcUcDemiPeriode) )).alias(VarPassif.mtPmUc),

    ]).with_columns([#Calcul des montants de prestations de rachat totaux puis update des PM
        (pl.col(VarPassif.mtPmEu)*pl.col(VarPassif.txPrstRt)).alias(VarPassif.mtPrstRtEuBrt),
        (pl.col(VarPassif.mtPmUc)*pl.col(VarPassif.txPrstRt)).alias(VarPassif.mtPrstRtUcBrt),
        (pl.col(VarPassif.mtPmEu)*( 1.0 - pl.col(VarPassif.txPrstRt))).alias(VarPassif.mtPmEu),
        (pl.col(VarPassif.mtPmUc)*( 1.0 - pl.col(VarPassif.txPrstRt))).alias(VarPassif.mtPmUc),

    ]).with_columns([#Calcul des montants de prestations de décès puis update des PM
        (pl.col(VarPassif.mtPmEu)*pl.col(VarPassif.txPrstDcAsseExp)).alias(VarPassif.mtPrstDcEuBrt),
        (pl.col(VarPassif.mtPmUc)*pl.col(VarPassif.txPrstDcAsseExp)).alias(VarPassif.mtPrstDcUcBrt),
        (pl.col(VarPassif.mtPmEu)*( 1.0 - pl.col(VarPassif.txPrstDcAsseExp))).alias(VarPassif.mtPmEu),
        (pl.col(VarPassif.mtPmUc)*( 1.0 - pl.col(VarPassif.txPrstDcAsseExp))).alias(VarPassif.mtPmUc),

        # TODO : Vérifier ces formules 
        (pl.col(VarPassif.mtPmEu)*pl.col(VarPassif.txIcEuDemiPeriode)).alias(VarPassif.mtIcEuRest),
        (pl.col(VarPassif.mtPmUc)*pl.col(VarPassif.txIcUcDemiPeriode)).alias(VarPassif.mtIcUcRest),
        ((pl.col(VarPassif.mtPmEuAv)*( 1.0 + pl.col(VarPassif.txIcEuDemiPeriode))-pl.col(VarPassif.mtPmEu))*pl.col(VarPassif.txIcEuDemiPeriode)).alias(VarPassif.mtIcEuSort),
        ((pl.col(VarPassif.mtPmUcAv)*( 1.0 + pl.col(VarPassif.txIcUcDemiPeriode))-pl.col(VarPassif.mtPmUc))*pl.col(VarPassif.txIcUcDemiPeriode)).alias(VarPassif.mtIcUcSort),

    ]).with_columns([#Actualisation des Pm à fin de période
        (pl.col(VarPassif.mtPmEu)*( 1.0 + pl.col(VarPassif.txIcEuDemiPeriode) )).alias(VarPassif.mtPmEu),
        (pl.col(VarPassif.mtPmUc)*( 1.0 + pl.col(VarPassif.txIcUcDemiPeriode) )).alias(VarPassif.mtPmUc),

    ]).with_columns([# Calcul des montants de chargements 
        (pl.col(VarPassif.mtPrstRtEuBrt)*pl.col(VarPassif.txPrstChgt)).alias(VarPassif.mtPrstRtEuChgt),
        (pl.col(VarPassif.mtPrstRtUcBrt)*pl.col(VarPassif.txPrstChgt)).alias(VarPassif.mtPrstRtUcChgt),
        (pl.col(VarPassif.mtPrstDcEuBrt)*pl.col(VarPassif.txPrstChgt)).alias(VarPassif.mtPrstDcEuChgt),
        (pl.col(VarPassif.mtPrstDcUcBrt)*pl.col(VarPassif.txPrstChgt)).alias(VarPassif.mtPrstDcUcChgt),

    ]).with_columns([ # Calcul des montants nets 
        (pl.col(VarPassif.mtPrstRtEuBrt)-pl.col(VarPassif.mtPrstRtEuChgt)).alias(VarPassif.mtPrstRtEuNet),
        (pl.col(VarPassif.mtPrstRtUcBrt)-pl.col(VarPassif.mtPrstRtUcChgt)).alias(VarPassif.mtPrstRtUcNet),
        (pl.col(VarPassif.mtPrstDcEuBrt)-pl.col(VarPassif.mtPrstDcEuChgt)).alias(VarPassif.mtPrstDcEuNet),
        (pl.col(VarPassif.mtPrstDcUcBrt)-pl.col(VarPassif.mtPrstDcUcChgt)).alias(VarPassif.mtPrstDcUcNet),

    ]).with_columns([ #Calculs des prestas au total
        (pl.col(VarPassif.mtPrstDcEuBrt)+pl.col(VarPassif.mtPrstRtEuBrt)).alias(VarPassif.mtPrstTotEuBrt),
        (pl.col(VarPassif.mtPrstDcEuNet)+pl.col(VarPassif.mtPrstRtEuNet)).alias(VarPassif.mtPrstTotEuNet),
        (pl.col(VarPassif.mtPrstDcEuChgt)+pl.col(VarPassif.mtPrstRtEuChgt)).alias(VarPassif.mtPrstTotEuChgt),
        (pl.col(VarPassif.mtPrstDcUcBrt)+pl.col(VarPassif.mtPrstRtUcBrt)).alias(VarPassif.mtPrstTotUcBrt),
        (pl.col(VarPassif.mtPrstDcUcNet)+pl.col(VarPassif.mtPrstRtUcNet)).alias(VarPassif.mtPrstTotUcNet),
        (pl.col(VarPassif.mtPrstDcUcChgt)+pl.col(VarPassif.mtPrstRtUcChgt)).alias(VarPassif.mtPrstTotUcChgt)

    ]).with_columns( # Calculs des frais généraux
        (pl.col(VarFgx.txFgxPmEu)*pl.col(VarPassif.mtPmEu)).alias(VarFgx.mtFgxPmEu),
        (pl.col(VarFgx.txFgxPmUc)*pl.col(VarPassif.mtPmUc)).alias(VarFgx.mtFgxPmUc),
        (pl.col(VarFgx.txFgxPrstEu)*pl.col(VarPassif.mtPrstTotEuBrt)).alias(VarFgx.mtFgxPrstEu),
        (pl.col(VarFgx.txFgxPrstUc)*pl.col(VarPassif.mtPrstTotUcBrt)).alias(VarFgx.mtFgxPrstUc),
        (pl.col(VarPassif.tfgse)*pl.col(VarPassif.mtPmEu)).alias(VarPassif.mtFgseEu),
        (pl.col(VarPassif.tfgse)*pl.col(VarPassif.mtPmUc)).alias(VarPassif.mtFgseUc) # TODO : Peut être mettre à jour le mtPm en leur soustrayant les fgse
    ).with_columns( # Calculs des fuites potentielles
        (pl.col(VarPassif.mtPmEu)-(pl.col(VarPassif.mtPmEuAv)+pl.col(VarPassif.mtIcEuRest)+pl.col(VarPassif.mtIcEuSort)-pl.col(VarPassif.mtPrstTotEuBrt))).alias(VarAlm.mtFuiteVcEu),
        (pl.col(VarPassif.mtPmUc)-(pl.col(VarPassif.mtPmUcAv)+pl.col(VarPassif.mtIcUcRest)+pl.col(VarPassif.mtIcUcSort)-pl.col(VarPassif.mtPrstTotUcBrt))).alias(VarAlm.mtFuiteVcUc)
    )

    return mpPassifEpProjPerf
