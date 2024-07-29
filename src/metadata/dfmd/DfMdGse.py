from dataclasses import dataclass, field
from enum import auto
from typing import OrderedDict
import polars as pl


from metadata.dd.DdActif import VarActif
from metadata.dd.DdGse import VarGse
from metadata.dd.DdProjection import VarProj
from metadata.dd.DdS2 import VarS2
from utils.DfMd import DfMd



class DfMdGse:
    
    def __init__(self) :
        
        self.mdGseCtRefInput : DfMd = DfMd(
            pks=[VarProj.cdTrajectoire, VarProj.dtTrajectoire, VarGse.cdCtRef, VarActif.maturite, VarS2.cdChocS2Gse], 
            columns=[
                VarGse.tzc
            ]
        )
        
        # self.mdGseCtRef : DfMd = DfMd(
        #     pks=[VarS2.cdChocS2Gse, VarActif.maturite, VarProj.intraperiod], 
        #     columns=[VarGse.tzc]
        # )

        self.mdGseCtRefObligPzc : DfMd = DfMd(
            pks=[VarS2.cdChocS2Gse, VarActif.maturite, VarProj.intraperiod], 
            columns=[VarGse.pzc]
        )

        self.mdGseCtRefCashPerf : DfMd = DfMd(
            pks=[VarS2.cdChocS2Gse, VarProj.period, VarProj.intraperiod], 
            columns=[VarGse.facteurPerfTot]
        )

        self.mdGseOutputObligInput : DfMd = DfMd(
            pks=[VarProj.cdTrajectoire, VarProj.dtTrajectoire, VarProj.scenario, VarActif.cdClasseActif, VarS2.cdChocS2Gse,  VarActif.maturite, VarProj.period], 
            columns=[VarGse.tzc]
        )

        self.mdGseOutputIndicesInput : DfMd = DfMd(
            pks=[VarProj.cdTrajectoire, VarProj.dtTrajectoire ,VarProj.scenario, VarS2.cdChocS2Gse, VarActif.cdClasseActif, VarProj.period], 
            columns=[VarGse.txPerfTot, VarGse.txDividendes]
        )

        self.mdGseOutputObligPzc : DfMd = DfMd(
            pks=[VarS2.cdChocS2Gse, 
                 VarProj.scenario,
                 VarProj.period,
                 VarActif.maturite,
                 VarProj.intraperiod], 
            columns=[VarGse.pzc]
        )

        self.mdGseOutputIndicesPerf : DfMd = DfMd(
            pks=[VarS2.cdChocS2Gse, VarProj.scenario, VarProj.period, VarActif.cdClasseActif], 
            columns=[
                VarGse.facteurPerfTot, VarGse.facteurPerfNet, VarGse.txDividendes
            ]
        )

        self.mdGseOutputCashPerf : DfMd = DfMd(
            pks=[VarS2.cdChocS2Gse, VarProj.scenario, VarProj.period, VarProj.intraperiod], 
            columns=[VarGse.facteurPerfTot]
        )

        self.mdGseOutputDeflateur : DfMd = DfMd(
            pks=[VarS2.cdChocS2Gse, VarProj.scenario, VarProj.period, VarProj.intraperiod], 
            columns=[VarGse.deflateur]
        )

        self.mdGseOutputInflationInput : DfMd = DfMd(
            pks=[VarProj.cdTrajectoire, VarProj.dtTrajectoire, VarProj.scenario, VarProj.period, VarActif.maturite, VarS2.cdChocS2Gse], 
            columns=[VarGse.txInflation]
        )
        
        self.mdGseOutputInflationInitS2 : DfMd = DfMd(
            pks=[VarS2.cdChocS2PassifIcFgx, VarProj.scenario, VarProj.period], 
            columns=[            
                VarGse.txInflation,
                VarGse.facteurInflationCum
            ]
        )

dfMdGse = DfMdGse()
