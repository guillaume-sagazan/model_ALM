import os
from polars import DataFrame
from config.TrtConfig import TrtConfig 
import polars as pl

from dao.Dao import getDao
from metadata.dfmd.DfMdS2 import dfMdS2

def loadFsHypS2Chocs() -> DataFrame : 
    return getDao().readData(tableName='hyp_s2_chocs', plSchema=dfMdS2.mdHypS2Chocs.plSchemaWithCdTable)

def loadFsHypS2ChocsSpread() -> DataFrame : 
    return getDao().readData(tableName='hyp_s2_chocs_spread', plSchema=dfMdS2.mdHypS2ChocsSpread.plSchemaWithCdTable)

