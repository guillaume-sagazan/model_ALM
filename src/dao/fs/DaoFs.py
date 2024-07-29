from dataclasses import dataclass, field
import logging
import os
from typing import OrderedDict
import polars as pl
from polars import DataFrame
from config.TrtConfig import TrtConfig
from dao.Dao import Dao

@dataclass(kw_only=True)
class DaoFs(Dao):

    trtCfg : TrtConfig
    fdBase : str = field(init=False)
    fdTrt : str = field(init=False)
    fdInputs : str = field(init=False)
    fdLogs : str = field(init=False)
    fdOutputs : str = field(init=False)

    def __post_init__(self):
        self.fdBase = os.path.join(os.getcwd(),"data")
        self.fdTrt = os.path.join(self.fdBase, self.trtCfg.trtName)
        self.fdInputs = os.path.join(self.fdTrt,"inputs")
        self.fdLogs = os.path.join(self.fdTrt,"logs")
        self.fdOutputs = os.path.join(self.fdTrt,"outputs")
        
        if not os.path.exists(self.fdLogs):
            os.makedirs(self.fdLogs)
        for f in os.listdir(self.fdLogs):
            os.remove(os.path.join(self.fdLogs, f))

        if not os.path.exists(self.fdOutputs):
            os.makedirs(self.fdOutputs)
        for f in os.listdir(self.fdOutputs):
            os.remove(os.path.join(self.fdOutputs, f))


    def readData(self, tableName : str, plSchema : OrderedDict[str, pl.DataType] = None) -> DataFrame:
        
        df = pl.read_csv(os.path.join(self.fdInputs, tableName + ".csv"))
        if not plSchema is None:
            for var in plSchema.keys():
                if not var in df.columns:
                    logging.error("Variable " + var + " not found in " + tableName)
                    return None
                else : 
                    df = df.with_columns(pl.col(var).cast(plSchema[var]))

        return df
    
    def writeOutputFile(self, fName:str, fContent:str) :
        """Méthode permettant d'écrire un fichier depuis les paramètres passés

        :param fdPath: Chemin vers le répertoire
        :type fdPath: str
        :param fName: Nom du fichier
        :type fName: str
        :param fContent: Contenu du fichier à écrire
        :type fContent: str
        :returns: None
        :rtype: None
        """
        f = open(os.path.join(self.fdOutputs, fName), 'w')
        f.write(fContent)
        f.close()

    def writeLogFile(self, fName:str, fContent:str) :
        """Méthode permettant d'écrire un fichier depuis les paramètres passés

        :param fdPath: Chemin vers le répertoire
        :type fdPath: str
        :param fName: Nom du fichier
        :type fName: str
        :param fContent: Contenu du fichier à écrire
        :type fContent: str
        :returns: None
        :rtype: None
        """
        f = open(os.path.join(self.fdLogs, fName), 'w')
        f.write(fContent)
        f.close()

    def writeData(self, tableName : str, df : DataFrame, plSchema = None, condition : bool = True):
        """Méthode permettant d'écrire un dataframe dans un répertoire donné, selon un nom de fichier donné
        :param df: Dataframe écrit
        :type df: DataFrame
        :param fdPath: Chemin du répertoire cible
        :type fdPath: str
        :param fileName: Nom du fichier à utiliser
        :type fileName: str
        :returns: None
        :rtype: None
        """
        path = os.path.join(self.fdOutputs, tableName + ".csv")
        try:
            df.write_csv(path, separator=',')
        except:
            logging.error("Could not write " + path)

    def getLoggingHandler(self):
        log_file_name = "logs.log"
        log_file_mode = 'w'
        log_file = os.path.join(self.fdLogs, log_file_name)
        ch = logging.FileHandler(log_file, mode=log_file_mode)
        ch.setLevel(logging.INFO)
        return ch