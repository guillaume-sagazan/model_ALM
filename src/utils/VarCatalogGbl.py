from dataclasses import dataclass

from metadata.dd.DdActif import ddActif
from metadata.dd.DdAlm import ddAlm
from metadata.dd.DdCommun import ddCommun
from metadata.dd.DdGse import ddGse
from metadata.dd.DdProjection import ddProj
from metadata.dd.DdS2 import ddS2
from metadata.dd.DdIfrs17 import ddIfrs17
from metadata.dd.DdStratInv import ddStratInv
from metadata.dd.DdFgx import ddFgx
from metadata.dd.DdPassifEp import ddPassifEp

from utils.VarCatalog import VarCatalog


@dataclass(kw_only=True)
class VarCatalogGbl(VarCatalog):
    def __post_init__(self):
        self.ddElements = {}
        self.ddElements.update(ddPassifEp.ddElements)
        self.ddElements.update(ddActif.ddElements)
        self.ddElements.update(ddAlm.ddElements)
        self.ddElements.update(ddCommun.ddElements)
        self.ddElements.update(ddFgx.ddElements)
        self.ddElements.update(ddGse.ddElements)
        self.ddElements.update(ddProj.ddElements)
        self.ddElements.update(ddS2.ddElements)
        self.ddElements.update(ddIfrs17.ddElements)
        self.ddElements.update(ddStratInv.ddElements)


        