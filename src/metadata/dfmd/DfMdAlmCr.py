import polars as pl

from metadata.dd.DdActif import VarActif
from metadata.dd.DdAlm import StratAlmCas, VarAlm
from metadata.dd.DdFgx import VarFgx
from metadata.dd.DdPassifEp import VarPassif
from metadata.dd.DdS2 import VarS2

from metadata.dfmd.DfMdCommun import DfMdCommun
from metadata.dfmd.DfMdPassifEp import DfMdPassif
from metadata.dfmd.DfMdProj import DfMdProj
from utils.DfMd import DfMd, buildDfMd

class DfMdAlmCr:
    
    def __init__(self):
        ######################################
        ### DataFrames associés aux Provisions comptables
        self.mdHypStratAlmInput : DfMd = DfMd(
            pks=[*DfMdCommun().mdPksCanton], 
            columns=[
                VarAlm.txPbMinReglSoldeFin, VarAlm.txPbMinReglSoldeTech, VarAlm.cdMethodeTxCible, 
                VarAlm.txCibleFixe,
                VarAlm.cdMethodePfiCleRepart, VarAlm.txIs
            ]
        )
        
        self.mdHypStratAlmTxServi : DfMd = DfMd(
            pks=[*DfMdCommun().mdPksCanton], 
            columns=[
                VarAlm.cdMethodeTxCible, VarAlm.txCibleFixe
            ]
        )

        self.mdHypStratAlmCr : DfMd = DfMd(
            pks=[*DfMdCommun().mdPksCanton], 
            columns=[
                VarAlm.txPbMinReglSoldeTech, VarAlm.txPbMinReglSoldeFin,
                VarAlm.cdMethodePfiCleRepart,
                VarAlm.txIs
            ]
        )

        self.mdMpProvOther : DfMd = DfMd(
            pks=[*DfMdCommun().mdPksCanton], 
            columns=[
                VarAlm.cdTypeCanton, VarActif.mtPre, VarAlm.mtReserveCapi, VarAlm.mtCapitauxPropres
            ]
        )

        self.mdMpProvOtherInitS2 : DfMd = DfMd(
            pks=[VarS2.cdChocS2, *self.mdMpProvOther.pks], 
            columns=self.mdMpProvOther.columns
        )

        self.mdMpProvPpe : DfMd = DfMd(
            pks=[*DfMdCommun().mdPksCanton, VarAlm.nbPpeGeneration], 
            columns=[
                VarAlm.mtPpe
            ]
        )

        self.mdMpProvPpeInitS2 : DfMd = DfMd(
            pks=[VarS2.cdChocS2, *self.mdMpProvPpe.pks], 
            columns=self.mdMpProvPpe.columns
        )

        self.mdProjProvPpe : DfMd = DfMd(
            pks=[VarS2.cdChocS2, *DfMdProj().mdPksScPerEv, *DfMdCommun().mdPksCanton, VarAlm.nbPpeGeneration], 
            columns=[
                VarAlm.mtPpeAv, VarAlm.mtPpe, VarAlm.nbPpeGenerationMax
            ]
        )

        self.mdProjProvOther : DfMd = DfMd(
            pks=[VarS2.cdChocS2, *DfMdProj().mdPksScPerEv, *DfMdCommun().mdPksCanton], 
            columns=[
                VarAlm.cdTypeCanton,
                VarAlm.mtReserveCapiAv, VarAlm.mtReserveCapi,
                VarActif.mtPreAv, VarActif.mtPre,
                VarAlm.mtCapitauxPropresAv, VarAlm.mtCapitauxPropres
            ]
        )

        self.mdPrdAdBilan : DfMd = DfMd(
            pks=[VarS2.cdChocS2, *DfMdProj().mdPksScPerEv, *DfMdCommun().mdPksCanton], 
            columns=[
                VarAlm.mtCapitauxPropres, VarPassif.mtPm, VarAlm.mtPpe,
                VarActif.mtVc, VarActif.mtPdd,
                VarAlm.mtReserveCapi, VarActif.mtPre,
                VarAlm.mtFuiteVc
            ]
        )
        
        self.mdPrdAdBilanErreurs : DfMd = DfMd(
            pks=[*DfMdCommun().mdPksErreurs, *self.mdPrdAdBilan.pks], 
            columns=self.mdPrdAdBilan.columns
        )

        ######################################
        ### DataFrames associés à la stratégie ALM
        self.mdAlmCrInputPassif  : DfMd = DfMd(
            pks=[VarS2.cdChocS2, *DfMdProj().mdPksScPer, *DfMdPassif().mdPksCntSupportEp], 
            columns=[
                VarPassif.txIc, VarPassif.txIcBrt, VarPassif.taf, VarPassif.tfgse, VarPassif.mtIcSort, VarPassif.mtIcRest, VarPassif.mtPbAss, VarPassif.mtPm
            ]
        )

        self.mdAlmCrInputTxCible : DfMd = DfMd(
            pks=[VarS2.cdChocS2, *DfMdProj().mdPksScPer, *DfMdCommun().mdPksCanton, VarAlm.stratAlmCas], 
            columns=[
                VarAlm.txServiBrt, VarAlm.stratAlmCasPriorite
            ]
        )

        self.mdAlmCrInputTxIcBrt : DfMd = DfMd(
            pks=[VarS2.cdChocS2, *DfMdProj().mdPksScPer, *DfMdCommun().mdPksCanton, VarPassif.txIcBrt], 
            columns=[VarAlm.pentePbBrt, VarAlm.pentePfi]
        )

        self.mdAlmCrInputActif : DfMd = DfMd(
            pks=[VarS2.cdChocS2, *DfMdProj().mdPksScPer, *DfMdCommun().mdPksCanton], 
            columns=[
                VarAlm.mtPfiInit, VarActif.mtPmvl,
                VarAlm.txPfiAsseRepartPc, VarFgx.mtFgxPlct, 
            ]
        )

        self.mdAlmCrAlmOutput : DfMd = DfMd(
            pks=[VarS2.cdChocS2, *DfMdProj().mdPksScPer, *DfMdCommun().mdPksCanton, VarAlm.stratAlmCas], 
            columns=[
                VarAlm.stratAlmCasPriorite,
                VarActif.mtPfi, VarAlm.txPfiAsseRepartPc, 
                VarAlm.mtPfiAssr, VarAlm.mtPfiAsse, VarAlm.mtPfiAssePb, 
                VarFgx.mtFgxPlct, VarPassif.mtFgseEu,
                VarAlm.mtPbBrtMinRegl,
                VarPassif.mtIcSort, VarPassif.mtIcRest, # VarPassif.mtPbAss,
                VarAlm.txServiBrt, VarPassif.mtPbBrt, VarActif.mtPmvr, VarAlm.mtPpeReprise, VarAlm.mtPpeDotation,
                VarAlm.mtResBrtAsse,
                VarAlm.mtResBrt
            ]
        )

        self.mdPrdAdAlmCr : DfMd = DfMd(
            pks=[VarS2.cdChocS2, *DfMdProj().mdPksScPerEv, *DfMdCommun().mdPksCanton, VarAlm.stratAlmCas], 
            columns=[
                VarAlm.mtPfiAssr,
                VarAlm.mtPfiAsse,
                VarAlm.mtResBrtAsse,
                VarAlm.mtResBrt,
                VarFgx.mtFgxPlct
            ]
        )

dfMdAlmCr = DfMdAlmCr()

stratAlmCasOrdrePriorite = pl.DataFrame(
    data={
        VarAlm.stratAlmCas :            [StratAlmCas.TX_CIBLE, StratAlmCas.TX_CIBLE_DIV2, StratAlmCas.TMG],
        VarAlm.stratAlmCasPriorite :    [0, 1, 2]
    },
    schema=buildDfMd([VarAlm.stratAlmCas, VarAlm.stratAlmCasPriorite])
)

