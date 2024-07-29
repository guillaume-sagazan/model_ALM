from datetime import date, datetime
import logging
import os
from config.TrtConfig import TrtConfig
from config.ErrConfig import ErrConfig
from config.ProjConfig import ProjConfig
from config.OutputConfig import OutputConfig
from metadata.dd.DdAlm import CdMethodeInitEquilibreBilan
from metadata.dd.DdGse import ScUnivers
from metadata.dd.DdProjection import ModeProjection
from metadata.dd.DdS2 import CdChocS2

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s %(levelname)s %(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S")


def writeTrtConfig(trtCfg : TrtConfig):
    with open(os.path.join(os.getcwd(),'data',trtCfg.trtName,'trtCfg.json'), 'w') as file:
        # Écrire une chaîne de caractères dans le fichier
        file.write(trtCfg.to_json())

logging.info('Création des configurations de traitement')

errCfgDefault : ErrConfig = ErrConfig()
outputCfgAll : OutputConfig = OutputConfig()
outputCfgPrd : OutputConfig = OutputConfig(
    genererOutputDebug=False,
    genererOutputPrdAd=True,
    genererOutputPrdQrt=True,
    genererOutputRctInitActif=False,
    genererOutputRctInitPassif=False,
    genererOutputRctInitGse=False,
    genererOutputRctLoad=False,
    genererOutputRctProjActif=False,
    genererOutputRctProjAlmCr=False,
    genererOutputRctProjPassif=False,
    genererOutputRctProjProv=False,
    genererOutputRctProjStratInv=False
)

logging.info('Création de alm_detrn_central_2212')
projConfigAlmDetRnCentral : ProjConfig = ProjConfig(

    cdChocS2List=[CdChocS2.central],
    projModeProjection = ModeProjection.ALM,
    projHorizon = 40,
    projDateDebut = date.fromisoformat('2022-12-31'),
    methodeInitEquilibreBilan = CdMethodeInitEquilibreBilan.CASH,

    ### Paramétrage des scenarii économiques
    gseScCrnAutoBuild = True,
    gseScUnivers = ScUnivers.RN,
    gseScEcoListStr = '1',
    gseObligMaturiteMaxAutoDetect = True,
    gseObligMaturiteMax = 600

)
writeTrtConfig(TrtConfig(
    trtName='alm_detrn_central_2212',
    projCfg=projConfigAlmDetRnCentral,
    errCfg=errCfgDefault,
    outputCfg=outputCfgAll
))

logging.info('Création de alm_detrn_allchocs_2212')
projConfigAlmDetRnAllChocs : ProjConfig = ProjConfig(

    cdChocS2List=[ cdChocS2.value for cdChocS2 in CdChocS2],
    projModeProjection = ModeProjection.ALM,
    projHorizon = 40,
    projDateDebut = date.fromisoformat('2022-12-31'),
    methodeInitEquilibreBilan = CdMethodeInitEquilibreBilan.CASH,

    ### Paramétrage des scenarii économiques
    gseScCrnAutoBuild = True,
    gseScUnivers = ScUnivers.RN,
    gseScEcoListStr = '1',
    gseObligMaturiteMaxAutoDetect = True,
    gseObligMaturiteMax = 600

)

writeTrtConfig(TrtConfig(
    trtName='alm_detrn_allchocs_2212',
    projCfg=projConfigAlmDetRnAllChocs,
    errCfg=errCfgDefault,
    outputCfg=outputCfgPrd
))

