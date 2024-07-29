import logging
import polars as pl
from polars import DataFrame, LazyFrame
from metadata.dd.DdActif import CdClasseActif, VarActif
from metadata.dd.DdProjection import VarProj
from metadata.dd.DdS2 import VarS2
from metadata.dd.DdStratInv import VarStratInv
from metadata.dfmd.DfMdActif import dfMdActif
from metadata.dfmd.DfMdProj import dfMdProj
from metadata.dfmd.DfMdCommun import dfMdCommun
# from dao.writers.ResultsWriter import ResultsWriter
# from outputs.ProjResult import ProjResultRctProjActif


def stratInvInputOutputBuild(period:int, dfCdChocS2Sc:DataFrame,  mpActifIndicesProj:DataFrame, hypStratInvTxAllocCible:DataFrame) -> DataFrame:

    logging.info(f'StratInv ({period}) : Algo')

    # Agrégation à la maille canton des mtVmAv
    stratInvInputOutput = hypStratInvTxAllocCible.join(
            dfCdChocS2Sc.select([VarS2.cdChocS2, VarS2.cdChocS2Gse, VarProj.scenario]),
            how='cross'
        ).with_columns(
            pl.lit(period).cast(pl.Int32).alias(VarProj.period)
        ).join(
            pl.concat([ mpActifIndicesProj]).select([*dfMdActif.mdStratInvInputOutput.pks, VarActif.mtVm]).rename({VarActif.mtVm : VarActif.mtVmAv}).group_by(dfMdActif.mdStratInvInputOutput.pks).sum(),
            how='left',
            on=[VarS2.cdChocS2, VarS2.cdChocS2Gse, VarProj.scenario, VarProj.period, *dfMdActif.mdHypStratInvTxAllocCible.pks]
        ).with_columns(
            pl.col(VarActif.mtVmAv).fill_null(0.0) #Au cas où l'on aurait pas d'obligations en portefeuille
        ).with_columns([
            pl.col(VarActif.mtVmAv).sum().over([*dfMdProj.mdPksScPer,*dfMdCommun.mdPksCanton]).alias(VarStratInv.mtVmAvCanton),
            pl.col(VarActif.mtVmAv).sum().over([*dfMdProj.mdPksScPer,*dfMdCommun.mdPksCanton,VarActif.cdClasseActif]).alias(VarStratInv.mtVmAvCdClasseActif),
        ]).with_columns([
            (pl.col(VarStratInv.mtVmAvCanton) * pl.col(VarStratInv.txAllocCible)).alias(VarStratInv.mtVmCibleCdClasseActif),
        ]).with_columns(
            ( pl.col(VarStratInv.mtVmCibleCdClasseActif)
                / pl.col(VarStratInv.mtVmAvCdClasseActif)
            ).alias(VarStratInv.facteurAchatVente)
        ).with_columns(
            pl.when(
                (pl.col(VarActif.cdClasseActif)==CdClasseActif.OBLIGATION)
                &((pl.col(VarStratInv.mtVmCibleCdClasseActif) - pl.col(VarStratInv.mtVmAvCdClasseActif)) > 0.0))
            .then(pl.col(VarStratInv.mtVmCibleCdClasseActif) - pl.col(VarStratInv.mtVmAvCdClasseActif))
            .otherwise(0.0)
            .alias(VarStratInv.mtAchatOblig)
        )
    
    return stratInvInputOutput

