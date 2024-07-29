from dataclasses import dataclass, field, fields
from dataclasses_json import dataclass_json, config

from datetime import date

import polars as pl
from polars import DataFrame

from metadata.dd.DdAlm import CdMethodeInitEquilibreBilan
from metadata.dd.DdGse import ScUnivers, VarGse
from metadata.dd.DdProjection import ModeProjection, VarProj
from metadata.dd.DdS2 import CdChocS2, VarS2
from metadata.dfmd.DfMdS2 import refCdChocS2
from utils.collection import convertStringToIntList


@dataclass_json
@dataclass
class ProjConfig :
    """Classe stockant la configuration d'une projection.
    :param cdChocS2List: Liste des chocs S2 à jouer. Valeur par défaut = [TypeChocS2.central])
    :type cdChocS2List: list[TypeChocS2]
    :param dfCdChocS2: DataFrame contenant les chocs S2. Initialisé dans la fonction __post_init__ à partir de chocS2List
    :type dfCdChocS2: DataFrame[]
    :param projModeProjection: Mode de projection pour la projection considérée. Valeur par défaut = ModeProjection.ACTIF_SEUL
    :type projModeProjection: ModeProjection
    :param projHorizon: Horizon de projection. Valeur par défaut = 10
    :type projHorizon: int
    :param projDateDebut: Date de début de la projection. Valeur par défaut = 2022-12-31
    :type projDateDebut: datetime
    :param projDateDebutAnnee: Année de début de projection. Initialisé dans la fonction __post_init__ à partir de projDateDebut
    :type projDateDebutAnnee: int
    :param projDtImage: Date Image. Initialisé dans la fonction __post_init__ à partir de projDateDebut
    :type projDtImage: str
    :param methodeInitEquilibreBilan: Méthode utilisée pour équilibrer le bilan à l'initialisation de la projection
    :type methodeInitEquilibreBilan: CdMethodeInitEquilibreBilan
    :param gseScCrnAutoBuild: Booléen décrivant si les variables économiques du scenario CRN sont calculées en mémoire par le programme ou si elles sont issues du fichier IGSE. Valeur par défaut = False
    :type gseScCrnAutoBuild: bool
    :param gseScUnivers: Univers de projection utilisé. Valeur par défaut = ScUnivers.RN
    :type gseScUnivers: ScUnivers
    :param gseScEcoListStr: Liste des scenarios économiques à projeter au format chaine de caractères. Valeur par défaut = '1'
    :type gseScEcoListStr: str
    :param gseScEcoList: Liste des scenarios économiques à projeter au format liste d'entiers. Initialisé dans la fonction __post_init__ à partir de gseScEcoListStr
    :type gseScEcoList: list[int]
    :param gseObligMaturiteMaxAutoDetect: Booléen activant ou désactivant la détection automatique de la maturité max des obligations. Valeur par défaut = True
    :type gseObligMaturiteMaxAutoDetect: bool
    :param gseObligMaturiteMax: Maturité max des obligations. Valeur par défaut = 50
    :type gseObligMaturiteMax: int
    :param societe: Société. Valeur par défaut = 'ACCENTURE'
    :type societe: str
    """

    cdChocS2List: list[CdChocS2] = field(default_factory = lambda: [CdChocS2.central])
    dfCdChocS2 : DataFrame = field(init=False)
    dfCdChocS2Sc : DataFrame = field(init=False)
    
    projModeProjection: ModeProjection = field(default=ModeProjection.ACTIF_SEUL)
    projHorizon: int = field(default = 10)
    projHorizonList: int = field(init = False)
    projDateDebut: date = field(
        metadata=config(
            encoder=date.isoformat,
            decoder=date.fromisoformat
        ),
        default=date.fromisoformat('2022-12-31'))
    
    projDateDebutAnnee: int = field(init=False)

    methodeInitEquilibreBilan: CdMethodeInitEquilibreBilan = field(default=CdMethodeInitEquilibreBilan.FONDS_PROPRES)

    ### Paramétrage des scenarii économiques
    gseScCrnAutoBuild: bool = field(default=False)
    gseScUnivers: ScUnivers = field(default = ScUnivers.RN)
    gseScEcoListStr: str = field(default='1')
    gseScEcoList: list[int] = field(init=False)
    gseObligMaturiteMaxAutoDetect: bool = field(default=True)
    gseObligMaturiteMax: int = field(default=50)

    ### Choix du périmètre à lancer (société)
    societe: str = field(default='ACCENTURE')

    def __post_init__(self):
        """Initialise les différents paramètres et génère des erreurs dans les cas suivants :
        - si gseScUnivers != ScUnivers.RN
        - si gseScCrnAutoBuild and gseScUnivers!= ScUnivers.RN
        - si gseScCrnAutoBuild and gseScEcoList!=[1]

        :return:
        :rtype:
        """
        self.projDateDebutAnnee = self.projDateDebut.year
        self.projHorizonList = list(range(self.projHorizon+1))
        self.gseScEcoList = convertStringToIntList(self.gseScEcoListStr)
        if self.gseScUnivers != ScUnivers.RN:
            raise (Exception("Le modèle à date ne sait gérer que l'univers Risque Neutre"))
        if self.gseScCrnAutoBuild and self.gseScUnivers!= ScUnivers.RN:
            raise(Exception("ProjConfig : Dans le cas où scCrnAutoBuild=VRAI, scUnivers doit être égal à RN"))
        if self.gseScCrnAutoBuild and self.gseScEcoList!=[1]:
            raise(Exception("ProjConfig : Dans le cas où scCrnAutoBuild=VRAI, scList doit être égal à [1]"))

        self.dfCdChocS2 = refCdChocS2.filter(pl.col(VarS2.cdChocS2).is_in(self.cdChocS2List))
        self.dfCdChocS2Sc = self.dfCdChocS2.with_columns(
            pl.lit(self.gseScEcoList).alias(VarProj.scenario)
        ).explode(VarProj.scenario).with_columns(pl.col(VarProj.scenario).cast(pl.Int32))

        if self.gseScCrnAutoBuild:
            self.gseObligMaturiteMaxAutoDetect=False