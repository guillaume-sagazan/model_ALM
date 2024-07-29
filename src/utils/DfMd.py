
from enum import auto
import polars as pl
from dataclasses import dataclass, field
from typing import OrderedDict

from utils.VarCatalogGbl import VarCatalogGbl
from utils.StrEnumExt import StrEnumIso

def buildDfMd(ddColumnList : list[str], additionalColumns : dict[str, pl.DataType] = None) -> OrderedDict[str, pl.DataType] :
    dfMdColumns : dict[str, pl.DataType] = {var : VarCatalogGbl().ddElements[var].data_type for var in ddColumnList}
    if not additionalColumns is None : 
        dfMdColumns.update(additionalColumns)
    return OrderedDict[str, pl.DataType](dfMdColumns)

@dataclass
class DfMd:
    
    pks : list[str]
    columns : list[str]
    colCdTable : str = field(default='cd_table')
    plSchema : OrderedDict[str, pl.DataType] = field(init=False)
    allColumns : list[str] = field(init=False)
    
    pksWithCdTable : list[str] = field(init=False)
    plSchemaWithCdTable : OrderedDict[str, pl.DataType] = field(init=False)
    allColumnsWithCdTable : list[str] = field(init=False)

    def __post_init__(self):
        
        self.plSchema = buildDfMd([*self.pks, *self.columns])
        self.allColumns = [*self.pks, *self.columns]

        if not self.colCdTable is None : 
            self.plSchemaWithCdTable = buildDfMd([self.colCdTable, *self.pks, *self.columns])
            self.allColumnsWithCdTable = [self.colCdTable, *self.pks, *self.columns]
            self.pksWithCdTable = [self.colCdTable, *self.pks]
        else :
            self.plSchemaWithCdTable = buildDfMd([*self.pks, *self.columns])
            self.allColumnsWithCdTable = [*self.pks, *self.columns]
            self.pksWithCdTable = [*self.pks]