from metadata.dd.DdActif import VarActif
from metadata.dd.DdAlm import VarAlm
from metadata.dd.DdCommun import VarCommun
from metadata.dd.DdProjection import VarProj
from metadata.dd.DdS2 import VarS2

from metadata.dd.DdStratInv import VarStratInv
from metadata.dfmd.DfMdS2 import dfMdS2
from metadata.dfmd.DfMdCommun import dfMdCommun
from metadata.dfmd.DfMdProj import dfMdProj
from utils.DfMd import DfMd


class DfMdActif:
    def __init__(self) :
        
        self.mdPksCdClasseActifDetail  : list[str] = [VarActif.cdClasseActif, VarActif.cdClasseActifDetail]
        self.mdPksActifUnitaire : list[str] = [*dfMdCommun.mdPksCanton, *self.mdPksCdClasseActifDetail, VarActif.cdIsin]
        self.mdPksActifUnitaireFwdCf : list[str] = [*self.mdPksActifUnitaire, VarActif.maturite, VarProj.intraperiod]

        self.mdPksCdChocS2ActifUnitaire : list[str] = [*dfMdS2.mdPksChocS2Actif, *self.mdPksActifUnitaire]

        self.mdPksMpActif : list[str] = [*dfMdProj.mdPksTrajectoire, *self.mdPksActifUnitaire]
        self.mdPksMpActifErreurs : list[str] = [*dfMdCommun.mdPksErreurs, *self.mdPksMpActif]
        self.mdPksProjActifCalcVm :list[str] = [*dfMdS2.mdPksChocS2Actif, *dfMdProj.mdPksScPer, *self.mdPksActifUnitaire]

        # self.mdMpActifOblig : DfMd = DfMd(
        #     pks=[*self.mdPksMpActif], 
        #     columns=[
        #         VarCommun.dtDateTerme,
        #         VarActif.mtNominal,
        #         VarActif.mtVm,
        #         VarActif.nbDuration,
        #         VarActif.txCpn,
        #         VarActif.txRemboursement,
        #         VarActif.mtVc,
        #         VarActif.cdCqs
        #     ]
        # )

        # self.mdMpActifObligInitGbl : DfMd = DfMd(
        #     pks=self.mdMpActifOblig.pks, 
        #     columns=[*self.mdMpActifOblig.columns, VarCommun.dtDateTermeAnnee, VarActif.nbPeriodTerme]
        # )

        # self.mdMpActifObligInitS2 : DfMd = DfMd(
        #     pks=[*dfMdS2.mdPksChocS2Actif, *self.mdMpActifObligInitGbl.pks], 
        #     columns=[*self.mdMpActifObligInitGbl.columns, VarActif.txVmRn, VarActif.mtVmRn, VarActif.txTra, VarActif.mtVcTra, VarActif.mtVcTraError]
        # )

        # self.mdProjActifObligMp : DfMd = DfMd(
        #     pks=[*dfMdS2.mdPksChocS2Actif, *dfMdProj.mdPksScPer, *self.mdPksActifUnitaire], 
        #     columns=self.mdMpActifObligInitS2.columns
        # )
                
        # self.mdMpActifObligErreurs : DfMd = DfMd(
        #     pks=self.mdPksMpActifErreurs, 
        #     columns=[
        #         *self.mdMpActifOblig.columns,
        #         VarActif.txTraMin, VarActif.mtVcTraMin, VarActif.txTraMax, VarActif.mtVcTraMax
        #     ]
        # )

        self.mdMpActifIndices : DfMd = DfMd(
            pks=[*self.mdPksMpActif], 
            columns=[
                VarActif.mtVm,
                VarActif.mtVc,
                VarActif.txActionT1,
                VarActif.txActionT2,
                VarActif.txActionStrat,
                VarActif.mtPdd,
            ]
        )

        self.mdMpActifIndicesInitGbl : DfMd = DfMd(
            pks=self.mdMpActifIndices.pks, 
            columns=[ *self.mdMpActifIndices.columns, VarActif.mtPmvl ]
        )

        self.mdMpActifIndicesInitS2 : DfMd = DfMd(
            pks=[*dfMdS2.mdPksChocS2Actif, *self.mdMpActifIndicesInitGbl.pks], 
            columns=self.mdMpActifIndices.columns
        )

        self.mdMpActifIndicesProj : DfMd = DfMd(
            pks=[*dfMdProj.mdPksScPerEv, *self.mdMpActifIndicesInitS2.pks], 
            columns=[
                *self.mdMpActifIndicesInitS2.columns,
                VarActif.mtVmAv, VarActif.mtVcAv,
                VarActif.mtPfi, VarActif.mtCf,
                VarAlm.mtFuiteEco, VarAlm.mtFuiteVc
            ]
        )

        # self.mdMpActifIndicesErreurs : DfMd = DfMd(
        #     pks=self.mdPksMpActifErreurs, 
        #     columns=self.mdMpActifIndices.columns
        # )

        # self.mdMpActifCashInitS2 : DfMd = DfMd(
        #     pks=[*dfMdS2.mdPksChocS2Actif, *self.mdPksActifUnitaire], 
        #     columns=[VarActif.mtVm, VarActif.mtVc]
        # )
        
        # self.mdMpActifCashErreurs : DfMd = DfMd(
        #     pks=self.mdPksMpActifErreurs, 
        #     columns=[VarActif.mtVm, VarActif.mtVc]
        # )

        # self.mdMpActifObligCfInitS2: DfMd = DfMd(
        #     pks=[*dfMdS2.mdPksChocS2Actif, *self.mdPksActifUnitaireFwdCf], 
        #     columns=[VarActif.mtCf]
        # )

        # self.mdProjActifObligCf: DfMd = DfMd(
        #     pks=[*dfMdS2.mdPksChocS2Actif, *dfMdProj.mdPksScPer, *self.mdPksActifUnitaireFwdCf], 
        #     columns=[VarActif.mtCf]
        # )

        # self.mdProjActif : DfMd = DfMd(
        #     pks=[
        #         *dfMdS2.mdPksChocS2Actif, *dfMdProj.mdPksScPerEv, *self.mdPksActifUnitaire,
        #         VarActif.nbPeriodTerme
        #     ], 
        #     columns=[
        #         VarActif.mtVmAv,
        #         VarActif.mtVm,
        #         VarActif.mtVcAv,
        #         VarActif.mtVc,
        #         VarActif.mtPmvl,
        #         VarActif.mtPfi,
        #         VarActif.mtCf,
        #         VarAlm.mtFuiteEco,
        #         VarAlm.mtFuiteVc,
        #         VarActif.mtPdd
        #     ]
        # )

        ######################################
        ### DataFrames associés aux Actifs : Stratégie d'investissement

        self.mdStratInvInputOutput : DfMd = DfMd(
            pks=[*dfMdS2.mdPksChocS2Actif, *dfMdProj.mdPksScPer,*dfMdCommun.mdPksCanton, VarActif.cdClasseActif], 
            columns=[    
                VarActif.mtVmAv, VarStratInv.mtVmAvCanton, VarStratInv.txAllocCible, 
                VarStratInv.mtVmAvCdClasseActif, VarStratInv.mtVmCibleCdClasseActif, VarStratInv.mtAchatOblig, VarStratInv.facteurAchatVente
            ]
        )

        ######################################
        ### DataFrames associés aux Actifs : Stratégie d'investissement
        self.mdHypStratInvInput : DfMd = DfMd(
            pks=[*dfMdCommun.mdPksCanton, VarActif.cdClasseActif], 
            columns=[
                VarStratInv.txAllocCible, VarStratInv.txObligAchatCpn, 
                VarStratInv.nbObligAchatMaturite, VarStratInv.txFraisPlct
            ]
        )

        self.mdHypStratInvTxAllocCible : DfMd = DfMd(
            pks=[*dfMdCommun.mdPksCanton, VarActif.cdClasseActif], 
            columns=[
                VarStratInv.txAllocCible
            ]
        )

        self.mdHypStratInvObligAchat : DfMd = DfMd(
            pks=[*dfMdCommun.mdPksCanton, VarActif.cdClasseActif], 
            columns=[
                VarStratInv.txObligAchatCpn, VarStratInv.nbObligAchatMaturite
            ]
        )

        self.mdHypStratInvTxFraisPlct : DfMd = DfMd(
            pks=[*dfMdCommun.mdPksCanton, VarActif.cdClasseActif], 
            columns=[
                VarStratInv.txFraisPlct
            ]
        )

        ######################################
        ### DataFrames associés aux Actifs : Performance  
        # pkName='ChocS2|Scenario|Iteration|Canton|FamPdt|TypeFlux|Intraperiod',
        self.mdMpActifCashInputCf : DfMd = DfMd(
            pks=[
                *dfMdS2.mdPksChocS2Actif, *dfMdProj.mdPksScPerIntra,
                *dfMdCommun.mdPksCanton, VarS2.cdTypeFlux
            ], 
            columns=[
                VarActif.mtCf,
            ]
        )

        self.mdPrdAdActif : DfMd = DfMd(
            pks=[VarS2.cdChocS2, *dfMdProj.mdPksScPerEv, *dfMdCommun.mdPksCanton, VarActif.cdClasseActif], 
            columns=[
                VarActif.mtVmAv, VarActif.mtVm, 
                VarActif.mtVcAv, VarActif.mtVc, 
                VarActif.mtPmvl, VarActif.mtPfi, 
                VarActif.mtCf, VarActif.mtPdd, 
                VarAlm.mtFuiteEco, VarAlm.mtFuiteVc
            ]
        )

dfMdActif = DfMdActif()