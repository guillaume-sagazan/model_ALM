from dataclasses import dataclass, field
from enum import auto
from typing import OrderedDict
import polars as pl

from metadata.dd.DdCommun import VarCommun



class DfMdCommun:
    def __init__(self) :
        self.mdPksSociete = [VarCommun.cdSociete]
        self.mdPksCanton = [VarCommun.cdSociete, VarCommun.cdCanton]
        self.mdPksErreurs = [VarCommun.typeErreur, VarCommun.erreur, VarCommun.typeErreurAction]

dfMdCommun = DfMdCommun()