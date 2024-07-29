import logging
from typing import Tuple
import polars as pl
from polars import DataFrame

from domaines.gse.expr.GseExpr import calcCashPerf, calcPzc
from domaines.gse.ops.GseCashPerfBuild import gseOutputCashPerfBuild
from metadata.dd.DdActif import CdClasseActif, VarActif
from metadata.dd.DdGse import VarGse
from metadata.dd.DdProjection import IntraPeriod, VarProj
from metadata.dd.DdS2 import VarS2
from metadata.dfmd.DfMdGse import dfMdGse

TX_INFLATION_DEFAULT_VALUE = 0.01
TX_DIVIDENDES_DEFAULT_VALUE = 0.00




def gseOutputBuildCrn(
        gseCtRefObligPzc : DataFrame,
        projHorizon : int,
        gseObligMaturiteMax : int,
        txDividendes : float = TX_DIVIDENDES_DEFAULT_VALUE
        ) -> Tuple[DataFrame, DataFrame, DataFrame]:

    """Méthode en charge de la construction automatique des
    
    :param gseCtRefObligPzc: Prix zéro coupon associés à la courbe des taux de référence
    :type gseCtRefObligPzc: DataFrame
    :param projHorizon: Horizon de projection
    :type projHorizon: int
    :param gseObligMaturiteMax: Maturité maximum à prendre en compte pour la valorisation des obligations
    :type gseObligMaturiteMax: int
    :param tx_dividendes: Taux de dividendes. Valeur par défaut = 0.0
    :type tx_dividendes:  float
    
    :return:
        * DataFrame[GseOutputObligPzc] : Prix zéro coupon utilisés pour la valorisation des obligations
        * DataFrame[GseOutputIndicesPerf] : Performance des actifs indiciels
        * DataFrame[gseOutputCashPerf] : Performance du cash
    
    L'ensemble des outputs sont construits sur la base du calcul des différents taux forward issus de la courbe des taux de référence en input de cette méthode.
    
    """
    logging.debug("Initialisation : Global : Gse : Construction gseOutputObligPzcCrn")
    gseOutputObligPzcCrn = gseCtRefObligPzc.filter(pl.col(VarActif.maturite) <= projHorizon + gseObligMaturiteMax) \
                    .with_columns(pl.lit(1).alias(VarProj.scenario).cast(pl.Int32)) \
                    .with_columns(pl.lit(list(range(0,projHorizon + 1))).alias(VarProj.period)) \
                    .explode(VarProj.period) \
                    .with_columns(pl.col(VarProj.period).alias(VarProj.period).cast(pl.Int32)) \
                    .with_columns((pl.col(VarActif.maturite) - pl.col(VarProj.period)).alias(VarActif.maturite)) \
                    .filter(pl.col(VarActif.maturite) >= 0) \
                    .sort([VarProj.scenario, VarProj.period, VarProj.intraperiod, VarActif.maturite])

    gseOutputObligPzcCrnOffset = gseCtRefObligPzc.filter(pl.col(VarProj.intraperiod) == IntraPeriod.END) \
        .drop(VarProj.intraperiod) \
        .rename(
            {VarActif.maturite : VarProj.period, VarGse.pzc : "pzcStart"}
        )
                         
    gseOutputObligPzcCrn = gseOutputObligPzcCrn \
                            .join(gseOutputObligPzcCrnOffset, on=[VarS2.cdChocS2Gse, VarProj.period], how='left') \
                            .filter((pl.col(VarProj.period) >= 0) & (pl.col(VarProj.period) <= projHorizon)) \
                            .sort([VarProj.scenario, VarProj.period, VarActif.maturite, VarProj.intraperiod]) \
                            .with_columns((pl.col(VarGse.pzc) / pl.col("pzcStart")).alias(VarGse.pzc)) \
                            .with_columns(
                                pl.when(pl.col(VarActif.maturite) == 0)
                                .then(pl.lit(1.0))
                                .otherwise(pl.col(VarGse.pzc))
                                .alias(VarGse.pzc)
                            ).drop("pzcStart")

    
    logging.debug("Initialisation : Global : Gse : Construction gseOutputCashPerfCrn")
    gseOutputCashPerfCrn = gseOutputCashPerfBuild(gseOutputObligPzcCrn, projHorizon)

    gseOutputIndicesPerfCrn = gseOutputCashPerfCrn.filter(pl.col(VarProj.intraperiod) == IntraPeriod.BEG) \
        .drop(VarProj.intraperiod) \
        .with_columns(pl.lit([CdClasseActif.ACTION, CdClasseActif.IMMOBILIER]).alias(VarActif.cdClasseActif)) \
        .explode(VarActif.cdClasseActif) \
        .with_columns(pl.lit(txDividendes).alias(VarGse.txDividendes)) \
        .with_columns((pl.col(VarGse.facteurPerfTot) - pl.col(VarGse.txDividendes)).alias(VarGse.facteurPerfNet))

    logging.info("Initialisation : Global : Gse : Fin")

    return gseOutputObligPzcCrn, gseOutputIndicesPerfCrn, gseOutputCashPerfCrn