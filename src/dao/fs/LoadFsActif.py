import os
from typing import Tuple
from polars import DataFrame
from config.TrtConfig import TrtConfig 
import polars as pl

from dao.Dao import getDao
from metadata.dfmd.DfMdActif import dfMdActif

def loadFsMpActifIndices() -> DataFrame :
    return getDao().readData(tableName='mp_actif_indices', plSchema=dfMdActif.mdMpActifIndices.plSchemaWithCdTable)

# def loadFsMpActifOblig() -> DataFrame : 
#     return readData(tableName='mp_actif_oblig', plSchema=dfMdActif.mdMpActifOblig.plSchemaWithCdTable)

def loadFsHypStratInv() -> Tuple[DataFrame, DataFrame, DataFrame] : 
    hypStratInv = getDao().readData(tableName='hyp_strat_inv', plSchema=dfMdActif.mdHypStratInvInput.plSchemaWithCdTable)
    
    hypStratInvTxAllocCible = hypStratInv.select(dfMdActif.mdHypStratInvTxAllocCible.allColumns)
    hypStratInvObligAchat = hypStratInv.select(dfMdActif.mdHypStratInvObligAchat.allColumns)
    hypStratInvFraisPlct = hypStratInv.select(dfMdActif.mdHypStratInvTxFraisPlct.allColumns)
    
    return hypStratInvTxAllocCible, hypStratInvObligAchat, hypStratInvFraisPlct
