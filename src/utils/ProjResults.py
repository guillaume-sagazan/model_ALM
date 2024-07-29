import polars as pl
from polars import DataFrame
from dataclasses import dataclass, field

@dataclass
class ProjResults():
    results : dict[str, list[DataFrame]] = field(init=False)
    
    def __post_init__(self):
        self.results = {}
    
    def append(self, tableName : str, df : DataFrame, condition : bool = True):
        if condition:
            if tableName not in self.results:
                self.results[tableName] = []
            self.results[tableName].append(df)

    def reset(self, outputName : str):
        if outputName == '*':
            self.results = {}
        if outputName in self.results:
            self.results[outputName] = []
