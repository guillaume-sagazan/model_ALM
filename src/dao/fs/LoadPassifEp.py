import os
from typing import Tuple
from polars import DataFrame
from config.TrtConfig import TrtConfig 
import polars as pl

from dao.Dao import getDao
from metadata.dfmd.DfMdPassifEp import dfMdPassifEp


def loadFsMpPassifEp() -> DataFrame :
    return getDao().readData(tableName='mp_passif_ep', plSchema=dfMdPassifEp.mdMpPassifEp.plSchemaWithCdTable)

def loadFsHypPassifEp() -> Tuple[DataFrame, DataFrame,DataFrame, DataFrame] : 
    hypPassifEpFgx = getDao().readData(tableName='hyp_passif_ep_fgx', plSchema=dfMdPassifEp.mdHypPassifEpFgx.plSchemaWithCdTable)
    hypPassifEpPrstRt = getDao().readData(tableName='hyp_passif_ep_prst_rt', plSchema=dfMdPassifEp.mdHypPassifEpPrstRt.plSchemaWithCdTable)
    hypMortGen = getDao().readData(tableName='hyp_mort_gen', plSchema=dfMdPassifEp.mdHypMortGen.plSchemaWithCdTable)
    hypMort = getDao().readData(tableName='hyp_mort', plSchema=dfMdPassifEp.mdHypMort.plSchemaWithCdTable)

    return hypPassifEpFgx, hypPassifEpPrstRt,hypMortGen,hypMort
