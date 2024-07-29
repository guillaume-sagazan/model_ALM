import os
import logging
import sys
import dataclasses_json
from datetime import date, datetime
import polars as pl

dataclasses_json.cfg.global_config.encoders[date] = date.isoformat
dataclasses_json.cfg.global_config.decoders[date] = date.fromisoformat
dataclasses_json.cfg.global_config.encoders[datetime] = datetime.isoformat
dataclasses_json.cfg.global_config.decoders[datetime] = datetime.fromisoformat

pl.enable_string_cache()

from orchestrateur.Orchestrateur import lancerTrtCfg

# from dao.configuration.DaoConfig import DaoConfig, DaoStrategy
# from dao.daoConnexion.DaoConnexionManager import DaoConnexionManager
from datetime import datetime, date

from utils.LoggerSetup import setup_logger
from config.TrtConfig import TrtConfig
from metadata.dfmd.DfMdActif import dfMdActif
from metadata.dfmd.DfMdGse import DfMdGse
from metadata.dfmd.DfMdS2 import dfMdS2
from utils.collection import isStrInListFullMatch



if __name__ == "__main__":
    
    wDir = os.path.join(os.getcwd(), 'data')

    trtFiltre = sys.argv[1]
    trtFiltre = trtFiltre.split(',')

    for root, dirs, files in os.walk(wDir):
        for trtName in dirs:
            trtCfgJsonFilePath = os.path.join(wDir, trtName, "trtCfg.json")
            if isStrInListFullMatch(trtName, trtFiltre) and os.path.isfile(trtCfgJsonFilePath):

                with open(trtCfgJsonFilePath, "r") as fTrtCfg:
                    trtCfg: TrtConfig = TrtConfig.from_json(fTrtCfg.read())
                    trtCfg.trtName = trtName

                lancerTrtCfg(trtCfg)