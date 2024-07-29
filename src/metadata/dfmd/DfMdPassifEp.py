from metadata.dd.DdActif import VarActif
from metadata.dd.DdAlm import VarAlm
from metadata.dd.DdCommun import VarCommun
from metadata.dd.DdFgx import VarFgx
from metadata.dd.DdGse import VarGse
from metadata.dd.DdPassifEp import VarPassif
from metadata.dd.DdProjection import VarProj
from metadata.dd.DdS2 import VarS2
from metadata.dd.DdIfrs17 import VarIfrs17
from metadata.dfmd.DfMdS2 import dfMdS2
from metadata.dfmd.DfMdCommun import dfMdCommun
from metadata.dfmd.DfMdProj import dfMdProj
from utils.DfMd import DfMd
from utils.collection import listUnion

class DfMdPassifEp:
    def __init__(self) :

        self.mdPksMpPassifEp : list[str] = [*dfMdCommun.mdPksCanton, VarIfrs17.cdPrtfIfrs17, VarPassif.cdFampdt, VarPassif.cdCnt]

        #######################
        ### Données au chargement
        self.mdHypPassifEpFgx : DfMd = DfMd(
            pks=[VarCommun.cdSociete, VarPassif.cdFampdt], 
            columns=[
                VarFgx.txFgxPmEu, VarFgx.txFgxPrstEu, VarFgx.txFgxPlctEu, VarFgx.txFgxPmUc, VarFgx.txFgxPrstUc, VarFgx.txFgxPlctUc
            ]
        )

        self.mdHypPassifEpPrstRt : DfMd = DfMd(
            pks=[VarPassif.nbCntAncienneteAnnee, VarPassif.cdPrstRtCat], 
            columns=[
                VarPassif.txPrstRt
            ]
        )

        self.mdHypMort : DfMd = DfMd(
            pks=[ VarPassif.sexe, VarPassif.age], 
            columns=[
                VarPassif.qx
            ]
        )

        self.mdHypMortGen : DfMd = DfMd(
            pks=[ VarPassif.generation, VarPassif.sexe, VarPassif.age], 
            columns=[
                VarPassif.qx
            ]
        )

        self.mdMpPassifEp : DfMd = DfMd(
            pks=[*dfMdProj.mdPksTrajectoire, *self.mdPksMpPassifEp], 
            columns=[
                VarPassif.nbCnt,
                VarPassif.cdAsseSexe,
                VarPassif.dtAsseNaiss,
                VarPassif.dtCntEffet,
                VarPassif.mtPmEu,
                VarPassif.cdHrgEu,
                VarPassif.mtPmUc,
                VarPassif.cdHrgUc,
                VarPassif.cdPrstRtCat,
                VarPassif.cdCapitalisation,
                VarPassif.tmg,
                VarPassif.tmgType,
                VarPassif.taf,
                VarPassif.tfgse,
                VarPassif.tfgseUc,
                VarPassif.cdHypMortExp,
                VarPassif.cdHypMortProv,
                VarPassif.txPrstChgt,
                VarActif.txActionT1, 
                VarActif.txActionT2, 
                VarActif.txActionStrat, 
                VarActif.txImmobilier
            ]
        )

        self.mdMpPassifEpInitGbl : DfMd = DfMd(
            pks=self.mdMpPassifEp.pks, 
            columns=[*self.mdMpPassifEp.columns, 
                     VarPassif.nbAsseAgeAnnee,
                     VarPassif.nbAsseAgeMois,
                     VarPassif.nbCntAncienneteAnnee,
                     VarPassif.nbCntAncienneteMois,
                     VarPassif.tmgBrt,
                     VarPassif.generation
            ]
        )

        self.mdMpPassifEpInitS2 : DfMd = DfMd(
            pks=[*dfMdS2.mdPksChocS2PassifMp, *self.mdMpPassifEpInitGbl.pks],
            columns=self.mdMpPassifEpInitGbl.columns
        )

        self.mdMpPassifEpErreurs : DfMd = DfMd(
            pks=[*dfMdCommun.mdPksErreurs, *self.mdMpPassifEpInitGbl.pks], 
            columns=self.mdMpPassifEpInitGbl.columns
        )

        ######################################
        ### Données par itération
        self.mdMpPassifEpProj : DfMd = DfMd(
            pks=[*dfMdS2.mdPksChocS2PassifMp, *dfMdProj.mdPksScPerEv, *self.mdPksMpPassifEp], 
            columns=[
                *self.mdMpPassifEpInitS2.columns, 
                VarPassif.mtPmEuAv,
                VarPassif.mtPmUcAv,
                VarPassif.nbCntAv
            ]
        )

        self.mdMpPassifEpProjHypsPrst : DfMd = DfMd(
                pks=[VarS2.cdChocS2PassifPrst, VarProj.period, *self.mdPksMpPassifEp], 
                columns=[
                    VarPassif.txPrstRt,
                    VarPassif.txPrstDcAsseExp,
                    VarPassif.txPrstChgt
                ]
            )

        self.mdMpPassifEpProjHypsIcFgx : DfMd = DfMd(
            pks=[VarS2.cdChocS2PassifIcFgx, *dfMdProj.mdPksScPer, *self.mdPksMpPassifEp], 
            columns=[
                VarFgx.txFgxPrstEu, 
                VarFgx.txFgxPmEu,
                VarFgx.txFgxPrstUc, 
                VarFgx.txFgxPmUc,
                VarPassif.txIcEu, 
                VarPassif.txIcEuBrt, 
                VarPassif.txIcUc,
                VarPassif.txIcEuDemiPeriode, 
                VarPassif.txIcEuBrtDemiPeriode, 
                VarPassif.txIcUcDemiPeriode,
                VarPassif.taf, 
                VarPassif.tfgse, 
                VarGse.facteurInflationCum
            ]
        )

        self.mdMpPassifEpProjPerf : DfMd = DfMd(
            pks=self.mdMpPassifEpProj.pks, 
            columns=[
                *self.mdMpPassifEpProj.columns,
                VarPassif.mtPrstTotEuBrt, 
                VarPassif.mtPrstTotEuNet, 
                VarPassif.mtPrstTotEuChgt,
                VarPassif.mtPrstDcEuBrt, 
                VarPassif.mtPrstDcEuNet, 
                VarPassif.mtPrstDcEuChgt,
                VarPassif.mtPrstRtEuBrt, 
                VarPassif.mtPrstRtEuNet, 
                VarPassif.mtPrstRtEuChgt,
                
                VarPassif.mtPrstTotUcBrt, 
                VarPassif.mtPrstTotUcNet, 
                VarPassif.mtPrstTotUcChgt,
                VarPassif.mtPrstDcUcBrt, 
                VarPassif.mtPrstDcUcNet, 
                VarPassif.mtPrstDcUcChgt,
                VarPassif.mtPrstRtUcBrt, 
                VarPassif.mtPrstRtUcNet, 
                VarPassif.mtPrstRtUcChgt,
                
                VarPassif.mtIcEuRest, 
                VarPassif.mtIcEuSort, 
                VarPassif.mtIcUcRest, 
                VarPassif.mtIcUcSort, 
                
                VarPassif.mtFgseUc,
                VarPassif.mtFgseEu,
                
                VarFgx.mtFgxPrstEu, 
                VarFgx.mtFgxPmEu,
                VarFgx.mtFgxPrstUc, 
                VarFgx.mtFgxPmUc,
            ]
        )
            
        self.mdMpPassifEpProjAlmCr : DfMd = DfMd(
            pks=self.mdMpPassifEpProj.pks, 
            columns=[
                *self.mdMpPassifEpProj.columns,
                VarPassif.mtPbBrt, 
                VarPassif.mtPbNet, 
                VarPassif.mtCsg
            ]
        )

        self.mdAlmCrAlmOutputPassif : DfMd = DfMd(
            pks=[VarS2.cdChocS2, *dfMdProj.mdPksScPer, *self.mdPksMpPassifEp, VarAlm.stratAlmCas], 
            columns=[
                VarAlm.txServiBrt, VarAlm.txServiNet,
                VarPassif.mtPbAss, VarPassif.mtPbBrt, VarPassif.mtCsg, VarPassif.mtPbNet
            ]
        )

        self.mdPrdAdPassifEp : DfMd = DfMd(
            pks=[VarS2.cdChocS2, *dfMdProj.mdPksScPerEv, *dfMdCommun.mdPksCanton, VarPassif.cdFampdt], 
            columns=listUnion([
                self.mdMpPassifEpProj.columns,
                self.mdMpPassifEpProjPerf.columns,
                self.mdMpPassifEpProjAlmCr.columns,
            ])
        )

dfMdPassifEp = DfMdPassifEp()