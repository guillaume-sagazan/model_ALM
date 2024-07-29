import io
import logging
import os
import polars as pl
import cProfile
import pstats

from config.TrtConfig import TrtConfig
from dao.Dao import dao
from dao.fs.LoadFsActif import loadFsHypStratInv, loadFsMpActifIndices
from dao.fs.LoadFsGse import loadFsGseCtRef, loadFsGseOutputIndices, loadFsGseOutputOblig, loadFsGseOutputInflation
from dao.fs.LoadFsS2 import loadFsHypS2Chocs, loadFsHypS2ChocsSpread
from dao.fs.LoadPassifEp import loadFsHypPassifEp, loadFsMpPassifEp
from dao.Dao import setDao, getDao
from dao.fs.DaoFs import DaoFs
from domaines.actifs.events.InitGblActif import initGblActif
from domaines.actifs.events.InitProjActif import initProjActif
from domaines.actifs.events.InitS2Actif import initS2Actif
from domaines.actifs.events.PerfActif import perfActif
from domaines.actifs.ops.PrdAdActifs import prdAdActifBuild
from domaines.gse.events.InitGblGse import initGblGse
from domaines.gse.events.InitS2Gse import initS2Gse
from domaines.passif.events.InitGblPassif import initGblPassif
from domaines.passif.events.InitS2Passif import initS2PassifEp
from domaines.passif.events.InitProjPassifEp import initProjPassifEp
from domaines.passif.events.PerfPassifEp import perfPassifEp
from domaines.passif.ops.PrdAdPassif import prdAdPassifBuild
from domaines.stratinv.events.StratInv import stratInv
from metadata.dd.DdProjection import ModeProjection, VarProj
from metadata.dd.DdPassifEp import ddPassifEp
from utils.LoggerSetup import setup_logger
from utils.ProjResults import ProjResults

