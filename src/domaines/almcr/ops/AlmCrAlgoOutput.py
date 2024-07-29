from typing import Iterable, Tuple
import polars as pl
from polars import DataFrame

from dao.writers.ResultsWriter import ResultsWriter
from domaines.almcr.expr.AlmCrExpr import calcMtPbBrtBesoinTxCible, calcMtPfiAsse, calcMtPfiAssePb, calcMtPfiAssr, calcMtPfiBesoinTxCible
from domaines.almcr.pipelines.AlmCrAlgoUtils import almCrAlmOutputPassifFromTxServiBrt
from metadata.dd.DdFgx import VarFgx
from metadata.dd.DdActif import VarActif
from metadata.dd.DdAlm import VarAlm, StratAlmCas
from metadata.dd.DdPassifEp import VarPassif
from metadata.dd.DdCommun import VarCommun
from metadata.dd.DdProjection import VarProj
from metadata.dd.DdS2 import VarS2
from metadata.dfmd.DfMdCommun import DfMdCommun
from metadata.dfmd.DfMdAlmCr import DfMdAlm,stratAlmCasOrdrePriorite
from metadata.dfmd.DfMdPassifEp import DfMdPassif
from metadata.dfmd.DfMdProj import DfMdProj

def buildStratAlmOutput(
        almCrInputPassif:DataFrame,
        almCrInputActif:DataFrame,
        almCrInputPpe:DataFrame,
        almCrInputTxServiCible:DataFrame,
        prdAdPassifPerf:DataFrame,
        ) -> DataFrame:

    # Calcul de la PB Brute sur la base du txServiNet
    almCrInputTxIcBrt = almCrInputPassif.with_columns([
        ( pl.col(VarPassif.mtPbAss) * pl.col(VarPassif.taf) ).alias(VarAlm.pentePbBrt),
        pl.col(VarPassif.mtPbAss).alias(VarAlm.pentePfi)
    ]).groupby(dfMdAlmCr.mdAlmCrInputTxIcBrt.pks).agg([
        pl.col(VarAlm.pentePbBrt).sum(),
        pl.col(VarAlm.pentePfi).sum()
    ]).sort(
        dfMdAlmCr.mdAlmCrInputTxIcBrt.pks
    ).with_columns([
        pl.col(VarAlm.pentePbBrt).cumsum().over([VarS2.cdChocS2, *DfMdProj().mdPksScPer, *DfMdCommun().mdPksCanton]).alias(VarAlm.pentePbBrt),
        pl.col(VarAlm.pentePfi).sum().over([VarS2.cdChocS2, *DfMdProj().mdPksScPer, *DfMdCommun().mdPksCanton]).alias(VarAlm.pentePfi)
    ])

    ResultsWriter().writeDf2Table(df=almCrInputTxIcBrt, tableName='almCrInputTxIcBrt')

    pksAlmCrAlmOutputTxIcBrt = set(dfMdAlmCr.mdAlmCrAlmOutput.pks) - {VarAlm.stratAlmCas} | {VarAlm.txServiBrt}
    pksAlmCrAlmOutputMtPfiTmg = set(dfMdAlmCr.mdAlmCrAlmOutput.pks) - {VarAlm.stratAlmCas}

    almCrAlmOutputPassifTxIcBrt = \
        almCrAlmOutputPassifFromTxServiBrt(almCrInputPassif, almCrInputTxIcBrt, VarPassif.txIcBrt) \
        .group_by(pksAlmCrAlmOutputTxIcBrt).agg(
            pl.col(VarAlm.pentePbBrt).mean(),
            pl.col(VarAlm.pentePfi).mean(),
            pl.col(VarPassif.mtPbBrt).sum(),
            pl.col(VarActif.mtPfi).sum()
        ).with_columns(
            pl.col(VarActif.mtPfi).min().over(pksAlmCrAlmOutputMtPfiTmg).alias('mt_pfi_tmg')
        ).rename({
            VarAlm.txServiBrt : VarAlm.txServiBrt + "_" + VarPassif.txIcBrt,
            VarPassif.mtPbBrt : VarPassif.mtPbBrt + "_" + VarPassif.txIcBrt,
            VarActif.mtPfi : VarActif.mtPfi + "_" + VarPassif.txIcBrt
        })
    
    ResultsWriter().writeDf2Table(df=almCrAlmOutputPassifTxIcBrt, tableName='almCrAlmOutputPassifTxIcBrt')

    almCrAlmOutputTxCible = \
        almCrAlmOutputPassifFromTxServiBrt(almCrInputPassif, almCrInputTxServiCible, VarAlm.txCible) \
        .select(
            set(dfMdAlmCr.mdAlmCrAlmOutput.pks) | {VarPassif.mtIcRest, VarPassif.mtIcSort, VarAlm.txServiBrt, VarPassif.mtPbBrt, VarActif.mtPfi}
        ).group_by(dfMdAlmCr.mdAlmCrAlmOutput.pks).agg([
            pl.col(VarPassif.mtIcSort).sum(),
            pl.col(VarPassif.mtIcRest).sum(),
            pl.col(VarAlm.txServiBrt).mean(),
            pl.col(VarPassif.mtPbBrt).sum(),
            pl.col(VarActif.mtPfi).sum(),
        ]).rename({
            VarAlm.txServiBrt : VarAlm.txServiBrt + "_" + VarAlm.txCible,
            VarPassif.mtPbBrt : VarPassif.mtPbBrt + "_" + VarAlm.txCible,
            VarActif.mtPfi : VarActif.mtPfi + "_" + VarAlm.txCible
        })

    ResultsWriter().writeDf2Table(df=almCrAlmOutputTxCible, tableName='almCrAlmOutputPassifTxCible')
    ResultsWriter().writeDf2Table(df=prdAdPassifPerf, tableName='prdAdPassifPerf')

    almCrAlmOutput = almCrAlmOutputTxCible.join(
        almCrAlmOutputPassifTxIcBrt,
        how='left',
        on=set(almCrAlmOutputTxCible.columns) & set(almCrAlmOutputPassifTxIcBrt.columns)
    ).join(
        stratAlmCasOrdrePriorite,
        how='left',
        on=VarAlm.stratAlmCas
    ).join(
        almCrInputActif,
        how='left',
        on=dfMdAlmCr.mdAlmCrInputActif.pks
    ).join(
        almCrInputPpe,
        how='left',
        on=dfMdAlmCr.mdAlmCrInputActif.pks
    ).join(
        prdAdPassifPerf.select([*dfMdAlmCr.mdAlmCrInputActif.pks, VarPassif.mtFgseEu]),
        how='left',
        on=dfMdAlmCr.mdAlmCrInputActif.pks
    ).with_columns([
        pl.lit(0.0).alias(VarActif.mtPmvr),
        pl.lit(0.0).alias(VarAlm.mtPpeDotation),
        pl.lit(0.0).alias(VarAlm.mtPbBrtMinRegl)
    ]).with_columns([
        calcMtPfiAssr(alias=VarAlm.mtPfiAssr),
        calcMtPfiAsse(alias=VarAlm.mtPfiAsse)
    ]).with_columns([
        calcMtPfiAssePb(alias=VarAlm.mtPfiAssePb),
    ])
    
    ResultsWriter().writeDf2Table(df=almCrAlmOutput, tableName='almCrAlmOutput0')

    almCrAlmOutput = almCrAlmOutput.with_columns([
        calcMtPfiBesoinTxCible(alias=VarAlm.mtPfiBesoinTxCible),
    ]).with_columns( # Consommation des PMVL
        pl.when(
            pl.col(VarAlm.mtPfiBesoinTxCible) * pl.col(VarActif.mtPmvl) <= 0
        )
        .then(pl.lit(0.0))
        .when(
            (pl.col(VarAlm.mtPfiBesoinTxCible) <= 0.0) & (pl.col(VarActif.mtPmvl) <= 0)
        )
        .then(pl.max_horizontal(pl.col(VarActif.mtPmvl), pl.col(VarAlm.mtPfiBesoinTxCible)))
        .when(
            (pl.col(VarAlm.mtPfiBesoinTxCible) >= 0.0) & (pl.col(VarActif.mtPmvl) >= 0)
        )
        .then(pl.min_horizontal(pl.col(VarActif.mtPmvl), pl.col(VarAlm.mtPfiBesoinTxCible)))
        .alias(VarActif.mtPmvr)      
    ).with_columns(
        ( pl.col(VarAlm.mtPfiAssePb) + pl.col(VarActif.mtPmvr) ).alias(VarActif.mtPfi)
    ).with_columns(
        pl.when(pl.col(VarActif.mtPfi) - pl.col(VarActif.mtPfi + "_" + VarPassif.txIcBrt) >= 0.0 )
        .then(pl.col(VarActif.mtPfi) - pl.col(VarActif.mtPfi + "_" + VarPassif.txIcBrt))
        .otherwise(None)
        .alias('mt_pfi_tx_ic_brt_ecart')
    ).with_columns(
        pl.col('mt_pfi_tx_ic_brt_ecart').min().over(dfMdAlmCr.mdAlmCrAlmOutput.pks).alias('mt_pfi_tx_ic_brt_ecart_min')
    )

    ResultsWriter().writeDf2Table(df=almCrAlmOutput, tableName='almCrAlmOutputAll')

    almCrAlmOutput = almCrAlmOutput.filter(
        ( pl.col('mt_pfi_tx_ic_brt_ecart') == pl.col('mt_pfi_tx_ic_brt_ecart_min') ) |
        ( pl.col('mt_pfi_tx_ic_brt_ecart_min').is_null() & ( pl.col(VarActif.mtPfi + '_' + VarPassif.txIcBrt) == pl.col('mt_pfi_tmg') )
    
    )).with_columns([
        
        pl.when(pl.col('mt_pfi_tx_ic_brt_ecart').is_null())
        .then(pl.col(VarPassif.mtPbBrt + "_" + VarPassif.txIcBrt))
        .otherwise( pl.col(VarPassif.mtPbBrt + "_" + VarPassif.txIcBrt) + pl.col('mt_pfi_tx_ic_brt_ecart') * pl.col(VarAlm.pentePbBrt) / pl.col(VarAlm.pentePfi))
        .alias(VarPassif.mtPbBrt),

        pl.when(pl.col('mt_pfi_tx_ic_brt_ecart').is_null())
        .then(pl.col(VarAlm.txServiBrt + "_" + VarPassif.txIcBrt))
        .otherwise( pl.col(VarAlm.txServiBrt + "_" + VarPassif.txIcBrt) + pl.col('mt_pfi_tx_ic_brt_ecart') / pl.col(VarAlm.pentePfi))
        .alias(VarAlm.txServiBrt),

    ]).with_columns(
        (
            pl.col(VarAlm.mtPfiAssePb) - pl.col(VarPassif.mtIcRest) - pl.col(VarPassif.mtPbBrt) 
            + pl.col(VarAlm.mtPpeDotation) - pl.col(VarAlm.mtPpeReprise)
        ).alias(VarAlm.mtResBrtAsse)
    ).with_columns(
        (
            pl.col(VarAlm.mtPfiAssr) + pl.col(VarAlm.mtResBrtAsse)
        ).alias(VarAlm.mtResBrt)
    )

    
    ResultsWriter().writeDf2Table(df=almCrAlmOutput, tableName='almCrAlmOutputDebug')
    ResultsWriter().writeDf2Table(df=almCrAlmOutput.select(dfMdAlmCr.mdAlmCrAlmOutput.allColumns), tableName='almCrAlmOutputDebugResult')

    return almCrAlmOutput.select(dfMdAlmCr.mdAlmCrAlmOutput.allColumns)