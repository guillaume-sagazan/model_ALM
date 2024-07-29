from dataclasses import dataclass, field
import os
from dataclasses_json import dataclass_json

from config.ErrConfig import ErrConfig
from config.OutputConfig import OutputConfig
from config.ProjConfig import ProjConfig

@dataclass_json
@dataclass
class TrtConfig:

    """Classe stockant la configuration d'un traitement du modèle ALM
    
    :param trtCode: Code associé au traitement
    :type trtCode: int
    :param trtName: Nom du traitement
    :type trtName: str
    :param errCfg: ProjConfig associée à la gestion des erreurs
    :type errCfg: ErrConfig
    :param projCfg: ProjConfig associée à la projection
    :type projCfg: ProjConfig
    :param outputCfg: ProjConfig associée aux outputs du traitement
    :type outputCfg: OutputConfig
    """
    trtName: str
    errCfg: ErrConfig
    projCfg: ProjConfig
    outputCfg : OutputConfig
    fdInputsPath : str = field(init=False)
    fdOutputPath : str = field(init=False)

    def __post_init__(self):
        self.fdInputsPath = f"{os.getcwd()}/data/{self.trtName}/inputs"
        self.fdOutputPath = f"{os.getcwd()}/data/{self.trtName}/outputs"