def lancerTrtCfg(trtCfg : TrtConfig):

    with cProfile.Profile() as prInit:
        
        setDao(DaoFs(trtCfg=trtCfg))
        setup_logger(getDao().getLoggingHandler(), level=logging.INFO)
        projResults = ProjResults()

        logging.info(f'************************************************************************')
        logging.info(f'*** Lancement du traitement : {trtCfg.trtName}')
        logging.info(f'************************************************************************')

        projCfg = trtCfg.projCfg
        outputCfg = trtCfg.outputCfg
        errCfg = trtCfg.errCfg

        logging.info(f"Suppression des précédents outputs")
        logging.info(f"Mode de projection : {projCfg.projModeProjection.name}")
        logging.info(f"Horizon de projection : {projCfg.projHorizon}")
        logging.info(f"Liste des chocs s2 à jouer : {', '.join([el.__str__() for el in projCfg.cdChocS2List])}")
        logging.info(f"Liste des scenarios à jouer : {projCfg.gseScEcoListStr}")

        logging.info(f"Import des données - Gse")
        gseCtRefInput=loadFsGseCtRef()
        gseOutputIndicesInput=loadFsGseOutputIndices()
        gseOutputObligInput=loadFsGseOutputOblig()
        gseOutputInflationInput=loadFsGseOutputInflation()

        logging.info(f"Import des données - Actif")
        mpActifIndices = loadFsMpActifIndices()
        hypStratInvTxAllocCible, hypStratInvObligAchat, hypStratInvFraisPlct = loadFsHypStratInv()

        logging.info(f"Import des données - Passif")
        mpPassifEp = loadFsMpPassifEp()
        hypPassifEpFgx, hypPassifEpPrstRt,hypMortGen,hypMort = loadFsHypPassifEp()

        logging.info(f"Import des données - S2")
        hypS2Chocs = loadFsHypS2Chocs()
        hypS2ChocsSpread = loadFsHypS2ChocsSpread()
       

        logging.info(f"Initialisation : Global : Gse")
        gseCtRefObligPzc,gseCtRefCashPerf,gseOutputObligPzc,gseOutputIndicesPerf,gseOutputCashPerf,gseOutputDeflateur = initGblGse(
            dfCdChocS2 = projCfg.dfCdChocS2,
            gseObligMaturiteMax = projCfg.gseObligMaturiteMax,
            gseScEcoList = projCfg.gseScEcoList,
            gseScUnivers = projCfg.gseScUnivers,
            gseScCrnAutoBuild=projCfg.gseScCrnAutoBuild,
            projHorizon = projCfg.projHorizon,
            gseCtRef = gseCtRefInput,
            gseOutputIndicesInput = gseOutputIndicesInput,
            gseOutputInflationInput = gseOutputInflationInput,
            gseOutputObligInput = gseOutputObligInput,
        )

        getDao().writeData(tableName="gseCtRefObligPzc", df=gseCtRefObligPzc, condition=outputCfg.genererOutputRctInitGse)
        getDao().writeData(tableName="gseCtRefCashPerf", df=gseCtRefCashPerf, condition=outputCfg.genererOutputRctInitGse)
        getDao().writeData(tableName="gseOutputObligPzc", df=gseOutputObligPzc, condition=outputCfg.genererOutputRctInitGse)
        getDao().writeData(tableName="gseOutputIndicesPerf", df=gseOutputIndicesPerf, condition=outputCfg.genererOutputRctInitGse)
        getDao().writeData(tableName="gseOutputCashPerf", df=gseOutputCashPerf, condition=outputCfg.genererOutputRctInitGse)
        getDao().writeData(tableName="gseOutputDeflateur", df=gseOutputDeflateur, condition=outputCfg.genererOutputRctInitGse)

        gseCtRefObligPzcCentral, gseOutputInflationInitS2 = initS2Gse(dfCdChocS2=projCfg.dfCdChocS2,hypS2Chocs =hypS2Chocs, gseCtRefObligPzc=gseCtRefObligPzc, gseOutputInflationInput = gseOutputInflationInput)
        
        logging.info(f"Initialisation : Global : Passif")

        mpPassifEpInitGbl = initGblPassif(mpPassifEp = mpPassifEp, projDateDebut=projCfg.projDateDebut)
        getDao().writeData(df=mpPassifEpInitGbl, tableName="mpPassifEpInitGbl", condition=outputCfg.genererOutputRctInitPassif)

        logging.info(f"Initialisation : Global : Actif")
        mpActifIndicesInitGbl,mpActifIndicesInitGblErreurs = initGblActif(mpActifIndices)
        getDao().writeData(tableName="mpActifIndicesInitGbl", df=mpActifIndicesInitGbl, condition=outputCfg.genererOutputRctInitActif)
        getDao().writeData(tableName="mpActifIndicesInitGblErreurs", df=mpActifIndicesInitGblErreurs)

        logging.info(f"**********************************************************************************")
        logging.info(f"Initialisation Choc S2 : Ajout de l'axe cdChocS2 + Application des chocs en t=0")
        logging.info(f"**********************************************************************************")
        logging.info(f"Initialisation Choc S2 : Passif")

        mpPassifEpInitS2 = initS2PassifEp(mpPassifEpInitGbl=mpPassifEpInitGbl, hypS2Chocs = hypS2Chocs, dfCdChocS2=projCfg.dfCdChocS2)
        getDao().writeData(tableName="mpPassifEpInitS2", df=mpPassifEpInitS2, condition=outputCfg.genererOutputRctInitPassif)

        logging.info(f"Initialisation Choc S2 : Actifs")
        mpActifIndicesInitS2 = initS2Actif(mpActifIndicesInitGbl=mpActifIndicesInitGbl,
                                        dfCdChocS2=projCfg.dfCdChocS2,
                                        hypS2Chocs=hypS2Chocs)
        getDao().writeData(tableName="mpActifIndicesInitS2", df=mpActifIndicesInitS2, condition=outputCfg.genererOutputRctInitActif)

        logging.info(f"****************************")
        logging.info(f"Initialisation Projection")
        logging.info(f"****************************")
        logging.info(f"Initialisation Projection : Actifs")
        mpActifIndicesProj = initProjActif(mpActifIndicesInitS2=mpActifIndicesInitS2,
                                        scEcoList=projCfg.gseScEcoList)
        
        projResults.append(tableName="mpActifIndicesProj", df=mpActifIndicesProj, condition=outputCfg.genererOutputRctInitActif)
        prdAdActif = prdAdActifBuild(mpActifIndicesProj)
        projResults.append(tableName="prdAdActif", df=prdAdActif, condition=outputCfg.genererOutputPrdAd)
        

        logging.info(f"Initialisation Projection : Passifs ")
        mpPassifEpProj, mpPassifEpProjHypsPrst,mpPassifEpProjHypsIcFgx = initProjPassifEp(mpPassifEpInitS2=mpPassifEpInitS2,
                                                                                           scEcoList=projCfg.gseScEcoList,
                                                                                            projHorizonList=projCfg.projHorizonList, 
                                                                                            hypPassifEpFgx = hypPassifEpFgx ,
                                                                                            gseOutputInflationInitS2 = gseOutputInflationInitS2 , 
                                                                                            hypPassifEpPrstRt = hypPassifEpPrstRt,
                                                                                            hypMortGen = hypMortGen,
                                                                                            hypMort = hypMort, 
                                                                                            gseOutputIndicesPerfT = gseOutputIndicesPerf)
        getDao().writeData(df=mpPassifEpProj, tableName="mpPassifEpInitProj",condition=outputCfg.genererOutputRctInitPassif)


        projResults.append(tableName="mpPassifEpProj", df=mpPassifEpProj, condition=outputCfg.genererOutputRctInitPassif)
        prdAdPassifEp = prdAdPassifBuild(mpPassifEpProj)
        projResults.append(tableName="prdAdPassifEp", df=prdAdPassifEp, condition=outputCfg.genererOutputPrdAd)


    with cProfile.Profile() as prProj:

        logging.info(f"****************************")
        logging.info(f"Début de la projection")
        logging.info(f"****************************")
        for period in range(1, trtCfg.projCfg.projHorizon + 1):
            logging.info(f"Perf ({period})")
            logging.info(f"Perf Passif")
            mpPassifEpProjPerf, mpActifCashInputCfPerfPassif = perfPassifEp(mpPassifEpProj=mpPassifEpProj, 
                              mpPassifEpProjHypsIcFgxT=mpPassifEpProjHypsIcFgx,
                              mpPassifEpProjHypsPrstT=mpPassifEpProjHypsPrst,
                              period = period )
            
            projResults.append(tableName="mpPassifEpProj", df=mpPassifEpProjPerf, condition=outputCfg.genererOutputRctProjPassif)
            projResults.append(tableName="mpActifCashInputCf", df=mpActifCashInputCfPerfPassif, condition=outputCfg.genererOutputRctProjActif)
            prdAdPassifEp = prdAdPassifBuild(mpPassifEpProj)
            projResults.append(tableName="prdAdPassifEp", df=prdAdPassifEp, condition=outputCfg.genererOutputPrdAd)

            logging.info(f"Perf Actif")
            mpActifIndicesProj = perfActif(mpActifIndicesProj=mpActifIndicesProj,
                                        gseCtRefCashPerfT=gseCtRefCashPerf.filter(pl.col(VarProj.period)==period),
                                        gseOutputIndicesPerfT=gseOutputIndicesPerf.filter(pl.col(VarProj.period)==period),
                                        period=period)
            
            projResults.append(tableName="mpActifIndicesProj", df=mpActifIndicesProj, condition=outputCfg.genererOutputRctProjActif)
            prdAdActif = prdAdActifBuild(mpActifIndicesProj)
            projResults.append(tableName="prdAdActif", df=prdAdActif, condition=outputCfg.genererOutputPrdAd)
        

            logging.info(f'StratInv ({period})')
            stratInvInputOutput,mpActifIndicesProj = stratInv(
                period=period,
                dfCdChocS2Sc=projCfg.dfCdChocS2Sc,
                mpActifIndicesProj=mpActifIndicesProj,
                hypStratInvTxAllocCible=hypStratInvTxAllocCible
            )
            projResults.append(tableName="stratInvInputOutput", df=stratInvInputOutput, condition=outputCfg.genererOutputRctProjStratInv)
            projResults.append(tableName="mpActifIndicesProj", df=mpActifIndicesProj, condition=outputCfg.genererOutputRctProjActif)
            prdAdActif = prdAdActifBuild(mpActifIndicesProj)
            projResults.append(tableName="prdAdActif", df=prdAdActif, condition=outputCfg.genererOutputPrdAd)

            logging.info(f'Alm & Cr ({period}) : Algorithme de détermination du txServiBrt')
        
        if projCfg.projModeProjection == ModeProjection.ALM:
            logging.info(f'Construction des outputs Qrt')

            # ResultsWriter().projResults.projResultPrdQrt.buildOutputPrdQrtBeScPeriodTypeFluxCf()
            # ResultsWriter().writeOutputPrdQrtBeScPeriodTypeFluxCf()
            # ResultsWriter().projResults.projResultPrdQrt.outputPrdQrtBeScPeriodTypeFlux = prdQrtBeScPeriodTypeFluxBuild(
            #     dfCdChocS2=projCfg.dfCdChocS2,
            #     prdQrtBeScPeriodTypeFluxCf=ResultsWriter().projResults.projResultPrdQrt.outputPrdQrtBeScPeriodTypeFluxCf, 
            #     gseOutputDeflateur=gseOutputDeflateur)
            
            # ResultsWriter().projResults.projResultPrdQrt.outputPrdQrtBeSc = prdQrtBeScBuild(
            #     ResultsWriter().projResults.projResultPrdQrt.outputPrdQrtBeScPeriodTypeFlux)
            
            # ResultsWriter().projResults.projResultPrdQrt.outputPrdQrtBe = prdQrtBeBuild(
            #     ResultsWriter().projResults.projResultPrdQrt.outputPrdQrtBeSc)

            # ResultsWriter().writeOutputPrdQrt()

        logging.info(f'Ecriture des résultats')
        for outputName, dfList in projResults.results.items():
            dfList = [df for df in dfList if df is not None]
            if dfList != []:
                getDao().writeData(df=pl.concat(dfList, how='diagonal'), tableName=f"{outputName}", condition=True)
        
        logging.info(f"Logs des performances associées à l'initialistion !")
        prResultsInit = pstats.Stats(prInit)
        prResultsInit.sort_stats(pstats.SortKey.TIME)
        s = io.StringIO()
        prResultsInit.stream = s
        prResultsInit.print_stats()
        getDao().writeLogFile(fName="perf_initialisation.txt", fContent=s.getvalue())
        
        logging.info(f"Logs des performances associées à la projection !")
        prResultsProj = pstats.Stats(prProj)
        prResultsProj.sort_stats(pstats.SortKey.TIME)
        s = io.StringIO()
        prResultsProj.stream = s
        prResultsProj.print_stats()
        getDao().writeLogFile(fName="perf_projection.txt", fContent=s.getvalue())

        logging.info(f'Fin de la projection !')
        
        