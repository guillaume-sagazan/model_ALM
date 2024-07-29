from polars import DataFrame

from metadata.dd.DdActif import VarActif
from metadata.dd.DdPassifEp import VarPassif
from metadata.dd.DdProjection import IntraPeriod, VarProj
from metadata.dd.DdS2 import VarS2
import polars as pl
from metadata.dfmd.DfMdPassifEp import dfMdPassifEp
from metadata.dfmd.DfMdActif import dfMdActif

def mpActifCashInputCfPerfPassifBuild(mpPassifEpProjPerf : DataFrame) -> DataFrame :
    mpActifCashInputCfPerfPassif = mpPassifEpProjPerf.select(
            [*dfMdPassifEp.mdMpPassifEpProjPerf.pks,
             VarPassif.mtPrstRtEuNet, VarPassif.mtPrstDcEuNet,
             VarPassif.mtPrstRtEuChgt, VarPassif.mtPrstDcEuChgt,
             VarPassif.mtFgseEu, VarPassif.mtPrstRtUcNet, 
             VarPassif.mtPrstDcUcNet, VarPassif.mtPrstRtUcChgt, 
             VarPassif.mtPrstDcUcChgt, VarPassif.mtFgseUc,
            ])\
        .group_by(set(dfMdPassifEp.mdMpPassifEpProjPerf.pks) & set(dfMdActif.mdMpActifCashInputCf.pks)).sum() \
        .melt(
            id_vars=set(dfMdPassifEp.mdMpPassifEpProjPerf.pks) & set(dfMdActif.mdMpActifCashInputCf.pks),
            value_vars=[
                VarPassif.mtPrstRtEuNet, VarPassif.mtPrstDcEuNet,
                VarPassif.mtPrstRtEuChgt, VarPassif.mtPrstDcEuChgt,
                VarPassif.mtFgseEu,VarPassif.mtPrstRtUcNet, VarPassif.mtPrstDcUcNet,
                VarPassif.mtPrstRtUcChgt, VarPassif.mtPrstDcUcChgt,
                VarPassif.mtFgseUc
            ],
            variable_name=VarS2.cdTypeFlux,
            value_name=VarActif.mtCf
        ).with_columns([
            pl.col(VarS2.cdTypeFlux).cast(pl.Categorical),
            (-pl.col(VarActif.mtCf)).alias(VarActif.mtCf),
            pl.lit(IntraPeriod.BEG).alias(VarProj.intraperiod)
        ]).select(dfMdActif.mdMpActifCashInputCf.allColumns)
    
    return mpActifCashInputCfPerfPassif 


