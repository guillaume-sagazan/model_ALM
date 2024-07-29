import polars as pl
from metadata.dd.DdActif import VarActif
from metadata.dd.DdAlm import VarAlm
from metadata.dd.DdCommun import VarCommun
from metadata.dd.DdFgx import VarFgx
from metadata.dd.DdPassifEp import VarPassif
from metadata.dd.DdProjection import VarProj
from metadata.dd.DdS2 import CdChocS2, VarS2
from metadata.dfmd.DfMdCommun import dfMdCommun
from metadata.dfmd.DfMdProj import dfMdProj
from utils.DfMd import DfMd, buildDfMd



class DfMdS2:
    
    def __init__(self) :
        
        self.mdPksChocS2PassifMp : list[str] = [VarS2.cdChocS2, VarS2.cdChocS2Gse, VarS2.cdChocS2PassifPrst, VarS2.cdChocS2PassifIcFgx] 
        self.mdPksChocS2Actif : list[str] = [VarS2.cdChocS2, VarS2.cdChocS2Gse]

        self.mdDfCdChocS2 : DfMd = DfMd(
            pks=[VarS2.cdChocS2], 
            columns=[
                VarS2.cdChocS2Gse,
                VarS2.cdChocS2PassifPrst,
                VarS2.cdChocS2PassifIcFgx
            ]
        )

        self.mdDfCdChocS2Sc : DfMd = DfMd(
            pks=[VarS2.cdChocS2, VarProj.scenario], 
            columns=[
                VarS2.cdChocS2Gse,
                VarS2.cdChocS2PassifPrst,
                VarS2.cdChocS2PassifIcFgx
            ]
        )
        
        self.mdHypS2Chocs : DfMd = DfMd(
            pks=[VarS2.cdChocS2], 
            columns=[
                VarS2.txChocMort,
                VarS2.txChocLongevity,
                VarS2.txChocExpense,
                VarS2.txChocExpenseInflation,
                VarS2.txChocMortCat,
                VarS2.txChocLapse,
                VarS2.txChocLapseMass,
                VarS2.txChocEquityT1,
                VarS2.txChocEquityT2,
                VarS2.txChocEquityStrat,
                VarS2.txChocProperty,
                VarS2.txChocRevision,
                VarS2.txChocInval,
            ]
        )

        self.mdHypS2ChocsInit : DfMd = DfMd(
            pks=self.mdHypS2Chocs.pks, 
            columns=[VarS2.cdChocS2Gse, VarS2.cdChocS2PassifIcFgx, VarS2.cdChocS2PassifPrst, *self.mdHypS2Chocs.columns]
        )

        self.mdHypS2ChocsSpread : DfMd = DfMd(
            pks=[VarActif.cdClasseActifDetail, VarS2.nbDurationMin, VarS2.nbDurationMax, VarActif.cdCqs], 
            columns=[
                VarS2.txChocSpreadA,VarS2.txChocSpreadB
            ]
        )

dfMdS2 = DfMdS2()

refCdChocS2 : pl.DataFrame = pl.DataFrame(data={
    VarS2.cdChocS2 :                    [CdChocS2.central,    CdChocS2.lapseDown,   CdChocS2.lapseUp,     CdChocS2.lapseMass,       CdChocS2.mortality,   CdChocS2.longevity,   CdChocS2.mortalityCat,    CdChocS2.expense,     CdChocS2.ratesUp,     CdChocS2.ratesDown,   CdChocS2.property,    CdChocS2.equity,      CdChocS2.spread],
    VarS2.cdChocS2Gse :                 [CdChocS2.central,    CdChocS2.central,     CdChocS2.central,     CdChocS2.central,         CdChocS2.central,     CdChocS2.central,     CdChocS2.central,         CdChocS2.central,     CdChocS2.ratesUp,     CdChocS2.ratesDown,   CdChocS2.central,     CdChocS2.central,     CdChocS2.central],
    VarS2.cdChocS2PassifPrst :          [CdChocS2.central,    CdChocS2.lapseDown,   CdChocS2.lapseUp,     CdChocS2.lapseMass,       CdChocS2.mortality,   CdChocS2.longevity,   CdChocS2.mortalityCat,    CdChocS2.central,     CdChocS2.central,     CdChocS2.central,     CdChocS2.central,     CdChocS2.central,     CdChocS2.central],
    VarS2.cdChocS2PassifIcFgx :         [CdChocS2.central,    CdChocS2.central,     CdChocS2.central,     CdChocS2.central,         CdChocS2.central,     CdChocS2.central,     CdChocS2.central,         CdChocS2.expense,     CdChocS2.ratesUp,     CdChocS2.ratesDown,   CdChocS2.central,     CdChocS2.central,     CdChocS2.central]
}, schema=buildDfMd([VarS2.cdChocS2, VarS2.cdChocS2Gse, VarS2.cdChocS2PassifPrst, VarS2.cdChocS2PassifIcFgx]))

mappingCfBe = pl.DataFrame(data={
    VarS2.cdTypeFlux :          [VarPassif.mtPmEu,  VarPassif.mtPmUc,   VarAlm.mtPpe,   VarPassif.mtPrstRtEuNet,    VarPassif.mtPrstDcEuNet,    VarFgx.mtFgxPmEu,   VarFgx.mtFgxPrstEu,     VarFgx.mtFgxPlctEu, VarPassif.mtPrstRtUcNet,    VarPassif.mtPrstDcUcNet,    VarFgx.mtFgxPmUc,   VarFgx.mtFgxPrstUc,     VarFgx.mtFgxPlctUc],
    VarS2.cdTypeProvMvBeNav :   [VarS2.mtBeBrt,     VarS2.mtBeBrt,      VarS2.mtBeBrt,  VarS2.mtBeBrt,              VarS2.mtBeBrt,              VarS2.mtBeBrt,      VarS2.mtBeBrt,          VarS2.mtBeBrt,      VarS2.mtBeBrt,              VarS2.mtBeBrt,              VarS2.mtBeBrt,      VarS2.mtBeBrt,          VarS2.mtBeBrt],
    VarCommun.facteur :         [-1.0,              -1.0,               -1.0,           -1.0,                       -1.0,                       -1.0,               -1.0,                   -1.0,               -1.0,                       -1.0,                       -1.0,               -1.0,                   -1.0]
},schema=buildDfMd([VarS2.cdTypeFlux, VarS2.cdTypeProvMvBeNav, VarCommun.facteur]))