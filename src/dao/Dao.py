from dataclasses import dataclass
import polars as pl
from typing import OrderedDict
from polars import DataFrame


@dataclass(kw_only=True)
class Dao:
    def readData(self, tableName : str, plSchema : OrderedDict[str, pl.DataType] = None) -> DataFrame:
        pass

    def writeOutputFile(self, fName:str, fContent:str) :
        pass
    
    def writeLogFile(self, fName:str, fContent:str) :
        pass

    def writeData(self, tableName : str, df : DataFrame, plSchema = None, condition : bool = True):
        pass

    def getLoggingHandler(self):
        pass

dao : Dao = None

def setDao(daoImpl : Dao) :
    global dao
    dao = daoImpl

def getDao() -> Dao :
    return dao