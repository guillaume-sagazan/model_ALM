import os
from polars import DataFrame
from config.TrtConfig import TrtConfig 
import polars as pl

from dao.Dao import getDao
from metadata.dfmd.DfMdGse import dfMdGse

def loadFsGseCtRef() -> DataFrame :
    return getDao().readData(tableName='gse_ct_ref', plSchema=dfMdGse.mdGseCtRefInput.plSchemaWithCdTable)


def loadFsGseOutputIndices() -> DataFrame : 
    return getDao().readData(tableName='gse_output_indices', plSchema=dfMdGse.mdGseOutputIndicesInput.plSchemaWithCdTable)

def loadFsGseOutputOblig() -> DataFrame :
    return getDao().readData(tableName='gse_output_oblig', plSchema=dfMdGse.mdGseOutputObligInput.plSchemaWithCdTable)

def loadFsGseOutputInflation() -> DataFrame : 
    return getDao().readData(tableName='gse_output_inflation', plSchema=dfMdGse.mdGseOutputInflationInput.plSchemaWithCdTable)
