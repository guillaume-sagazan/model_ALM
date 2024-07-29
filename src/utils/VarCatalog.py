from abc import ABC
from dataclasses import dataclass, field
from enum import StrEnum
import polars as pl

from dataclasses_json import dataclass_json

@dataclass(kw_only=True)
class DataTypeDesc:
    data_type : pl.DataType
    description : str
    valeursPossibles : list = field(default_factory=list)
    

@dataclass(kw_only=True)
class VarCatalog():

    ddElements:dict[str, DataTypeDesc] = field(init=False)

    def __post_init__(self):
        self.ddElements = {}

    def checkVarListNotRegistered(self, varlist : list[str]):
        return [var for var in varlist if not self.ddElements.__contains__(var)]
            
