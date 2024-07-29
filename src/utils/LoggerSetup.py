import logging
import os
from dao.Dao import Dao

def setup_logger(loggingHandler, level):

    if not logging.getLogger('').hasHandlers():
        logger = logging.getLogger('')
        logger.setLevel(level)
        
        sh = logging.StreamHandler()
        logger.addHandler(sh)
       
        loggingHandler.setLevel(level)
        logger.addHandler(loggingHandler)

        formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
        for h in logger.handlers:
            h.setFormatter(formatter)
